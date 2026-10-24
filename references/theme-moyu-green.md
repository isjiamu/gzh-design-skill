# 公众号排版组件库 —— 摸鱼绿

> **使用说明**：本组件库为「摸鱼绿」主题（移植自摸鱼小李绿色杂志风），所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：绿色杂志风，卡片丰富、信息密度高。emerald 主色 + 黄色高亮点睛、杂志快讯封面、横向滚动目录、标签化章节。适合教程、测评、清单、工具盘点类文章。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`、`<svg>`、`<video>`、`<h4>`~`<h6>`
> - ✅ 支持内联 `style`、`linear-gradient`（可渲染但有暗色模式检测风险，文字背景默认用纯色）、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>/<h3>` 等基础标签
> - ⚠️ **粘贴实测崩坏（2026-10 验证）**：`display:flex`+`gap` 行布局、横向滚动 `overflow-x:scroll`、负字距 `letter-spacing:-Npx`、中文 `text-align:justify` 都会在粘贴进编辑器后变形——本主题组件已全部改写为**垂直堆叠 + margin**、同行元素 `display:inline-block`，改动时不得回退这些写法
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（圆点、渐变分割线、装饰短横、时间线竖线）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`——微信编辑器会自动"纠正"导致样式被重写。正确做法：拆成多个 `<p>`，每个 `<p>` 只有一个字号；高亮样式统一挂在外层 `<span>` 上
> - 不用 `position:absolute` 做划线/高亮，删除线用 `text-decoration:line-through`
> - 结构化区域（如封面顶部图片槽位）没有内容时**整块删掉**，不留空 section
> - **图片 `<img>` 的 src 必须是公网 http(s) URL**（推荐素材库 mmbiz.qpic.cn 地址）；相对路径/本地路径粘贴时会被静默剥掉
> - 图标一律用 Emoji 或文字，**不用 SVG**（会被剥掉）；视频只放占位框，提示在编辑器手动插入

---

## 设计变量速查表

```
主色调：       #059669（emerald-600）
辅色：         #10B981（emerald-500）
浅绿装饰：     #34D399 / #6EE7B7 / #A7F3D0
浅绿边框：     #BBF7D0
浅绿背景：     #ECFDF5 / #F0FDF4
黄色高亮：     #FDE68A
黄色背景（警告）：#FFFBEB
黄色文字（警告）：#92400E
红色下划线：   #FECACA（对比/否定专用）
警告橙色：     rgb(255,76,0)
警告灰色：     rgb(136,136,136)
标题色：       #111827
正文色：       #374151
次要文字：     #4B5563
注释/标签：    #6B7280
辅助文字：     #9CA3AF
分隔线：       #D1D5DB
浅边框：       #E5E7EB
浅灰背景：     #F3F4F6
极浅灰：       #F9FAFB
正文字号：     14px（不可改）
正文行高：     1.9
全局行高：     1.8
最大宽度：     677px
内容区边距：   0 20px（模块左右各 20px）
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.8;">

  <!-- 所有组件放在这里 -->

</section>
```

> 不设 `letter-spacing` 与 `overflow-x:hidden`：前者实测在部分组件上被规范化后改变字宽、后者对粘贴后的渲染无意义，徒增被改写的风险。

---

## 组件 2 封面 cover-breaking（杂志快讯封面）

> **文案策略（先读，比代码重要）**：
> - 封面标题和公众号外标题是**两层标题**，必须视角错开——外标题卖"为什么点开"，封面卖"里面讲什么"
> - 已知外标题时，主标题**禁止原样复述**其核心关键词（产品名/功能名/场景词）；未知外标题时从五个视角（**数字反差 / 角色革命 / 案例串 / 方法论 / 情绪钩子**）自选一个直出，不停下来问
> - 产品名/功能名只允许出现在**底部品牌条**或**副标题关键词条**，不出现在大字主标题
> - 仅当用户要求"帮我定封面方向"时才列 3-5 个方向让用户选

> **粘贴安全说明（2026-10 实测改写）**：旧版封面用 flex 行布局 + 负字距大标题，粘贴后整卡变形。现版为纯垂直堆叠：顶部图片槽（可选）→ 文字区 → 底部绿条，全部块级元素顺序排列，无任何 flex/负字距。

**有顶部大图版**：

```html
<section style="margin:0 0 28px;background:#ffffff;border:1px solid #A7F3D0;border-radius:16px;overflow:hidden;">
  <section style="margin:0;">
    <span leaf=""><img src="{{封面大图URL}}" style="width:100%;height:auto;display:block;"></span>
  </section>
  <section style="padding:18px 22px 16px;">
    <p style="margin:0 0 8px;font-size:12px;font-weight:700;color:#059669;">
      <span leaf="">{{顶部标签}} · {{日期}}</span>
    </p>
    <p style="margin:0 0 8px;font-size:14px;color:#D1D5DB;text-decoration:line-through;">
      <span leaf="">{{划线旧认知}}</span>
    </p>
    <p style="margin:0 0 8px;font-size:22px;font-weight:900;color:#111827;line-height:1.45;">
      <span leaf="">{{主标题行1}}</span><span style="color:#059669;"><span leaf="">{{绿色高亮词}}</span></span>
    </p>
    <p style="margin:0;font-size:13px;color:#6B7280;line-height:1.7;">
      <span leaf="">{{副标题关键词}}</span>
    </p>
  </section>
  <section style="background:#059669;padding:12px 22px;">
    <p style="margin:0;font-size:13px;color:#ffffff;font-weight:600;line-height:1.6;">
      <span leaf="">{{底部品牌条文字}}</span>
    </p>
  </section>
