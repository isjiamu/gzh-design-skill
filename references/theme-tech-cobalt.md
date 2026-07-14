# 公众号排版组件库 —— 科技钴蓝

> **使用说明**：本组件库为「科技钴蓝」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：冷静清晰的科技刊读风，卡片丰富、信息密度高。钴蓝主色负责结构和导航，黄色高亮负责关键结论，搭配杂志快讯封面、横向滚动目录和标签化章节。适合 AI 工具、开发教程、产品说明、工作流指南等技术内容。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（圆点、渐变分割线、装饰短横、时间线竖线）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`——微信编辑器会自动"纠正"导致样式被重写。正确做法：拆成多个 `<p>`，每个 `<p>` 只有一个字号；高亮样式统一挂在外层 `<span>` 上
> - 不用 `position:absolute` 做划线/高亮，删除线用 `text-decoration:line-through`
> - 结构化区域（如封面右侧图片槽位）没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
主色调：       #1D4ED8（cobalt-700）
辅色：         #2563EB（blue-600）
浅蓝装饰：     #60A5FA / #93C5FD
浅蓝边框：     #BFDBFE
浅蓝背景：     #EFF6FF
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
全局行高：     1.75
字间距：       0.5px
最大宽度：     677px
内容区边距：   0 20px（模块左右各 20px）
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 封面 cover-breaking（杂志快讯封面）

> **文案策略（先读，比代码重要）**：
> - 封面标题和公众号外标题是**两层标题**，必须视角错开——外标题卖"为什么点开"，封面卖"里面讲什么"
> - 已知外标题时，主标题**禁止原样复述**其核心关键词（产品名/功能名/场景词）；未知外标题时从五个视角（**数字反差 / 角色革命 / 案例串 / 方法论 / 情绪钩子**）自选一个直出，不停下来问
> - 产品名/功能名只允许出现在**底部品牌条**或**副标题关键词条**，不出现在大字主标题
> - 仅当用户要求"帮我定封面方向"时才列 3-5 个方向让用户选

**有右侧图片版**：

```html
<section style="margin:0 0 32px;background:#fff;border:1.5px solid rgba(29,78,216,0.15);border-radius:20px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.06);width:100%;">
  <section style="padding:32px 28px 28px;">
    <section style="display:flex;align-items:center;gap:8px;margin-bottom:28px;">
      <span style="width:6px;height:6px;background:#1D4ED8;border-radius:50%;"><span leaf=""><br></span></span>
      <span style="font-size:11px;font-weight:700;letter-spacing:3px;color:#1D4ED8;"><span leaf="">{{顶部标签}}</span></span>
      <section style="flex:1;height:1px;overflow:hidden;background:linear-gradient(to right,rgba(29,78,216,0.12),transparent);"><span leaf=""><br></span></section>
      <span style="font-size:10px;color:#D1D5DB;font-weight:600;"><span leaf="">{{日期}}</span></span>
    </section>
    <section style="display:flex;align-items:center;gap:20px;">
      <section style="flex:1;min-width:0;">
        <p style="font-size:15px;color:#D1D5DB;margin:0 0 6px;text-decoration:line-through;letter-spacing:0.5px;">
          <span leaf="">{{划线旧认知}}</span>
        </p>
        <p style="font-size:24px;font-weight:900;color:#111827;margin:0;line-height:1.05;letter-spacing:-2px;">
          <span leaf="">{{主标题行1}}</span>
          <span style="color:#1D4ED8;"><span leaf="">{{钴蓝高亮词}}</span></span>
        </p>
        <p style="font-size:24px;font-weight:900;color:#1D4ED8;margin:0 0 16px;line-height:1.05;letter-spacing:-2px;">
          <span leaf="">{{主标题行2}}</span>
        </p>
        <section style="width:48px;height:3px;background:linear-gradient(to right,#1D4ED8,#60A5FA);border-radius:2px;margin-bottom:12px;">
          <span leaf=""><br></span>
        </section>
        <p style="font-size:13px;color:#9CA3AF;margin:0;line-height:1.7;letter-spacing:0.5px;">
          <span leaf="">{{副标题关键词}}</span>
        </p>
      </section>
      <section style="flex-shrink:0;width:110px;height:110px;border-radius:16px;overflow:hidden;border:1px solid rgba(29,78,216,0.1);box-shadow:0 4px 12px rgba(0,0,0,0.06);">
        <!-- 封面右侧图片，保留原图代码 -->
      </section>
    </section>
  </section>
  <section style="background:linear-gradient(135deg,#1D4ED8,#2563EB);padding:12px 28px;display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:12px;color:rgba(255,255,255,0.9);margin:0;font-weight:600;letter-spacing:0.5px;">
      <span leaf="">{{底部左侧文字}}</span>
    </p>
    <section style="display:flex;gap:4px;">
      <span style="background:rgba(255,255,255,0.2);padding:1px 6px;border-radius:3px;font-size:8px;color:#fff;font-weight:600;"><span leaf="">{{标签1}}</span></span>
      <span style="background:rgba(255,255,255,0.2);padding:1px 6px;border-radius:3px;font-size:8px;color:#fff;font-weight:600;"><span leaf="">{{标签2}}</span></span>
    </section>
  </section>
