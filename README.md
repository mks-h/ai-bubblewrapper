# AI Bubblewrapper

Wrap your AI agent in a safety [bubblewrap][bwrap] before it goes rogue with
the CLI access! This makes sure your agent doesn't have write access in places
it has no business writing to.

Especially applicable to [OpenCode][opencode] and [Pi][pi], but also
[Codex][codex] if you want to run it without nagging permission prompts.

[bwrap]: https://github.com/containers/bubblewrap
[opencode]: opencode.ai
[pi]: pi.dev
[codex]: https://learn.chatgpt.com/docs/codex/cli

## Installation

Clone this repo somewhere, then create a symlink in a PATH directory like so:

```
# Assuming you're in the repo dir and ~/.local/bin is in the PATH
ln -sr ./ai-bwrap ~/.local/bin/ai-bwrap
```

Installing it this way lets you update it in the future by running `git pull`
in the repo. Although you should still check whether the installation
instructions have changed when doing an update.

## Usage

Run `ai-bwrap opencode` instead of running `opencode` or, better yet, alias
these commands in your shell configuration file.

For Bash on Fedora, I like to create a file in the `~/.bashrc.d/` directory
with the following content:

```
alias opencode='ai-bwrap opencode'
alias pi='ai-bwrap pi'
alias codex='ai-bwrap codex'
```

But you might have to use the regular `~/.bashrc` file depending on your Bash
configuration.

## Scope

The goal of this project is to protect the user data from being destroyed or
tempered with when agents are given access to the shell or other dangerous
tools. Only Linux support is provided.

The *anti-goals* of this project are:
- Implementing a fine-grained or any other kind of permission system
- Extensive configurability

## Limitations

When your agent tries to update itself, it will most likely fail due to the
read-only filesystem. In that case, run it without the sandbox just once to let
it update. If you have aliased the agent commands, bypass the alias with the
backslash (`\`) like so:

```
\opencode upgrade
\pi update
\codex update
```
