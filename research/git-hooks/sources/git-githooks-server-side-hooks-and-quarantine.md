---
source: https://git-scm.com/docs/githooks
source_date: 2026-04
researched: 2026-09-26
---

# git documentation: server-side hooks (pre-receive, update, post-receive) and the quarantine environment

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. Sources: githooks (last updated in 2.54.0) and https://git-scm.com/docs/git-receive-pack (QUARANTINE ENVIRONMENT section).

- pre-receive: invoked by git-receive-pack "just before starting to update refs on the remote repository". "This hook executes once for the receive operation." It takes no arguments; stdin has one line per ref, `<old-oid> SP <new-oid> SP <ref-name>`. "If the hook exits with non-zero status, none of the refs will be updated." Stdout and stderr are forwarded to the pushing client, so the hook can explain the rejection.
- update: runs once per ref, with three parameters (ref name, old object name, new object name). Non-zero "prevents git receive-pack from updating that ref", so it can reject some refs of a push and accept others. Page use cases: enforce fast-forward only, and "access control without relying on filesystem ownership and group membership" for users restricted to git commands over the wire.
- post-receive and post-update run after the work is done and "cannot affect the outcome" (post-receive: "does not affect the outcome of git receive-pack, as it is called after the real work is done").
- Push options: `git push --push-option=...` values reach pre-receive and post-receive through `GIT_PUSH_OPTION_COUNT` and `GIT_PUSH_OPTION_0...`, only if negotiated.
- push-to-checkout only matters when `receive.denyCurrentBranch` is `updateInstead`.
- Quarantine (git-receive-pack): incoming objects go to a temporary quarantine directory and are "migrated into the main object store only after the pre-receive hook has completed". A failed push leaves no on-disk data. "The pre-receive hook MUST NOT update any refs to point to quarantined objects", and ref updates from within pre-receive are automatically rejected.
- The pre-receive/update hooks run on the machine that receives the push, so what they can check is the pushed refs and commits, not the developer's working tree or the agent's session. They run wherever the repository is hosted; whether a host allows custom ones is a hosting question (see [GitHub note](github-pre-receive-hooks-and-branch-protection.md)).
- The page does not mention any client flag that skips pre-receive or update; `--no-verify` on `git push` is documented as toggling the client-side pre-push hook only (see [no-verify scope note](git-commit-push-merge-rebase-no-verify-scope.md)).
