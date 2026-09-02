# 公众号排版组件库 —— 卡片笔记风（Card Flow）

> **使用说明**：本组件库为「卡片笔记风」主题（灵感来自 Notion / 卡片笔记系统），所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：靛紫卡片化 + 结构清晰 + 信息分块。每个章节是一张独立圆角卡片，浅靛下划线为主标记、左竖条块引用、靛紫仅在锚点处出现。卡片容器承载知识块，大量留白、弱装饰、清单友好。适合知识整理、读书笔记、清单体、方法论拆解，也覆盖观点、深度分析、盘点、教程类文章。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（渐变分割线、END 短线、时间线竖线、圆点、卡片分隔条）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`——微信编辑器会自动"纠正"导致样式被重写。正确做法：拆成多个 `<p>`，每个 `<p>` 只有一个字号；高亮样式统一挂在外层 `<span>` 上
> - 不用 `position:absolute` 做划线/高亮，删除线用 `text-decoration:line-through`
> - 结构化区域（如引言卡右下署名、图片说明、卡片右侧图片槽位）没有内容时**整块删掉**，不留空 section
> - 卡片容器用实线细边 / 浅底承载，**不要用四周虚线框（dashed）包正文标题或正文块**

---

## 设计变量速查表

```
主色调：       #6366F1（靛紫）
主色调深：     #4338CA（深靛/靛蓝）
主色调浅：     #C7D2FE（浅靛蓝，下划线/左竖条专用）
主色调极浅：   #EEF2FF（浅靛底，引言卡/标签/提示底）
卡底色：       #F9FAFB（章节卡片外的全局底色 / 数据卡底）
标题色：       #111827（近黑）
正文色：       #374151（深灰）
辅助文字色：   #6B7280（中灰）
淡靛标记色：   #C7D2FE（下划线/左竖条/渐变高亮）
标签底色：     #EEF2FF，标签文字色：#4338CA
细边色：       #E5E7EB
警示底/线/字： #FEF3C7 / #D97706 / #92400E（注意事项专用）
卡片阴影：     0 2px 12px -2px rgba(99,102,241,0.10)
浅卡阴影：     0 2px 8px -2px rgba(99,102,241,0.08)
正文字号：     15px（不可改）
行高：         1.8
字间距：       0.5px
最大宽度：     677px
内容区边距：   0 10px（模块左右各 10px）
圆角：         16px（卡片）/ 12px（小卡）/ 8px（标签块）/ 20px（药丸）
```

字体栈：`-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif`

---

## 组件 1 全局容器

> 整体背景用极浅灰 `#F9FAFB`，让白底卡片自然浮起——这是卡片笔记风的地基。

```html
<section style="max-width:677px;margin:0 auto;background:#F9FAFB;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;padding:8px 0 24px;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（浅靛底大圆角卡）

> **文案策略（先读，比代码重要）**：
> - 引言卡金句和公众号外标题是**两层**，视角要错开——外标题卖"为什么点开"，引言卡卖"核心观点是什么"
> - 已知外标题时，金句**禁止原样复述**其核心关键词；从文章第一段或核心论点提炼一句有张力的判断句
> - 右下署名按文章实际作者填，未知则整行删掉，**不要固定写"甲木"**
> - 靛紫底白字标签仅在本卡片内使用（视觉焦点），正文中的关键词标签一律用浅靛底深靛字（组件 7b）

```html
<section style="margin:16px 10px 28px;background:#EEF2FF;border-radius:16px;padding:28px 24px 20px;border-left:4px solid #6366F1;box-shadow:0 2px 12px -2px rgba(99,102,241,0.10);">
  <p style="font-size:36px;color:#6366F1;font-weight:900;margin:0 0 4px;line-height:0.8;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:700;color:#111827;margin:8px 0 12px;line-height:1.8;padding-left:2px;">
    <span leaf="">{{金句前段}}</span>
    <span style="background:#6366F1;color:#ffffff;padding:2px 8px;border-radius:6px;"><span leaf="">{{高亮关键词}}</span></span>
    <span leaf="">{{金句收尾}}</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#6B7280;margin:0;letter-spacing:1px;">
    <span leaf="">—— {{作者名，未知则删整行}}</span>
  </p>
