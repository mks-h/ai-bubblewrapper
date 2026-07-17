# AI Bubblewrapper

Wrap your AI agent in a safety [bubblewrap][bwrap] before it goes rogue with
the CLI access! Mounts your system read-only, only allowing writes to the
<abbr title="Current Working Directory">CWD</abbr> and agent directories.

Especially applicable to [Opencode][opencode] and [Pi][pi], but also
[Codex][codex] if you want to run it without nagging permission prompts.

[bwrap]: https://github.com/containers/bubblewrap
[opencode]: opencode.ai
[pi]: pi.dev
[codex]: https://learn.chatgpt.com/docs/codex/cli

## Installation

Clone this repo somewhere for future updates, then create a symlink in a PATH
directory, like so:
```
# Assuming you're in the repo dir and ~/.local/bin is in PATH
ln -sr ./ai-bwrap ~/.local/bin/ai-bwrap
```

This way you'd be able to update this script by running `git pull` in the repo
dir. That being said, always check whether these instructions changed when
updating.

## Usage

Run `ai-bwrap opencode` instead of running `opencode`, or better yet — alias
these commands in you shell configuration file.

For Bash on Fedora, I like to create `~/.bashrc.d/agents` with the following
content:
```
alias opencode='ai-bwrap opencode'
alias pi='ai-bwrap pi'
alias codex='ai-bwrap codex'
```
But you might have to use regular `~/.bashrc` depending on your Bash
configuration.

## Limitations

When your agent tries to update itself, it will most likely fail due to the
read-only filesystem. In that case, run it without this script once just to let
it update. If you have aliased the agent commands, bypass the alias like so:
```
\opencode
# or
\pi update
```
