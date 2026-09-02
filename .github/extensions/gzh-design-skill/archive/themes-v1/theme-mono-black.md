# 甲木公众号排版组件库 —— 黑白灰色系

> **使用说明**：本组件库为「黑白灰色系」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：水墨质感 + 编辑风极简、银灰下划线为主标记、灰色左竖条引用、纯黑仅在锚点处出现。整体追求高端杂志般的冷静克制与留白之美。
>
> **公众号平台限制须知**：
> - 不支持 `<style>` 标签、`<script>` 标签、CSS class
> - 不支持 `position: fixed/absolute`、`float`
> - 不支持 `@media` 媒体查询、`@keyframes` 动画
> - 不支持 `display: grid`
> - 支持内联 `style` 属性
> - 支持 `display: flex`（有限支持）
> - 支持 `linear-gradient`
> - 支持 `border-radius`、`box-shadow`
> - 支持 `<section>`、`<p>`、`<span>`、`<strong>`、`<img>` 等基础标签

---

## 设计变量速查表

```
主色调：       #1A1A1A（墨黑）
主色调深：     #0D0D0D（深邃黑）
主色调浅：     #6B7280（岩灰）
主色调极浅：   #F3F4F6（雾白）
主色调背景：   #F9FAFB（极淡灰底）
标记色：       #D1D5DB（银灰，下划线/左竖条专用）
强调背景：     #E5E7EB（浅灰背景）
标题色：       #111827（纯黑）
正文色：       #374151（深灰）
辅助文字色：   #9CA3AF（中灰）
分割线色：     #E5E7EB
左竖条色：     #D1D5DB（银灰左竖条）
正文字号：     15px
行高：         1.8
字间距：       0.5px
内容区边距：   0 10px（左右各 10px）
```

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（墨黑底 + 暗色阴影）

> 深黑底 + 暗色阴影光晕 + 大白引号 + 白底黑字关键词高亮 + 右下署名。无左竖线，圆角 12px。整体营造沉浸式开场质感。

```html
<section style="margin:10px 10px 32px;background:#1A1A1A;border-radius:12px;box-shadow:0 4px 24px -4px rgba(0,0,0,0.25);padding:28px 24px 22px;overflow:hidden;">
  <p style="font-size:42px;color:rgba(255,255,255,0.3);font-weight:900;margin:0;line-height:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:800;color:#F9FAFB;margin:12px 0 8px;line-height:1.75;padding-left:4px;">
    <span style="background:#F3F4F6;color:#1A1A1A;padding:2px 8px;border-radius:4px;"><span leaf="">高亮关键词</span></span>
    <span leaf=""> ，不是模型，而是懂得如何 </span>
    <span style="background:#F3F4F6;color:#1A1A1A;padding:2px 8px;border-radius:4px;"><span leaf="">驾驭</span></span>
    <span leaf=""> 它们的我们。</span>
  </p>
  <p style="text-align:right;font-size:12px;color:rgba(255,255,255,0.35);margin:8px 0 0;letter-spacing:1px;">
    <span leaf="">—— 甲木</span>
  </p>
</section>
```

**效果**：深黑底色营造沉浸式入场感，暗色阴影让卡片浮起，白底黑字标签在暗底上清晰醒目，署名用低透白色保持克制。

> **注意**：开头卡片内的关键词高亮用白底黑字（`background:#F3F4F6;color:#1A1A1A`），这是卡片内部深色背景下的反转处理。正文中的关键词标签则用浅灰底深色字（见组件 7b）。

---

## 组件 3 前言导读区域（黑底白字目录卡片）

> 三列目录卡片，黑色背景编号区 + 深色标题

```html
<section style="padding:0 10px 32px;">
  <p style="font-size:14px;color:#9CA3AF;margin:0 0 14px;letter-spacing:1px;">
    <span leaf="">本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#F9FAFB;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;">
      <p style="display:inline-block;background:#1A1A1A;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#111827;margin:0;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="flex:1;background:#F9FAFB;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;">
      <p style="display:inline-block;background:#1A1A1A;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#111827;margin:0;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="flex:1;background:#F9FAFB;border-radius:10px;padding:16px 12px;text-align:center;border:1px solid #E5E7EB;">
      <p style="display:inline-block;background:#1A1A1A;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#111827;margin:0;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（黑色渐变）

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#9CA3AF,#1A1A1A,#9CA3AF,transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题组件（黑底编号标签 + 标题）

> 黑色实底编号标签 + 灰色英文小标签 + 黑色中文大标题，底部黑色线

```html
<section style="margin-top:48px;margin-bottom:28px;padding:0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #1A1A1A;">
    <section style="display:flex;align-items:center;">
      <span style="display:inline-block;background:#1A1A1A;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#6B7280;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size:18px;font-weight:800;color:#111827;margin:0;letter-spacing:0.5px;">
          <span leaf="">中文章节标题</span>
        </h3>
      </section>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**（编号用 ∞ 替代数字）：