</section>
```

**无图版**：把上面第一个内层 `<section>`（图片槽）整块删掉即可，其余不变。

**可替换元素**：
- `{{封面大图URL}}` → 公网 http(s) 图片地址（相对路径会被静默剥掉）；无图时整槽删除
- `{{顶部标签}}` → 如 `TUTORIAL · 品牌实战`、`FIELD NOTE · 实测`；`{{日期}}` → 如 `2026.10`
- `{{划线旧认知}}` → 被颠覆的旧观念（例：`3D 场景要专业团队？`）
- `{{主标题行1}}` → 标题主文（黑色）；`{{绿色高亮词}}` → 标题中的绿色强调词
- `{{副标题关键词}}` → 简短关键词，用 `·` 分隔
- `{{底部品牌条文字}}` → 产品/品牌名 + 标签，一行写清（例：`flash-1017 实测 · 案例 · Unity`）

---

## 组件 3 目录 toc-list（竖排目录）

2 个及以上章节时生成。展示**精选的 3 个核心看点**（章节多于 3 个时挑最重要的 3 个），最后一条固定为"写在最后"（编号 ///）。

> **粘贴安全说明**：旧版 toc-scroll 横向滚动目录（`overflow-x:scroll` + 卡片横排）实测粘贴后滚动能力被剥、卡片挤压变形，已废弃。现版为浅绿底卡片内竖排行，数字用绿色加粗行内标记。

```html
<section style="margin:0 20px 28px;padding:16px 16px 8px;background:#F0FDF4;border-radius:12px;">
  <p style="margin:0 0 12px;font-size:12px;font-weight:700;color:#059669;">
    <span leaf="">目录</span>
  </p>
  <p style="margin:0 0 8px;font-size:14px;color:#111827;line-height:1.7;">
    <span style="color:#059669;font-weight:700;"><span leaf="">01</span></span><span leaf=""> {{看点1}}</span>
  </p>
  <p style="margin:0 0 8px;font-size:14px;color:#111827;line-height:1.7;">
    <span style="color:#059669;font-weight:700;"><span leaf="">02</span></span><span leaf=""> {{看点2}}</span>
  </p>
  <p style="margin:0 0 8px;font-size:14px;color:#111827;line-height:1.7;">
    <span style="color:#059669;font-weight:700;"><span leaf="">03</span></span><span leaf=""> {{看点3}}</span>
  </p>
  <p style="margin:0 0 8px;font-size:14px;color:#111827;line-height:1.7;">
    <span style="color:#059669;font-weight:700;"><span leaf="">///</span></span><span leaf=""> 写在最后</span>
  </p>
</section>
```

---

## 组件 4 章节标题 chapter-title

第一个章节用 `margin:16px 20px 20px`，后续章节用 `margin:40px 20px 20px`。最后一章编号用 `///`。

> **粘贴安全说明**：旧版用 flex 横排（编号+竖线+标题）+ 负字距，粘贴后错位变形。现版为「绿色顶边线 + 三行竖排」，实测粘贴稳定。

```html
<section style="margin:40px 20px 20px;padding-top:8px;border-top:2px solid #059669;">
  <p style="margin:12px 0 0;font-size:13px;font-weight:700;color:#059669;">
    <span leaf="">{{01}}</span>
  </p>
  <p style="margin:4px 0 0;font-size:20px;font-weight:900;color:#111827;line-height:1.4;">
    <span leaf="">{{中文标题}}</span>
  </p>
  <p style="margin:4px 0 0;font-size:12px;color:#9CA3AF;">
    <span leaf="">{{ENGLISH · 英文副标题}}</span>
  </p>
</section>

<!-- 本章节正文内容跟在标题 section 之后 -->
```

