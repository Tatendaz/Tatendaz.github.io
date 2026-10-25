# About Tatenda Zhou

I am a Software & Systems Architect and SRE with 10+ years in enterprise software. These days I build open-source tools that review, test and measure the work of AI coding agents, and I teach engineering teams to hand real work to those agents.

## What I work on

- **Tools for AI coding agents.** Review gates, a second agent that tests mobile apps before a PR opens, quota meters and model pickers. All open source; the list is below.
- **Agent evaluation.** I benchmarked Codex models on 50 SWE-bench Verified tasks and found agents searching or reading files outside their workspace in 14 of 304 runs. The report is [openai/codex#53166](https://github.com/openai/codex/issues/53166).
- **Native mobile.** iOS and Android apps built for the store: auth, payments, polish.
- **Reliability.** Cloud infrastructure, CI/CD, monitoring and alerting. I own reliability, not just features.

## Workshops for engineering teams

**From chat to coding agent** is a half-day or full-day workshop for teams of 5 to 20 developers. Each developer hands a real ticket from the team's backlog to a coding agent, then we set up the checks that stop bad work before it reaches main. Remote first, flat fee per team. Details: https://tatendaz.github.io/#workshops

## Podcasts and talks

I am open to podcast interviews and talks about AI coding agents: how to check their work, what they cost, and how to run several at once. I was a guest on the Koshelek Team podcast (["From Zimbabwe to Russia: how a foreigner built a successful IT career"](https://www.youtube.com/watch?v=w9U4Nsl0aL0), in Russian), and I am a former club president of a Toastmasters club in Saint Petersburg.

## Open-source tools for coding agents

Each has a project page on this site and its source on GitHub.

- [coderabbit-failover](https://tatendaz.github.io/coderabbit-failover/): one CodeRabbit review budget shared across agents, with a local Claude Code backup review when CodeRabbit is rate-limited. Source: https://github.com/Tatendaz/coderabbit-failover
- [CodeAndConfirm](https://tatendaz.github.io/codeandconfirm/): a second agent tests iOS and Android changes on the simulator and emulator before the PR opens. Source: https://github.com/Tatendaz/codeandconfirm
- [T-mods](https://tatendaz.github.io/T-mods/): Claude Code mods, including one that refuses `gh pr merge` until CI is green and a real review exists. Source: https://github.com/Tatendaz/T-mods
- [QuotaSignal](https://tatendaz.github.io/QuotaSignal/): ChatGPT and Codex weekly quota in the macOS menu bar or Windows tray. Source: https://github.com/Tatendaz/QuotaSignal
- [Model Picker](https://tatendaz.github.io/model-picker/): model and effort suggestions for Codex and Claude Code. Source: https://github.com/Tatendaz/model-picker
- [Mission Control](https://tatendaz.github.io/mission-control/): a project board built from git, PRs and Claude Code session logs. Source: https://github.com/Tatendaz/mission-control
- [herdr-launcher](https://tatendaz.github.io/herdr-launcher/): unofficial macOS Dock launcher for the herdr TUI. Source: https://github.com/Tatendaz/herdr-launcher

## More projects

- [claude-usage](https://github.com/Tatendaz/claude-usage): your Claude quota, live in the terminal status bar. Project page: https://tatendaz.github.io/claude-usage/
- [yapui](https://github.com/Tatendaz/yapui): live HTML preview with a two-way feedback loop between you and the coding agent. Project page: https://tatendaz.github.io/yapui/
- [promptups](https://github.com/Tatendaz/promptups): webcam rep counting wired into Claude Code hooks. Project page: https://tatendaz.github.io/promptups/
- [Vergance](https://github.com/Tatendaz/Vergance): gaze and voice as a hands-free input layer for macOS. Project page: https://tatendaz.github.io/Vergance/
- [LangChain FDE curriculum](https://github.com/Tatendaz/langchain-fde-curriculum): shipping production agents as a forward-deployed engineer. Project page: https://tatendaz.github.io/langchain-fde-curriculum/
- [Showcase](https://github.com/Tatendaz/showcase): architecture, screenshots and engineering decisions from private work across AI, quant and mobile.

## Follow and contact

- X: https://x.com/realtatendazhou
- LinkedIn: https://www.linkedin.com/in/tatendazhou
- GitHub: https://github.com/Tatendaz
- Email for workshops, podcasts and talks: tatendaz@me.com. The contact page (https://tatendaz.github.io/contact/) lists what to include.

---

HTML version: https://tatendaz.github.io/about/ · Agent guide: https://tatendaz.github.io/llms.txt
