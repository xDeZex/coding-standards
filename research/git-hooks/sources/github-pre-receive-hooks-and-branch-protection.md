---
source: https://docs.github.com/en/enterprise-server@latest/admin/enforcing-policies/enforcing-policy-with-pre-receive-hooks/about-pre-receive-hooks
source_date: undated
researched: 2026-09-26
---

# GitHub docs: pre-receive hooks (Enterprise Server) and protected branches

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. Pages: "About pre-receive hooks" (GitHub Enterprise Server 3.22 docs) and "About protected branches" (github.com docs). Vendor documentation, undated, changes with the product.

## Pre-receive hooks (GitHub Enterprise Server only)

- "Pre-receive hooks are scripts that run on the GitHub Enterprise Server appliance... each script runs in an isolated environment and can perform checks on the content of the push. The scripts will cause the push to be accepted if the exit status is 0, or rejected if the exit status is non-zero." Examples listed: commit message formats, locking a branch, blocking keywords or file types, "Prevent a PR author from merging their own changes".
- Performance: "all combined pre-receive hooks should run in under five seconds"; "a fixed timeout budget of 5 seconds (shared across all hooks)". A table says a timeout rejects the push when enforcement is enabled and "Push may fail" even when a hook is only in testing. Advice: avoid API requests and long-running git operations inside the hook.
- The page describes this as an appliance feature; it does not say whether github.com supports custom pre-receive hooks. Not verified here.
- It contrasts push rules (built in, UI/API, "audit logs", "bypass lists") with pre-receive scripts.

## Protected branches (github.com)

- Branch protection can require status checks, approving reviews and other conditions before merging into a branch. "By default, the restrictions of a branch protection rule don't apply to people with admin permissions to the repository or custom roles with the 'bypass branch protections' permission", unless "Do not allow bypassing the above settings" is enabled. "People and apps with admin permissions to a repository are always able to push to a protected branch" when branch restrictions limit pushers.
- Required status check results can be set by "Any person or integration with write permissions to a repository", unless a specific GitHub App is selected as the expected source.
- Relevance: a server-side gate exists on the host, but who can bypass it is configured there. That a server-side check is beyond the local agent's reach depends on whose credentials the agent's push carries; not stated on the pages.