---

## 组件 5 正文段落 paragraph

```html
<p style="margin:0 20px 16px;font-size:14px;line-height:1.9;color:#374151;">
  <span leaf="">{{正文内容}}</span>
</p>
```

不用 `text-align:justify`（中文两端对齐粘贴后字距被拉花），默认左对齐。段间距较大时用 `margin-bottom:24px`。

---

## 组件 6 行内样式（9 种 + 使用原则）

### 6a. 绿色加粗（核心概念、关键结论、品牌名/产品名）

```html
<strong style="color:#059669;"><span leaf="">文字</span></strong>
```

### 6b. 绿色背景标签

```html
<strong style="color:#059669;background:rgba(5,150,105,0.1);padding:0 4px;border-radius:2px;"><span leaf="">文字</span></strong>
```

### 6c. 黄色纯色高亮（一段话中最想让读者注意的短语，每段不超过 1-2 处）

```html
<span style="background:#FDE68A;padding:0 4px;border-radius:2px;font-weight:600;color:#111827;"><span leaf="">文字</span></span>
```

### 6d. 黄色底部高亮（下划线效果）

```html
<span style="color:#111827;font-weight:bold;border-bottom:3px solid #FDE68A;"><span leaf="">文字</span></span>
```

### 6e. 绿色下划线（次要强调，**正文关键词的默认标记**）

```html
<span style="border-bottom:2px solid #A7F3D0;font-weight:600;"><span leaf="">文字</span></span>
```

### 6f. 红色下划线（对比、否定、需要注意的内容）

```html
<span style="border-bottom:2px solid #FECACA;"><span leaf="">文字</span></span>
```

### 6g. 代码标签（行内代码）

```html
<span style="background:#F3F4F6;color:#1F2937;padding:2px 6px;border-radius:4px;font-size:13px;font-weight:600;"><span leaf="">code</span></span>
```

### 6h. 获取方式标签（黄色背景）

```html
<span style="background:#FDE68A;color:#1F2937;padding:2px 6px;border-radius:4px;font-size:13px;font-weight:700;"><span leaf="">「关键词」</span></span>
```

### 6i. 删除线灰色（旧的/被淘汰的概念）

```html
<span style="background:#F3F4F6;color:#6B7280;padding:2px 6px;border-radius:4px;font-size:13px;text-decoration:line-through;font-weight:600;"><span leaf="">旧词</span></span>
```

**使用原则**：
1. 绿色加粗用于核心概念、关键结论、品牌名/产品名
2. 黄色高亮每段不超过 1-2 处
3. 绿色下划线用于次要强调（正文关键词逐段标记用它）
4. 红色下划线用于对比、否定
5. 删除线灰色用于被淘汰的概念
6. 一段文字中不要同时使用超过 2 种高亮效果

---

## 组件 7 内容标签组（STEP / CASE / SKILL / TOOL）

> **粘贴安全说明**：旧版用 flex 把胶囊和 `<h4>` 标题排同一行，`<h4>` 粘贴后样式丢失、flex 行变形。现版胶囊与标题各占一行（两个 `<p>`），实测稳定。

### 7a. step-label（STEP 步骤标签）

```html
<section style="margin:0 20px 24px;">
  <p style="margin:0 0 8px;">
    <span style="display:inline-block;background:#111827;color:#ffffff;font-size:12px;font-weight:700;padding:3px 8px;border-radius:10px;"><span leaf="">STEP 01</span></span>
  </p>
  <p style="margin:0 0 12px;font-size:16px;font-weight:800;color:#111827;line-height:1.5;">
    <span leaf="">{{步骤标题}}</span>
  </p>
  <p style="margin:0;font-size:14px;color:#4B5563;line-height:1.9;">
    <span leaf="">{{步骤内容}}</span>
  </p>
</section>
```

### 7b. case-label（CASE 案例标签）

```html
<section style="margin:0 20px 24px;">
  <p style="margin:0 0 8px;">
    <span style="display:inline-block;background:#E5E7EB;color:#6B7280;font-size:12px;font-weight:700;padding:3px 8px;border-radius:10px;"><span leaf="">CASE 01</span></span>
  </p>
  <p style="margin:0 0 12px;font-size:16px;font-weight:800;color:#111827;line-height:1.5;">
    <span leaf="">{{案例标题}}</span>
  </p>
  <!-- 案例内容 -->
</section>
```