```html
<span style="display:inline-block;background:#1A1A1A;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

---

## 组件 6 正文段落

> **关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**银灰下划线（7d）**进行标记。这是本风格的核心视觉特征——让读者快速扫到每段的重点。

**基础段落**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">正文内容的前半部分，引出核心概念</span>
  <span style="border-bottom:2px solid #D1D5DB;font-weight:600;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字，太短没意义，太长失去焦点
- 如果一段没有特别重要的内容，可以不标

---

## 组件 7 正文高亮样式（5 种变体 + 使用策略）

> **核心设计理念**：克制用色，黑色只在真正需要的锚点出现。在纯黑白灰的世界里，靠粗细、深浅、虚实来制造层次。
>
> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 银灰下划线** -- 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 黑色加粗** -- 普通加粗为主，黑色加粗仅用于极少数锚点
> 3. **7b 浅灰底深色字标签** -- 核心概念标签（每篇 2~4 个）
> 4. **7c 浅灰背景** -- 次要关键词补充
> 5. **7e 灰色荧光笔** -- 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，绝大部分加粗使用此样式。**黑色加粗**仅用于极少数关键锚点（如产品名、步骤编号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong><span leaf="">普通加粗强调</span></strong>
```

黑色加粗（仅限关键锚点）：
```html
<strong style="color:#1A1A1A;"><span leaf="">黑色加粗，仅用于产品名/步骤/CTA</span></strong>
```

### 7b. 浅灰底深色字标签

> 浅灰背景 + 深色文字，干净利落。用于核心概念（每篇 2~4 个）

```html
<span style="background:#E5E7EB;color:#111827;padding:2px 6px;border-radius:3px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅灰背景高亮

> 柔和的背景标注，适用于次要关键词

```html
<span style="background:#F3F4F6;padding:1px 6px;border-radius:3px;font-weight:600;color:#374151;"><span leaf="">浅灰背景关键词</span></span>
```

### 7d. 银灰下划线 -- 最常用

> **本风格的标志性标记方式**。颜色为银灰 `#D1D5DB`，温和内敛，适合高频使用。在纯黑白灰体系中提供恰到好处的视觉锚点。

```html
<span style="border-bottom:2px solid #D1D5DB;font-weight:600;"><span leaf="">银灰下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">AI 竞争已进入下半场：上半场拼模型能力，下半场拼</span>
  <span style="border-bottom:2px solid #D1D5DB;font-weight:600;"><span leaf="">分发能力</span></span>
  <span leaf="">。微信的策略清晰：不做模型、不限生态，只做一件事——</span>
  <span style="border-bottom:2px solid #D1D5DB;font-weight:600;"><span leaf="">把 AI 入口握在手里</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 灰色荧光笔效果

> 底部 40% 浅灰高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg,transparent 60%,#E5E7EB 60%);font-weight:700;color:#111827;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用高亮块（3 种变体）

### 8a. 雾白左竖条金句引用（视觉焦点最强）

> 极淡灰底 + 银灰左竖条，用于核心金句。文字用深色加粗，干净有力。

```html
<section style="background:#F9FAFB;border-radius:0 10px 10px 0;padding:18px 22px;margin-bottom:24px;border-left:4px solid #1A1A1A;">
  <p style="font-size:16px;font-weight:800;color:#111827;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 浅灰背景引用块（Prompt/内容块）

> 浅灰底 + 实线细边框，用于展示 Prompt、引用内容等

```html
<section style="background:#F3F4F6;border-radius:10px;padding:18px 20px;margin-bottom:24px;border:1px solid #E5E7EB;">
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">浅灰引用内容，可以包含</span>
    <span style="border-bottom:2px solid #D1D5DB;font-weight:600;"><span leaf="">下划线加粗的关键句</span></span>
  </p>
</section>
```

### 8c. 极淡左竖条引用（轻量旁注）

> 近白底 + 浅灰左竖条，用于轻量旁注、个人吐槽等

```html
<section style="border-left:4px solid #D1D5DB;padding:14px 20px;margin-bottom:24px;background:#FAFAFA;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#6B7280;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">轻量旁注内容，左竖条简洁不抢戏</span>
  </p>
</section>
```

---

## 组件 9 提示/警示条

> 浅灰底 + 银灰左竖条 + 深色文字，用于重要提醒、核心结论

```html
<section style="background:#F3F4F6;border-left:4px solid #1A1A1A;border-radius:0 8px 8px 0;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:700;color:#374151;margin:0;line-height:1.8;">
    <span leaf="">这里是重要提示或核心结论</span>
  </p>
</section>
```

