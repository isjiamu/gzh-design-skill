# 贡献指南 · Contributing

欢迎为 gzh-design 贡献新主题风格、修复排版问题或改进文档。

## 项目结构速览

- `SKILL.md` — 排版工作流主文档（Agent 入口）
- `references/` — 6 套主题组件库 + 通用增量库 + 主题索引 + 主题生成器 + 触发用例
- `scripts/` — 两个校验脚本（见下方「可验证循环」）
- `assets/` — 演示输入文章
- `docs/gallery/` — 主题风格的浏览器预览

## 可验证循环（改动前后都要跑）

任何改动组件库或 SKILL 后，按这个双关卡闭环自检，两关全绿才提 PR：

```bash
# 源头关：扫所有组件库的 HTML 块，查大空白 / 正文虚线框 / 平台禁用项
python3 scripts/component_lint.py .

# 产物关：用改动后的 skill 排版 assets/sample-article.md，再校验产物
python3 scripts/validate_gzh_html.py <生成的.html>
```

- `component_lint.py` 须 **0 ERROR**
- `validate_gzh_html.py` 须 **0 ERROR、半角标点 0 WARN**

细节见 `references/eval-cases.md` 的「维护 · 可验证循环」一节。

## 新增一套主题风格

1. 照 `references/theme-red-white.md` 的结构，新建一份 `references/theme-{你的英文标识}.md`（如 `theme-ocean-breeze.md`；内含设计变量 + 各组件 HTML + 模板骨架 + 映射规则，标题里的风格显示名可用中文）。
2. 硬性约束：所有样式内联、文字用 `<span leaf="">` 包裹、禁 `div/class/id/style/grid/position/var/@media`、正文强调用左竖条或小标签而**非四周虚线框**、代码块用「每行一个 `<p>`」而**非 `white-space:pre`**。
3. 在 `references/theme-index.md` 登记（主色 + 适用场景 + 组件库文件 + 正文下划线 CSS）。
4. 跑可验证循环，两关全绿。
5. 提 PR，附上用 `assets/sample-article.md` 生成的预览 HTML。

## 提交规范

- 一个 PR 只做一件事（一套新主题 / 一处修复 / 一处文档）。
- commit 信息说清「改了什么 + 为什么」。
- 不要提交本地排版产物（`.gitignore` 已忽略 `*_排版_*.html`）。