### 7c. skill-label / tool-label（编号标签）

```html
<section style="margin:0 20px 24px;">
  <p style="margin:0 0 8px;">
    <span style="display:inline-block;background:#111827;color:#ffffff;font-size:12px;font-weight:700;padding:3px 8px;border-radius:10px;"><span leaf="">SKILL 1</span></span>
  </p>
  <p style="margin:0 0 12px;font-size:16px;font-weight:800;color:#111827;line-height:1.5;">
    <span leaf="">{{名称}}</span>
  </p>
</section>
```

`SKILL 1` 可替换为 `TOOL 摄像机`、`TOOL 打光` 等。

---

## 组件 8 代码/命令/Prompt

### 8a. prompt-block（PROMPT 展示块）

```html
<p style="font-size:13px;color:#374151;margin:0 0 16px;line-height:1.8;">
  <span style="display:inline-block;background:#059669;color:#fff;font-size:11px;font-weight:700;padding:1px 7px;border-radius:3px;margin-right:6px;vertical-align:middle;letter-spacing:0.5px;"><span leaf="">PROMPT</span></span>
  <span style="font-size:12px;color:#9CA3AF;font-weight:700;"><span leaf="">{{提示词内容}}</span></span>
</p>
```

### 8b. cmd-block（CMD 单行命令块）

```html
<p style="font-size:13px;color:#374151;margin:0 0 24px;line-height:1.8;">
  <span style="display:inline-block;background:#111827;color:#fff;font-size:11px;font-weight:700;padding:1px 7px;border-radius:3px;margin-right:6px;vertical-align:middle;letter-spacing:0.5px;"><span leaf="">CMD</span></span>
  <span style="background:#F3F4F6;color:#1F2937;padding:2px 6px;border-radius:4px;font-size:13px;font-weight:600;"><span leaf="">{{命令内容}}</span></span>
</p>
```

### 8c. 多行代码块 → 用通用增量库

多行代码块**不设主题专属组件**，直接用 `common-components.md` 的 1a 深色代码块（每行一个 `<p style="margin:0">`，禁 `white-space:pre`）；浅色场景用 1b 并把左竖条换成 `#059669`。

---

## 组件 9 引用与亮点

### 9a. quote-box（灰色虚线引用框）

所有引用、补充说明的**默认组件**（虚线框是本主题的风格特征，仅此组件与 9b 保留 dashed）：

```html
<section style="background:#F9FAFB;border:1px dashed #D1D5DB;border-radius:8px;padding:12px 16px;margin:0 20px 24px;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.6;">
    {{引用内容，可嵌入绿色加粗等内联样式}}
  </p>
</section>
```

### 9b. oneliner-card（一句话亮点卡片）

> 兼容性关键规则：**不要把 `font-size` 打在 `<strong>` 上**，不要在同一个 `<p>` 里混多个字号；高亮样式统一挂在外层 `<span>` 上。

单行版（只有主金句）：

```html
<section style="background:#FFF;border:1px dashed #BBF7D0;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#059669;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{亮点内容}}</span></span>
  </p>
</section>
```

带前缀引导语版（两段式）：

```html
<section style="background:#FFF;border:1px dashed #BBF7D0;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="font-size:12px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">
    <span leaf="">{{引导语}}</span>
  </p>
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#059669;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{亮点内容}}</span></span>
  </p>
</section>
```

带下方补充说明版：

```html
<section style="background:#FFF;border:1px dashed #BBF7D0;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="margin:0 0 6px;line-height:1.6;">
    <span style="font-size:15px;color:#059669;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{高亮内容}}</span></span>
  </p>
  <p style="font-size:13px;color:#9CA3AF;margin:0;line-height:1.5;">
    <span leaf="">{{补充说明}}</span>
  </p>
</section>
```

### 9c. subtitle-highlight（小节黄色浅底标题）

```html
<p style="font-size:15px;font-weight:900;color:#111827;margin-bottom:16px;">
  <span style="background:#FDE68A;padding:0 4px;"><span leaf="">{{小节标题}}</span></span>
</p>
```

可加 `margin-top:32px` 增加上间距。

### 9d. center-divider（居中金句分隔）

```html
<p style="font-size:14px;margin-bottom:20px;text-align:center;color:#059669;font-weight:700;letter-spacing:1px;border-top:1px solid #F3F4F6;border-bottom:1px solid #F3F4F6;padding:12px 0;">
  <span leaf="">{{居中金句}}</span>
</p>
```

---