</section>
```

**无右侧图片版**（文章没有封面头像图时用这个，标题区满宽）：

```html
<section style="margin:0 0 32px;background:#fff;border:1.5px solid rgba(29,78,216,0.15);border-radius:20px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.06);width:100%;">
  <section style="padding:32px 28px 28px;">
    <section style="display:flex;align-items:center;gap:8px;margin-bottom:28px;">
      <span style="width:6px;height:6px;background:#1D4ED8;border-radius:50%;"><span leaf=""><br></span></span>
      <span style="font-size:11px;font-weight:700;letter-spacing:3px;color:#1D4ED8;"><span leaf="">{{顶部标签}}</span></span>
      <section style="flex:1;height:1px;overflow:hidden;background:linear-gradient(to right,rgba(29,78,216,0.12),transparent);"><span leaf=""><br></span></section>
      <span style="font-size:10px;color:#D1D5DB;font-weight:600;"><span leaf="">{{日期}}</span></span>
    </section>
    <section>
      <p style="font-size:15px;color:#D1D5DB;margin:0 0 6px;text-decoration:line-through;letter-spacing:0.5px;">
        <span leaf="">{{划线旧认知}}</span>
      </p>
      <p style="font-size:24px;font-weight:900;color:#111827;margin:0;line-height:1.05;letter-spacing:-2px;">
        <span leaf="">{{主标题行1}}</span>
        <span style="color:#1D4ED8;"><span leaf="">{{钴蓝高亮词}}</span></span>
      </p>
      <p style="font-size:24px;font-weight:900;color:#1D4ED8;margin:0 0 16px;line-height:1.05;letter-spacing:-2px;">
        <span leaf="">{{主标题行2}}</span>
      </p>
      <section style="width:48px;height:3px;background:linear-gradient(to right,#1D4ED8,#60A5FA);border-radius:2px;margin-bottom:12px;">
        <span leaf=""><br></span>
      </section>
      <p style="font-size:13px;color:#9CA3AF;margin:0;line-height:1.7;letter-spacing:0.5px;">
        <span leaf="">{{副标题关键词}}</span>
      </p>
    </section>
  </section>
  <section style="background:linear-gradient(135deg,#1D4ED8,#2563EB);padding:12px 28px;display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:12px;color:rgba(255,255,255,0.9);margin:0;font-weight:600;letter-spacing:0.5px;">
      <span leaf="">{{底部左侧文字}}</span>
    </p>
    <section style="display:flex;gap:4px;">
      <span style="background:rgba(255,255,255,0.2);padding:1px 6px;border-radius:3px;font-size:8px;color:#fff;font-weight:600;"><span leaf="">{{标签1}}</span></span>
      <span style="background:rgba(255,255,255,0.2);padding:1px 6px;border-radius:3px;font-size:8px;color:#fff;font-weight:600;"><span leaf="">{{标签2}}</span></span>
    </section>
  </section>
