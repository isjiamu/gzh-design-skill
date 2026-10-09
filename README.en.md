> 🤝 **A joint project by Jiamu × [Moyu Xiaoli (摸鱼小李)](https://mp.weixin.qq.com/s/EMahAzgfAbRQrYukWE7_IQ)** — the components, theme design and quality bar are shaped by both authors' hands-on WeChat publishing practice. Special thanks to Xiaoli.

<div align="center">

# gzh-design-skill · WeChat Layout Skill

**Turn Markdown into polished HTML you can paste straight into the WeChat editor**

6 curated themes + theme generator · code blocks / images / GIFs · auto section numbers & keyword marks · two-gate quality checks

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/code)
[![Themes](https://img.shields.io/badge/themes-6%20+%20generator-059669)](references/theme-index.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Agents](https://img.shields.io/badge/Claude%20Code%20·%20Codex%20·%20Cursor-supported-8b5cf6.svg)](#-quick-start)

English ｜ [中文](README.md)

</div>

---

A layout Skill for AI agents (Claude Code / Codex / Cursor …). You write Markdown; it renders HTML with **fully inlined styles that survive pasting into the WeChat editor** — auto section numbers, keyword underlines, intro cards, code blocks, images, merged author signature — with scripts that deterministically enforce WeChat's platform limits.

## ✨ Features

- **6 curated themes**: Moyu Green (default) · Red & White · Graphite Minimal · Zen Whitespace · Moyu Ticket · Olive Journal — each a self-contained thick component library (design tokens + dozens of components + visual-hierarchy table + article-type recipe table).
- **Theme generator**: none fit? Describe a style in one line or drop a reference image, and generate a fresh component library saved for reuse (see `references/theme-generator.md`).
- **Full content support**: code blocks (dark/light, monospace), images, GIFs (with an animated badge), inline code, quotes, lists, product badges, Markdown hyperlinks (auto-converted to superscript footnotes + an end-of-article "References" list).
- **Smart layout**: auto section numbering (last chapter ∞ / ///), 1–3 keyword underlines per paragraph, intro card & TOC distilled from the body, de-duplicated signature.
- **Full-width CJK punctuation** in prose; kept as-is inside code blocks.
- **Paste-safe**: all styles inlined, every text node wrapped in `<span leaf="">`, avoiding `<style>/<div>/class/grid/position` that WeChat strips.
- **Two-gate quality checks**: `component_lint.py` (library source) + `validate_gzh_html.py` (final output) form a reproducible edit → verify → fix loop.
- **One-click copy**: a preview page with a **Copy** button — click to copy the rich text and paste straight into WeChat, no manual select-all.

## ✅ Good for / ❌ Not for

**✅ Good for**: opinion/analysis · tutorials/how-tos · reviews/tool roundups · knowledge notes/methodology · interviews/features · data recaps · lifestyle/personal essays · case studies — turning Markdown / Word / PDF / plain text long-form into paste-ready WeChat HTML; also generating custom themes from a description or reference image.

**❌ Not for**: generic web/landing pages (use a frontend skill) · slide decks (use a PPT skill) · pure image posters / social cards (use a social-card skill) · non-WeChat layout · **writing the article** (this skill only lays out — bring the Markdown first).

## 🗂 Common use cases

| Your content | How to lay it out |
|---|---|
| Opinion / deep long-form | Red & White or Graphite Minimal; keyword underlines + pull-quotes |
| Product review / tool roundup | Moyu Green or Moyu Ticket; step/tool-labels + cards, by recipe |
| Tutorial / how-to | Moyu Green; step-labels + code blocks + numbered lists |
| Data recap / annual report | Moyu Green or Olive Journal; data cards + tables |
| Zen / minimal essay | Zen Whitespace; generous whitespace + centered serif quotes |
| Editorial notes / deep review | Olive Journal; editor's note + sections + dark summary box |
| Word / PDF draft → WeChat | auto-normalize format → then pick a theme by topic |
| A style beyond the built-ins | Theme generator: make one from a line or an image |

## 🎨 6 Curated Themes

One long-form article laid out in all 6 themes (full-fidelity screenshots with real images):

<table>
<tr>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-green.png?v=1" width="250"><br><sub><b>Moyu Green (default)</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-red-white.png?v=1" width="250"><br><sub><b>Red & White</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-graphite-minimal.png?v=1" width="250"><br><sub><b>Graphite Minimal</b></sub></td>
</tr>
<tr>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-zen-whitespace.png?v=1" width="250"><br><sub><b>Zen Whitespace</b></sub></td>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-ticket.png?v=1" width="250"><br><sub><b>Moyu Ticket</b></sub></td>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-olive-journal.png?v=1" width="250"><br><sub><b>Olive Journal</b></sub></td>
</tr>
</table>

> 📚 **All 6 themes → [docs/all-themes.md](docs/all-themes.md)**　|　or open `docs/gallery/index.html` for the interactive full HTML.

### Theme cheat-sheet

| | Theme | Best for |
|---|---|---|
| ![](https://placehold.co/12/059669/059669.png) `#059669` | Moyu Green (default) | Tutorials, reviews, checklists, tool roundups |
| ![](https://placehold.co/12/DC2626/DC2626.png) `#DC2626` | Red & White | Deep analysis, opinions, strong takes |
| ![](https://placehold.co/12/52525B/52525B.png) `#52525B` | Graphite Minimal | Design, tech commentary, premium brand |
| ![](https://placehold.co/12/4A5D52/4A5D52.png) `#4A5D52` | Zen Whitespace | Zen, minimal living, reflective essays |
| ![](https://placehold.co/12/059669/059669.png) `#059669` | Moyu Ticket | Tool comparisons, creative reviews (ticket motif) |
| ![](https://placehold.co/12/1e1f23/1e1f23.png) `#1e1f23` | Olive Journal | Editorial notes, deep reviews, case recaps |

> English slug, library file and underline CSS for each theme: see [`references/theme-index.md`](references/theme-index.md). Need another style? Have the AI generate one with the [theme generator](references/theme-generator.md).

## 🚀 Quick Start

```bash
# One-line install (recommended)
npx skills add https://github.com/isjiamu/gzh-design-skill

# Or manual clone
git clone https://github.com/isjiamu/gzh-design-skill.git ~/.claude/skills/gzh-design
```

Or just ask **any agent** (Claude Code / Codex / Cursor …):

> Please find and install the skill at https://github.com/isjiamu/gzh-design-skill

Then, once installed, tell your agent:

> Lay out `article.md` as WeChat HTML using the Moyu Green theme.

## 💬 Community

Scan to join the **official WeChat Work group** (dynamic QR, auto-invite) — chat about WeChat layout & Agent Skills:

<img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/group-qr.png" width="220" alt="WeChat Work group QR">

> QR expired? Add WeChat **`zuiyn_soul`** (note "gzh-design") to get invited.

## 📖 Workflow

1. **Pick a theme** — auto-suggests the best fit by topic and asks you to confirm (defaults to Moyu Green); or specify one, or generate a new one.
2. **Load libraries** — the chosen theme lib + the shared incremental lib (code/image/label).
3. **Parse Markdown** — headings, chapters, bold, highlight, quotes, images, code, lists.
4. **Assemble HTML** — from real components; apply numbering, underlines, full-width punctuation, signature.
5. **Validate** — run `validate_gzh_html.py`, ship only at 0 ERROR.
6. **Output** — a clean fragment + a preview page with a **Copy** button; open it, click "Copy to WeChat", then paste into the editor (no manual select-all).

## 🧩 Platform limits (enforced)

Output obeys: no `<style>/<script>/<div>`, no `class/id`, no `position:fixed/absolute/sticky`, `float`, `@media/@keyframes`, `display:grid`, CSS variables, external fonts; all styles inlined; every text node wrapped in `<span leaf="">`. Checked deterministically by scripts, not by model discipline.

## 🔁 Verifiable loop

```bash
python3 scripts/component_lint.py .            # source gate: anti-patterns in libraries
python3 scripts/validate_gzh_html.py out.html  # output gate: final HTML compliance
```

Source gate flags `white-space:pre` (blank bloat), full-border dashed frames in prose, and forbidden platform items — must be 0 ERROR. Output gate flags forbidden tags, `<span leaf>` wrapping, half-width punctuation — must be 0 ERROR / 0 half-width WARN.

## 💡 Why it's built this way

- **Constraint beats freedom** — preset palettes + fixed components lock in a quality floor instead of letting the model improvise each time.
- **Paste-safe by design** — fully inlined styles + every text node in `<span leaf="">`, avoiding exactly what the WeChat editor strips.
- **Quality by script, not discipline** — two gates (`component_lint` at source + `validate_gzh_html` on output) deterministically check platform rules and punctuation.
- **Model-agnostic** — layout logic lives in libraries and scripts, not any one model's tricks; Claude / GPT / Gemini / Chinese models all produce the same result.
- **Agent-friendly** — input and output are plain-text Markdown / HTML any agent can read, write, edit and verify — native to Claude Code / Codex / Cursor.

## 📁 Structure

```
gzh-design/
├── SKILL.md                 # layout workflow (agent entry)
├── references/              # 6 theme libs + generator + shared lib + theme-index + eval-cases
├── scripts/                 # validate_gzh_html.py + component_lint.py
├── assets/                  # sample-article.md + theme-previews/
└── docs/gallery/            # browser preview of themes
```

## 🎯 Principles

- **Constraint over freedom** — preset palettes and fixed components guarantee a quality floor.
- **Determinism to scripts** — hard rules go to the linters; the model only judges content.
- **Small labels, not dashed frames** — emphasis uses left bars / pill labels; dashed frames are reserved for the centered "asset placeholder".
- **Reproducible** — every lesson becomes a gotcha or a check, guarded by the verifiable loop.
- **Model-agnostic** — works with any capable LLM (Claude, GPT, Gemini, plus Chinese models like DeepSeek, Kimi, Qwen, GLM); layout lives in the libraries and linters, not model-specific tricks, so switching models keeps the same result.
- **Recipe over free choice** — pick the component combo from the theme's article-type recipe table first, then assemble; same-genre articles stay visually consistent.
- **Restrained color** — primary only at anchors (≤5/article), mostly white + gray, color as punctuation.

## 🧠 Make your own theme

### Theme generation — one line or one reference image

Not enough with the built-in 6? Have the AI make one. Driven by the second workflow in [`references/theme-generator.md`](references/theme-generator.md):

1. **Collect preferences** (asked all at once): theme description required (or a reference image); name / colors / font / radius / shadow / use-case auto-filled if blank.
2. **Generate a block library**: 45–75 blocks of full inline-style HTML saved to `assets/theme-previews/{id}.html` — review the whole page at once in a browser.
3. **Convert + register**: turn it into `references/theme-{id}.md` (add `<span leaf>`, the five required sections), register in theme-index, pass `component_lint.py` at 0 ERROR.
4. **First-class from then on**: use it exactly like a built-in theme.

> Try: *"Generate a new WeChat theme — mono magazine, Klein-blue accent, serif type"* or *"Build a component library from this reference image."*

### Color pairing — a repeatable palette structure the AI can auto-fill

Every theme is built on a **design-token palette** with fixed roles: a recognizable **primary** (anchors only, ≤5/article), **light tints** of it for card / quote / label backgrounds, one **contrasting accent** for highlights, a **neutral gray scale** carrying ~90% of the text, and a **light underline color** for per-paragraph keyword marks. Restraint: mostly white + gray, color only as punctuation, ≤2 highlights per paragraph.

Give just a primary color or a vibe, and the generator derives the whole harmonious palette (tints, borders, highlight, grays, underline) with readable contrast:

> *"Use #7C9EB2 misty-blue as the primary and generate a fresh travel-essay WeChat theme."*

## ❓ FAQ

**Will styles survive pasting into WeChat?** Yes — everything is inlined and every text node is `<span leaf="">`-wrapped, enforced by the validator.

**Can I add my own theme?** Two ways: (1) have the AI generate one via `references/theme-generator.md`; (2) hand-write one per `CONTRIBUTING.md` and open a PR.

**Can it output several themes at once?** Yes — say "lay this out in each of these themes" for a batch to choose from.

**How do I update?** Re-run `npx skills add https://github.com/isjiamu/gzh-design-skill`, or `git pull` in the install dir.

**What if the agent's output isn't compliant?** Run `scripts/validate_gzh_html.py`; fix on ERROR until both gates are green. Still stuck? Open an Issue.

## ⭐ Star History

If this project helps you, a Star means a lot 🙏

<a href="https://www.star-history.com/?repos=isjiamu%2Fgzh-design-skill&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&theme=dark&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
 </picture>
</a>

## 🤝 Contributing · 📄 License

See [CONTRIBUTING.md](CONTRIBUTING.md). Co-built by **Jiamu × Moyu Xiaoli** — the component libraries and theme design standards come from both authors' WeChat publishing practice.

**AGPL-3.0 © 2026 Jiamu × Moyu Xiaoli.** Key terms:

1. **Attribution required** — keep the copyright and co-author notice.
2. **Derivatives must be open source** — any modified version, fork or redistribution must be released under AGPL-3.0 (or a compatible license) with full source.
3. **Network use must be open** — even deploying a modified version as a SaaS / web service (without distributing the code) requires publishing the source — this is what sets AGPL apart from GPL.
4. **No closed-source, proprietary, or paid-only distribution.**

Full terms in [LICENSE](LICENSE).

> 🤝 **AI Agent & model vendors welcome to co-create**: want to integrate gzh-design into your product or deeply co-build on it? We'd love that — contact Jiamu for the co-creation agreement.
