# 通用增量组件库 —— 代码块 · 图片/GIF · 小标签标题 · 脚注/参考资料

> **跨所有主题通用**。主题专属组件（引言卡、章节标题、签名等）读各自主题库；本文件提供四类**所有主题都需要**的组件：代码块、图片/GIF、小标签标题、脚注/参考资料。
>
> **配色占位**：下面用红白色系（主色 `#DC2626`、浅底 `#FEF2F2`、浅标 `#FEE2E2`、深字 `#991B1B`）做示例。换其它主题时，把这几个值替换为该主题"设计变量速查表"里的对应色；代码块深色版各主题可共用，浅色版用主题主色做左竖条。
>
> **平台限制**：同主题库——禁 `<style>/<script>/class/id/div/position/float/@media/grid`，只用内联 + `flex`，文字全部 `<span leaf="">` 包裹。

---

## 一、代码块组件（Markdown ``` 围栏 → 这里）

文章里的代码、命令、Prompt 提示词、配置等，**必须用代码块组件**，不要塞进普通段落或引用块。代码块内的英文、半角符号、缩进都要原样保留（代码不适用"中文全角标点"规则）。

### 1a. 深色代码块（默认，技术感强，适配所有主题）

```html
<section style="margin:0 0 20px;border-radius:8px;overflow:hidden;background:#1E293B;box-shadow:0 4px 16px -8px rgba(15,23,42,0.4);">
  <section style="display:flex;align-items:center;padding:9px 14px;background:#0F172A;">
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#FF5F56;margin-right:7px;font-size:0;line-height:0;overflow:hidden;">.</span>
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#FFBD2E;margin-right:7px;font-size:0;line-height:0;overflow:hidden;">.</span>
    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#27C93F;font-size:0;line-height:0;overflow:hidden;">.</span>
    <span style="margin-left:12px;font-size:12px;color:#64748B;font-family:Consolas,Monaco,monospace;letter-spacing:1px;"><span leaf="">python</span></span>
  </section>
  <section style="padding:11px 14px;">
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">def make_skill(name):</span></p>
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">　　return f"已生成 {name}"</span></p>
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;"><span leaf="">print(make_skill("gzh-design"))</span></p>
  </section>
</section>
```

要点（**关键，避免大段空白**）：① 顶栏三色圆点 + 语言名（无语言可删该 span）；② **每行代码用一个 `<p style="margin:0;...">`，不要用 `white-space:pre`**——否则 HTML 源码里 span 前的缩进和行间换行会被原样渲染成大左缩进 + 空行；③ 需要缩进时在 span 文字里用全角空格 `　`（不要靠源码空格）；④ 行距只靠 `line-height:1.6` 控制，padding 用 `11px 14px`，保持紧凑；⑤ 长行会自动换行，不溢出。

### 1b. 浅色代码块（适配浅色温和主题，如玫瑰粉/天蓝/焦糖棕）

```html
<section style="margin:0 0 20px;border-radius:8px;overflow:hidden;background:#F6F8FA;border:1px solid #E5E7EB;border-left:3px solid #DC2626;">
  <section style="padding:7px 14px;border-bottom:1px solid #E5E7EB;">
    <span style="font-size:12px;color:#9CA3AF;font-family:Consolas,Monaco,monospace;letter-spacing:1px;"><span leaf="">bash</span></span>
  </section>
  <section style="padding:11px 14px;">
    <p style="margin:0;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#24292F;"><span leaf="">npx skills add gzh-design</span></p>
  </section>
</section>
```

（左竖条 `#DC2626` 换成当前主题主色；多行同 1a：每行一个 `<p style="margin:0">`，不用 `white-space:pre`，缩进用全角空格 `　`。）

### 1c. 行内代码（正文中的 `code` 短片段）

```html
<span style="background:#F1F5F9;color:#DC2626;padding:1px 6px;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:14px;"><span leaf="">SKILL.md</span></span>
```

（文字色 `#DC2626` 换主题主色；底色保持中性浅灰。）

---

## 二、图片 / GIF 组件（Markdown `![](...)` → 这里）

文章里**每一处图片、GIF、截图占位都要保留并转成下面的组件**，不得遗漏；`src` 原样保留用户给的 URL 或相对路径。GIF 动图与普通图片都用 `<img>`（公众号原生支持 GIF 自动播放），区别只在加不加"动图"角标说明。

### 2a. 标准图片（带说明）

```html
<section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom:8px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

无说明文字时删掉下方 `<p>`，并把图片容器 `margin-bottom` 改回 `10px`。

> **图片尺寸自适应**：`<img>` 用 `max-width:100%;height:auto;display:block;margin:0 auto`——按图片自身尺寸显示并居中，大图缩到容器宽、小图保持原尺寸，**不用 `width:100%` 强制铺满**（小图被拉伸会糊）。

### 2b. GIF 动图（同图片，加"GIF 动图"角标）

```html
<section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom:8px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="动图URL.gif" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
<p style="text-align:center;margin:0 0 24px;">
  <span style="display:inline-block;background:#FEE2E2;color:#991B1B;font-size:11px;font-weight:700;padding:1px 8px;border-radius:4px;margin-right:6px;"><span leaf="">GIF 动图</span></span>
  <span style="font-size:12px;color:#9CA3AF;"><span leaf="">动图说明文字</span></span>