## 组件 10 提示与信息

### 10a. warn-tip（踩坑提示）

```html
<section style="padding:6px 0 4px;margin-bottom:16px;">
  <p style="margin-bottom:6px;font-size:12px;font-weight:700;color:#9CA3AF;letter-spacing:1px;">
    <span style="color:rgb(255,76,0);"><span leaf="">！踩坑提示 🕳</span></span>
  </p>
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;">
    <span style="color:rgb(136,136,136);font-weight:bold;"><span leaf="">{{提示内容}}</span></span>
  </p>
</section>
```

标题可改为 `！真正的战场 🕳`、`！目前最大的槽点 🕳` 等。

### 10b. green-tip（绿色提示）

```html
<section style="padding:6px 0 4px;margin-bottom:16px;">
  <p style="margin-bottom:6px;font-size:12px;font-weight:700;color:#9CA3AF;letter-spacing:1px;">
    <span style="color:#059669;"><span leaf="">✦ {{提示标题}}</span></span>
  </p>
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;">
    {{提示内容}}
  </p>
</section>
```

### 10c. yellow-warning（黄色警告框）

```html
<section style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:12px;padding:12px 16px;margin-bottom:20px;">
  <p style="font-size:13px;color:#92400E;margin:0;font-weight:700;">
    <span leaf="">{{警告内容}}</span>
  </p>
</section>
```

### 10d. green-info（绿色信息框）

```html
<section style="background:#F0FDF4;padding:12px 16px;border-radius:8px;border:1px solid #BBF7D0;margin:0 20px 20px;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;">
    {{信息内容}}
  </p>
</section>
```

---

## 组件 11 布局组件

### 11a. pill-list（绿色胶囊列表）

基本版：

```html
<section style="margin-bottom:14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:13px;font-weight:700;color:#059669;background:rgba(5,150,105,0.08);padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#059669;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{列表项文字}}</span></span>
  </p>
</section>
```

带说明文字版：

```html
<section style="margin:0 20px 14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:13px;font-weight:700;color:#059669;background:rgba(5,150,105,0.08);padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#059669;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{标题}}</span></span>
  </p>
  <p style="font-size:13px;color:#4B5563;margin:0;line-height:1.7;">
    <span leaf="">{{描述内容}}</span>
  </p>
</section>
```

### 11b. flow-cards（三步流程卡片，竖排）

> **粘贴安全说明**：旧版横排三卡 + flex + gap 实测粘贴后挤压变形，已改为竖排（卡片顺序堆叠、中间一行居中 `↓`）。

```html
<section style="background:#F9FAFB;padding:16px;border-radius:12px;border:1px solid #F3F4F6;margin:0 20px 24px;">
  <section style="text-align:center;padding:10px 8px;background:#059669;border-radius:8px;margin-bottom:6px;">
    <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;">
      <span leaf="">{{步骤1标题}}</span>
    </p>
    <p style="font-size:11px;color:rgba(255,255,255,0.85);margin:0;line-height:1.5;">
      <span leaf="">{{步骤1描述}}</span>
    </p>
  </section>
  <p style="text-align:center;color:#D1D5DB;font-size:14px;margin:0 0 6px;line-height:1;">
    <span leaf="">↓</span>
  </p>
  <section style="text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;margin-bottom:6px;">
    <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
      <span leaf="">{{步骤2标题}}</span>
    </p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;line-height:1.5;">
      <span leaf="">{{步骤2描述}}</span>
    </p>
  </section>
  <p style="text-align:center;color:#D1D5DB;font-size:14px;margin:0 0 6px;line-height:1;">
    <span leaf="">↓</span>
  </p>
  <section style="text-align:center;padding:10px 8px;background:#fff;border:1px solid #A7F3D0;border-radius:8px;">
    <p style="font-size:13px;font-weight:800;color:#059669;margin:0 0 3px;">
      <span leaf="">{{步骤3标题}}</span>
    </p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;line-height:1.5;">
      <span leaf="">{{步骤3描述}}</span>
    </p>
  </section>
  <p style="font-size:12px;color:#9CA3AF;text-align:center;margin:12px 0 0;">
    <span leaf="">{{底部说明文字}}</span>
  </p>
</section>
```

箭头 `↓` 可替换为 `×` 做对比型布局。

### 11c. three-col-cards（三项对比卡片，竖排）

> **粘贴安全说明**：同 11b，横排三列已改竖排三卡。