</section>
```

**可替换元素**：
- `{{顶部标签}}` → 如 `TUTORIAL · 品牌实战`、`AI VIDEO · 实战案例`、`BREAKING`（建议 10-15 字符以内）
- `{{日期}}` → 如 `2026.07`
- `{{划线旧认知}}` → 被颠覆的旧观念（例：`MV要专业团队？`）
- `{{主标题行1}}` → 标题前半段（黑色）；`{{钴蓝高亮词}}` → 标题中的钴蓝强调词；`{{主标题行2}}` → 标题第二行（全钴蓝）
- `{{副标题关键词}}` → 简短关键词，用 `·` 分隔
- `{{底部左侧文字}}` → 产品/品牌名；`{{标签1/2}}` → 底部小标签

---

## 组件 3 目录 toc-scroll（横向滚动目录）

2 个及以上章节时生成。第一个卡片钴蓝高亮，最后一个固定为"写在最后"（PART ///）。

```html
<section style="margin:0 20px 32px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">
    <p style="font-size:10px;color:#9CA3AF;margin:0;text-transform:uppercase;letter-spacing:2px;font-weight:600;">
      <span leaf="">📦 {{N}} Parts + Conclusion</span>
    </p>
    <p style="font-size:10px;color:#9CA3AF;margin:0;">
      <span leaf="">👉 滑动</span>
    </p>
  </section>
  <section style="overflow-x:scroll;-webkit-overflow-scrolling:touch;white-space:nowrap;padding-bottom:8px;">
    <!-- 第一个（当前高亮，钴蓝背景） -->
    <section style="display:inline-block;white-space:normal;vertical-align:top;width:110px;background:linear-gradient(135deg,#1D4ED8,#2563EB);border-radius:12px;padding:12px;margin-right:8px;">
      <p style="font-size:9px;font-weight:700;color:rgba(255,255,255,0.7);letter-spacing:1px;margin:0 0 5px;">
        <span leaf="">PART 01</span>
      </p>
      <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;">
        <span leaf="">{{章节名}}</span>
      </p>
      <p style="font-size:10px;color:rgba(255,255,255,0.7);margin:0;">
        <span leaf="">{{副标题}}</span>
      </p>
    </section>
    <!-- 后续章节（白色背景），按需重复 -->
    <section style="display:inline-block;white-space:normal;vertical-align:top;width:110px;background:#fff;border:1px solid #E5E7EB;border-radius:12px;padding:12px;margin-right:8px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">
      <p style="font-size:9px;font-weight:700;color:#9CA3AF;letter-spacing:1px;margin:0 0 5px;">
        <span leaf="">PART 02</span>
      </p>
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">{{章节名}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;">
        <span leaf="">{{副标题}}</span>
      </p>
    </section>
    <!-- 最后一个（写在最后） -->
    <section style="display:inline-block;white-space:normal;vertical-align:top;width:110px;background:#fff;border:1px solid #E5E7EB;border-radius:12px;padding:12px;box-shadow:0 2px 6px rgba(0,0,0,0.04);">
      <p style="font-size:9px;font-weight:700;color:#9CA3AF;letter-spacing:1px;margin:0 0 5px;">
        <span leaf="">PART ///</span>
      </p>
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">写在最后</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;">
        <span leaf="">{{副标题}}</span>
      </p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节标题 chapter-title

第一个章节用 `margin-top:16px`，后续章节用 `margin-top:48px`。最后一章编号用 `///`，PART 改为 `LAST`。

```html
<section style="margin-top:48px;margin-bottom:32px;padding:0 20px;">
  <section style="display:flex;align-items:center;gap:16px;margin-bottom:24px;">
    <section style="text-align:center;flex-shrink:0;">
      <p style="margin:0;font-size:28px;font-weight:900;color:#1D4ED8;line-height:1;letter-spacing:-2px;">
        <span leaf="">{{01}}</span>
      </p>
      <p style="margin:0;font-size:8px;font-weight:700;color:#D1D5DB;letter-spacing:2px;">
        <span leaf="">PART</span>
      </p>
    </section>
    <span style="width:1px;height:36px;background:#E5E7EB;flex-shrink:0;"><span leaf=""><br></span></span>
    <section>
      <p style="margin:0 0 1px;font-size:17px;font-weight:900;color:#111827;letter-spacing:0.3px;">
        <span leaf="">{{中文标题}}</span>
      </p>
      <p style="margin:0;font-size:11px;font-weight:600;color:#9CA3AF;letter-spacing:1.5px;">
        <span leaf="">{{ENGLISH · 英文副标题}}</span>
      </p>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

---

## 组件 5 正文段落 paragraph

```html
<p style="margin-bottom:16px;font-size:14px;line-height:1.9;text-align:justify;">
  <span leaf="">{{正文内容}}</span>