---

## 组件 10 图片容器

```html
<section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.06);margin-bottom:10px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时，图片 `margin-bottom` 改为 `8px`：

```html
<section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.06);margin-bottom:8px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 11 加粗正文段落

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#111827;">
  <span leaf="">加粗的结论性短句</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#111827;">
  <span style="background:linear-gradient(180deg,transparent 60%,#E5E7EB 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

---

## 组件 12 数据/要点卡片组

### 两列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#F9FAFB;border-radius:10px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #E5E7EB;">
    <p style="font-size:28px;font-weight:900;color:#1A1A1A;margin:0 0 4px;line-height:1;"><span leaf="">14亿</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#F9FAFB;border-radius:10px;padding:18px 16px;text-align:center;border:1px solid #E5E7EB;">
    <p style="font-size:28px;font-weight:900;color:#1A1A1A;margin:0 0 4px;line-height:1;"><span leaf="">3步</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

---

## 组件 13 标签胶囊

### 浅灰底深色字（默认）

```html
<span style="display:inline-block;background:#E5E7EB;color:#374151;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

### 黑色描边（轻量）

```html
<span style="display:inline-block;border:1px solid #1A1A1A;color:#1A1A1A;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 14 END 结尾分割线

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:2px;width:60px;background:linear-gradient(to right,transparent,#1A1A1A);margin-right:12px;"></span>
      <span style="font-size:11px;color:#1A1A1A;letter-spacing:3px;font-weight:700;"><span leaf="">END</span></span>
      <span style="height:2px;width:60px;background:linear-gradient(to left,transparent,#1A1A1A);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部作者签名区

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin-bottom:10px;border-radius:12px;overflow:hidden;">
    <span leaf=""><img src="个人名片或引导图URL" style="max-width:100%;"></span>
  </section>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察，AI 干货内容</span>
  </p>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#1A1A1A;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 开头引言卡片（墨黑底 + 暗色阴影） -->
  <!-- 组件2 -->

  <!-- 2. 前言正文（开场白） -->
  <section style="padding:0 10px 20px;">
    <!-- 组件6 正文段落 x N -->
  </section>

  <!-- 3. 目录导航 -->
  <!-- 组件3 黑底白字目录卡片 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件4 黑色渐变分割线 -->

  <!-- 5. 第一章 -->
  <!-- 组件5（黑底编号标签 01 + 标题） -->
  <!--   组件6正文 + 组件7高亮 + 组件8引用 + 组件9提示条 + 组件10图片 + 组件12数据卡片 -->

  <!-- 6. 章节分割线 -->

  <!-- 7. 第二章 -->
  <!-- 组件5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- 8. 章节分割线 -->

  <!-- 9. 结语章节 -->
  <!-- 组件5（∞ 变体） -->

  <!-- 10. END 分割线 -->
  <!-- 组件14 -->

  <!-- 11. 尾部签名 -->
  <!-- 组件15 -->

</section>
```

---

## 视觉层级设计（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 黑色加粗 `color:#1A1A1A` | 产品名、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 银灰下划线 `#D1D5DB` | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 左竖条 + 浅底 / 小标签 | 引用、旁注、提示 | 按需 |

**克制原则**：
- 白底黑字标签（`bg:#F3F4F6;color:#1A1A1A`）**仅在开头卡片内使用**（深色背景反转），正文中用浅灰底深色字替代
- 黑色加粗全文不超过 5 处
- 引用框统一用虚线风格，不用实线左竖条
- 黑色渐变仅出现在分割线和 END 线
- 整体追求「留白」和「呼吸感」，灰色系的层次变化比颜色变化更重要

---

## Markdown -> 黑白灰排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 墨黑底暗色阴影引言卡片 | 文章开头的引用 |
| `## 章节标题` | 组件 5 章节标题 | 黑底编号标签 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，主动标记关键词下划线 |
| `**加粗文字**` | 组件 7a 普通加粗（默认）或黑色加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 浅灰底深色字标签 | 核心概念 |
| `<u>下划线</u>` | 组件 7d 银灰下划线 | 2px `#D1D5DB` |
| `> 引用段落`（金句） | 组件 8a 雾白左竖条 | 核心金句 |
| `> 引用段落`（旁注） | 组件 8c 极淡左竖条 | 轻量旁注 |
| `!> 提示文字` | 组件 9 提示条 | 浅灰底左竖条 |
| `![](图片)` | 组件 10 图片容器 | 圆角卡片 + 说明 |
| 数据展示 | 组件 12 数据卡片组 | 黑色大号数据 |
| 行内标签 | 组件 13 标签胶囊 | 浅灰底为默认 |
| `---` | 组件 4 章节分割线 | 黑色渐变 |
| 文末 | 组件 14 + 15 | END线 + 签名 |