```html
<section style="background:#F9FAFB;padding:16px;border-radius:12px;border:1px solid #F3F4F6;margin:0 20px 28px;">
  <section style="text-align:center;padding:10px 8px;background:#059669;border-radius:8px;margin-bottom:6px;">
    <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;">
      <span leaf="">{{卡片1标题}}</span>
    </p>
    <p style="font-size:11px;color:rgba(255,255,255,0.85);margin:0;line-height:1.5;">
      <span leaf="">{{卡片1描述}}</span>
    </p>
  </section>
  <section style="text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;margin-bottom:6px;">
    <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
      <span leaf="">{{卡片2标题}}</span>
    </p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;line-height:1.5;">
      <span leaf="">{{卡片2描述}}</span>
    </p>
  </section>
  <section style="text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;">
    <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
      <span leaf="">{{卡片3标题}}</span>
    </p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;line-height:1.5;">
      <span leaf="">{{卡片3描述}}</span>
    </p>
  </section>
</section>
```

### 11d. timeline（时间线列表，左竖条版）

> **粘贴安全说明**：旧版用 flex 画圆点+竖线轨道、`<h4>` 标题，粘贴后轨道错位、标题样式丢失。现版每个节点是一个「绿色左竖条」卡片：胶囊一行、标题一行、英文一行、内容一段，实测粘贴稳定。节点按需重复，无首尾节点区别。

```html
<section style="margin:0 20px 22px;padding:0 0 4px 14px;border-left:3px solid #059669;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#111827;color:#ffffff;font-size:12px;font-weight:700;padding:3px 8px;border-radius:10px;"><span leaf="">{{CASE 01}}</span></span>
  </p>
  <p style="margin:0 0 4px;font-size:16px;font-weight:800;color:#111827;line-height:1.5;">
    <span leaf="">{{标题}}</span>
  </p>
  <p style="margin:0 0 10px;font-size:12px;color:#9CA3AF;">
    <span leaf="">{{英文副标题}}</span>
  </p>
  <p style="margin:0 0 12px;font-size:14px;line-height:1.9;color:#374151;">
    <span leaf="">{{内容}}</span>
  </p>
  <!-- 节点配图（可选）：<section style="margin:0;text-align:center;"><span leaf=""><img src="{{公网图片URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span></section> -->
</section>
```

### 11e. tool-card（工具说明卡片）

基本版：

```html
<section style="background:#fff;border-radius:12px;padding:16px 20px;box-shadow:0 4px 16px rgba(5,150,105,0.12);margin-bottom:24px;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.8;">
    {{说明内容}}
  </p>
</section>
```

居中高亮版（同 oneliner-card 规则：拆多个 `<p>`，不要 `<strong>` 带 font-size/border-bottom）：

```html
<section style="background:#fff;border-radius:12px;padding:16px 20px;box-shadow:0 4px 16px rgba(5,150,105,0.12);margin-bottom:24px;text-align:center;">
  <p style="font-size:13px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">
    <span leaf="">{{小字}}</span>
  </p>
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#059669;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{高亮大字}}</span></span>
  </p>
</section>
```

### 11f. table（表格）

本主题保留 `<table>` 组件（摸鱼绿实测微信可用）；Markdown 表格优先用它，数据密度低时也可改用 11c 三列卡片。

```html
<section style="margin:0 20px 24px;">
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    <thead>
      <tr>
        <th style="background:#059669;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题1}}</span></th>
        <th style="background:#059669;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题2}}</span></th>
        <th style="background:#059669;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题3}}</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
      </tr>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
      </tr>
    </tbody>
  </table>
</section>
```

偶数行自动带浅灰背景 `#F9FAFB`，列数按实际需求增减。

### 11g. ordered-list（数字编号列表）

> **粘贴安全说明**：旧版编号圆圈用 flex + inline-flex 居中，实测变形。现版编号是行内 `inline-block` 圆（`line-height` 撑高居中），与文字同在一个 `<p>` 内。

```html
<section style="margin:0 20px 24px;">
  <p style="font-size:14px;color:#374151;margin:0 0 12px;line-height:1.9;">
    <span style="display:inline-block;width:22px;height:22px;line-height:22px;text-align:center;background:#059669;color:#fff;font-size:11px;font-weight:700;border-radius:50%;margin-right:8px;"><span leaf="">1</span></span><span leaf="">{{列表项内容}}</span>
  </p>
  <p style="font-size:14px;color:#374151;margin:0 0 12px;line-height:1.9;">
    <span style="display:inline-block;width:22px;height:22px;line-height:22px;text-align:center;background:#059669;color:#fff;font-size:11px;font-weight:700;border-radius:50%;margin-right:8px;"><span leaf="">2</span></span><span leaf="">{{列表项内容}}</span>
  </p>
  <p style="font-size:14px;color:#374151;margin:0 0 12px;line-height:1.9;">
    <span style="display:inline-block;width:22px;height:22px;line-height:22px;text-align:center;background:#059669;color:#fff;font-size:11px;font-weight:700;border-radius:50%;margin-right:8px;"><span leaf="">3</span></span><span leaf="">{{列表项内容}}</span>
  </p>
</section>
```