</p>
```

段间距较大时用 `margin-bottom:24px`。

---

## 组件 6 行内样式（9 种 + 使用原则）

### 6a. 钴蓝加粗（核心概念、关键结论、品牌名/产品名）

```html
<strong style="color:#1D4ED8;"><span leaf="">文字</span></strong>
```

### 6b. 钴蓝背景标签

```html
<strong style="color:#1D4ED8;background:rgba(29,78,216,0.1);padding:0 4px;border-radius:2px;"><span leaf="">文字</span></strong>
```

### 6c. 黄色渐变高亮（一段话中最想让读者注意的短语，每段不超过 1-2 处）

```html
<span style="background:linear-gradient(120deg,#FDE68A 0%,rgba(255,255,255,0) 100%);padding:0 4px;border-radius:2px;font-weight:600;color:#111827;"><span leaf="">文字</span></span>
```

### 6d. 黄色底部高亮（下划线效果）

```html
<span style="color:#111827;font-weight:bold;border-bottom:3px solid #FDE68A;"><span leaf="">文字</span></span>
```

### 6e. 钴蓝下划线（次要强调，**正文关键词的默认标记**）

```html
<span style="border-bottom:2px solid #93C5FD;font-weight:600;"><span leaf="">文字</span></span>
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
1. 钴蓝加粗用于核心概念、关键结论、品牌名/产品名
2. 黄色高亮每段不超过 1-2 处
3. 钴蓝下划线用于次要强调（正文关键词逐段标记用它）
4. 红色下划线用于对比、否定
5. 删除线灰色用于被淘汰的概念
6. 一段文字中不要同时使用超过 2 种高亮效果

---

## 组件 7 内容标签组（STEP / CASE / SKILL / TOOL）

### 7a. step-label（STEP 步骤标签）

```html
<section style="margin-bottom:24px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#111827;color:#fff;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">STEP 01</span></span>
    <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
      <span leaf="">{{步骤标题}}</span>
    </h4>
  </section>
  <p style="font-size:14px;margin:0 0 16px;color:#4B5563;line-height:1.9;text-align:justify;">
    <span leaf="">{{步骤内容}}</span>
  </p>
</section>
```

### 7b. case-label（CASE 案例标签）

```html
<section style="margin-bottom:28px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#E5E7EB;color:#6B7280;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">CASE 01</span></span>
    <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
      <span leaf="">{{案例标题}}</span>
    </h4>
  </section>
  <!-- 案例内容 -->
</section>
```

### 7c. skill-label / tool-label（编号标签）

```html
<section style="margin-bottom:28px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#111827;color:#fff;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">SKILL 1</span></span>
    <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
      <span leaf="">{{名称}}</span>
    </h4>
  </section>
</section>
```

`SKILL 1` 可替换为 `TOOL 摄像机`、`TOOL 打光` 等。

---

## 组件 8 代码/命令/Prompt

### 8a. prompt-block（PROMPT 展示块）

```html
<p style="font-size:13px;color:#374151;margin:0 0 16px;line-height:1.8;">
  <span style="display:inline-block;background:#1D4ED8;color:#fff;font-size:11px;font-weight:700;padding:1px 7px;border-radius:3px;margin-right:6px;vertical-align:middle;letter-spacing:0.5px;"><span leaf="">PROMPT</span></span>
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

多行代码块**不设主题专属组件**，直接用 `common-components.md` 的 1a 深色代码块（每行一个 `<p style="margin:0">`，禁 `white-space:pre`）；浅色场景用 1b 并把左竖条换成 `#1D4ED8`。

---

## 组件 9 引用与亮点

### 9a. quote-box（浅蓝左边框引用块）

所有引用、补充说明的**默认组件**，用左边框建立层级，避免四周虚线框干扰阅读：

```html
<section style="background:#F9FAFB;border-left:3px solid #93C5FD;border-radius:0 8px 8px 0;padding:12px 16px;margin-bottom:24px;text-align:justify;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.6;">
    <span leaf="">{{引用内容，可嵌入钴蓝加粗等内联样式}}</span>
  </p>
</section>
```

### 9b. oneliner-card（一句话亮点卡片）

> 兼容性关键规则：**不要把 `font-size` 打在 `<strong>` 上**，不要在同一个 `<p>` 里混多个字号；高亮样式统一挂在外层 `<span>` 上。

单行版（只有主金句）：

```html
<section style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#1D4ED8;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{亮点内容}}</span></span>
  </p>
</section>
```

带前缀引导语版（两段式）：

```html
<section style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="font-size:12px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">
    <span leaf="">{{引导语}}</span>
  </p>
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#1D4ED8;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{亮点内容}}</span></span>
  </p>
</section>
```

带下方补充说明版：