</p>
```

（角标底色 `#FEE2E2` → 主题浅底色，字色 `#991B1B` → 主题深字色，取自该主题"设计变量速查表"；无色块的极简主题改用细线描边胶囊：边框与字色用主题主色、背景透明。）若原文只写了图片但没给 URL，用 `src="图片URL"` 占位并在交付时提醒用户补图，**不要凭空编造图床链接**。

---

### 2c. 待补素材占位（**居中板块**，用于 GIF / 录屏 / 视频 / 成果图待补处）

文章里 `【插入xxx】`、待录屏、待补 GIF/视频/截图等占位，一律用这个**居中**板块，不要用左对齐的提示块。所有排版风格通用，浅底柔虚线框 + 居中图标与说明，一眼看出"此处待补"。

```html
<section style="margin:0 0 24px;padding:30px 20px;border:1.5px dashed #DAD7D2;border-radius:14px;background:#FAFAF8;text-align:center;">
  <p style="margin:0 0 10px;font-size:26px;line-height:1;"><span leaf="">🎬</span></p>
  <p style="margin:0;font-size:14px;font-weight:700;color:#9CA3AF;letter-spacing:1px;"><span leaf="">待补素材</span></p>
  <p style="margin:8px 0 0;font-size:13px;color:#B8B5B0;line-height:1.7;"><span leaf="">此处插入：创建 skill 的录屏演示</span></p>
</section>
```

- 图标按素材类型换：🎬 视频/录屏、🖼 图片、📊 信息图、📎 附件。
- 这是**唯一允许用虚线框（dashed）的场景**——因为它表达"占位/待补"语义，与正文强调用的小标签不冲突。
- 各主题可把虚线色/底色微调成主题中性色，但保持居中、留白、柔和。

---

## 三、小标签标题组件（突出标题/强调，**替代虚线框**）

> **设计取向**：强调一段内容或起一个小标题时，优先用下面的"小标签 / 左竖条"形式，**不要用四周虚线框（dashed）包一个标题**——虚线框笨重、抢戏。小标签更轻、更现代。
>
> **使用优先级**：先查所选主题库的映射规则——主题库有等价语义组件（自己的金句块/提示块/小标题）就用主题库版本保持气质一致；没有时才用本节组件并按下面规则换色。
>
> **换色规则**（示例为红白色值，按所选主题"设计变量速查表"替换）：
> - 3a 左竖条 `#DC2626` → 主题主色；3b 药丸底 `#DC2626` → 主题主色（字保持白）
> - 3c 序号药丸底 `#FEE2E2` → 主题浅底色，序号字 `#991B1B` → 主题深字色
> - 3d/3e 块底 `#FEF2F2` → 主题浅底色，竖条/类型标签 `#DC2626` → 主题主色
> - **无色块的极简主题**（留白禅意/石墨极简等）：3a 竖条细化为 `2–3px`，3d/3e 去掉底色、只留左竖条 + 大留白，贴合该主题气质。

### 3a. 左竖条小标题（最推荐，干净）

```html
<p style="margin:28px 0 14px;font-size:16px;font-weight:800;color:#1C1917;line-height:1.5;border-left:4px solid #DC2626;padding-left:12px;">
  <span leaf="">小标题文字</span>
</p>
```

### 3b. 药丸标签小标题（实色底，最醒目）

```html
<p style="margin:28px 0 14px;">
  <span style="display:inline-block;background:#DC2626;color:#FFFFFF;font-size:14px;font-weight:700;padding:5px 16px;border-radius:6px;"><span leaf="">小标题文字</span></span>
</p>
```

### 3c. 序号药丸 + 标题（清单/步骤）

```html
<p style="margin:24px 0 12px;font-size:15px;font-weight:800;color:#1C1917;line-height:1.6;">
  <span style="display:inline-block;background:#FEE2E2;color:#991B1B;border-radius:5px;padding:1px 9px;margin-right:8px;font-weight:900;"><span leaf="">01</span></span>
  <span leaf="">要点标题</span>
</p>
```

### 3d. 金句引用（左竖条版，取代旧的虚线框金句）

```html
<section style="margin:0 0 24px;background:#FEF2F2;border-radius:0 10px 10px 0;border-left:4px solid #DC2626;padding:16px 20px;">
  <p style="font-size:16px;font-weight:800;color:#991B1B;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句」</span>
  </p>
</section>
```

### 3e. 提示 / 旁注块（左竖条 + 类型小标签，取代旧的虚线提示框）

```html
<section style="margin:0 0 24px;background:#FEF2F2;border-radius:0 8px 8px 0;border-left:4px solid #DC2626;padding:14px 18px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#DC2626;color:#FFFFFF;font-size:11px;font-weight:700;padding:2px 10px;border-radius:4px;letter-spacing:1px;"><span leaf="">提示</span></span>
  </p>
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;">
    <span leaf="">提示或旁注的正文内容</span>
  </p>
</section>
```

