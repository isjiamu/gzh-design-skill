> 🤝 **本项目由 甲木 × [「摸鱼小李」](https://mp.weixin.qq.com/s/EMahAzgfAbRQrYukWE7_IQ) 联名共建** —— 排版组件、主题设计与质量标准凝聚了两人的公众号实践与共同打磨，特别感谢小李。

<div align="center">

# gzh-design-skill · 公众号排版技能

**把 Markdown 一键排成可直接粘贴进微信公众号编辑器的精致 HTML**

6 套精选主题 + 主题生成器 · 代码块/图片/GIF · 自动章节编号与关键词标记 · 双关卡质量校验

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/code)
[![Themes](https://img.shields.io/badge/themes-6%20+%20generator-059669)](references/theme-index.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Agents](https://img.shields.io/badge/Claude%20Code%20·%20Codex%20·%20Cursor-supported-8b5cf6.svg)](#-快速开始)

[English](README.en.md) ｜ 中文

</div>

---

一个给 AI Agent（Claude Code / Codex / Cursor 等）用的公众号排版 Skill。你写完 Markdown，它按你选的主题，生成**样式全内联、粘贴到公众号编辑器不掉格式**的 HTML——自动编章节号、标关键词下划线、配引言卡与目录、处理代码块和图片、合并作者签名，并用脚本确定性地兜住公众号平台的各种限制。

## ✨ 核心特性

- **6 套精选主题**：摸鱼绿（默认）· 红白 · 石墨极简 · 留白禅意 · 摸鱼票据 · 橄榄手记 —— 每套都是自成体系的厚组件库（设计变量 + 数十个精细组件 + 视觉层级表 + 文章类型配方表）。
- **主题生成器**：不满足现成主题？用一句话描述或一张参考图，生成一套全新组件库并保存本地复用（见 `references/theme-generator.md`）。
- **内容全兼容**：代码块（深/浅色，等宽不折行）、图片、GIF（带动图角标）、行内代码、引用、列表、产品徽章。
- **智能排版**：章节自动编号（末章 ∞ / ///）、每段主动标 1–3 个关键词下划线、从正文提炼引言卡与目录、作者签名去重合并。
- **中文全角标点**：正文自动规范全角，代码块内原样保留。
- **不掉格式**：所有样式内联、文字 `<span leaf="">` 包裹，规避 `<style>/<div>/class/grid/position` 等公众号会过滤的写法。
- **双关卡质量校验**：`component_lint.py`（组件库源头）+ `validate_gzh_html.py`（最终产物），构成可复现的「改→验→修」闭环。
- **一键复制**：生成带「复制」按钮的预览页，点一下把富文本复制到剪贴板，直接粘进公众号，免手动全选。

## 👀 效果预览

6 套主题各排同一篇长文（真实长图，含配图、引言卡、编号章节、金句、名词旁注等完整组件）：

<table>
<tr>
<td colspan="3" align="center"><img src="https://origin.picgo.net/2026/07/07/-40619312d679bc34.jpg" width="100%"><br><sub><b>摸鱼绿（默认）</b></sub></td>
</tr>
<tr>
<td colspan="3" align="center"><img src="https://origin.picgo.net/2026/07/07/-084eb2b9d6f8d5e2.jpg" width="100%"><br><sub><b>红白色系</b></sub></td>
</tr>
<tr>
<td colspan="3" align="center"><img src="https://origin.picgo.net/2026/07/07/-747b33f502544254.jpg" width="100%"><br><sub><b>橄榄手记</b></sub></td>
</tr>
<tr>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-graphite-minimal.png?v=1" width="250"><br><sub><b>石墨极简风</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-zen-whitespace.png?v=1" width="250"><br><sub><b>留白禅意风</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-ticket.png?v=1" width="250"><br><sub><b>摸鱼票据风</b></sub></td>
</tr>
</table>

> 📚 **6 套完整长图 → [docs/all-themes.md](docs/all-themes.md)**　｜　克隆后浏览器打开 `docs/gallery/index.html` 可看可交互的完整 HTML。

## ✅ 适合 / ❌ 不适合

**✅ 适合**：观点/深度分析 · 教程/操作指南 · 测评/工具盘点 · 知识整理/方法论 · 访谈/人物特稿 · 数据复盘/报告 · 生活/情感随笔 · 案例实战 —— 把 Markdown / Word / PDF / 纯文本长文，一键排成可直接粘进公众号编辑器的 HTML；也能按描述或参考图生成自定义主题。

**❌ 不适合**：普通网页/落地页（用前端 skill）· PPT（用 PPT skill）· 纯图片海报/社交卡片（用社交卡片类 skill）· 非公众号平台的排版 · **代写文章**（本 skill 只排版、不写作——先有 Markdown 再用它）。

## 🗂 常见使用场景

| 你的内容 | 推荐怎么排 |
|---|---|
| 观点 / 深度长文 | 红白 或 石墨极简；关键词下划线 + 金句引用 + 居中金句 |
| 产品测评 / 工具盘点 | 摸鱼绿 或 摸鱼票据；step/tool-label + 卡片，按配方表走 |
| 教程 / 操作指南 | 摸鱼绿；step-label + 代码块 + 编号列表 |
| 数据复盘 / 年度报告 | 摸鱼绿 或 橄榄手记；数据卡 + 表格 |
| 禅意 / 极简随笔 | 留白禅意；大留白 + 居中衬线引用 |
| 内刊 / 深度评测 / 案例复盘 | 橄榄手记；编者按 + 分节 + 暗色摘要框 |
| Word / PDF 稿转公众号 | 先自动格式归一化 → 再按题材选主题 |
| 想要现成之外的风格 | 主题生成器：一句话或参考图现造一套 |

## 🎨 6 套精选主题

覆盖绝大多数公众号题材，每套都打磨到「拿来即用」：

| 主题 | 适合 |
|---|---|
| **摸鱼绿**（默认） | 教程、测评、清单、工具盘点（卡片丰富、信息密度高） |
| **红白色系** | 深度分析、观点、力量感话题（经典编辑风） |
| **石墨极简风** | 设计、科技评论、专业观点、高端品牌 |
| **留白禅意风** | 禅意、极简生活、深度随笔（呼吸感最强） |
| **摸鱼票据风** | 工具对比、创意评测（票据视觉隐喻） |
| **橄榄手记** | 内刊手记、深度评测、案例复盘（编辑部内刊质感） |

> 主色、下划线色值等**完整速查表见文末 [附录](#-完整主题速查表)**；不够用就让 AI [生成新主题](#-faq)。

## 🚀 快速开始

### 方式一：一行安装（推荐）

```bash
npx skills add https://github.com/isjiamu/gzh-design-skill
```

### 方式二：让 AI 自己装

对**任意 Agent**（Claude Code / Codex / Cursor 等）说一句：

> 请帮我查找并自动安装 https://github.com/isjiamu/gzh-design-skill 这个 skill

它会自行 clone 到对应的 skills 目录并接入。

### 方式三：手动 clone

```bash
git clone https://github.com/isjiamu/gzh-design-skill.git ~/.claude/skills/gzh-design
```

装好后，直接对 Agent 说：

> 用摸鱼绿把这篇文章排成公众号 HTML：`article.md`

## 💬 交流群

扫码加入**官方企业微信交流群**（活码自动邀请入群，一起交流公众号排版 & Agent Skills 玩法）：

<img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/group-qr.png" width="220" alt="企业微信交流群二维码">

> 扫码失效？加作者微信 **`zuiyn_soul`**（备注「gzh-design」）拉你进群。

## 📖 使用流程

1. **选主题** — 按题材自动推荐最契合的主题并请你一步确认（默认摸鱼绿）；也可直接指定，或让 AI 生成新主题。
2. **读组件库** — 读所选主题库 + 通用增量库（代码块/图片/小标签）。
3. **解析 Markdown** — 识别标题、章节、加粗、高亮、引用、图片、代码块、列表。
4. **装配 HTML** — 用组件库里的真实组件拼装，落实编号、下划线、全角、签名。
5. **校验** — 跑 `validate_gzh_html.py`，ERROR 清零才交付。
6. **输出** — 生成干净正文 + 带「复制」按钮的预览页；浏览器打开预览页点右上角「复制到公众号」，再去编辑器粘贴即可（免手动全选）。

## 🧩 公众号平台限制（已内置兜底）

生成的 HTML 严格遵守：禁 `<style>/<script>/<div>`、`class/id`、`position:fixed/absolute/sticky`、`float`、`@media/@keyframes`、`display:grid`、CSS 变量、外部字体；样式全部内联；所有文字用 `<span leaf="">` 包裹。这些由校验脚本确定性检查，而非靠模型自觉。

## 🔁 可验证循环

改组件库或工作流后，用双关卡闭环防回归：

```bash
python3 scripts/component_lint.py .            # 源头关：扫组件库反模式
python3 scripts/validate_gzh_html.py out.html  # 产物关：扫最终 HTML 合规
```

- **源头关** 查 `white-space:pre`（大空白）、正文四周虚线框、平台禁用项 —— 须 0 ERROR。
- **产物关** 查禁用标签、`<span leaf>` 包裹、半角标点 —— 须 0 ERROR / 半角 0 WARN。
- 逻辑：源头干净 → 产物必然干净。详见 `references/eval-cases.md`。

## 💡 为什么这么设计

- **约束优于自由** — 预设主题色板 + 固定组件先保住输出下限，不让模型每次现场发挥、风格飘忽。
- **样式粘贴不掉** — 全内联样式 + 每个文字节点 `<span leaf="">` 包裹，专门规避公众号会过滤的写法，粘进去不塌。
- **质量靠脚本不靠自觉** — 双关卡（源头 `component_lint` + 产物 `validate_gzh_html`）确定性检查平台红线和标点，不靠模型「记得住」。
- **换模型不走样** — 排版逻辑全沉淀在组件库和脚本里，不依赖某家模型，Claude / GPT / Gemini / 国产模型都能跑出一致效果。
- **Agent 友好** — 输入输出全是纯文本 Markdown / HTML，任何 Agent 都能读、写、改、验，天然适配 Claude Code / Codex / Cursor。

## 📁 目录结构

```
gzh-design/
├── SKILL.md                    # 排版工作流主文档（Agent 入口）
├── references/
│   ├── theme-index.md          # 6 套主题索引（主色/适用/下划线，单一来源）
│   ├── theme-*.md              # 6 套主题组件库（theme-moyu-green.md 等）
│   ├── theme-generator.md      # 主题生成器（按描述/参考图生成新主题）
│   ├── common-components.md    # 跨主题通用增量组件（代码块/图片/小标签）
│   ├── format-normalize.md     # 格式归一化（docx/pdf/纯文本 → Markdown）
│   └── eval-cases.md           # 触发用例 + 可验证循环
├── scripts/
│   ├── validate_gzh_html.py    # 产物合规校验
│   └── component_lint.py       # 组件库源头检查
├── assets/
│   ├── sample-article.md       # 演示输入
│   └── theme-previews/         # 主题生成器产出的区块库预览
└── docs/gallery/               # 主题浏览器预览
```

## 🎯 设计原则

- **约束而非自由** — 用预设主题色板和固定组件保证输出下限，不让模型现场发挥。
- **确定性下沉脚本** — 平台限制这类死规则交给校验脚本，模型只做内容判断。
- **小标签，不用虚线框** — 强调用左竖条/药丸标签，笨重的四周虚线框只留给「待补素材」居中占位。
- **每处经验都可复现** — 踩过的坑写进 gotchas 和校验脚本，用可验证循环防回归。
- **配方优于自由** — 先按文章类型查主题库的「配方表」定组件组合，再装配，同类文章排版气质稳定。
- **克制用色** — 主色只在锚点出现（全文 ≤5 处），大面积白底 + 灰阶，彩色只做点缀。
- **灰阶承重** — 约 90% 的文字交给一套中性灰阶，色彩不承担正文阅读，避免花哨。

## 🧠 方法论：不止 6 套，自己造主题

### 主题生成：一句话 / 一张参考图，现造一套新主题

内置 6 套不够用时不必等更新——让 AI 现造一套。背后是 [`references/theme-generator.md`](references/theme-generator.md) 定义的第二条工作流：

1. **收集偏好**（一次问全，不逐条追问）：主题描述必填（或给参考图），名称 / 主色 / 背景 / 正文色 / 强调色 / 装饰色 / 字体 / 圆角 / 阴影 / 适用场景可留空自动补全。
2. **生成区块库**：AI 产出 45~75 个区块的完整 HTML 组件库，存到 `assets/theme-previews/{id}.html`，浏览器整页一次浏览确认风格（不逐块问）。
3. **转标准主题库 + 登记**：确认后转成 `references/theme-{id}.md`（补 `<span leaf>`、补齐五章节：变量表 / 组件 / 骨架 / 配方表 / 映射表），登记进 theme-index，跑 `component_lint.py` 到 0 ERROR。
4. **即刻同权**：之后排版和内置主题完全一样，直接说「用 XX 主题排这篇」。

**怎么触发**：

> 按「黑白杂志、克莱因蓝点睛、衬线字体」的气质，给公众号排版生成一套新主题
>
> 按这张参考图（附图）做一套公众号排版组件库

仓库里 `assets/theme-previews/theme-mono-blue-editorial.html` 就是这样生成的一套「墨蓝刊读风」样例。

### 颜色搭配：一套可复制的配色结构，AI 自动生成协调色板

每套主题的视觉都建立在一张**设计变量色板**上——配色不是拍脑袋，而是固定的角色分工：

| 角色 | 作用 | 取色思路 |
|---|---|---|
| **主色** | 章节编号、锚点强调、封面点睛 | 一个有辨识度的品牌色（`#059669` emerald / `#DC2626` 正红 …）|
| **浅底 / 浅边框** | 卡片背景、引用块、标签底 | 主色同色系的极浅色（主色 + 大量白）|
| **点睛高亮色** | 每段 1~2 处黄底 / 渐变高亮 | 与主色冷暖对比的第二色（绿配黄）|
| **中性灰阶** | 正文 / 标题 / 辅助 / 分割线 | `#111827 → #9CA3AF` 一套灰阶，承担 90% 的文字 |
| **下划线标记色** | 正文关键词逐段标记 | 主色的浅色版（`#A7F3D0` / `#FECACA`），温和不抢戏 |

**克制三原则**：① 主色只在锚点出现（全文 ≤5 处）；② 大面积白底 + 灰阶，彩色只点缀；③ 一段内高亮 ≤2 种。

**让 AI 自动配**：只给一个主色或一句气质描述，主题生成器就据此推导整套协调色板——浅底、边框、高亮、灰阶、下划线色自动生成并保证可读对比度：

> 以 `#7C9EB2` 雾蓝为主色，生成一套清新旅行随笔风的公众号主题

## 🗺 Roadmap

- [x] 主题生成器：按描述/参考图生成自定义主题
- [ ] 更多精选内置主题（欢迎 [提建议](../../issues/new?template=theme_request.md)）
- [ ] 主题静态截图预览（docs/screenshots/）
- [ ] GitHub Pages 在线画廊
- [ ] 一键把整篇 Markdown + 配图打包导出

## ❓ FAQ

**Q：粘贴到公众号后样式会掉吗？**
A：不会。所有样式内联、文字 `<span leaf="">` 包裹，这正是校验脚本强制的重点。

**Q：能自己加主题吗？**
A：两种方式。① **让 AI 生成**：说「按这个风格 / 这张图生成一套公众号主题」，它会走 `references/theme-generator.md` 的流程生成组件库、登记并复用。② **手写贡献**：照 `CONTRIBUTING.md` 的「新增一套主题风格」，跑通可验证循环即可提 PR。

**Q：只能在 Claude Code 用吗？**
A：不限。任何能读取 Skill 目录的 Agent（Codex / Cursor 等）都能用，工作流在 `SKILL.md`。

**Q：对模型有要求吗？国产模型行不行？**
A：不挑模型，**国内外模型都能跑出一致效果**。排版逻辑全部沉淀在组件库和校验脚本里，不依赖某家模型的特殊能力——Claude、GPT、Gemini，以及 DeepSeek、Kimi、通义千问、智谱 GLM 等国产模型都可以。模型只负责按规则填充内容，硬约束由校验脚本确定性兜底，所以换模型不会导致排版走样。

**Q：能一次出多套主题对比吗？**
A：能。说「用这几套主题各排一遍这篇」即可批量生成多套供你挑。

**Q：怎么更新到最新版？**
A：重新跑 `npx skills add https://github.com/isjiamu/gzh-design-skill`，或到安装目录 `git pull`。

**Q：Agent 写出来不合规怎么办？**
A：跑 `scripts/validate_gzh_html.py`，报 ERROR 就回到装配步骤修；两关全绿才交付，仍有问题欢迎开 Issue。

## 📋 完整主题速查表

| 主色 | 主题 | 适用 |
|---|---|---|
| ![](https://placehold.co/12/059669/059669.png) `#059669` | 摸鱼绿（默认） | 教程、测评、清单、工具盘点 |
| ![](https://placehold.co/12/DC2626/DC2626.png) `#DC2626` | 红白色系 | 深度分析、观点、力量感话题 |
| ![](https://placehold.co/12/52525B/52525B.png) `#52525B` | 石墨极简风 | 设计、科技评论、专业观点、高端品牌 |
| ![](https://placehold.co/12/4A5D52/4A5D52.png) `#4A5D52` | 留白禅意风 | 禅意、极简生活、深度随笔 |
| ![](https://placehold.co/12/059669/059669.png) `#059669` | 摸鱼票据风 | 工具对比、创意评测（票据视觉隐喻） |
| ![](https://placehold.co/12/1e1f23/1e1f23.png) `#1e1f23` | 橄榄手记 | 内刊手记、深度评测、案例复盘 |

> 每套主题的英文标识、组件库文件、下划线 CSS 见 [`references/theme-index.md`](references/theme-index.md)。
> 需要别的风格？让 AI 用 [主题生成器](#-faq) 现生成一套。

## ⭐ Star History

如果这个项目帮到了你，点个 Star 支持一下～

<a href="https://www.star-history.com/?repos=isjiamu%2Fgzh-design-skill&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&theme=dark&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
 </picture>
</a>

## 🤝 贡献

欢迎新主题、修复与文档改进，请先读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📄 License

**AGPL-3.0 © 2026 甲木 × 摸鱼小李**

本项目采用 **GNU AGPL-3.0** 协议，要点：

1. **必须署名** — 保留版权与联名署名声明
2. **衍生品必须开源** — 任何修改版本、Fork、二次分发，必须以 AGPL-3.0（或兼容协议）公开发布，提供完整源代码
3. **网络服务也要开源** — 即使只是把修改版本部署成 SaaS / Web 服务给别人用而不分发代码，也要公开源代码（这是 AGPL 区别于 GPL 的核心）
4. **不允许闭源、专有化、仅付费分发**

完整条款见 [LICENSE](LICENSE)。

> 🤝 **欢迎 AI Agent 厂商、模型厂商共创**：想把 gzh-design 集成进产品、或基于它做深度共建，我们很欢迎——共创协议请联系甲木。

## 🙏 致谢

- 本项目由 **甲木 × 摸鱼小李** 联名共建：核心组件库与主题设计标准凝聚了两人的公众号排版实践。
- 质量工程（可验证循环）由 skill-optimizer 审计驱动打磨。

---

<div align="center">

<img src="https://origin.picgo.net/2026/07/07/22e8d28de5f71eee085939b2f4c1f19548b19a67a79bdb68.png" width="600" alt="甲木 × 摸鱼小李 公众号名片">

<sub>关注我们的公众号，获取更多 AI 干货与排版实践 👆</sub>

</div>
