---
source: https://git-scm.com/docs/git-commit
source_date: 2026-06
researched: 2026-09-26
---

# git documentation: which commands take --no-verify and what it skips

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. Pages: git-commit, git-push, git-merge, git-rebase (each stripped to text, the option and HOOKS sections read), git-cherry-pick (searched: no hook or no-verify text on the page). Extends the [existing no-verify note](../../hooks-as-test-gate/sources/git-hooks-pre-commit-and-no-verify.md).

- git-commit: `--no-verify` "Bypass the pre-commit and commit-msg hooks." HOOKS section: the command "can run commit-msg, prepare-commit-msg, pre-commit, post-commit and post-rewrite hooks". A separate `--no-post-rewrite` option bypasses the post-rewrite hook.
- git-push: `--no-verify` "Toggle the pre-push hook... The default is --verify, giving the hook a chance to prevent the push. With --no-verify, the hook is bypassed completely."
- git-merge: `--no-verify`: "By default, the pre-merge and commit-msg hooks are run. When --no-verify is given, these are bypassed."
- git-rebase: `--no-verify` "bypasses the pre-rebase hook". The rebase page's Hooks section says the two backends' calling of post-commit and post-checkout was "by accident of implementation rather than by design" and "We will likely make rebase stop calling either of these hooks in the future." The page does not say pre-commit runs on each replayed commit.
- git-cherry-pick page read: no hook or no-verify text.
- So the bypass is per command: a commit hook, a push hook, a merge hook and a rebase hook each have their own flag, and prepare-commit-msg is not covered by commit's flag. Pre-existing note: the flag sits on the same command line the agent types.
- Not stated on any page: whether `git commit` run by another tool through a library (libgit2, an IDE) runs hooks. Not checked.
