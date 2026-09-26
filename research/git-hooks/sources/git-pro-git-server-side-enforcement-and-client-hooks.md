---
source: https://git-scm.com/book/en/v2/Customizing-Git-An-Example-Git-Enforced-Policy
source_date: undated
researched: 2026-09-26
---

# Pro Git: An Example Git-Enforced Policy (client hooks mirror server hooks)

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. Also read: https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks (the [existing note](../../hooks-as-test-gate/sources/git-hooks-pre-commit-and-no-verify.md) already quotes its clone sentence).

- The chapter builds "client scripts that help the developer know if their push will be rejected and server scripts that actually enforce the policies."
- The server-side `update` hook does the enforcing (commit-message pattern, per-path ACLs): "as long as that update script is there and executable, your repository will never have a commit message without your pattern in it, and your users will be sandboxed."
- Its stated downside: users' pushes "are rejected", "Having their carefully crafted work rejected at the last minute can be extremely frustrating and confusing; and furthermore, they will have to edit their history to correct it". The book's answer is client-side hooks "that users can run to notify them when they're doing something that the server is likely to reject", so problems are fixed "before committing".
- "Because hooks aren't transferred with a clone of a project, you must distribute these scripts some other way and then have your users copy them to their .git/hooks directory and make them executable... Git won't set them up automatically."
- The client pre-commit example is "roughly the same script as the server-side part", reading the staging area instead of the commit log. One example client hook (checking for non-fast-forward pushes) is described as "very slow and is often unnecessary" because "if you don't try to force the push with -f, the server will warn you and not accept the push".
- The pattern the book describes is therefore two layers: an enforcing server hook and an advisory client hook that gives early feedback. It is a description of a design, not a measurement.
- From the Git Hooks page: "There are two groups of these hooks: client-side and server-side. Client-side hooks are triggered by operations such as committing and merging, while server-side hooks run on network operations such as receiving pushed commits."
