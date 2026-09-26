---
source: https://git-scm.com/docs/githooks
source_date: 2026-04
researched: 2026-09-26
---

# git documentation: githooks, the full hook list, inputs and effects

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. The page header says "githooks last updated in 2.54.0" (2026-04-20). This note adds the parts the [existing pre-commit note](../../hooks-as-test-gate/sources/git-githooks-pre-commit-bypass.md) and [no-verify note](../../hooks-as-test-gate/sources/git-hooks-pre-commit-and-no-verify.md) do not cover; it does not repeat the pre-commit/no-verify/hooksPath quotes recorded there.

## Mechanics common to all hooks

- "Hooks that don't have the executable bit set are ignored."
- Before invoking a hook git changes directory to the root of the working tree (non-bare) or `$GIT_DIR` (bare). Hooks run during a push (pre-receive, update, post-receive, post-update, push-to-checkout) "are always executed in $GIT_DIR".
- Environment variables such as `GIT_DIR` and `GIT_WORK_TREE` are exported to the hook; a hook that runs git in another repository "should clear these environment variables".
- Hooks get input through "the environment, command-line arguments, and stdin", per hook.
- "All the git commit hooks are invoked with the environment variable GIT_EDITOR=: if the command will not bring up an editor" (that is, hooks can run with no editor and no interaction).

## Which hooks can block (exit non-zero) and which cannot

Can block, per the page:
- pre-commit (no arguments; aborts before the commit is created). pre-merge-commit (aborts the merge commit). prepare-commit-msg (non-zero aborts; one to three parameters: message file, message source, commit id). commit-msg (one parameter, the message file; may edit the file in place; "invoked by git-commit and git-merge").
- pre-rebase (can "prevent a branch from getting rebased"). pre-push ("git push will abort without pushing anything"; parameters are remote name and location; stdin lines `<local-ref> SP <local-object-name> SP <remote-ref> SP <remote-object-name>`, so it sees which refs and objects are going to be pushed, including deletions). pre-auto-gc. pre-applypatch and applypatch-msg (for `git am`). sendemail-validate.
- Server-side, see the [server-side note](git-githooks-server-side-hooks-and-quarantine.md): pre-receive, update, push-to-checkout, reference-transaction (only in its "preparing" and "prepared" states).

Cannot affect the outcome, "meant primarily for notification": post-commit, post-applypatch, post-receive, post-update, post-merge ("cannot affect the outcome of git merge"), post-rewrite. post-checkout "cannot affect the outcome of git switch or git checkout, other than that the hook's exit status becomes the exit status of these two commands."

Other hooks named on the page: fsmonitor-watchman, post-index-change, proc-receive, and four git-p4 hooks. post-checkout also runs after `git clone` (unless `--no-checkout`) and `git worktree add`.

## What a hook sees

- pre-commit takes "no parameters"; it sees the working tree and index through git commands it runs itself. The page says nothing about a summary of what is staged; a script has to ask git.
- pre-push sees ref names and object ids on stdin, not file contents; a script must inspect the object ids itself.
- Hooks are tied to specific porcelain commands. The page attaches the commit hooks to `git commit` (and merge for pre-merge-commit and commit-msg). It does not say the commit hooks run for other ways to create a commit; that plumbing commands such as `git commit-tree` do not run pre-commit is not stated on this page (our inference only).
- pre-merge-commit page text: if a merge has conflicts, "At that point, this hook will not be executed, but the pre-commit hook will".

## Defaults

The default (sample) pre-commit hook "prevents the introduction of non-ASCII filenames and lines with trailing whitespace"; the default commit-msg hook detects duplicate Signed-off-by trailers; the default update hook prevents unannotated tags. All samples ship disabled (see the [config note](git-config-hookspath-and-config-based-hooks.md)).