```html
<section style="background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:14px 16px;margin-bottom:24px;text-align:center;">
  <p style="margin:0 0 6px;line-height:1.6;">
    <span style="font-size:15px;color:#1D4ED8;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{高亮内容}}</span></span>
  </p>
  <p style="font-size:13px;color:#9CA3AF;margin:0;line-height:1.5;">
    <span leaf="">{{补充说明}}</span>
  </p>
</section>
```

### 9c. subtitle-highlight（小节黄色下划线标题）

```html
<p style="font-size:15px;font-weight:900;color:#111827;margin-bottom:16px;">
  <span style="background:linear-gradient(180deg,transparent 65%,#FDE68A 65%);padding:0 4px;"><span leaf="">{{小节标题}}</span></span>
</p>
```

可加 `margin-top:32px` 增加上间距。

### 9d. center-divider（居中金句分隔）

```html
<p style="font-size:14px;margin-bottom:20px;text-align:center;color:#1D4ED8;font-weight:700;letter-spacing:1px;border-top:1px solid #F3F4F6;border-bottom:1px solid #F3F4F6;padding:12px 0;">
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

### 10b. cobalt-tip（钴蓝提示）

```html
<section style="padding:6px 0 4px;margin-bottom:16px;">
  <p style="margin-bottom:6px;font-size:12px;font-weight:700;color:#9CA3AF;letter-spacing:1px;">
    <span style="color:#1D4ED8;"><span leaf="">✦ {{提示标题}}</span></span>
  </p>
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;">
    <span leaf="">{{提示内容}}</span>
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

### 10d. cobalt-info（钴蓝信息框）

```html
<section style="background:#EFF6FF;padding:12px 16px;border-radius:8px;border:1px solid #BFDBFE;margin-bottom:20px;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.7;text-align:justify;">
    <span leaf="">{{信息内容}}</span>
  </p>
</section>
```

---

## 组件 11 布局组件

### 11a. pill-list（钴蓝胶囊列表）

基本版：

```html
<section style="margin-bottom:14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:13px;font-weight:700;color:#1D4ED8;background:rgba(29,78,216,0.08);padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#1D4ED8;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{列表项文字}}</span></span>
  </p>
</section>
```

带说明文字版：

```html
<section style="margin-bottom:14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:13px;font-weight:700;color:#1D4ED8;background:rgba(29,78,216,0.08);padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#1D4ED8;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{标题}}</span></span>
  </p>
  <p style="font-size:13px;color:#4B5563;margin:0;line-height:1.7;text-align:justify;">
    <span leaf="">{{描述内容}}</span>
  </p>
</section>
```

### 11b. flow-cards（三步横排流程卡片）

```html
<section style="background:#F9FAFB;padding:16px;border-radius:12px;border:1px solid #F3F4F6;margin-bottom:24px;">
  <section style="display:flex;align-items:stretch;justify-content:center;gap:6px;">
    <section style="flex:1;text-align:center;padding:10px 8px;background:linear-gradient(135deg,#1D4ED8,#2563EB);border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;">
        <span leaf="">{{步骤1标题}}</span>
      </p>
      <p style="font-size:10px;color:rgba(255,255,255,0.8);margin:0;line-height:1.5;">
        <span leaf="">{{步骤1描述}}</span>
      </p>
    </section>
    <section style="display:flex;align-items:center;color:#D1D5DB;font-size:14px;padding:0 4px;">
      <span leaf="">→</span>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">{{步骤2标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{步骤2描述}}</span>
      </p>
    </section>
    <section style="display:flex;align-items:center;color:#D1D5DB;font-size:14px;padding:0 4px;">
      <span leaf="">→</span>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #93C5FD;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#1D4ED8;margin:0 0 3px;">
        <span leaf="">{{步骤3标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{步骤3描述}}</span>
      </p>
    </section>
  </section>
  <p style="font-size:12px;color:#9CA3AF;text-align:center;margin:12px 0 0;letter-spacing:0.5px;">
    <span leaf="">{{底部说明文字}}</span>
  </p>
</section>
```

箭头 `→` 可替换为 `×` 做对比型布局。

### 11c. three-col-cards（三列对比卡片）

