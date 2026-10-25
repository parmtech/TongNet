#!/usr/bin/env python3
"""Create evidence-based daily TongNet GitHub Issue/commit snapshot.

Never sets issue DONE, creates fabricated progress or claims tests passed.
Only writes Markdown derived from GitHub API. Intended to run via
tracking-daily.yml after GitHub Actions is enabled by repository owner.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
REPO = os.environ.get("GITHUB_REPOSITORY", "manbir6-ux/TongNet")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
BASE = f"https://api.github.com/repos/{REPO}"

def fetch_json(path: str):
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN/ GH_TOKEN required; do not fake a snapshot.")
    req = urllib.request.Request(
        BASE + path, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "TongNet-project-control/1.0",
        }
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)

def get_issues():
    results = []
    for page in range(1, 21):
        batch = fetch_json(f"/issues?state=all&per_page=100&page={page}&sort=created&direction=asc")
        if not isinstance(batch, list):
            raise RuntimeError("GitHub returned invalid issue data.")
        results.extend(item for item in batch if "pull_request" not in item)
        if len(batch) < 100:
            break
    return results

def safe_cell(x):
    return str(x or "").replace("|", "\\|").replace("\n", " ").replace("\r", " ")[:200]

def build_report(issues, commits, now):
    local = now.astimezone(ZoneInfo("Australia/Sydney"))
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    day = local.strftime("%Y-%m-%d")
    states = Counter(x.get("state", "unknown") for x in issues)
    lines = [
        f"# TongNet — Automated GitHub Status Snapshot — {day}",
        "",
        f"**Generated UTC:** {stamp}  ",
        f"**Local Australia/Sydney date:** {day}  ",
        f"**Source:** [Live GitHub Issues](https://github.com/{REPO}/issues) and verified GitHub commit API; **NOT** test results, code-review approval or actual software completion.",
        "",
        f"**Issues:** {len(issues)} total; **{states['open']} OPEN**, **{states['closed']} CLOSED**. Closed counts mean only GitHub issue state; each must still have linked evidence/accepted PR.",
        "",
        "| Issue | GitHub state | Title | Last updated UTC |",
        "|---|---|---|---|",
    ]
    for item in sorted(issues, key=lambda x: x.get("number", 0)):
        n = item["number"]
        title = safe_cell(item.get("title", ""))
        state = safe_cell(item.get("state", "unknown")).upper()
        updated = safe_cell(item.get("updated_at", ""))
        lines.append(f"| [#{n}](https://github.com/{REPO}/issues/{n}) | {state} | {title} | {updated} |")
    lines += ["", "## Most recent repository commits", ""]
    if not commits:
        lines.append("No recent commits returned from GitHub.")
    else:
        for item in commits[:12]:
            sha = item.get("sha", "")
            title = (item.get("commit", {}).get("message", "").split("\n") or [""])[0]
            lines.append(f"- [\`{sha[:10]}\`](https://github.com/{REPO}/commit/{sha}) — {safe_cell(title)}")
    lines += [
        "", "## Mandatory interpretation", "",
        "- No **task implementation** is completed just because a Markdown plan or issue exists.",
        "- An OPEN issue may have a draft PR; verify live PR/test evidence before resuming.",
        "- A CLOSED issue without an accepted reviewable evidence trail must be reopened.",
        "- Current canonical worker handoff: [tracking/HANDOFF.md](https://github.com/" + REPO + "/blob/main/tracking/HANDOFF.md).",
        "- All RED technical/legal blockers remain blocking until GitHub task evidence and owner approval; snapshots never certify mainnet.",
        "",
    ]
    return day, "\n".join(lines)

def write_report(day: str, report: str):
    daily = ROOT / "tracking" / "auto" / f"{day}.md"
    daily.parent.mkdir(parents=True, exist_ok=True)
    targets = (
        daily,
        ROOT / "tracking" / "AUTO_STATUS.md",
        ROOT / "docs" / "PROJECT_STATUS.md",  # Older project-control links stay valid.
    )
    for p in targets:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(report, encoding="utf-8")

def main():
    if REPO != "manbir6-ux/TongNet":
        raise RuntimeError(f"Refusing to use unexpected repository: {REPO}")
    now = datetime.now(timezone.utc)
    issues = get_issues()
    if not issues:
        raise RuntimeError("Refusing empty issue snapshot: could be permissions or API error.")
    commits = fetch_json("/commits?per_page=12")
    day, report = build_report(issues, commits, now)
    write_report(day, report)
    print(f"Saved verified issue/commit snapshot {day}: {len(issues)} issues.")
    print("This output is a GitHub status record, NOT a crypto security audit.")

if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, urllib.error.URLError, OSError, ValueError) as exc:
        print(f"ERROR: Unable to generate trusted snapshot: {exc}", file=sys.stderr)
        sys.exit(1)