---

## 组件 12 媒体组件

### 12a. image（图片容器）

**`<img>` 的 src 必须是公网 http(s) URL**（推荐公众号素材库的 mmbiz.qpic.cn 地址）——相对路径/本地路径粘贴时会被静默剥掉，只留下文字。图片自适应居中、不铺满：

```html
<section style="margin:0 20px 28px;text-align:center;">
  <span leaf=""><img src="{{公网图片URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
</section>
```

### 12b. video-placeholder（视频占位框）

> **纠正**：旧版 video-card 注释"保留原始视频代码不修改"不成立——`<video>` 标签和本地视频文件**无法随粘贴带入编辑器**。视频一律用本占位框，并在交付时提示用户在编辑器对应位置手动「插入视频」。

```html
<section style="margin:0 20px 28px;padding:22px 16px;border:1px dashed #A7F3D0;border-radius:12px;background:#F0FDF4;text-align:center;">
  <p style="margin:0 0 8px;font-size:13px;font-weight:700;color:#059669;">
    <span leaf="">VIDEO 01 · {{视频描述}}</span>
  </p>
  <p style="margin:0;font-size:13px;color:#6B7280;line-height:1.7;">
    <span leaf="">粘贴后请在公众号编辑器插入视频：{{视频文件名}}</span>
  </p>
</section>
```

---

## 组件 13 结尾组件

### 13a. footer-cta（互动三连区，即本主题的签名/CTA 区）

> **纠正**：旧版注释"SVG 图标微信支持，原样保留"不成立——`<svg>` 粘贴进编辑器后会被静默剥掉，只剩三个空方块。现版去掉图标，用居中文案表达三连引导，实测粘贴稳定。

固定文案照写：

```html
<section style="margin:0 20px 24px;padding:24px 16px;background:#F9FAFB;border:1px solid #E5E7EB;border-radius:12px;text-align:center;">
  <p style="margin:0 0 8px;font-size:14px;font-weight:700;color:#111827;line-height:1.7;">
    <span leaf="">既然看到这里了，如果觉得有用，随手点个赞、在看、转发三连吧。</span>
  </p>
  <p style="margin:0;font-size:14px;color:#059669;font-weight:700;">
    <span leaf="">点赞 · 在看 · 转发</span>
  </p>
</section>
```

**签名文案适配**：SKILL.md 的作者签名（"我是 {{作者名}}…"两段，默认占位、由用户替换）以正文段落（组件 5）形式放在 footer-cta **之前**；footer-cta 内部文案保持上面的固定句式，两者不重复出现"三连"字样时可将签名第二段并入 footer-cta 顶部文字。

### 13b. brand-card（品牌尾图）

```html
<section style="text-align:center;" nodeleaf="">
  <!-- 保留原始品牌尾图代码不修改 -->
</section>
```

有品牌尾图素材时放在 footer-cta 之后，无素材整块省略。

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.8;">

  <!-- 1. 封面（组件2 cover-breaking，有图/无图二选一） -->

  <!-- 2. 目录（组件3 toc-list，2+ 章节时生成，紧跟封面之下） -->

  <!-- 3. 开头引言（组件9b oneliner-card，文章有开头金句时） -->

  <!-- 4. 前言正文（组件5 段落 × N，段落自带 0 20px 左右边距） -->

  <!-- 5. 第一章（组件4 chapter-title，margin:16px 20px 20px） -->
  <!--    章内：组件5 正文 + 组件6 行内样式 + 组件7 标签 + 组件8 代码 + 组件9 引用亮点 + 组件10 提示 + 组件11 布局 + 组件12 媒体 -->

  <!-- 6. 第二章…第N章（组件4，margin:40px 20px 20px） -->

  <!-- 7. 结语章（组件4 变体：编号 ///，章名"写在最后"） -->

  <!-- 8. 互动三连（组件13a footer-cta，前面放固定签名段落） -->

  <!-- 9. 品牌尾图（组件13b，有素材才加） -->