</section>
```

---

## 组件 3 前言导读区域（本文看点，三列目录卡片）

> 3 个及以上章节时生成。白底小卡 + 靛紫药丸编号 + 深色标题；展示**精选 3 个核心看点**，不是全量章节列表。

```html
<section style="padding:0 10px 28px;">
  <p style="font-size:13px;color:#6B7280;margin:0 0 12px;letter-spacing:1px;">
    <span leaf="">📌 本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#ffffff;border-radius:12px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;box-shadow:0 2px 8px -2px rgba(99,102,241,0.08);">
      <p style="display:inline-block;background:#6366F1;color:#ffffff;font-size:11px;font-weight:800;padding:2px 10px;border-radius:20px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#111827;margin:0;line-height:1.5;"><span leaf="">{{看点一}}</span></p>
    </section>
    <section style="flex:1;background:#ffffff;border-radius:12px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;box-shadow:0 2px 8px -2px rgba(99,102,241,0.08);">
      <p style="display:inline-block;background:#6366F1;color:#ffffff;font-size:11px;font-weight:800;padding:2px 10px;border-radius:20px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#111827;margin:0;line-height:1.5;"><span leaf="">{{看点二}}</span></p>
    </section>
    <section style="flex:1;background:#ffffff;border-radius:12px;padding:16px 12px;text-align:center;border:1px solid #E5E7EB;box-shadow:0 2px 8px -2px rgba(99,102,241,0.08);">
      <p style="display:inline-block;background:#6366F1;color:#ffffff;font-size:11px;font-weight:800;padding:2px 10px;border-radius:20px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#111827;margin:0;line-height:1.5;"><span leaf="">{{看点三}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节卡片容器（核心特征组件）

> 每个 `##` 章节整章装入独立的白底圆角卡片（`#ffffff` + `border-radius:16px` + 细边 + 柔和阴影 + 充足 padding）。章节之间靠卡片容器天然分离，**无需额外分割线**。章节标题（组件 5）嵌在卡片顶部，正文内容装在卡片里。

```html
<section style="margin:0 10px 20px;background:#ffffff;border-radius:16px;border:1px solid #E5E7EB;box-shadow:0 2px 12px -2px rgba(99,102,241,0.08);padding:28px 24px 24px;overflow:hidden;">

  <!-- 组件 5 章节标题（药丸编号 + 英文标签 + 中文标题）放卡片顶部 -->
  <!-- 章节正文内容（组件 6/7/8/9/10/11/12…）放在这里 -->

</section>
```

**结语章节变体**（浅靛底卡片，区别于普通白底）：

```html
<section style="margin:0 10px 20px;background:#EEF2FF;border-radius:16px;border:1px solid #C7D2FE;box-shadow:0 2px 12px -2px rgba(99,102,241,0.12);padding:28px 24px 24px;overflow:hidden;">

  <!-- 组件 5 结语变体（∞ 编号）+ 结语正文 -->

</section>
```

---

## 组件 5 章节标题（药丸编号 + 标题）

> 靛紫药丸编号 + 英文小标签 + 中文大标题，底部无横线，靠卡片容器本身区隔。只给 `##` 章节用；`###` 子标题走组件 6b。

```html
<section style="display:flex;align-items:center;margin-bottom:20px;">
  <span style="display:inline-block;background:#6366F1;color:#ffffff;font-size:14px;font-weight:900;padding:4px 14px;border-radius:20px;margin-right:14px;line-height:1.4;white-space:nowrap;"><span leaf="">01</span></span>
  <section>
    <p style="font-size:10px;color:#6366F1;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
      <span leaf="">{{ENGLISH TAG}}</span>
    </p>
    <h3 style="font-size:18px;font-weight:800;color:#111827;margin:0;letter-spacing:0.5px;">
      <span leaf="">{{中文章节标题}}</span>
    </h3>
  </section>
</section>
```

**结语章节变体**（编号用 `∞` 替代数字，英文标签用 `THE END` / `EPILOGUE`）：

```html
<span style="display:inline-block;background:#6366F1;color:#ffffff;font-size:14px;font-weight:900;padding:4px 14px;border-radius:20px;margin-right:14px;line-height:1.4;white-space:nowrap;"><span leaf="">∞</span></span>
```

**完整章节示例（标题嵌入卡片容器）**：

```html
<section style="margin:0 10px 20px;background:#ffffff;border-radius:16px;border:1px solid #E5E7EB;box-shadow:0 2px 12px -2px rgba(99,102,241,0.08);padding:28px 24px 24px;overflow:hidden;">
  <section style="display:flex;align-items:center;margin-bottom:20px;">
    <span style="display:inline-block;background:#6366F1;color:#ffffff;font-size:14px;font-weight:900;padding:4px 14px;border-radius:20px;margin-right:14px;line-height:1.4;white-space:nowrap;"><span leaf="">01</span></span>
    <section>
      <p style="font-size:10px;color:#6366F1;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
        <span leaf="">SECTION ONE</span>
      </p>
      <h3 style="font-size:18px;font-weight:800;color:#111827;margin:0;letter-spacing:0.5px;">
        <span leaf="">章节标题文字</span>
      </h3>
    </section>
  </section>

  <!-- 正文内容 -->

</section>
```

---

## 组件 6 正文段落

> **关键规则**：每段主动识别 1~3 个关键短语，用**浅靛下划线（7d）**标记——这是本风格的核心视觉特征，让读者快速扫到每段重点。

**基础段落**：

```html
<p style="margin-bottom:18px;font-size:15px;line-height:1.8;text-align:justify;color:#374151;">
  <span leaf="">{{正文内容}}</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认）：

```html
<p style="margin-bottom:18px;font-size:15px;line-height:1.8;text-align:justify;color:#374151;">
  <span leaf="">{{前半句}}</span>
  <span style="border-bottom:2px solid #C7D2FE;font-weight:600;color:#111827;"><span leaf="">{{需要强调的关键短语}}</span></span>
  <span leaf="">{{后半句}}</span>
</p>
```

**标记原则**：每段选 1~3 个关键短语（4~15 字）加下划线，不要整段都标；优先标核心观点、结论判断、关键数据、专有名词；无重点的段落可不标。

---

## 组件 6b 子标题（`###` 小节标题）

> `###` 子标题用靛紫左竖条 + 深色标题，**不套用组件 5 的药丸编号章节样式**（编号章节只给 `##`）。用在章节卡片内部承载子话题。

```html
<section style="border-left:3px solid #6366F1;padding-left:12px;margin:24px 0 14px;">
  <p style="font-size:15px;font-weight:800;color:#111827;margin:0;letter-spacing:0.3px;line-height:1.4;">
    <span leaf="">{{子标题}}</span>
  </p>
</section>
```

---

## 组件 7 正文高亮样式（6 种变体 + 使用策略）

> **核心理念**：克制用色，靛紫只在真正需要的锚点出现。留白与低饱和度是本风格的底色。
>
> **优先级**：① 7d 浅靛下划线（正文默认标记）→ ② 7a 普通加粗为主、靛紫加粗仅锚点 → ③ 7b 浅靛底深靛字标签（每篇 2~4 个）→ ④ 7c 浅靛背景（次要）→ ⑤ 7e 荧光笔（偶尔长句强调）→ ⑥ 7f 行内代码

### 7a. 加粗强调

普通加粗（默认，绝大部分加粗用这个）：

```html
<strong><span leaf="">普通加粗强调</span></strong>
```

靛紫加粗（仅限产品名/步骤/CTA 等锚点，全文 ≤5 处）：

```html
<strong style="color:#6366F1;"><span leaf="">靛紫加粗锚点</span></strong>
```

### 7b. 浅靛底深靛字标签（核心概念，每篇 2~4 个）

```html
<span style="background:#EEF2FF;color:#4338CA;padding:2px 7px;border-radius:5px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅靛背景高亮（次要关键词）

```html
<span style="background:#EEF2FF;padding:1px 6px;border-radius:4px;font-weight:600;color:#4338CA;"><span leaf="">浅靛背景关键词</span></span>
```

### 7d. 浅靛下划线（最常用，本风格标志性标记）

```html
<span style="border-bottom:2px solid #C7D2FE;font-weight:600;color:#111827;"><span leaf="">浅靛下划线关键词</span></span>
```

### 7e. 荧光笔效果（偶尔用于长句强调）

```html
<span style="background:linear-gradient(180deg,transparent 60%,#C7D2FE 60%);font-weight:700;color:#111827;"><span leaf="">荧光笔效果的重要长句</span></span>
```

### 7f. 行内代码

```html
<span style="background:#F3F4F6;color:#4338CA;padding:2px 6px;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:14px;font-weight:600;"><span leaf="">code</span></span>
```

---

## 组件 8 引用高亮块（4 种变体）

> 所有引用均用左竖条（`border-left:4px solid`）+ 浅底形式，**不使用四周虚线框（dashed）**。

### 8a. 靛底左竖条金句引用（视觉焦点最强，核心金句）

```html
<section style="background:#EEF2FF;border-radius:0 10px 10px 0;border-left:4px solid #6366F1;padding:16px 20px;margin-bottom:20px;">
  <p style="font-size:15px;font-weight:700;color:#4338CA;margin:0;line-height:1.8;">
    <span leaf="">「{{核心观点或关键金句}}」</span>
  </p>
</section>
```

### 8b. 白底浅靛竖条引用块（Prompt / 引用内容）

```html
<section style="background:#ffffff;border:1px solid #E5E7EB;border-left:4px solid #C7D2FE;border-radius:0 10px 10px 0;padding:16px 20px;margin-bottom:20px;">
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    {{引用内容，可含 7d 下划线等内联样式}}
  </p>
</section>
```

### 8c. 极浅灰底竖条引用（轻量旁注、个人吐槽）

```html
<section style="border-left:4px solid #E5E7EB;padding:12px 18px;margin-bottom:20px;background:#F9FAFB;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#6B7280;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">{{轻量旁注内容}}</span>
  </p>
</section>
```

### 8d. 居中金句分隔（章节间的过渡金句）

```html
<p style="font-size:15px;margin:0 0 20px;text-align:center;color:#6366F1;font-weight:700;letter-spacing:1px;border-top:1px solid #EEF2FF;border-bottom:1px solid #EEF2FF;padding:14px 10px;">
  <span leaf="">{{居中金句}}</span>
</p>
```

---

## 组件 9 提示 / 警示条

### 9a. 靛紫提示条（重要提醒、核心结论）

```html
<section style="background:#EEF2FF;border-left:4px solid #6366F1;border-radius:0 10px 10px 0;padding:14px 20px;margin-bottom:20px;">
  <section style="display:flex;align-items:center;margin-bottom:6px;">
    <span style="display:inline-block;background:#6366F1;color:#ffffff;font-size:11px;font-weight:700;padding:1px 8px;border-radius:20px;margin-right:8px;"><span leaf="">💡 提示</span></span>
  </section>
  <p style="font-size:14px;font-weight:600;color:#4338CA;margin:0;line-height:1.8;">
    <span leaf="">{{重要提示或核心结论}}</span>
  </p>
</section>
```

### 9b. 警示条（琥珀色，注意事项 / 风险）

```html
<section style="background:#FEF3C7;border-left:4px solid #D97706;border-radius:0 10px 10px 0;padding:14px 20px;margin-bottom:20px;">
  <section style="display:flex;align-items:center;margin-bottom:6px;">
    <span style="display:inline-block;background:#D97706;color:#ffffff;font-size:11px;font-weight:700;padding:1px 8px;border-radius:20px;margin-right:8px;"><span leaf="">⚠️ 注意</span></span>
  </section>
  <p style="font-size:14px;font-weight:600;color:#92400E;margin:0;line-height:1.8;">
    <span leaf="">{{注意事项或警示信息}}</span>
  </p>
</section>
```

---

## 组件 10 内容标签组（STEP / SKILL / TOOL / CASE）

> 教程用 STEP、盘点用 SKILL/TOOL、案例用 CASE。靛紫底白字编号标签 + 标题。

### 10a. step-label（教程步骤 / 盘点条目 / 案例标签）

```html
<section style="margin-bottom:22px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#6366F1;color:#ffffff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:6px;"><span leaf="">STEP 01</span></span>
    <span style="font-size:15px;font-weight:800;color:#111827;"><span leaf="">{{步骤标题}}</span></span>
  </section>
  <p style="font-size:15px;margin:0 0 16px;color:#374151;line-height:1.8;text-align:justify;">
    {{步骤内容}}
  </p>
</section>
```

`STEP 01` 可替换为 `SKILL 1`、`TOOL 摄像机`、`CASE 01`（盘点/案例场景）；盘点场景标签底色可改浅靛 `#EEF2FF`+字 `#4338CA` 做次级层次。

### 10b. tool-card（工具 / 条目说明卡）

```html
<section style="background:#ffffff;border-radius:12px;padding:16px 20px;border:1px solid #E5E7EB;box-shadow:0 2px 12px -2px rgba(99,102,241,0.10);margin-bottom:20px;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;">
    {{条目说明内容}}
  </p>
</section>
```

---

## 组件 11 列表组件

### 11a. ordered-list（靛紫圆标数字编号列表）

```html
<section style="margin-bottom:20px;">
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#6366F1;color:#ffffff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">1</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#6366F1;color:#ffffff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">2</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#6366F1;color:#ffffff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">3</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
</section>
```

### 11b. check-list（对勾色块清单，卡片笔记风特色）

> 每项靛紫方块 + 对勾 + 正文，清单感强，装进浅灰底小卡承载知识块。

```html
<section style="background:#F9FAFB;border-radius:12px;padding:18px 20px;margin-bottom:20px;border:1px solid #E5E7EB;">
  <section style="display:flex;align-items:flex-start;margin-bottom:12px;">
    <span style="display:inline-block;width:20px;height:20px;background:#6366F1;border-radius:6px;margin-right:12px;margin-top:1px;text-align:center;line-height:20px;font-size:12px;color:#ffffff;flex-shrink:0;"><span leaf="">✓</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.7;flex:1;">
      <span leaf="">{{第一个要点，可稍长，支持换行}}</span>
    </p>
  </section>
  <section style="display:flex;align-items:flex-start;margin-bottom:12px;">
    <span style="display:inline-block;width:20px;height:20px;background:#6366F1;border-radius:6px;margin-right:12px;margin-top:1px;text-align:center;line-height:20px;font-size:12px;color:#ffffff;flex-shrink:0;"><span leaf="">✓</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.7;flex:1;">
      <span leaf="">{{第二个要点}}</span>
    </p>
  </section>
  <section style="display:flex;align-items:flex-start;">
    <span style="display:inline-block;width:20px;height:20px;background:#6366F1;border-radius:6px;margin-right:12px;margin-top:1px;text-align:center;line-height:20px;font-size:12px;color:#ffffff;flex-shrink:0;"><span leaf="">✓</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.7;flex:1;">
      <span leaf="">{{第三个要点}}</span>
    </p>
  </section>
</section>
```

### 11c. dot-list（单行圆点要点，并列短要点）

```html
<section style="display:flex;align-items:flex-start;margin-bottom:10px;">
  <span style="display:inline-block;width:8px;height:8px;background:#6366F1;border-radius:50%;margin-right:12px;margin-top:7px;flex-shrink:0;"><span leaf=""><br></span></span>
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.7;flex:1;">
    <span leaf="">{{列表项文字}}</span>
  </p>
</section>
```

### 11d. timeline（时间线 / 递进脉络，访谈经历、案例演进）

```html
<section style="display:flex;margin-bottom:20px;">
  <section style="display:flex;flex-direction:column;align-items:center;margin-right:16px;flex-shrink:0;">
    <section style="width:14px;height:14px;border-radius:50%;border:3px solid #6366F1;background:#fff;margin-top:4px;"><span leaf=""><br></span></section>
    <section style="width:2px;background:#C7D2FE;flex:1;margin-top:4px;min-height:44px;"><span leaf=""><br></span></section>
  </section>
  <section style="flex:1;padding-bottom:12px;">
    <p style="margin:0 0 6px;font-size:15px;font-weight:800;color:#111827;"><span leaf="">{{节点标题}}</span></p>
    <p style="font-size:15px;margin:0;color:#374151;line-height:1.8;text-align:justify;">{{节点内容}}</p>
  </section>
</section>
```

最后一个节点去掉竖线段（删掉那条 `width:2px` 的 section）。

---

## 组件 12 数据 / 要点卡片组

### 两列版

```html
<section style="display:flex;margin-bottom:20px;">
  <section style="flex:1;background:#F9FAFB;border-radius:12px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;">
    <p style="font-size:28px;font-weight:900;color:#6366F1;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:12px;color:#6B7280;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
  <section style="flex:1;background:#F9FAFB;border-radius:12px;padding:18px 16px;text-align:center;border:1px solid #E5E7EB;">
    <p style="font-size:28px;font-weight:900;color:#6366F1;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:12px;color:#6B7280;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display:flex;margin-bottom:20px;">
  <section style="flex:1;background:#F9FAFB;border-radius:12px;padding:16px 10px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;">
    <p style="font-size:24px;font-weight:900;color:#6366F1;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#6B7280;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
  <section style="flex:1;background:#F9FAFB;border-radius:12px;padding:16px 10px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;">
    <p style="font-size:24px;font-weight:900;color:#6366F1;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#6B7280;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
  <section style="flex:1;background:#F9FAFB;border-radius:12px;padding:16px 10px;text-align:center;border:1px solid #E5E7EB;">
    <p style="font-size:24px;font-weight:900;color:#6366F1;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#6B7280;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 表格（真实数据表用）

```html
<section style="margin-bottom:20px;overflow-x:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:14px;">
    <thead>
      <tr>
        <th style="background:#6366F1;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题}}</span></th>
        <th style="background:#6366F1;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题}}</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;"><span leaf="">{{内容}}</span></td>
      </tr>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #E5E7EB;color:#374151;background:#F9FAFB;"><span leaf="">{{内容}}</span></td>
      </tr>
    </tbody>
  </table>
</section>
```

---

## 组件 13 标签胶囊

浅靛底深靛字（默认）：

```html
<span style="display:inline-block;background:#EEF2FF;color:#4338CA;font-size:12px;font-weight:700;padding:3px 10px;border-radius:20px;margin-right:6px;border:1px solid #C7D2FE;"><span leaf="">标签名</span></span>
```

靛紫描边（轻量）：

```html
<span style="display:inline-block;border:1px solid #6366F1;color:#6366F1;font-size:12px;font-weight:600;padding:2px 10px;border-radius:20px;margin-right:6px;"><span leaf="">标签名</span></span>
```

灰色描边（中性）：

```html
<span style="display:inline-block;border:1px solid #E5E7EB;color:#6B7280;font-size:12px;font-weight:500;padding:2px 10px;border-radius:20px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 14 图片容器

```html
<section style="background:#ffffff;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 2px 10px -2px rgba(99,102,241,0.08);margin-bottom:10px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="{{图片URL}}" style="max-width:100%;display:block;"></span>
  </section>
</section>
```

带说明文字时，图片 `margin-bottom` 改 `8px`，其后加：

```html
<p style="font-size:12px;color:#6B7280;text-align:center;margin:0 0 20px;">
  <span leaf="">— {{图片说明}}</span>
</p>
```

多行代码块用通用增量库 `common-components.md` 的 1a 深色 / 1b 浅色（左竖条换 `#6366F1`），禁 `white-space:pre`。

---

## 组件 15 END 结尾分割线

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 28px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:48px;background:linear-gradient(to right,transparent,#C7D2FE);margin-right:12px;"><span leaf=""><br></span></span>
      <span style="font-size:11px;color:#6366F1;letter-spacing:3px;font-weight:700;"><span leaf="">END</span></span>
      <span style="height:1px;width:48px;background:linear-gradient(to left,transparent,#C7D2FE);margin-left:12px;"><span leaf=""><br></span></span>
    </section>
  </section>
</section>
```

---

## 组件 16 尾部作者签名区

> 固定签名文案以卡片形式呈现；有个人名片/引导图素材才放图，无素材整块删。

```html
<section style="padding:0 10px;">
  <section style="background:#ffffff;border-radius:16px;border:1px solid #E5E7EB;padding:24px;margin-bottom:16px;">
    <p style="margin-bottom:12px;font-size:15px;line-height:1.8;color:#374151;">
      <span leaf="">我是甲木，热衷于分享一些 AI 观察、AI 干货内容。</span>
    </p>
    <p style="margin-bottom:0;font-size:15px;line-height:1.8;color:#374151;">
      <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
      <strong style="color:#6366F1;"><span leaf="">点赞、在看、转发</span></strong>
      <span leaf="">三连，我们下篇见。</span>
    </p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#F9FAFB;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;padding:8px 0 24px;">

  <!-- 1. 开头引言卡片（组件2，浅靛底大圆角卡） -->

  <!-- 2. 前言正文（组件6 段落 × N，放 0 10px 边距 section，第一章之前的开场白） -->

  <!-- 3. 前言导读（组件3，3+ 章节时生成，精选 3 看点） -->

  <!-- 4. 第一章（组件4 卡片容器 + 组件5 药丸编号标题） -->
  <!--    章内：组件6 正文 + 6b 子标题 + 7 行内高亮 + 8 引用 + 9 提示 + 10 标签组 + 11 列表 + 12 数据 + 14 图片，知识块善用卡片承载 -->

  <!-- 5. 第二章…第N章（组件4 + 组件5，编号递增，章节靠卡片容器天然分隔，无需分割线） -->

  <!-- 6. 结语章（组件4 浅靛底变体 + 组件5 变体：编号 ∞，英文 THE END） -->

  <!-- 7. END 分割线（组件15） -->

  <!-- 8. 尾部签名（组件16 白底圆角签名卡） -->

</section>
```

**骨架铁律**：引言卡在最前；导读区在前言正文之后、第一章之前；章节各自装进白底圆角卡片、靠容器隔离，不用额外分割线；结语用浅靛底卡片 + ∞ 编号变体；一篇只有一个 END + 一个签名区。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 靛紫加粗 7a `color:#6366F1` / 靛底白字（仅引言卡）/ 金句引用 8a | 产品名、关键结论、核心金句 | 全文 ≤5 处 |
| **标记层** | 浅靛下划线 7d（默认）/ 浅靛底标签 7b | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 章节卡片 4 / 左竖条引用 8x / 提示 9x / 标签组 10 / 清单卡 11-12 | 章节隔离、引用、旁注、提示、结构化信息 | 结构性 |

**克制原则**：
- 靛底白字标签（`bg:#6366F1`）**仅在引言卡内**，正文关键词标签用浅靛底深靛字 7b
- 靛紫加粗全文 ≤5 处
- 章节区隔靠卡片容器本身完成，不需要额外分割线
- 列表/清单优先用对勾色块 11b（清单感更强），并列短要点才用圆点 11c
- 引用/提示统一用左竖条 + 浅底 + 类型小标签，**不用四周虚线框（dashed）**

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3，避免花哨。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 观点/深度分析 | 正文6 + 金句引用8a + 居中金句8d | 浅靛引用8b、check-list 11b、子标题6b |
| 教程/操作指南 | step-label 10a + 代码块（通用库1a）+ ordered-list 11a | 靛紫提示9a、tool-card 10b |
| 盘点/工具清单 | skill/tool-label 10a + tool-card 10b + check-list 11b | 数据卡12、标签胶囊13 |
| 访谈/人物特稿 | 正文6 + 金句引用8a（引语）+ timeline 11d（经历脉络） | 居中金句8d、灰底旁注8c |
| 数据复盘/报告 | 数据卡12（两列/三列）+ 表格12 + ordered-list 11a | 靛紫提示9a、荧光笔7e |
| 生活/情感随笔 | 正文6 + 居中金句8d + 灰底旁注8c | 金句引用8a（少量）、check-list 11b |
| 案例实战 | case-label 10a / timeline 11d + step-label 10a | 浅靛引用8b、警示条9b |

所有类型共用固定结构：引言卡 2 + 导读 3（3+ 章节）+ 章节卡片 4/5 + END 15 + 签名 16。

---

## Markdown → 卡片笔记风排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| 文章开头 `> 引言金句` | 组件 2 浅靛底大圆角引言卡 | 视角与外标题错开 |
| `## 章节标题` | 组件 4 卡片容器 + 组件 5 药丸标题 | 整章装白底圆角卡片，编号 01/02…，末章 ∞ + THE END |
| `### 子标题` | 组件 6b 靛紫左竖条小标题 | 不套药丸编号章节样式 |
| 普通段落 | 组件 6 正文段落 | 每段主动标 1~3 处浅靛下划线 7d |
| `**加粗文字**` | 组件 7a 普通加粗（默认）/ 靛紫加粗（锚点 ≤5） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 浅靛底深靛字标签 | 核心概念 |
| `<u>下划线</u>` / `++文字++` | 组件 7d 浅靛下划线 | 次要强调 |
| `~~删除线~~` | `text-decoration:line-through` + 灰字 | 被淘汰概念 |
| 行内 `` `code` `` | 组件 7f 行内代码 | |
| `> 引用段落`（金句） | 组件 8a 靛底左竖条 | 核心金句 |
| `> 引用段落`（旁注） | 组件 8c 灰底左竖条 | 轻量旁注 |
| 核心金句 | 组件 8a / 8d 居中金句 | 视觉焦点 |
| 操作步骤 | 组件 10a step-label | STEP 01/02… |
| 技能/工具清单 | 组件 10a skill/tool-label + 10b tool-card | |
| 案例/经历脉络 | 组件 10a case-label / 11d timeline | |
| Prompt 提示词 | 组件 8b 白底浅靛引用块 / 通用库 1a（长多行） | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色 / 1b 浅色（左竖条换 #6366F1） | 每行一个 `<p style="margin:0">` |
| 并列要点（短） | 组件 11c dot-list | 靛紫圆点 |
| 重要清单 | 组件 11b check-list | 靛紫方块对勾，清单感 |
| `1. 2. 3.` 编号列表 | 组件 11a ordered-list | 靛紫圆标 |
| 数据展示 | 组件 12 数据卡片组 | 靛紫大号数据 |
| Markdown 表格 | 组件 12 表格 | 偶数行浅灰底 |
| 注意/警告 | 组件 9a 靛紫提示 / 9b 琥珀警示 | |
| 行内标签 | 组件 13 标签胶囊 | 浅靛底默认 |
| `---` | 无需额外分割线 | 章节已由卡片容器隔离 |
| `![](图片)` | 组件 14 图片容器 | 圆角卡片 + 说明 |
| 文末 | 组件 15 END + 16 签名 | |
</content>
</invoke>
