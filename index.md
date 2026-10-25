# Tatenda Zhou: open-source tools for AI coding agents

Software & Systems Architect, SRE. Open to work, workshops and talks.

10+ years in enterprise software. I build open-source tools that review, test and measure the work of AI coding agents.

- Follow on X: https://x.com/realtatendazhou
- Follow on LinkedIn: https://www.linkedin.com/in/tatendazhou
- GitHub: https://github.com/Tatendaz
- Email: tatendaz@me.com

## Open-source tools for coding agents

Tools I built to trust coding agents with real work. Each has a project page on this site and its source on GitHub.

### Review and QA

- [coderabbit-failover](https://tatendaz.github.io/coderabbit-failover/): shares one CodeRabbit review budget across agents. When CodeRabbit is rate-limited, a local Claude Code review takes over and posts a commit status. Python, Claude Code skill. Source: https://github.com/Tatendaz/coderabbit-failover
- [CodeAndConfirm](https://tatendaz.github.io/codeandconfirm/): one agent builds, a second agent tries to break it. Codex runs user flows on the iOS Simulator and Android Emulator and returns a verdict pinned to the tested commit. Python. Source: https://github.com/Tatendaz/codeandconfirm
- [T-mods](https://tatendaz.github.io/T-mods/): function-hook plugins for Claude Code. One refuses `gh pr merge` until CI is green and a real review exists. TypeScript. Source: https://github.com/Tatendaz/T-mods

### Cost, models and many agents at once

- [QuotaSignal](https://tatendaz.github.io/QuotaSignal/): your ChatGPT and Codex weekly quota in the macOS menu bar or Windows tray, with alerts at 50%, 20% and 10%. Python. Source: https://github.com/Tatendaz/QuotaSignal
- [Model Picker](https://tatendaz.github.io/model-picker/): asks TypeSafe's JEV model which model and effort level fit the task, and shows the answer in chat. It never changes a setting. Python, Codex and Claude Code plugin. Source: https://github.com/Tatendaz/model-picker
- [Mission Control](https://tatendaz.github.io/mission-control/): a project board that builds itself from git, PRs, Claude Code session logs and an idea inbox, and launches agents into herdr from any card. Node, macOS. Source: https://github.com/Tatendaz/mission-control
- [herdr-launcher](https://tatendaz.github.io/herdr-launcher/): unofficial macOS Dock launcher for the herdr TUI. Click the ram, get herdr in your terminal. Shell. Source: https://github.com/Tatendaz/herdr-launcher

## Why I check what agents do

I benchmarked Codex models on 50 SWE-bench Verified tasks. In 14 of 304 runs, the agent searched or read files outside its workspace, and some runs found the upstream fix instead of working out the bug. I reported it with the raw logs and repro scripts in [openai/codex#53166](https://github.com/openai/codex/issues/53166).

A passing test does not prove the agent did the work. The tools above, and the workshop below, are about checking that it did.

## Workshop: From chat to coding agent

A half-day or full-day workshop for engineering teams of 5 to 20 developers. Each developer hands a real ticket from your backlog to a coding agent, then we set up the checks that stop bad work before it reaches main. I teach with the tools on this page, run live on your code.

- Every developer hands at least one real ticket to an agent and reviews the result.
- Your team writes down the checks an agent's change must pass.
- One automatic gate goes into a real repo on the day.

Remote first. Half day (4 hours) or full day (7 hours). Flat fee per team. Pilot pricing for the first 3 teams: email tatendaz@me.com to ask. Ask about a workshop: tatendaz@me.com (subject "Workshop enquiry").

## Podcasts and talks

I'm open to podcast interviews and talks about AI coding agents: how to check their work, what they cost, and how to run several at once. Invite me: tatendaz@me.com (subject "Podcast or talk").

- Podcast guest on Koshelek Team: ["From Zimbabwe to Russia: how a foreigner built a successful IT career"](https://www.youtube.com/watch?v=w9U4Nsl0aL0) (episode in Russian).
- Former club president of a Toastmasters club in Saint Petersburg.

## More projects

- [claude-usage](https://github.com/Tatendaz/claude-usage): your Claude quota, live in the terminal status bar: iTerm2, tmux, WezTerm, kitty, starship. Project page: https://tatendaz.github.io/claude-usage/
- [yapui](https://github.com/Tatendaz/yapui): live HTML preview with a two-way feedback loop between you and the coding agent. Project page: https://tatendaz.github.io/yapui/
- [promptups](https://github.com/Tatendaz/promptups): do reps while Claude thinks: webcam rep counting wired into Claude Code hooks. Project page: https://tatendaz.github.io/promptups/
- [Vergance](https://github.com/Tatendaz/Vergance): gaze and voice as a hands-free input layer. Look, speak, and your intent goes to Claude. Project page: https://tatendaz.github.io/Vergance/
- [LangChain FDE](https://github.com/Tatendaz/langchain-fde-curriculum): a curriculum for shipping production agents as a forward-deployed engineer. Project page: https://tatendaz.github.io/langchain-fde-curriculum/
- [Showcase](https://github.com/Tatendaz/showcase): architecture, screenshots and engineering decisions from private work across AI, quant and mobile.

## Follow along

New tools, and what I learn from running coding agents every day, go to X and LinkedIn.

- Follow on X: https://x.com/realtatendazhou
- Follow on LinkedIn: https://www.linkedin.com/in/tatendazhou
- GitHub: https://github.com/Tatendaz
- Email (workshops, podcasts, talks): tatendaz@me.com

---

HTML version: https://tatendaz.github.io/ · Other pages: [About](https://tatendaz.github.io/about/index.md) · [Contact](https://tatendaz.github.io/contact/index.md) · [Privacy](https://tatendaz.github.io/privacy/index.md) · Agent guide: https://tatendaz.github.io/llms.txt
