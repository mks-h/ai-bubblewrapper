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
