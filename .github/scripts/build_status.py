#!/usr/bin/env python3
"""Render GitHub Issues to factual TongNet status. No synthetic work or test claims."""
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "manbir6-ux/TongNet")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = "docs/PROJECT_STATUS.md"
TASK_RE = re.compile(r"^\[(TN-[A-Z]+-\d{3})\]\s*(.+)$")
LEGACY_RE = re.compile(r"^\[(G\d+)\](\[P\d\])?\s*(.+)$")
FIELD_RE = re.compile(r"^\*\*(Status|Priority|Gate|Type|Depends on|Owner/worker|Evidence|Blocking decisions):\*\*\s*(.+)$", re.M)
VALID_STATUS = {"TODO", "READY", "IN_PROGRESS", "BLOCKED", "IN_REVIEW", "DONE"}

def safe(s):
    s = str(s or "").replace("\r", " ").replace("\n", " ").strip()
    s = re.sub(r"<[^>]*>", "", s)
    return re.sub(r"([\\|\x60*\[\]<>])", r"\\\1", s)[:300]

def fetch_issues():
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN not supplied; failing closed instead of inventing tasks")
    issues = []
    page = 1
    while True:
        api = "https://api.github.com/repos/{}/issues?state=all&per_page=100&page={}".format(REPO, page)
        req = urllib.request.Request(api, headers={
            "Authorization": "Bearer " + TOKEN,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "TongNet-status-sync/1.0",
        })
        with urllib.request.urlopen(req, timeout=30) as res:
            raw = json.load(res)
        if not isinstance(raw, list):
            raise RuntimeError("Unexpected GitHub API issue payload: refusing to overwrite status")
        issues += [i for i in raw if "pull_request" not in i]
        if len(raw) < 100:
            break
        page += 1
        if page > 100:
            raise RuntimeError("More than 10000 issues; stop rather than silently truncate")
    return issues

def fields(body):
    return {k: v.strip() for k, v in FIELD_RE.findall(body or "")}

def render(issues, checked):
    tasks, legacy = [], []
    for item in issues:
        m = TASK_RE.match(item.get("title", ""))
        lm = LEGACY_RE.match(item.get("title", ""))
        if m:
            f = fields(item.get("body"))
            declared = f.get("Status", "UNKNOWN").upper()
            if declared not in VALID_STATUS:
                declared = "UNKNOWN"
            state = item.get("state", "open")
            evidence = f.get("Evidence", "")
            if state == "closed":
                status = "DONE (evidence check)" if ("http" in evidence or "PR #" in evidence) else "CLOSED — VERIFY EVIDENCE"
            else:
                status = "OPEN/" + ("INCONSISTENT-DONE" if declared == "DONE" else declared)
            tasks.append({
                "id": m.group(1), "title": safe(m.group(2)),
                "status": status, "priority": safe(f.get("Priority", "?")),
                "gate": safe(f.get("Gate", "?")),
                "owner": safe(f.get("Owner/worker", "Unassigned")),
                "deps": safe(f.get("Depends on", "None")),
                "url": item.get("html_url", ""), "closed": state == "closed",
            })
        elif lm:
            legacy.append((safe(item.get("title", "")), item.get("html_url", ""),
                           item.get("state", "open")))
    tasks.sort(key=lambda t: ({"P0": 0, "P1": 1, "P2": 2}.get(t["priority"], 3),
                              t["gate"], t["id"]))
    open_tasks = [t for t in tasks if not t["closed"]]
    blocked = [t for t in open_tasks if "BLOCKED" in t["status"]]
    ready = [t for t in open_tasks if any(x in t["status"] for x in ("READY", "IN_PROGRESS"))]
    done = [t for t in tasks if t["closed"]]
    head = [
      "# TongNet — GitHub Issue-derived Project Status",
      "",
      "**Refreshed (UTC):** " + checked,
      "**Repository:** " + REPO,
      "**Status:** An issue snapshot only, not independent proof of tested software.",
      "",
      "## Summary",
      "",
      "- TN tasks: **{}**; open **{}**; closed **{}**; blocked by body status **{}**; ready/in progress **{}**.".format(
         len(tasks), len(open_tasks), len(done), len(blocked), len(ready)),
      "- Legacy pre-existing [G...] issues (preserved pending reconciliation): **{}**.".format(len(legacy)),
      "- Blockchain code/testnet/coin status: **not inferred from Issues**; verify merged source, CI and audit evidence directly.",
      "- An automated daily check does **not** mean any development work was done that day.",
      "",
      "## Ready / currently actionable",
      "",
    ]
    if not ready:
        head.append("No currently READY/IN_PROGRESS tasks reported. Review blockers manually.")
    else:
        for t in ready:
            head.append("- [{}]({}) — **{}**, owner {}, depends {}".format(
                safe(t["id"]), t["url"], t["status"], t["owner"], t["deps"]))
    head += [
       "",
       "## Canonical TN tasks (open and closed)",
       "",
       "| Issue | Priority | Gate | Reported status | Depends on | Owner |",
       "|---|---|---|---|---|---|",
    ]
    for t in tasks:
        head.append("| [{} — {}]({}) | {} | {} | {} | {} | {} |".format(
            t["id"], t["title"], t["url"], t["priority"], t["gate"],
            safe(t["status"]), t["deps"], t["owner"]))
    head += ["", "## Legacy issue migration inventory (DO NOT silently discard)", "",
             "Legacy issues existed outside the new TN-ID source-of-truth list. Review each for unique requirements, PRs and evidence; map it to a TN Issue before optionally closing as a duplicate. Legacy closure must not be mistaken for feature completion.", ""]
    if legacy:
        for title, url, state in sorted(legacy, key=lambda x: x[0]):
            head.append("- [{}]({}) — {}".format(title, url, safe(state)))
    else:
        head.append("No legacy issues.")
    head += [
      "",
      "## How to resume this project",
      "",
      "Read [AGENTS.md](../AGENTS.md) → [Project Control](PROJECT_CONTROL.md) → [Decision Register](DECISION_REGISTER_CURRENT.md) → [Work Log](WORK_LOG.md) → [Risk Audit](LONG_HORIZON_RISK_AUDIT.md) → selected issue/PR. Update issue + append real session log and tests. This status is rebuilt by [the workflow](../.github/workflows/status-sync.yml) from Github Issues only.",
      "",
      "If this status is old, the workflow may be disabled or not yet run. Trust actual GitHub Issues and merged PRs over this snapshot.",
      "",
    ]
    return "\n".join(head)

def main():
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    data = fetch_issues()
    output = render(data, now)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fp:
        fp.write(output)

if __name__ == "__main__":
    try:
        main()
    except (Exception,) as ex:
        print("Status sync FAILED (previous dashboard preserved):", str(ex), file=sys.stderr)
        sys.exit(1)