```html
<section style="background:#F9FAFB;padding:16px;border-radius:12px;border:1px solid #F3F4F6;margin-bottom:28px;">
  <section style="display:flex;align-items:stretch;justify-content:center;gap:6px;">
    <section style="flex:1;text-align:center;padding:10px 8px;background:linear-gradient(135deg,#1D4ED8,#2563EB);border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#fff;margin:0 0 3px;">
        <span leaf="">{{卡片1标题}}</span>
      </p>
      <p style="font-size:10px;color:rgba(255,255,255,0.8);margin:0;line-height:1.5;">
        <span leaf="">{{卡片1描述}}</span>
      </p>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">{{卡片2标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{卡片2描述}}</span>
      </p>
    </section>
    <section style="flex:1;text-align:center;padding:10px 8px;background:#fff;border:1px solid #E5E7EB;border-radius:8px;">
      <p style="font-size:13px;font-weight:800;color:#111827;margin:0 0 3px;">
        <span leaf="">{{卡片3标题}}</span>
      </p>
      <p style="font-size:10px;color:#9CA3AF;margin:0;line-height:1.5;">
        <span leaf="">{{卡片3描述}}</span>
      </p>
    </section>
  </section>
</section>
```

### 11d. timeline（时间线列表）

```html
<section style="display:flex;margin-bottom:28px;">
  <section style="display:flex;flex-direction:column;align-items:center;margin-right:16px;flex-shrink:0;">
    <section style="width:14px;height:14px;border-radius:50%;border:3px solid #1D4ED8;background:#fff;margin-top:4px;box-shadow:0 0 0 2px #fff;">
      <span leaf=""><br></span>
    </section>
    <section style="width:2px;background:#E5E7EB;flex:1;margin-top:4px;min-height:48px;">
      <span leaf=""><br></span>
    </section>
  </section>
  <section style="flex:1;padding-bottom:12px;">
    <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap;">
      <span style="display:inline-block;background:#111827;color:#fff;font-size:10px;font-weight:700;padding:2px 8px;border-radius:12px;"><span leaf="">{{CASE 01}}</span></span>
      <h4 style="font-size:15px;font-weight:800;color:#111827;margin:0;">
        <span leaf="">{{标题}}</span>
      </h4>
    </section>
    <p style="font-size:11px;font-weight:600;color:#9CA3AF;letter-spacing:1px;margin:0 0 12px;">
      <span leaf="">{{英文副标题}}</span>
    </p>
    <p style="font-size:14px;margin:0 0 16px;color:#4B5563;line-height:1.7;text-align:justify;">
      <span leaf="">{{内容}}</span>
    </p>
  </section>
</section>
```

最后一个时间线节点去掉竖线部分。

### 11e. tool-card（工具说明卡片）

基本版：

```html
<section style="background:#fff;border-radius:12px;padding:16px 20px;box-shadow:0 4px 16px rgba(29,78,216,0.12);margin-bottom:24px;">
  <p style="font-size:13px;color:#374151;margin:0;line-height:1.8;">
    <span leaf="">{{说明内容}}</span>
  </p>
</section>
```

居中高亮版（同 oneliner-card 规则：拆多个 `<p>`，不要 `<strong>` 带 font-size/border-bottom）：

```html
<section style="background:#fff;border-radius:12px;padding:16px 20px;box-shadow:0 4px 16px rgba(29,78,216,0.12);margin-bottom:24px;text-align:center;">
  <p style="font-size:13px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">
    <span leaf="">{{小字}}</span>
  </p>
  <p style="margin:0;line-height:1.6;">
    <span style="font-size:15px;color:#1D4ED8;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;"><span leaf="">{{高亮大字}}</span></span>
  </p>
</section>
```

### 11f. table（表格）

本主题保留经过现有主题验证的 `<table>` 组件；Markdown 表格优先用它，数据密度低时也可改用 11c 三列卡片。

```html
<section style="margin-bottom:24px;overflow-x:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    <thead>
      <tr>
        <th style="background:#1D4ED8;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题1}}</span></th>
        <th style="background:#1D4ED8;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题2}}</span></th>
        <th style="background:#1D4ED8;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题3}}</span></th>
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

```html
<section style="margin-bottom:24px;">
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#1D4ED8;color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">1</span></span>
    <p style="font-size:14px;color:#374151;margin:0;line-height:1.9;flex:1;">
      <span leaf="">{{列表项内容}}</span>
    </p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#1D4ED8;color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">2</span></span>
    <p style="font-size:14px;color:#374151;margin:0;line-height:1.9;flex:1;">
      <span leaf="">{{列表项内容}}</span>
    </p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#1D4ED8;color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">3</span></span>
    <p style="font-size:14px;color:#374151;margin:0;line-height:1.9;flex:1;">
      <span leaf="">{{列表项内容}}</span>
    </p>
  </section>