类型小标签文字可换：`提示` / `注意` / `重点` / `Prompt` / `旁注` 等。整块**没有任何 dashed 边框**，靠左竖条 + 浅底 + 小标签区分层次。

---

## 四、脚注 / 参考资料组件（Markdown `[text](url)` 超链接 → 这里）

> **触发**：正文里出现的 Markdown 超链接 `[text](url)`（图片链接 `![alt](url)` 走组件 2，不算；代码块围栏内的链接原样保留，不动）。公众号正文外链不可点击（见各主题"平台限制"），所以把超链接统一转成"正文 text + 上标编号 + 文末参考资料列表"的学术脚注形式，URL 作纯文本展示，**不要留可点击的 `<a>`**。
>
> **编号规则**：按链接在正文中**首次出现的顺序**递增编号 `[1] [2] …`；相同的 `(text,url)` 对复用同一编号（重复出现只标同一 `[n]`，不另起号）。
>
> **锚文本为空时**：`[](url)` 无锚文本，用 title 属性值；title 也空则用 URL 的域名作标签。
>
> **换色规则**（示例为红白色值，按所选主题"设计变量速查表"替换）：4a 上标 `#DC2626` → 主题主色；4b 标题左竖条 `#DC2626` → 主题主色、分隔线 `#FEE2E2` → 主题浅标色、编号 `#DC2626` → 主题主色、URL muted 色 `#9CA3AF` → 主题中性灰。
> - **无色块极简主题**（留白禅意/石墨极简等）：4a 去掉 `font-weight:700` 改 `font-weight:500`、颜色用主题主色；4b 标题改用该主题自有小标题组件（如细竖条版），去底色只留分隔线 + 大留白。

### 4a. 上标引用角标（inline，替换 `[text](url)` 里的链接部分）

正文里把 `[尤金·罗沙尔](url)` 替换为「尤金·罗沙尔 + 上标 `[1]`」：

```html
<span leaf="">尤金·罗沙尔</span><span leaf=""><sup style="font-size:0.62em;color:#DC2626;font-weight:700;vertical-align:super;line-height:0;margin-left:1px;"><span leaf="">[1]</span></sup></span>
```

- 编号 `[1]` 不可点击，仅作标记；`font-size:0.62em` 相对正文字号，`vertical-align:super` 上标。
- 与前面文字之间不加空格（紧贴锚文本），`margin-left:1px` 仅微调光学间距。
- `line-height:0` 防止上标撑高整行行距。

### 4b. 参考资料列表（文末区块，置于作者签名之前）

```html
<section style="margin:32px 0 0;padding:18px 10px 24px;border-top:1px solid #FEE2E2;">
  <p style="font-size:15px;font-weight:800;color:#1C1917;margin:0 0 14px;padding-left:10px;border-left:3px solid #DC2626;line-height:1.4;">
    <span leaf="">参考资料</span>
  </p>
  <p style="font-size:13px;color:#374151;margin:0 0 8px;line-height:1.9;">
    <span leaf=""><strong style="color:#DC2626;"><span leaf="">[1]</span></strong> 尤金·罗沙尔：<span style="color:#9CA3AF;word-break:break-all;">https://en.wikipedia.org/wiki/Eugene_Roshal</span></span>
  </p>
  <p style="font-size:13px;color:#374151;margin:0 0 8px;line-height:1.9;">
    <span leaf=""><strong style="color:#DC2626;"><span leaf="">[2]</span></strong> 第二条锚文本：<span style="color:#9CA3AF;word-break:break-all;">https://example.com/second</span></span>
  </p>
</section>
```

- 标题用左竖条小标题样式（同 3a 取向）；标题文字默认"参考资料"（原文用了"参考"/"来源"/"引用"等就照原文）。
- 每条一行 `<p>`（不用 `<ol>`，公众号对列表语义支持不稳）：`[n] 锚文本：URL`，编号主题主色加粗、锚文本正文色、URL muted 色 + `word-break:break-all` 防长链接溢出。
- **列表顺序与正文上标 `[n]` 一一对应**；正文里复用编号的，列表里只列一次。
- **位置**：放在正文最后一段之后、作者签名组件之前。文中无任何超链接时，不生成此区块。

---

## 选用速记

| 文章里出现 | 用哪个组件 |
|---|---|
| ` ``` 代码 / 命令 / Prompt 围栏 ``` ` | 1a 深色（默认）或 1b 浅色代码块 |
| 行内 `` `code` `` | 1c 行内代码 |
| `![](图片)` | 2a 标准图片 |
| `![](xxx.gif)` 或注明动图 | 2b GIF 动图 |
| 想给一段起小标题 / 强调 | 3a 左竖条（首选）/ 3b 药丸 / 3c 序号 |
| `> 金句` | 3d 金句左竖条块 |
| 提示 / 注意 / 旁注 | 3e 提示左竖条块（**不要用虚线框**） |
| 正文 `[text](url)` 超链接 | 4a 上标角标（正文）+ 4b 参考资料列表（文末） |