</section>
```

**骨架顺序铁律**：目录 toc-list **必须紧跟封面之下**，在开头引言和前言正文之前——读者先看全文地图再进入内容。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 绿色加粗 6a / 黄底下划线 6d / oneliner-card 9b | 核心概念、产品名、关键结论 | 全文 ≤5 处 |
| **标记层** | 绿色下划线 6e（默认）/ 黄色纯色高亮 6c | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | quote-box 9a / 提示 10x / 胶囊 11a / 卡片 11x | 引用、旁注、提示、结构化信息 | 按需 |

**克制原则**：
- 黄色高亮每段不超过 1-2 处；一段内不超过 2 种高亮效果
- 红色下划线只用于对比/否定，不做普通强调
- 绿色纯色背景仅出现在封面底条、目录首卡、流程首卡等结构位

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇的排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3，避免花哨。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 教程/操作指南 | step-label 7a + cmd/prompt 8a/8b + 代码块（通用库1a） | warn-tip 10a、green-tip 10b、flow-cards 11b |
| 盘点/工具清单 | skill/tool-label 7c + tool-card 11e + pill-list 11a | table 11f、oneliner-card 9b |
| 观点/深度分析 | paragraph 5 + quote-box 9a + oneliner-card 9b | center-divider 9d、subtitle-highlight 9c |
| 访谈/人物特稿 | paragraph 5 + quote-box 9a（引语）+ timeline 11d（经历脉络） | oneliner-card 9b、center-divider 9d |
| 数据复盘/报告 | three-col-cards 11c + table 11f + ordered-list 11g | green-info 10d、黄色纯色高亮 6c |
| 生活/情感随笔 | paragraph 5 + oneliner-card 9b + center-divider 9d | quote-box 9a（少量） |
| 案例实战 | case-label 7b / timeline 11d + step-label 7a | prompt-block 8a、yellow-warning 10c |

所有类型共用固定结构：封面 2 + 目录 3 + 章节标题 4 + 签名/三连 13。

---

## Markdown → 摸鱼绿排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置；封面主标题从中提炼（视角错开） |
| 文章开头 `> 引言` | 组件 9b oneliner-card 或并入封面副标题 | 开头金句 |
| `## 章节标题` | 组件 4 chapter-title | PART 01/02/03…，末章 /// + LAST |
| `### 子标题` | 组件 9c subtitle-highlight | 黄色浅底小节标题 |
| 普通段落 | 组件 5 paragraph | 每段主动标 1~3 处绿色下划线 6e |
| `**加粗文字**` | 组件 6a 绿色加粗 | 核心概念/品牌名 |
| `==高亮文字==` | 组件 6c 黄色纯色高亮 | 每段 ≤2 处 |
| `<u>下划线</u>` / `++文字++` | 组件 6e 绿色下划线 | 次要强调 |
| `~~删除线~~` | 组件 6i 删除线灰色 | 被淘汰的概念 |
| `> 引用段落`（非开头） | 组件 9a quote-box | 灰色虚线框（本主题特征） |
| 核心金句 | 组件 9b oneliner-card / 9d center-divider | 视觉焦点 |
| 操作步骤 | 组件 7a step-label（+ 8a/8b） | STEP 01/02… |
| 案例/场景 | 组件 7b case-label 或 11d timeline | CASE 01/02… |
| 技能/工具清单 | 组件 7c skill/tool-label + 11e tool-card | |
| Prompt 提示词 | 组件 8a prompt-block（短）/ 通用库 1a（长多行） | |
| 单行命令 | 组件 8b cmd-block | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色（默认）/ 1b 浅色（左竖条换 #059669） | 每行一个 `<p style="margin:0">` |
| 行内 `` `code` `` | 组件 6g 代码标签 | |
| 并列要点 | 组件 11a pill-list | |
| 流程（3 步） | 组件 11b flow-cards | 箭头可换 × 做对比 |
| 三项对比 | 组件 11c three-col-cards | |
| 递进/时间脉络 | 组件 11d timeline | |
| Markdown 表格 | 组件 11f table | 偶数行浅灰底 |
| `1. 2. 3.` 编号列表 | 组件 11g ordered-list | |
| 注意/警告 | 组件 10a warn-tip / 10c yellow-warning | |
| 亮点提示 | 组件 10b green-tip / 10d green-info | |
| `![](图片)` | 组件 12a image | src 必须是公网 http(s) URL，相对路径会被静默剥掉 |
| 视频 | 组件 12b video-placeholder | 视频无法粘贴带入，占位框提示编辑器手动插入 |
| 文末 | 组件 13a footer-cta（+ 13b brand-card） | 签名段落放 footer-cta 前 |
