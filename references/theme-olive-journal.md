# 公众号排版组件库 —— 橄榄手记

> **使用说明**：本组件库为「橄榄手记」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：内刊/编辑部手记质感——米白纸感底 + 墨黑强调 + 橄榄灰边框，橙色作画龙点睛的强调色，陶土棕作次强调/进行中状态色。信息密度偏高、分节形式多样（刊头条/期号徽章/前导词标题交替使用），适合系统性说明文档、深度评测、案例复盘一类内容，气质克制、理性、略带"内部资料"的严肃感。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（含 `gap`）、`box-shadow`、`border-radius`、`<svg>`（流程图/图标，微信支持）、`<section>/<p>/<span>/<strong>/<img>/<h3>/<h4>/<figure>/<figcaption>/<hr>/<ul>/<li>` 等基础标签
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 原始设计稿里出现的 `id="block-*"`、`class="..."`、`display:grid` 均已在下方组件中清除/替换为 `display:flex`，新增组件时同样不能带这三样
> - 行内代码一律用 `<span>` 模拟（不用 `<code>` 标签），风格与通用库 1c 保持同源
> - 图片一律只保留 `src`/`alt`/`style`，不要带 `class`/`data-ratio`/`data-w`/`data-imgqrcoded` 等编辑器内部属性
> - 流程示意图（组件 23）内文字用 SVG `<tspan leaf="">` 而非 `<span leaf="">`——SVG 是原子渲染，不受微信富文本重排影响，校验脚本可能仍会把这几处计入"未包裹"warning，属已知误报，可忽略

---

## 设计变量速查表

```
主题墨色（强调/CTA/深底）：      #1e1f23
标题色：                       #23251d
正文色：                       #4d4f46
次要文字：                     #65675e
弱化文字：                     #9ea096
边框/分隔线：                   #bfc1b7
米白背景：                     #fdfdf8
浅橄榄灰背景：                   #eeefe9
标签浅底：                     #e5e7e0
强调橙（关键词下划线/前导词/CTA）： #ed7b2f
陶土棕装饰（进行中/次强调）：       #d4c9b8（配边框 #b17816）
正文字号：                     14px
正文行高：                     1.9
全局行高：                     1.75
最大宽度：                     677px
容器内边距：                   8px
区块间距：                     margin-top: 24px（首块头图卡除外）
圆角：                         6px（统一小圆角，不用大圆角）
阴影：                         整体几乎无阴影，靠边框 + 色块分层，仅头图卡的插画占位区可有极轻装饰
```

字体栈：`'IBM Plex Sans',-apple-system,system-ui,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

**正文关键词下划线**（对应 theme-index"正文下划线 CSS"列）：`border-bottom:2px solid #ed7b2f;font-weight:600;color:#23251d;`——直接复用本主题头图卡"强调词"与重点观点卡里已经出现的橙色下划线语言，保持主题内一致。

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;padding:8px;box-sizing:border-box;background:#fdfdf8;color:#4d4f46;font-family:'IBM Plex Sans',-apple-system,system-ui,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.75;">

  <!-- 所有组件放在这里，第一个子元素是组件 2 头图卡，其余组件均自带 margin-top:24px -->

</section>
```

---

## 组件 2 头图卡 hero-card

**用途**：文章开篇头图区，内刊风格：顶部标签+日期条，主标题+强调词，侧边配一枚手绘风占位插画，底部深色摘要条收尾。整篇文章唯一一处、放在最前面，不设 `margin-top`。

**可替换字段**：`{{内刊标签}}` `{{日期}}` `{{旧标题占位}}`（可选，删除线小字，无需要时整行删除）`{{主标题}}` `{{强调词}}` `{{副标题说明}}` `{{底部摘要}}` `{{标签1}}` `{{标签2}}`

```html
<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;font-family:'IBM Plex Sans',-apple-system,system-ui,sans-serif;">
  <section style="padding:28px 24px 22px;">
    <section style="display:flex;align-items:center;gap:8px;margin-bottom:22px;">
      <span style="width:8px;height:8px;background:#1e1f23;border-radius:50%;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
      <span style="font-size:10px;font-weight:700;letter-spacing:3px;color:#65675e;"><span leaf="">{{内刊标签}}</span></span>
      <span style="flex:1;height:1px;background:#bfc1b7;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
      <span style="font-size:10px;color:#9ea096;font-weight:500;font-variant-numeric:tabular-nums;"><span leaf="">{{日期}}</span></span>
    </section>
    <section style="display:flex;align-items:stretch;gap:18px;">
      <section style="flex:1;min-width:0;">
        <p style="font-size:14px;color:#9ea096;margin:0 0 8px;letter-spacing:0.3px;text-decoration:line-through;"><span leaf="">{{旧标题占位}}</span></p>
        <p style="font-size:24px;font-weight:800;color:#23251d;margin:0 0 10px;line-height:1.15;letter-spacing:-0.75px;">
          <span leaf="">{{主标题}}</span><span style="color:#4d4f46;"><span leaf="">&nbsp;·&nbsp;</span></span><span style="border-bottom:3px solid #e5e7e0;"><span leaf="">{{强调词}}</span></span>
        </p>
        <section style="display:flex;align-items:center;gap:4px;margin-bottom:12px;">
          <span style="width:22px;height:3px;background:#1e1f23;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
          <span style="width:8px;height:3px;background:#bfc1b7;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
        </section>
        <p style="font-size:13px;color:#65675e;margin:0;line-height:1.7;"><span leaf="">{{副标题说明}}</span></p>
      </section>
      <section style="flex-shrink:0;width:112px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#eeefe9;border:1px dashed #bfc1b7;text-align:center;border-radius:6px;padding:8px;">
        <svg width="72" height="72" viewBox="0 0 64 64" aria-hidden="true" style="display:block;">
          <ellipse cx="32" cy="36" rx="22" ry="18" fill="none" stroke="#4d4f46" stroke-width="2"></ellipse>
          <circle cx="26" cy="30" r="3" fill="#4d4f46"></circle>
          <circle cx="38" cy="30" r="3" fill="#4d4f46"></circle>
          <path d="M28 40 Q32 44 36 40" fill="none" stroke="#4d4f46" stroke-width="1.5"></path>
          <path d="M12 34 L8 28 M52 34 L56 28" stroke="#bfc1b7" stroke-width="2" stroke-linecap="round"></path>
        </svg>
        <span style="font-size:8px;font-weight:700;color:#9ea096;letter-spacing:1px;margin-top:4px;"><span leaf="">DOODLE</span></span>
      </section>
    </section>
  </section>
  <section style="background:#1e1f23;padding:11px 24px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">
    <p style="font-size:12px;color:rgba(255,255,255,0.92);margin:0;font-weight:600;"><span leaf="">{{底部摘要}}</span></p>
    <section style="display:flex;gap:6px;flex-wrap:wrap;">
      <span style="background:#e5e7e0;color:#23251d;padding:3px 8px;border-radius:4px;font-size:8px;font-weight:700;border:1px solid #bfc1b7;"><span leaf="">{{标签1}}</span></span>
      <span style="background:#e5e7e0;color:#23251d;padding:3px 8px;border-radius:4px;font-size:8px;font-weight:700;border:1px solid #bfc1b7;"><span leaf="">{{标签2}}</span></span>
    </section>
  </section>
