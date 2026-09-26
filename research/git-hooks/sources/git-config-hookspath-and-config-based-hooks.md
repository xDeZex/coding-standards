---
source: https://git-scm.com/docs/git-hook
source_date: 2026-06
researched: 2026-09-26
---

# git documentation: core.hooksPath, hook.* config, git hook, and template directories

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. Pages read: git-config (core.hooksPath and the `hook.*` variables), git-hook (header: "git-hook last updated in 2.55.0", 2026-06-29), git-init (TEMPLATE DIRECTORY). The [existing githooks note](../../hooks-as-test-gate/sources/git-githooks-pre-commit-bypass.md) records the plain location rule; this adds what is new.

## core.hooksPath

- "By default Git will look for your hooks in the $GIT_DIR/hooks directory. Set this to different path... and Git will try to find your hooks in that directory." The path may be absolute or relative; "a relative path is taken as relative to the directory where the hooks are run".
- Purpose stated on the page: to "centrally configure your Git hooks instead of configuring them on a per-repository basis", or as an alternative to changing default hooks in `init.templateDir`.
- "You can also disable all hooks entirely by setting core.hooksPath to /dev/null. This is usually only advisable for expert users and on a per-command basis using configuration parameters of the form git -c core.hooksPath=/dev/null ....". So a second bypass exists that is not the `--no-verify` flag, and it covers every hook, including ones `--no-verify` does not (prepare-commit-msg, post-*). Whether an agent will use it is not stated anywhere read.

## Config-defined hooks (new in recent git)

- git-config documents `hook.<friendly-name>.command`, `.event` (multi-valued), `.enabled` (default true), `.parallel`, plus `hook.<event>.enabled`, `hook.<event>.jobs` and `hook.jobs`. Hooks can then be defined in system, global or local config rather than as files. The git-hook page says "when instructions suggest adding a script to .git/hooks/<hook-event>, you can specify it in the config instead", "This way you can share the script between multiple repos."
- `hook.<friendly-name>.enabled` is "particularly useful when a hook is defined in a system or global config file and needs to be disabled for a specific repository"; `hook.<event>.enabled=false` disables all hooks for an event.
- Order: commands run "in the order Git encounters their associated hook.<friendly-name>.event configs"; the traditional hook file from the hooks directory "is run last". `git hook list` prints which hooks will run for an event.
- Parallel: with `-j`/`hook.jobs` hooks can run concurrently, but "applypatch-msg, pre-commit, prepare-commit-msg, commit-msg, post-commit, post-checkout, and push-to-checkout" always run sequentially. Default is serial.
- `git hook run --ignore-missing` and `--allow-unknown-hook-name` exist for tools wrapping git; unknown event names are otherwise rejected "to help catch typos".
- Which git version added these is not stated on the pages read (the githooks page does not mention them at all in its body); the git-hook page history lists 2.43.0 through 2.55.0. Not checked how widely deployed such versions are.

## Template directory (git init)

- Files in the template directory "will be copied to the $GIT_DIR after it is created". Template order: `--template`, then `$GIT_TEMPLATE_DIR`, then `init.templateDir`, then `/usr/share/git-core/templates`. "The sample hooks are all disabled by default. To enable one of the sample hooks rename it by removing its .sample suffix."
- The git-init page says nothing about hooks in a tracked directory or about clone. Hooks reaching a repository is therefore a per-machine or per-clone step unless `core.hooksPath` (repo-local config also does not travel with a clone, our inference) or a system/global config is arranged.