</section>
```

---

## 组件 12 媒体组件

### 12a. image（图片容器）

```html
<section style="text-align:center;margin-bottom:24px;border-radius:12px;overflow:hidden;">
  <!-- 保留原始图片代码不修改 -->
</section>
```

### 12b. video-card（视频容器卡片）

```html
<section style="background:#fff;border-radius:16px;padding:12px;margin-bottom:32px;border:2px solid #1D4ED8;box-shadow:0 4px 12px rgba(29,78,216,0.1);">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="width:8px;height:8px;background:#1D4ED8;border-radius:50%;"><span leaf=""><br></span></span>
    <span style="font-size:11px;color:#1D4ED8;font-weight:700;letter-spacing:1px;"><span leaf="">VIDEO 01</span></span>
    <span style="flex:1;height:1px;background:linear-gradient(to right,rgba(29,78,216,0.2),transparent);"><span leaf=""><br></span></span>
    <span style="font-size:11px;color:#9CA3AF;"><span leaf="">{{视频描述}}</span></span>
  </section>
  <section style="border-radius:10px;overflow:hidden;">
    <!-- 保留原始视频代码不修改 -->
  </section>
</section>
```

---

## 组件 13 结尾组件

### 13a. footer-cta（互动三连区，即本主题的签名/CTA 区）

固定文案照写；SVG 图标微信支持，原样保留。

```html
<section style="background:radial-gradient(circle at center,#F9FAFB 0%,#FFFFFF 100%);border:1px solid #E5E7EB;border-radius:16px;padding:32px 20px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.03);margin:0 0 24px;">
  <p style="font-size:13px;font-weight:bold;color:#111827;margin-bottom:20px;line-height:1.6;">
    <span leaf="">既然看到这里了，如果觉得有用，随手点个赞、在看、转发三连吧。</span>
  </p>
  <section style="display:flex;justify-content:center;gap:24px;margin-bottom:16px;">
    <section style="text-align:center;cursor:pointer;color:#4B5563;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#fff;border-radius:12px;box-shadow:0 2px 4px rgba(0,0,0,0.05);border:1px solid #F3F4F6;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg>
      </section>
      <span style="font-size:10px;font-weight:600;"><span leaf="">点赞</span></span>
    </section>
    <section style="text-align:center;cursor:pointer;color:#4B5563;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#fff;border-radius:12px;box-shadow:0 2px 4px rgba(0,0,0,0.05);border:1px solid #F3F4F6;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"></circle><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path></svg>
      </section>
      <span style="font-size:10px;font-weight:600;"><span leaf="">在看</span></span>
    </section>
    <section style="text-align:center;cursor:pointer;color:#1D4ED8;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#EFF6FF;border-radius:12px;box-shadow:0 2px 4px rgba(29,78,216,0.15);border:1px solid #93C5FD;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18v-4a8 8 0 0 1 8-8h8"></path><polyline points="16 2 20 6 16 10"></polyline></svg>
      </section>
      <span style="font-size:10px;font-weight:600;"><span leaf="">转发</span></span>
    </section>
  </section>
  <p style="font-size:10px;color:#9CA3AF;letter-spacing:1px;margin:0;">
    <span leaf="">THANKS FOR READING</span>
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
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 封面（组件2 cover-breaking，有图/无图二选一） -->

  <!-- 2. 目录（组件3 toc-scroll，2+ 章节时生成，紧跟封面之下） -->

  <!-- 3. 开头引言（组件9b oneliner-card，文章有开头金句时） -->

  <!-- 4. 前言正文（开场白，组件5 段落 × N，放 0 20px 边距的 section 内） -->

  <!-- 5. 第一章（组件4 chapter-title，margin-top:16px） -->
  <!--    章内：组件5 正文 + 组件6 行内样式 + 组件7 标签 + 组件8 代码 + 组件9 引用亮点 + 组件10 提示 + 组件11 布局 + 组件12 媒体 -->

  <!-- 6. 第二章…第N章（组件4，margin-top:48px） -->

  <!-- 7. 结语章（组件4 变体：编号 ///，PART 改 LAST，章名"写在最后"） -->

  <!-- 8. 互动三连（组件13a footer-cta，前面放固定签名段落） -->

  <!-- 9. 品牌尾图（组件13b，有素材才加） -->

