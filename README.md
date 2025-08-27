# ClickUp Demo for ACME

This is a small sandbox I set up for my ClickUp SE interview. The goal is to show how GitHub activity (branches, commits, PRs) links back to ClickUp tasks using the `CU-<taskId>` reference.

Nothing production-ready here — just a couple of commits/branches and a tiny Flask server I used during prep.

## How I’m using it
- I’ll create a branch, commit, and PR that include the ClickUp task ID (e.g., `CU-86ab8ydtm`).
- In ClickUp, the GitHub widget on that task should show the related activity automatically.

## Files
- `server.py` — super small Flask app I used to test webhooks.
- `.github/pull_request_template.md` — reminder to include the ClickUp task ID.
- *(Optional)* `.github/workflows/require-clickup-id.yml` — CI check that a PR references a ClickUp task.

## Notes
This is only for a demo. The interesting part is how ClickUp auto-links GitHub activity when it sees the task ID in branch/commit/PR.