</section>
```

（`{{旧标题占位}}` 那一行没有真实"旧标题"内容时整行 `<p>` 删除，不留占位删除线空行。）

---

## 组件 3 章节标题 section-title

**用途**：大章节分隔，默认编号形式 01/02/03…，本主题最常用的章节标题。

**可替换字段**：`{{编号}}` `{{标题}}` `{{副标题}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;align-items:center;gap:14px;">
      <section style="text-align:center;flex-shrink:0;">
        <p style="margin:0;font-size:24px;font-weight:800;color:#23251d;line-height:1;letter-spacing:-2px;"><span leaf="">{{编号}}</span></p>
        <p style="margin:0;font-size:8px;font-weight:700;color:#9ea096;letter-spacing:2px;"><span leaf="">PART</span></p>
      </section>
      <span style="width:1px;height:36px;background:#bfc1b7;flex-shrink:0;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
      <section>
        <p style="margin:0 0 1px;font-size:17px;font-weight:800;color:#23251d;letter-spacing:0.2px;"><span leaf="">{{标题}}</span></p>
        <p style="margin:0;font-size:11px;font-weight:600;color:#65675e;letter-spacing:1.2px;"><span leaf="">{{副标题}}</span></p>
      </section>
    </section>
  </section>
</section>
```

---

## 组件 4 内刊标签条 masthead-minimal-label

**用途**：轻量分节条，比章节标题更轻，适合章节之间的期号/存档标记，或不需要大标题的小节过渡。

**可替换字段**：`{{刊头标签}}` `{{版本号}}` `{{存档说明}}`

```html
<section style="margin-top:24px;">
  <section style="background:#eeefe9;border:1px solid #bfc1b7;border-radius:6px;padding:12px 16px;font-family:'IBM Plex Sans',-apple-system,sans-serif;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">
    <p style="margin:0;font-size:10px;font-weight:800;letter-spacing:4px;color:#23251d;"><span leaf="">{{刊头标签}}</span></p>
    <section style="display:flex;gap:8px;flex-wrap:wrap;">
      <span style="font-size:10px;color:#65675e;font-weight:700;"><span leaf="">{{版本号}}</span></span>
      <span style="font-size:10px;color:#9ea096;"><span leaf="">{{存档说明}}</span></span>
    </section>
  </section>
</section>
```

---

## 组件 5 暗色标题条 masthead-black-strip

**用途**：强调型分节条，深色底，适合专题/特辑开篇，比组件 4 更重、更醒目，一篇文章慎用（≤1-2 处）。

**可替换字段**：`{{刊头标签}}` `{{说明文字}}`

```html
<section style="margin-top:24px;">
  <section style="background:#1e1f23;border:1px solid #23251d;border-radius:6px;overflow:hidden;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;">
      <p style="margin:0;font-size:10px;font-weight:800;letter-spacing:4px;color:#ffffff;"><span leaf="">{{刊头标签}}</span></p>
      <p style="margin:0;font-size:10px;color:rgba(255,255,255,0.68);"><span leaf="">{{说明文字}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 6 期号徽章条 masthead-issue-badge

**用途**：圆形编号徽章 + 说明，适合子章节或专题起始，比组件 3 章节标题更紧凑、更像"期刊卷号"。

**可替换字段**：`{{期号}}` `{{标题}}` `{{说明}}` `{{卷标}}`

```html
<section style="margin-top:24px;">
  <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:14px 16px;font-family:'IBM Plex Sans',-apple-system,sans-serif;display:flex;align-items:center;justify-content:space-between;gap:10px;">
    <section style="display:flex;align-items:center;gap:10px;">
      <span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:#1e1f23;color:#fff;font-size:11px;font-weight:800;"><span leaf="">{{期号}}</span></span>
      <section>
        <p style="margin:0 0 3px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;"><span leaf="">{{标题}}</span></p>
        <p style="margin:0;font-size:11px;color:#65675e;"><span leaf="">{{说明}}</span></p>
      </section>
    </section>
    <span style="font-size:10px;color:#9ea096;"><span leaf="">{{卷标}}</span></span>
  </section>
</section>
```

---

## 组件 7 步骤内联标题 step-heading-inline

**用途**：教程类文章的步骤小标题，"Step N" 药丸标签 + 标题文字，一行紧凑呈现。

**可替换字段**：`{{步骤序号}}` `{{步骤标题}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;align-items:center;gap:10px;">
      <span style="background:#1e1f23;color:#fff;padding:4px 10px;border-radius:4px;font-size:11px;font-weight:700;"><span leaf="">{{步骤序号}}</span></span>
      <span style="font-size:14px;font-weight:600;color:#4d4f46;"><span leaf="">{{步骤标题}}</span></span>
    </section>
  </section>
</section>
```

---

## 组件 8 强调标题 highlight-title

**用途**：三级标题，底纹强调（荧光笔式内阴影），比组件 7/9 更强调"标题本身值得注意"，适合观点类文章的核心论点小标题。

**可替换字段**：`{{标题文字}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <h3 style="font-size:18px;font-weight:700;color:#23251d;margin:0;padding:0 2px;display:block;width:fit-content;box-shadow:inset 0 -0.5em 0 rgba(245,78,0,0.18);"><span leaf="">{{标题文字}}</span></h3>
  </section>
</section>
```

---

## 组件 9 前导词标题 kicker-title

**用途**：带前导词（Kicker）+ 进度指示的标题，适合系列文章的分节，右侧可标"当前/总数"。

**可替换字段**：`{{Kicker标签}}` `{{标题}}` `{{进度}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;align-items:flex-end;gap:12px;flex-wrap:wrap;border-bottom:1px solid #bfc1b7;padding-bottom:10px;">
      <span style="font-size:10px;font-weight:800;letter-spacing:3px;color:#ed7b2f;text-transform:uppercase;"><span leaf="">{{Kicker标签}}</span></span>
      <span style="font-size:18px;font-weight:800;color:#23251d;line-height:1.2;"><span leaf="">{{标题}}</span></span>
      <span style="margin-left:auto;font-size:10px;color:#9ea096;font-variant-numeric:tabular-nums;"><span leaf="">{{进度}}</span></span>
    </section>
  </section>
</section>
```

---

## 组件 10 正文段落 richtext-paragraph

**用途**：普通正文，可内嵌下方"文字强调 a-e"任意子样式。字号/颜色/行高是本主题铁律。

**可替换字段**：`{{正文内容}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="margin:0;font-size:14px;line-height:1.9;text-align:justify;color:#4d4f46;">
      <span leaf="">{{正文内容}}</span>
    </p>
  </section>
</section>
```

### 文字强调（5 种子样式，正文段落内使用，一段不叠加超过 2 种）

**a. 强调加粗** —— 重要术语/产品名

```html
<strong style="color:#23251d;"><span leaf="">{{文字}}</span></strong>
```

**b. 浅底高亮框** —— 关键信息/数据

```html
<span style="background:#eeefe9;padding:1px 5px;border-radius:4px;font-weight:600;color:#23251d;border:1px solid #bfc1b7;"><span leaf="">{{文字}}</span></span>
```

**c. 橙色下划线** —— 重要短语（正文关键词的默认标记，对应 theme-index 权威下划线值）

```html
<span style="border-bottom:2px solid #ed7b2f;font-weight:600;color:#23251d;"><span leaf="">{{文字}}</span></span>
```

**d. 行内代码标签** —— 技术名词/字段名/命令

```html
<span style="background:#eeefe9;color:#23251d;padding:2px 6px;border-radius:4px;font-family:ui-monospace,Menlo,Monaco,Consolas,monospace;font-size:13px;border:1px solid #b6b7af;"><span leaf="">{{代码}}</span></span>
```

**e. 删除线旧词** —— 与"新旧对照段落"（组件 12）配套，单独用时表示"已废弃/被替代的说法"

```html
<span style="color:#9ea096;text-decoration:line-through;"><span leaf="">{{旧文字}}</span></span>
```

---

## 组件 11 行内代码段落 inline-code-paragraph

**用途**：正文中需要突出一小段代码/命令/字段名的整句表达（比文字强调 d 更完整的一句话场景）。

**可替换字段**：`{{正文前半}}` `{{代码}}` `{{正文后半}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="margin:0;font-size:14px;color:#4d4f46;line-height:1.9;">
      <span leaf="">{{正文前半}}&nbsp;</span><span style="background:#eeefe9;color:#23251d;padding:2px 6px;border-radius:4px;font-family:ui-monospace,Menlo,Monaco,Consolas,monospace;font-size:13px;border:1px solid #b6b7af;"><span leaf="">{{代码}}</span></span><span leaf="">&nbsp;{{正文后半}}</span>
    </p>
  </section>
</section>
```

---

## 组件 12 新旧对照段落 before-after-paragraph

**用途**：术语变更、观点修正、版本对比等"从 A 到 B"的一句话表达。

**可替换字段**：`{{旧表述}}` `{{新表述}}` `{{差异点}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="margin:0;font-size:14px;line-height:1.9;text-align:justify;color:#4d4f46;">
      <span style="font-size:14px;color:#9ea096;letter-spacing:0.3px;text-decoration:line-through;"><span leaf="">{{旧表述}}</span></span>
      <span style="margin-left:6px;font-weight:700;color:#23251d;"><span leaf="">{{新表述}}</span></span>
      <span style="margin-left:6px;background:#e5e7e0;padding:1px 5px;border-radius:4px;font-weight:600;color:#23251d;border:1px solid #bfc1b7;"><span leaf="">{{差异点}}</span></span>
    </p>
  </section>
</section>
```

---

## 组件 13 无序列表 bullet-list-basic

**用途**：简单并列条目，不需要标题+说明两层结构时用它（需要两层结构用组件 24）。

**可替换字段**：`{{列表项}}`（可重复 N 次）

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <ul style="margin:0;padding-left:22px;line-height:1.8;list-style-position:outside;">
      <li style="margin-bottom:8px;font-size:15px;color:#4d4f46;list-style-type:disc;">
        <section><span leaf="">{{列表项}}</span></section>
      </li>
    </ul>
  </section>
</section>
```

---

## 组件 14 编者按 editors-note

**用途**：深色标题条 + 浅底正文，用于章节前的提醒/背景说明，也可用作文章开头的引言卡。

**可替换字段**：`{{批注标签}}`（如 `EDITOR'S NOTE`）`{{批注小字}}` `{{编者按正文}}`

```html
<section style="margin-top:24px;">
  <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="padding:10px 16px;background:#1e1f23;display:flex;align-items:center;justify-content:space-between;gap:10px;">
      <p style="margin:0;font-size:10px;font-weight:800;letter-spacing:2px;color:#ffffff;"><span leaf="">{{批注标签}}</span></p>
      <span style="font-size:10px;color:rgba(255,255,255,0.65);"><span leaf="">{{批注小字}}</span></span>
    </section>
    <section style="padding:16px 18px 18px;background:#eeefe9;">
      <p style="margin:0;font-size:14px;line-height:1.9;color:#4d4f46;text-align:justify;"><span leaf="">{{编者按正文}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 15 重点观点卡 key-point-card

**用途**：段落级重点强调，比正文强调更完整——独立成一张卡片，内部用橙色下划线扣题。

**可替换字段**：`{{重点观点}}` `{{补充说明}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="background:#fdfdf8;border-radius:6px;padding:16px 18px;border:1px solid #bfc1b7;">
      <p style="font-size:14px;color:#4d4f46;margin:0;line-height:1.8;text-align:justify;">
        <strong style="color:#23251d;border-bottom:3px solid #ed7b2f;"><span leaf="">{{重点观点}}</span></strong><span leaf="">&nbsp;{{补充说明}}</span>
      </p>
    </section>
  </section>
</section>
```

---

## 组件 16 分割线 divider-solid

**用途**：简单实线分割，章节内部小段落之间的轻量切分。

```html
<section style="margin-top:24px;">
  <hr style="border:none;height:2px;background:#bfc1b7;margin:0;">
</section>
```

---

## 组件 17 分割点 divider-dots

**用途**：三色点缀分隔符，比实线更轻、更有设计感，适合情绪/生活类内容的段落间隔。

```html
<section style="margin-top:24px;">
  <section style="display:flex;align-items:center;justify-content:center;gap:10px;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <span style="width:8px;height:8px;border-radius:50%;background:#4d4f46;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
    <span style="width:8px;height:8px;border-radius:50%;background:#bfc1b7;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
    <span style="width:8px;height:8px;border-radius:50%;background:#ed7b2f;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
  </section>
</section>
```

---

## 组件 18 通栏图片 media-full-bleed-image

**用途**：无说明文字的通栏大图，边到边出血效果（负边距抵消容器 8px 内边距，让图片视觉上顶到最边缘）。

**可替换字段**：`{{图片URL}}`

```html
<section style="margin-top:24px;">
  <section style="padding:0 8px;margin:0 -8px;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="background:#fdfdf8;border-radius:6px;padding:6px;border:1px solid #bfc1b7;">
      <figure style="margin:0;border-radius:4px;overflow:hidden;">
        <span leaf=""><img src="{{图片URL}}" alt="通栏图片" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
      </figure>
    </section>
  </section>
</section>
```

---

## 组件 19 图片卡 image-card

**用途**：带说明文字的图片，`<img>` 的 `src` 原样保留用户给的 URL，不改写。

**可替换字段**：`{{图片URL}}` `{{图片说明}}`

```html
<section style="margin-top:24px;">
  <figure style="font-family:'IBM Plex Sans',-apple-system,sans-serif;margin:0;">
    <section style="border-radius:6px;overflow:hidden;border:1px solid #bfc1b7;display:block;">
      <span leaf=""><img src="{{图片URL}}" alt="图片" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
    </section>
    <figcaption style="font-size:13px;line-height:1.7;color:#65675e;text-align:center;margin-top:10px;"><span leaf="">{{图片说明}}</span></figcaption>
  </figure>
</section>
```

无说明文字时删掉 `<figcaption>`。

---

## 组件 20 图表占位卡 chart-card

**用途**：图表/可视化的占位展示区，标签+占位框。有真实图表图片时，把占位框内容换成组件 19 的图片写法。

**可替换字段**：`{{图表标签}}`（如 `CHART`）`{{占位说明}}`

```html
<section style="margin-top:24px;">
  <section style="padding:18px;border-radius:6px;background:#fdfdf8;border:1px solid #bfc1b7;text-align:center;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="margin:0 0 12px;font-size:12px;color:#65675e;font-weight:700;letter-spacing:1px;"><span leaf="">{{图表标签}}</span></p>
    <section style="min-height:140px;border-radius:6px;background:#eeefe9;display:flex;align-items:center;justify-content:center;border:1px dashed #bfc1b7;">
      <span style="font-size:14px;color:#4d4f46;"><span leaf="">{{占位说明}}</span></span>
    </section>
  </section>
</section>
```

---

## 组件 21 对比摘要卡 compare-summary

**用途**：二元对比（A vs B），左右两栏，一侧深底强调、一侧浅底常规，`vs` 居中分隔。

**可替换字段**：`{{左侧标题}}` `{{左侧说明}}` `{{右侧标题}}` `{{右侧说明}}`

```html
<section style="margin-top:24px;">
  <section style="background:#eeefe9;padding:16px;border-radius:6px;border:1px solid #bfc1b7;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;align-items:stretch;justify-content:center;gap:8px;">
      <section style="flex:1;text-align:center;padding:10px 8px;background:#1e1f23;border-radius:6px;border:1px solid #23251d;">
        <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;"><span leaf="">{{左侧标题}}</span></p>
        <p style="font-size:10px;color:rgba(255,255,255,0.75);margin:0;line-height:1.5;"><span leaf="">{{左侧说明}}</span></p>
      </section>
      <section style="display:flex;align-items:center;color:#bfc1b7;font-size:14px;padding:0 4px;"><span leaf="">vs</span></section>
      <section style="flex:1;text-align:center;padding:10px 8px;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;">
        <p style="font-size:13px;font-weight:800;color:#23251d;margin:0 0 3px;"><span leaf="">{{右侧标题}}</span></p>
        <p style="font-size:10px;color:#65675e;margin:0;line-height:1.5;"><span leaf="">{{右侧说明}}</span></p>
      </section>
    </section>
  </section>
</section>
```

---

## 组件 22 精简对照表 compare-table-lite

**用途**：真实数据/维度对照表格语义（参数表、字段表），用 `flex` 仿表格结构（不用 `table`/`grid`）。行数按需重复"数据行"结构。

**可替换字段**：`{{维度列名}}` `{{方案A名}}` `{{方案B名}}` + 每行 `{{行标题}}` `{{A值}}` `{{B值}}`

```html
<section style="margin-top:24px;">
  <section style="border-radius:6px;overflow:hidden;border:1px solid #bfc1b7;background:#fdfdf8;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;background:#eeefe9;border-bottom:1px solid #bfc1b7;">
      <section style="width:35%;padding:10px 12px;font-size:12px;font-weight:800;color:#23251d;"><span leaf="">{{维度列名}}</span></section>
      <section style="width:32.5%;padding:10px 12px;font-size:12px;font-weight:800;color:#23251d;border-left:1px solid #bfc1b7;"><span leaf="">{{方案A名}}</span></section>
      <section style="width:32.5%;padding:10px 12px;font-size:12px;font-weight:800;color:#23251d;border-left:1px solid #bfc1b7;"><span leaf="">{{方案B名}}</span></section>
    </section>
    <section style="display:flex;border-bottom:1px solid #bfc1b7;">
      <section style="width:35%;padding:10px 12px;font-size:13px;color:#4d4f46;"><span leaf="">{{行标题}}</span></section>
      <section style="width:32.5%;padding:10px 12px;font-size:13px;color:#23251d;border-left:1px solid #bfc1b7;"><span leaf="">{{A值}}</span></section>
      <section style="width:32.5%;padding:10px 12px;font-size:13px;color:#23251d;border-left:1px solid #bfc1b7;"><span leaf="">{{B值}}</span></section>
    </section>
    <section style="display:flex;">
      <section style="width:35%;padding:10px 12px;font-size:13px;color:#4d4f46;"><span leaf="">{{行标题}}</span></section>
      <section style="width:32.5%;padding:10px 12px;font-size:13px;color:#23251d;border-left:1px solid #bfc1b7;"><span leaf="">{{A值}}</span></section>
      <section style="width:32.5%;padding:10px 12px;font-size:13px;color:#23251d;border-left:1px solid #bfc1b7;"><span leaf="">{{B值}}</span></section>
    </section>
  </section>
</section>
```

（最后一行不带 `border-bottom`；行数不止 2 行时，中间行都带 `border-bottom:1px solid #bfc1b7`，只有最后一行不带。）

---

## 组件 23 流程示意图 flow-diagram

**用途**：技术流程/数据管线一类"从输入到输出"的示意图，SVG 绘制，节点用矩形+箭头连接，末端用深色终点框强调结果。

**可替换字段**：`{{FLOW标签}}` `{{流程说明}}` `{{图示脚注}}`，以及图中各节点文字（`SDK`/`ingest`/`队列`/`规则`/`聚合`/`输出`/`图表`/`live` 等，按实际流程改写）

```html
<section style="margin-top:24px;">
  <section style="background:#eeefe9;border-radius:6px;padding:22px 18px;border:1px solid #bfc1b7;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="font-size:10px;color:#65675e;margin:0 0 4px;text-transform:uppercase;letter-spacing:2px;font-weight:600;"><span leaf="">{{FLOW标签}}</span></p>
    <p style="font-size:13px;color:#23251d;font-weight:600;margin:0 0 8px;"><span leaf="">{{流程说明}}</span></p>
    <svg viewBox="0 0 400 82" style="width:100%;height:auto;" role="img" aria-label="流程示意">
      <rect x="2" y="14" width="58" height="48" rx="4" fill="#fdfdf8" stroke="#4d4f46" stroke-width="1.5"></rect>
      <text x="31" y="34" font-size="9" fill="#23251d" text-anchor="middle" font-weight="700" font-family="IBM Plex Sans,sans-serif"><tspan leaf="">节点一</tspan></text>
      <text x="31" y="48" font-size="8" fill="#65675e" text-anchor="middle"><tspan leaf="">说明</tspan></text>
      <line x1="66" y1="38" x2="82" y2="38" stroke="#4d4f46" stroke-width="1.5"></line>
      <polygon points="82,34 90,38 82,42" fill="#4d4f46"></polygon>
      <rect x="96" y="6" width="210" height="64" rx="6" fill="#fdfdf8" stroke="#bfc1b7" stroke-width="1"></rect>
      <text x="201" y="18" font-size="7" fill="#9ea096" text-anchor="middle" font-weight="600" letter-spacing="1"><tspan leaf="">处理层</tspan></text>
      <rect x="104" y="26" width="42" height="36" rx="4" fill="#e5e7e0" stroke="#bfc1b7"></rect>
      <text x="125" y="48" font-size="8" fill="#23251d" text-anchor="middle" font-weight="600"><tspan leaf="">节点二</tspan></text>
      <rect x="152" y="26" width="42" height="36" rx="4" fill="#e5e7e0" stroke="#bfc1b7"></rect>
      <text x="173" y="48" font-size="8" fill="#23251d" text-anchor="middle" font-weight="600"><tspan leaf="">节点三</tspan></text>
      <rect x="200" y="26" width="42" height="36" rx="4" fill="#e5e7e0" stroke="#bfc1b7"></rect>
      <text x="221" y="48" font-size="8" fill="#23251d" text-anchor="middle" font-weight="600"><tspan leaf="">节点四</tspan></text>
      <rect x="248" y="26" width="50" height="36" rx="4" fill="#d4c9b8" stroke="#b17816"></rect>
      <text x="273" y="48" font-size="8" fill="#23251d" text-anchor="middle" font-weight="600"><tspan leaf="">输出</tspan></text>
      <line x1="312" y1="38" x2="328" y2="38" stroke="#4d4f46" stroke-width="1.5"></line>
      <polygon points="328,34 336,38 328,42" fill="#4d4f46"></polygon>
      <rect x="340" y="12" width="56" height="52" rx="4" fill="#1e1f23"></rect>
      <text x="368" y="36" font-size="8" fill="#fff" text-anchor="middle" font-weight="700"><tspan leaf="">结果</tspan></text>
      <text x="368" y="50" font-size="8" fill="#ed7b2f" text-anchor="middle" font-weight="700"><tspan leaf="">live</tspan></text>
    </svg>
    <p style="font-size:11px;color:#65675e;margin:14px 0 0;border-top:1px solid #bfc1b7;padding-top:12px;line-height:1.5;"><span leaf="">{{图示脚注}}</span></p>
  </section>
</section>
```

---

## 组件 24 条目列表卡 item-list-card

**用途**：标题+说明两层结构的并列条目（比组件 13 无序列表信息量更大），胶囊标题 + 圆点色标 + 说明段落，可重复 N 次。

**可替换字段**：`{{条目标题}}` `{{条目说明}}`；圆点颜色可在 `#ed7b2f`（强调）/`#4d4f46`（常规）间轮换区分条目类型

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="margin-bottom:14px;">
      <p style="margin:0 0 6px;">
        <span style="display:inline-block;font-size:13px;font-weight:700;color:#23251d;background:#e5e7e0;padding:3px 10px;border-radius:999px;border:1px solid #bfc1b7;">
          <span style="display:inline-block;width:6px;height:6px;background:#ed7b2f;border-radius:50%;margin-right:5px;vertical-align:middle;overflow:hidden;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span><span leaf="">&nbsp;{{条目标题}}&nbsp;</span>
        </span>
      </p>
      <p style="font-size:13px;color:#4d4f46;margin:0;line-height:1.7;text-align:justify;"><span leaf="">{{条目说明}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 25 常见问题列表 faq-listing

**用途**：结尾或章节内的 FAQ 清单，编号+问题一行式，简洁不展开答案（答案另起正文段落）。

**可替换字段**：`{{FAQ标签}}`（如 `COMMON QUESTIONS`）`{{问题}}`（可重复 N 次）

```html
<section style="margin-top:24px;">
  <section style="background:#fdfdf8;border:1px solid #bfc1b7;padding:18px;box-sizing:border-box;border-radius:6px;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="margin:0 0 12px;font-size:10px;line-height:1.6;color:#9ea096;letter-spacing:3px;font-weight:800;"><span leaf="">{{FAQ标签}}</span></p>
    <section style="padding:10px 0;border-top:1px solid #bfc1b7;">
      <p style="margin:0;font-size:15px;line-height:1.8;color:#23251d;font-weight:800;"><span leaf="">01 / {{问题}}</span></p>
    </section>
    <section style="padding:10px 0;border-top:1px solid #bfc1b7;border-bottom:1px solid #bfc1b7;">
      <p style="margin:0;font-size:15px;line-height:1.8;color:#23251d;font-weight:800;"><span leaf="">02 / {{问题}}</span></p>
    </section>
  </section>
</section>
```

（问题多于 2 条时，中间条目只加 `border-top`，最后一条同时加 `border-top` + `border-bottom` 收尾。）

---

## 组件 26 案例时间线 case-timeline

**用途**：单个案例的完整展开——CASE 标签+标题、行业/规模、描述、配图、结果总结，左侧带时间线圆点+竖线。

**可替换字段**：`{{案例标题}}` `{{行业规模}}` `{{案例描述}}` `{{图片URL}}` `{{结果总结}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;">
      <section style="display:flex;flex-direction:column;align-items:center;margin-right:16px;flex-shrink:0;">
        <section style="width:14px;height:14px;border-radius:50%;border:3px solid #1e1f23;background:#fdfdf8;margin-top:4px;"><span leaf=""><br></span></section>
        <section style="width:2px;background:#bfc1b7;flex:1;margin-top:4px;min-height:48px;"><span leaf=""><br></span></section>
      </section>
      <section style="flex:1;padding-bottom:12px;">
        <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap;">
          <span style="display:inline-block;background:#1e1f23;color:#fff;font-size:10px;font-weight:700;padding:2px 8px;border-radius:999px;"><span leaf="">CASE</span></span>
          <h4 style="font-size:15px;font-weight:800;color:#23251d;margin:0;"><span leaf="">{{案例标题}}</span></h4>
        </section>
        <p style="font-size:11px;font-weight:600;color:#65675e;letter-spacing:1px;margin:0 0 12px;"><span leaf="">{{行业规模}}</span></p>
        <p style="font-size:14px;margin:0 0 14px;color:#4d4f46;line-height:1.7;text-align:justify;"><span leaf="">{{案例描述}}</span></p>
        <section style="text-align:center;margin-bottom:4px;">
          <span leaf=""><img src="{{图片URL}}" alt="案例配图" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:6px;border:1px solid #bfc1b7;"></span>
        </section>
        <p style="font-size:14px;margin:12px 0 0;color:#4d4f46;line-height:1.7;text-align:justify;"><strong style="color:#23251d;"><span leaf="">{{结果总结}}</span></strong></p>
      </section>
    </section>
  </section>
</section>
```

（无配图时删掉中间的图片 `<section>`；作为全文最后一个案例时，把最外层竖线 `<section>` 的 `flex:1;min-height:48px` 删掉，避免尾部多出一截空线。）

---

## 组件 27 信任墙 summary-logo-wall

**用途**：Logo/来源引用墙，3 个一行、自动换行，用于引用来源、合作方、参考资料出处等场景。

**可替换字段**：`{{标签}}`（如 `TRUST`/`来源`）`{{分组说明}}` + 6 个 `{{LOGO占位}}`（可增减数量）

```html
<section style="margin-top:24px;">
  <section style="padding:18px;border-radius:6px;background:#fdfdf8;border:1px solid #bfc1b7;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:14px;">
      <p style="margin:0;font-size:12px;color:#65675e;font-weight:700;letter-spacing:1px;"><span leaf="">{{标签}}</span></p>
      <span style="font-size:11px;color:#9ea096;"><span leaf="">{{分组说明}}</span></span>
    </section>
    <section style="display:flex;flex-wrap:wrap;gap:10px;">
      <section style="width:31%;height:46px;border-radius:6px;background:#eeefe9;border:1px solid #bfc1b7;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#9ea096;"><span leaf="">{{LOGO占位}}</span></section>
      <section style="width:31%;height:46px;border-radius:6px;background:#eeefe9;border:1px solid #bfc1b7;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#9ea096;"><span leaf="">{{LOGO占位}}</span></section>
      <section style="width:31%;height:46px;border-radius:6px;background:#eeefe9;border:1px solid #bfc1b7;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;color:#9ea096;"><span leaf="">{{LOGO占位}}</span></section>
    </section>
  </section>
</section>
```

---

## 组件 28 结尾行动区 ending-actions（本主题的签名/CTA 区）

**用途**：文章结尾，点赞·在看·收藏三连区，浅底图标块。

**签名文案适配**：SKILL.md 的作者签名（"我是 {{作者名}}…"两段，默认占位、由用户替换）以正文段落（组件 10）形式放在本组件**之前**；本组件内部 `{{文末互动引导}}` 直接使用 SKILL.md 固定的第二段（"如果你觉得今天这篇有收获…三连，我们下篇见"）。

**可替换字段**：`{{文末互动引导}}`

```html
<section style="margin-top:24px;">
  <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:22px 16px;text-align:center;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="font-size:13px;font-weight:700;color:#23251d;line-height:1.6;margin:0 0 14px;"><span leaf="">{{文末互动引导}}</span></p>
    <section style="display:flex;justify-content:center;gap:18px;margin-bottom:14px;flex-wrap:wrap;">
      <section style="text-align:center;color:#4d4f46;">
        <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#eeefe9;border-radius:6px;border:1px solid #bfc1b7;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg>
        </section>
        <span style="font-size:11px;font-weight:600;"><span leaf="">赞</span></span>
      </section>
      <section style="text-align:center;color:#4d4f46;">
        <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#eeefe9;border-radius:6px;border:1px solid #bfc1b7;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="3"></circle><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path></svg>
        </section>
        <span style="font-size:11px;font-weight:600;"><span leaf="">在看</span></span>
      </section>
      <section style="text-align:center;color:#23251d;">
        <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#d4c9b8;border-radius:6px;border:1px solid #b17816;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#23251d" stroke-width="1.8" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        </section>
        <span style="font-size:11px;font-weight:700;"><span leaf="">收藏</span></span>
      </section>
    </section>
    <p style="line-height:1.6;font-size:10px;color:#9ea096;letter-spacing:2px;margin:0;font-weight:500;"><span leaf="">THANKS FOR READING</span></p>
  </section>
</section>
```

---

## 组件 29 路线胶囊组 roadmap-pills

**用途**：流程阶段/路线图，胶囊标签横排，颜色区分状态：默认（浅底）/进行中（陶土棕）/已完成或终态（墨黑实底白字）。

**可替换字段**：`{{标签}}`（如 `ROADMAP`）+ N 个 `{{阶段名}}`

```html
<section style="margin-top:24px;">
  <section style="padding:18px;border-radius:6px;background:#fdfdf8;border:1px solid #bfc1b7;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <p style="margin:0 0 12px;font-size:11px;font-weight:800;letter-spacing:2px;color:#65675e;"><span leaf="">{{标签}}</span></p>
    <section style="display:flex;flex-wrap:wrap;gap:8px;">
      <span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#e5e7e0;border:1px solid #bfc1b7;font-size:12px;font-weight:700;color:#23251d;"><span leaf="">{{阶段名·默认}}</span></span>
      <span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#eeefe9;border:1px solid #bfc1b7;font-size:12px;font-weight:700;color:#23251d;"><span leaf="">{{阶段名·默认}}</span></span>
      <span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#d4c9b8;border:1px solid #b17816;font-size:12px;font-weight:700;color:#23251d;"><span leaf="">{{阶段名·进行中}}</span></span>
      <span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#1e1f23;border:1px solid #23251d;font-size:12px;font-weight:700;color:#ffffff;"><span leaf="">{{阶段名·终态}}</span></span>
    </section>
  </section>
</section>
```

---

## 组件 30 暗色摘要分栏 dark-summary-split

**用途**：深色底左右分栏，左侧放结论（"内部结案摘要"式表达），右侧放下一步/待办，适合数据复盘、项目复盘类文章的收束。

**可替换字段**：`{{SUMMARY标签}}` `{{左侧结论}}` `{{NEXT标签}}` `{{右侧说明}}`

```html
<section style="margin-top:24px;">
  <section style="border-radius:6px;overflow:hidden;border:1px solid #23251d;background:#1e1f23;font-family:'IBM Plex Sans',-apple-system,sans-serif;display:flex;align-items:stretch;">
    <section style="flex:1;padding:18px 18px 20px;border-right:1px solid rgba(255,255,255,0.08);">
      <p style="margin:0 0 8px;font-size:11px;letter-spacing:2px;color:rgba(255,255,255,0.55);font-weight:700;"><span leaf="">{{SUMMARY标签}}</span></p>
      <p style="margin:0;font-size:15px;line-height:1.9;color:rgba(255,255,255,0.92);"><span leaf="">{{左侧结论}}</span></p>
    </section>
    <section style="width:34%;min-width:120px;padding:18px;background:#23251d;display:flex;flex-direction:column;justify-content:center;gap:10px;">
      <span style="display:inline-block;padding:4px 8px;background:#eeefe9;color:#23251d;border-radius:4px;font-size:10px;font-weight:800;align-self:flex-start;"><span leaf="">{{NEXT标签}}</span></span>
      <p style="margin:0;font-size:13px;line-height:1.8;color:rgba(255,255,255,0.76);"><span leaf="">{{右侧说明}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 31 暗色摘要边框 dark-summary-outline

**用途**：深色底 + 反白内边框，收束全文的结论句/最强金句，适合观点类文章的终极收束（全文慎用，≤1 处）。

**可替换字段**：`{{CLOSING标签}}` `{{结尾金句}}`

```html
<section style="margin-top:24px;">
  <section style="background:#1e1f23;border:1px solid #23251d;padding:8px;box-sizing:border-box;border-radius:6px;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="border:1px solid rgba(255,255,255,0.16);border-radius:4px;padding:20px 22px;">
      <p style="margin:0 0 8px;font-size:10px;line-height:1.6;color:#a3a3a3;letter-spacing:4px;font-weight:800;"><span leaf="">{{CLOSING标签}}</span></p>
      <p style="margin:0;font-size:16px;line-height:1.9;color:#fafafa;font-weight:700;"><span leaf="">{{结尾金句}}</span></p>
    </section>
  </section>
</section>
```

（内层 `border` 用双层嵌套模拟"反白内边框"效果，不依赖 `position`，兼容公众号平台。）

---

## 组件 32 摘要横幅条 frontpage-summary-strip

**用途**：把结论压缩成一条可快速扫读的横幅，比组件 31 更轻，适合不需要"重锚点"的收束场景。

**可替换字段**：`{{摘要文字}}` `{{标签}}`（如 `SUMMARY`）

```html
<section style="margin-top:24px;">
  <section style="background:#eeefe9;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;">
      <p style="margin:0;font-size:13px;line-height:1.7;color:#23251d;font-weight:700;"><span leaf="">{{摘要文字}}</span></p>
      <span style="font-size:10px;color:#65675e;font-weight:800;letter-spacing:2px;"><span leaf="">{{标签}}</span></span>
    </section>
  </section>
</section>
```

---

## 组件 33 作者签名条 author-signature

**用途**：小巧的作者署名胶囊，圆形字头像 + 一行签名文字，用于文中人物引语归属或结尾前的署名标记。

**可替换字段**：`{{头像字}}`（姓名首字）`{{签名文字}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <span style="display:inline-flex;align-items:center;gap:10px;padding:8px 12px;background:#eeefe9;border:1px solid #bfc1b7;border-radius:999px;">
      <span style="width:22px;height:22px;border-radius:50%;background:#1e1f23;color:#fff;display:inline-flex;align-items:center;justify-content:center;font-size:10px;font-weight:800;"><span leaf="">{{头像字}}</span></span>
      <span style="font-size:12px;color:#23251d;font-weight:700;"><span leaf="">{{签名文字}}</span></span>
    </span>
  </section>
</section>
```

---

## 组件 34 结尾内容块 ending-content

**用途**：信息量最大的收尾形式——编号式"结尾标题"（呼应组件 3 的章节标题结构，用 `///`/`END` 替代数字编号）+ 两段收尾正文 + 一个高亮总结框。适合需要完整陈述收尾观点的文章。

**可替换字段**：`{{结尾标题}}` `{{结尾说明}}` `{{收尾段落1}}` `{{收尾段落2}}` `{{最后总结}}`

```html
<section style="margin-top:24px;">
  <section style="font-family:'IBM Plex Sans',-apple-system,sans-serif;">
    <section style="display:flex;align-items:center;gap:14px;margin-bottom:16px;">
      <section style="text-align:center;flex-shrink:0;">
        <p style="margin:0;font-size:24px;font-weight:800;color:#23251d;line-height:1;letter-spacing:-2px;"><span leaf="">///</span></p>
        <p style="margin:0;font-size:8px;font-weight:700;color:#9ea096;letter-spacing:2px;"><span leaf="">END</span></p>
      </section>
      <span style="width:1px;height:36px;background:#bfc1b7;flex-shrink:0;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;"><span leaf="">&nbsp;</span></span>
      <section>
        <p style="margin:0 0 1px;font-size:17px;font-weight:800;color:#23251d;letter-spacing:0.2px;"><span leaf="">{{结尾标题}}</span></p>
        <p style="margin:0;font-size:11px;font-weight:600;color:#65675e;letter-spacing:1.2px;"><span leaf="">{{结尾说明}}</span></p>
      </section>
    </section>
    <p style="margin:0 0 14px;font-size:14px;line-height:1.9;text-align:justify;color:#4d4f46;"><span leaf="">{{收尾段落1}}</span></p>
    <p style="margin:0 0 14px;font-size:14px;line-height:1.9;text-align:justify;color:#4d4f46;"><span leaf="">{{收尾段落2}}</span></p>
    <section style="background:#eeefe9;border-radius:6px;padding:16px 18px;border:1px solid #bfc1b7;text-align:center;">
      <p style="font-size:15px;color:#23251d;margin:0;line-height:1.6;"><strong style="border-bottom:3px solid #ed7b2f;"><span leaf="">{{最后总结}}</span></strong></p>
    </section>
  </section>
</section>
```

---

## 多行代码块 → 用通用增量库

本主题不设专属多行代码块组件；Markdown 的三反引号围栏代码块直接用 `common-components.md` 的 1a 深色代码块（默认）或 1b 浅色代码块，左竖条/强调色换成本主题墨色 `#1e1f23`；行内代码用本主题"文字强调 d"或组件 11。

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;padding:8px;box-sizing:border-box;background:#fdfdf8;color:#4d4f46;font-family:'IBM Plex Sans',-apple-system,system-ui,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;line-height:1.75;">

  <!-- 1. 头图卡（组件2 hero-card，唯一一处，不设 margin-top） -->

  <!-- 2. 开篇编者按（组件14 editors-note，可选，仅原文有独立引言/背景说明时使用） -->

  <!-- 3. 第一章（组件3 section-title，默认分节样式，编号01） -->
  <!--    章内按需组合：组件10 正文段落(+文字强调a-e) / 组件11 行内代码段落 / 组件12 新旧对照段落 / 组件13 无序列表 / 组件24 条目列表卡 -->
  <!--    / 组件18-19 图片 / 组件20 图表占位卡 / 组件21-22 对比 / 组件23 流程示意图 / 组件26 案例时间线 / 组件15 重点观点卡 / 组件7-9 次级小标题 -->

  <!-- 4. 第二章…第N章（同上结构，编号递增；章节之间如需轻量过渡可插组件4，需要强调型分节可插组件5/6，
       但一篇文章内分节样式不宜超过2种交替使用，避免节奏混乱） -->

  <!-- 5. 全文收束（四选一或组合，按文章类型定，见下方配方表）：
       组件31 暗色摘要边框（金句收束，全文≤1处）/ 组件30 暗色摘要分栏（结论+下一步）
       / 组件32 摘要横幅条（一句话摘要）/ 组件34 结尾内容块（信息量最大，完整陈述收尾） -->

  <!-- 6. 常见问题（组件25 faq-listing，可选） -->

  <!-- 7. 固定签名段落（组件10 正文段落，SKILL.md 固定文案第一段，ending-actions 之前） -->

  <!-- 8. 作者签名条（组件33 author-signature，可选） -->

  <!-- 9. 结尾行动区（组件28 ending-actions，{{文末互动引导}} 用 SKILL.md 固定文案第二段） -->

</section>

<!-- 10. 隐藏标记（外层容器之外，全文最后一个元素） -->
<p style="display:none;">
  <mp-style-type data-value="3"></mp-style-type>
</p>
```

**骨架铁律**：
- 头图卡（组件 2）全文唯一、必须在最前；隐藏标记必须在全局容器闭合**之后**。
- 组件 3/4/5/6/7/8/9 都是"标题类"组件但权重不同——组件 3 是默认主力，4/6 是轻/中量级分节过渡，5 是重量级强调（≤1-2 处），7/8/9 是章节内的二级标题；不要一篇文章里把所有变体都用一遍，选 2-3 种保持节奏统一即可。
- 组件 31 暗色摘要边框（反白内边框）是本主题最强的收束锚点，全文只在结尾用一次，不要在正文中段重复使用。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 暗色摘要边框 31、暗色标题条 5、头图卡 2 深色摘要条 | 全文最强收束、专题开篇 | 全文 ≤3 处 |
| **标记层** | 橙色下划线（文字强调 c）、浅底高亮框（文字强调 b） | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 重点观点卡 15、条目列表卡 24、编者按 14、各类分节条 4/6/9 | 小结、清单、过渡 | 按需 |

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇的排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 教程/操作指南 | 头图卡2 + 章节标题3 + 步骤内联标题7 + 正文段落10 + 行内代码段落11 + 无序列表13 | 流程示意图23、常见问题列表25、图片卡19 |
| 盘点/工具清单 | 头图卡2 + 章节标题3 + 条目列表卡24 + 对比摘要卡21/精简对照表22 + 图片卡19 | 路线胶囊组29、信任墙27 |
| 观点/深度分析 | 头图卡2 + 章节标题3 + 强调标题8 + 正文段落10 + 重点观点卡15 + 暗色摘要边框31 | 编者按14、新旧对照段落12 |
| 数据复盘/报告 | 头图卡2 + 期号徽章条6 + 前导词标题9 + 图表占位卡20 + 精简对照表22 + 暗色摘要分栏30 | 流程示意图23、行内代码段落11（指标术语） |
| 访谈/人物特稿 | 头图卡2 + 章节标题3 + 编者按14 + 正文段落10 + 案例时间线26 + 作者签名条33 | 新旧对照段落12（观点前后变化）、暗色摘要边框31（引语收束） |
| 生活/情感随笔 | 头图卡2 + 内刊标签条4 + 正文段落10 + 分割点17 + 重点观点卡15 | 摘要横幅条32 |
| 案例实战 | 头图卡2 + 章节标题3 + 案例时间线26 + 对比摘要卡21 + 结尾内容块34 | 信任墙27、重点观点卡15 |

所有类型共用固定结构：头图卡2 + 固定签名段落(组件10) + 结尾行动区28 + 隐藏标记。

---

## Markdown → 橄榄手记 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 头图卡2 主标题/强调词 | 平台标题另设，头图卡标题从中提炼 |
| 文章开头 `> 引言` | 组件14 编者按 或并入头图卡"底部摘要" | 视引言长度而定 |
| `## 章节标题` | 组件3 section-title（默认）/ 组件6 期号徽章条（专题式，可选变体） | 编号 01/02/03… |
| `### 子标题` | 组件7 步骤内联标题（教程步骤）/ 组件9 前导词标题（系列分节）/ 组件8 强调标题（观点强调） | 按语境三选一 |
| 普通段落 | 组件10 正文段落 | 每段主动标 1~3 处橙色下划线（文字强调 c） |
| `**加粗文字**` | 文字强调 a 强调加粗 | |
| `==高亮文字==` | 文字强调 b 浅底高亮框 | |
| `<u>下划线</u>` / `++文字++` | 文字强调 c 橙色下划线 | 次要强调（默认标记） |
| `~~删除文字~~` | 文字强调 e 删除线旧词 | 常与新表述搭配用组件12 |
| 行内 `` `code` `` / 技术名词/字段名 | 文字强调 d 行内代码标签 | 整句强调用组件11 |
| ` ``` 多行代码块 ``` ` | 通用库1a深色/1b浅色 | 左竖条换本主题墨色 `#1e1f23` |
| 无序/有序列表 | 组件13 无序列表（简单）/ 组件24 条目列表卡（需标题+说明两层） | |
| 表格 | 组件22 精简对照表（≥2列数据对照）/ 组件21 对比摘要卡（二元对比） | 不用 `table`/`grid`，flex 仿表格 |
| `![说明](图片)` | 组件19 图片卡 | 有说明才加 `<figcaption>` |
| `![](图片)` 无说明/通栏 | 组件18 通栏图片 | |
| `---` 分割线 | 组件16 分割线（正式）/ 组件17 分割点（轻松） | |
| `> 引用`（非开头） | 组件14 编者按 / 组件15 重点观点卡 | 视语气选择 |
| 案例/示例展开 | 组件26 案例时间线 | |
| 常见问题 | 组件25 常见问题列表 | |
| 文末总结/结语 | 组件34 结尾内容块 / 组件31 暗色摘要边框 / 组件30 暗色摘要分栏 / 组件32 摘要横幅条 | 四选一，按篇幅和语气选 |
| 文末 | 组件28 ending-actions（+ 固定签名段落） | 固定签名段落放 ending-actions 前 |