</section>
```

**骨架顺序铁律**：目录 toc-scroll **必须紧跟封面之下**，在开头引言和前言正文之前——读者先看全文地图再进入内容。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 钴蓝加粗 6a / 黄底下划线 6d / oneliner-card 9b | 核心概念、产品名、关键结论 | 全文 ≤5 处 |
| **标记层** | 钴蓝下划线 6e（默认）/ 黄色渐变高亮 6c | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | quote-box 9a / 提示 10x / 胶囊 11a / 卡片 11x | 引用、旁注、提示、结构化信息 | 按需 |

**克制原则**：
- 黄色高亮每段不超过 1-2 处；一段内不超过 2 种高亮效果
- 红色下划线只用于对比/否定，不做普通强调
- 渐变绿仅出现在封面底条、目录首卡、流程首卡等结构位

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇的排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3，避免花哨。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 教程/操作指南 | step-label 7a + cmd/prompt 8a/8b + 代码块（通用库1a） | warn-tip 10a、cobalt-tip 10b、flow-cards 11b |
| 盘点/工具清单 | skill/tool-label 7c + tool-card 11e + pill-list 11a | table 11f、oneliner-card 9b |
| 观点/深度分析 | paragraph 5 + quote-box 9a + oneliner-card 9b | center-divider 9d、subtitle-highlight 9c |
| 访谈/人物特稿 | paragraph 5 + quote-box 9a（引语）+ timeline 11d（经历脉络） | oneliner-card 9b、center-divider 9d |
| 数据复盘/报告 | three-col-cards 11c + table 11f + ordered-list 11g | cobalt-info 10d、黄色渐变高亮 6c |
| 生活/情感随笔 | paragraph 5 + oneliner-card 9b + center-divider 9d | quote-box 9a（少量） |
| 案例实战 | case-label 7b / timeline 11d + step-label 7a | prompt-block 8a、yellow-warning 10c |

所有类型共用固定结构：封面 2 + 目录 3 + 章节标题 4 + 签名/三连 13。

---

## Markdown → 科技钴蓝排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置；封面主标题从中提炼（视角错开） |
| 文章开头 `> 引言` | 组件 9b oneliner-card 或并入封面副标题 | 开头金句 |
| `## 章节标题` | 组件 4 chapter-title | PART 01/02/03…，末章 /// + LAST |
| `### 子标题` | 组件 9c subtitle-highlight | 黄色下划线小节标题 |
| 普通段落 | 组件 5 paragraph | 每段主动标 1~3 处钴蓝下划线 6e |
| `**加粗文字**` | 组件 6a 钴蓝加粗 | 核心概念/品牌名 |
| `==高亮文字==` | 组件 6c 黄色渐变高亮 | 每段 ≤2 处 |
| `<u>下划线</u>` / `++文字++` | 组件 6e 钴蓝下划线 | 次要强调 |
| `~~删除线~~` | 组件 6i 删除线灰色 | 被淘汰的概念 |
| `> 引用段落`（非开头） | 组件 9a quote-box | 灰色虚线框（本主题特征） |
| 核心金句 | 组件 9b oneliner-card / 9d center-divider | 视觉焦点 |
| 操作步骤 | 组件 7a step-label（+ 8a/8b） | STEP 01/02… |
| 案例/场景 | 组件 7b case-label 或 11d timeline | CASE 01/02… |
| 技能/工具清单 | 组件 7c skill/tool-label + 11e tool-card | |
| Prompt 提示词 | 组件 8a prompt-block（短）/ 通用库 1a（长多行） | |
| 单行命令 | 组件 8b cmd-block | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色（默认）/ 1b 浅色（左竖条换 #1D4ED8） | 每行一个 `<p style="margin:0">` |
| 行内 `` `code` `` | 组件 6g 代码标签 | |
| 并列要点 | 组件 11a pill-list | |
| 流程（3 步） | 组件 11b flow-cards | 箭头可换 × 做对比 |
| 三项对比 | 组件 11c three-col-cards | |
| 递进/时间脉络 | 组件 11d timeline | |
| Markdown 表格 | 组件 11f table | 偶数行浅灰底 |
| `1. 2. 3.` 编号列表 | 组件 11g ordered-list | |
| 注意/警告 | 组件 10a warn-tip / 10c yellow-warning | |
| 亮点提示 | 组件 10b cobalt-tip / 10d cobalt-info | |
| `![](图片)` | 组件 12a image | 原图代码保留 |
| 视频 | 组件 12b video-card | 原视频代码保留 |
| 文末 | 组件 13a footer-cta（+ 13b brand-card） | 签名段落放 footer-cta 前 |
