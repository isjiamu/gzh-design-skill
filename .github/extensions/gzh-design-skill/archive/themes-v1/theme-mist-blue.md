# 甲木公众号排版组件库 —— 雾蓝晴空风（Mist Blue）

> **使用说明**：本组件库为「雾蓝晴空风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：雾霾蓝 + 大留白 + 细线，清爽、宁静、通透、治愈。浅蓝白底，细线分层，圆角柔和，阴影极淡偏蓝，字号舒适，章节间距大。无任何四周虚线框，强调用左竖条 + 浅底 + 小标签。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>` 标签、`<script>` 标签、CSS class
> - ❌ 不支持 `position: fixed/absolute/sticky`、`float`
> - ❌ 不支持 `@media` 媒体查询、`@keyframes` 动画
> - ❌ 不支持 `display: grid`、CSS 变量 `var()`、外部字体
> - ✅ 支持内联 `style` 属性
> - ✅ 支持 `display: flex`（有限支持）
> - ✅ 支持 `linear-gradient`
> - ✅ 支持 `border-radius`、`box-shadow`
> - ✅ 支持 `<section>`、`<p>`、`<span>`、`<strong>`、`<img>` 等基础标签

---

## 设计变量速查表

```
主色调：       #7C9EB2（雾霾蓝）
主色调深：     #5B7F95（深雾蓝）
主色调浅：     #B8CDD9（浅雾蓝）
主色调极浅：   #F0F5F8（浅蓝底/全局背景）
卡片底色：     #FFFFFF（白）
标题色：       #3A4A54（深蓝灰）
正文色：       #5A6B74（中蓝灰）
辅助文字色：   #9AAAB2（浅灰蓝）
细线颜色：     #DEE7EC（分割线/边框）
下划线标记色：  #B8CDD9（浅雾蓝，温和不抢眼）
正文字号：     15px
行高：         1.85
字间距：       0.5px
内容区边距：   0 10px（左右各 10px）
圆角（卡片）：  12px
圆角（标签）：  6px
阴影（卡片）：  0 4px 20px -4px rgba(92,127,149,0.12)
```

---

## 组件 1 全局容器

```html
<section style="max-width: 677px;margin: 0 auto;background: #F0F5F8;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #5A6B74;line-height: 1.85;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（浅蓝底 + 雾蓝左竖条 + 雾蓝引号）

> 浅蓝圆角底 + 左侧雾蓝竖条装饰 + 大号雾蓝引号 + 雾蓝加粗关键词 + 右下署名。极淡偏蓝阴影，圆角 12px，呼吸感十足。

```html
<section style="margin: 10px 10px 36px;background: #FFFFFF;border-radius: 12px;box-shadow: 0 4px 20px -4px rgba(92,127,149,0.12);padding: 28px 24px 22px 20px;border-left: 4px solid #7C9EB2;overflow: hidden;">
  <p style="font-size: 40px;color: #7C9EB2;font-weight: 900;margin: 0;line-height: 0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size: 16px;font-weight: 700;color: #3A4A54;margin: 14px 0 10px;line-height: 1.85;padding-left: 4px;">
    <span style="background: #F0F5F8;color: #5B7F95;padding: 2px 8px;border-radius: 6px;font-weight: 700;"><span leaf="">高亮关键词</span></span>
    <span leaf="">，不是工具，而是懂得如何</span>
    <span style="background: #F0F5F8;color: #5B7F95;padding: 2px 8px;border-radius: 6px;font-weight: 700;"><span leaf="">驾驭</span></span>
    <span leaf="">它们的我们。</span>
  </p>
  <p style="text-align: right;font-size: 12px;color: #9AAAB2;margin: 10px 0 0;letter-spacing: 1px;">
    <span leaf="">—— 作者名（按文章作者/主题而定）</span>
  </p>
</section>
```

**效果**：白底浅蓝阴影浮起，左侧雾蓝竖条定调风格，浅蓝底色标签替代强烈色底，呼吸通透。

> **注意**：开头卡片内的关键词高亮用浅蓝底深雾蓝字（`background:#F0F5F8;color:#5B7F95`），与正文关键词标签保持风格统一，整体不刺眼。

---

## 组件 3 前言导读区域（浅蓝底目录卡片）

> 三列目录卡片，雾蓝细线边框 + 深雾蓝编号圆标 + 深蓝灰标题，清爽开阔。

```html
<section style="padding: 0 10px 36px;">
  <p style="font-size: 13px;color: #9AAAB2;margin: 0 0 14px;letter-spacing: 1.5px;">
    <span leaf="">· 本文看点 ·</span>
  </p>
  <section style="display: flex;justify-content: space-between;">
    <section style="flex: 1;background: #FFFFFF;border-radius: 10px;padding: 16px 12px;margin-right: 8px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
      <p style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 11px;font-weight: 800;padding: 2px 10px;border-radius: 10px;margin: 0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size: 13px;font-weight: 700;color: #3A4A54;margin: 0;line-height: 1.5;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="flex: 1;background: #FFFFFF;border-radius: 10px;padding: 16px 12px;margin-right: 8px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
      <p style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 11px;font-weight: 800;padding: 2px 10px;border-radius: 10px;margin: 0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size: 13px;font-weight: 700;color: #3A4A54;margin: 0;line-height: 1.5;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="flex: 1;background: #FFFFFF;border-radius: 10px;padding: 16px 12px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
      <p style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 11px;font-weight: 800;padding: 2px 10px;border-radius: 10px;margin: 0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size: 13px;font-weight: 700;color: #3A4A54;margin: 0;line-height: 1.5;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（雾蓝渐变细线）

```html
<section style="padding: 0 10px;">
  <section style="height: 1px;background: linear-gradient(to right, transparent, #B8CDD9, #7C9EB2, #B8CDD9, transparent);margin: 0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题组件（雾蓝编号 + 标题 + 细线）

> 雾蓝圆角编号徽章 + 英文小标签 + 中文大标题，底部雾蓝细线，呼吸感大间距。

```html
<section style="margin-top: 52px;margin-bottom: 28px;padding: 0 10px;">
  <section style="display: flex;align-items: center;justify-content: space-between;margin-bottom: 20px;padding-bottom: 14px;border-bottom: 1px solid #DEE7EC;">
    <section style="display: flex;align-items: center;">
      <span style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 16px;font-weight: 900;padding: 4px 14px;border-radius: 8px;margin-right: 14px;line-height: 1.4;letter-spacing: 1px;"><span leaf="">01</span></span>
      <section>
        <p style="font-size: 10px;color: #7C9EB2;font-weight: 700;letter-spacing: 3px;margin: 0 0 3px;text-transform: uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size: 18px;font-weight: 800;color: #3A4A54;margin: 0;letter-spacing: 0.5px;">
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
<span style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 16px;font-weight: 900;padding: 4px 14px;border-radius: 8px;margin-right: 14px;line-height: 1.4;letter-spacing: 1px;"><span leaf="">∞</span></span>
```

---

## 组件 6 正文段落

> **关键规则**：每个正文段落中，应主动识别 1～3 个**关键语句或关键词**，用**浅雾蓝下划线（7d）**进行标记。这是本风格的核心视觉特征——让读者快速扫到每段的重点，同时保持整体的通透宁静感。

**基础段落**：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;color: #5A6B74;">
  <span leaf="">正文内容，15px 字号，1.85 倍行高，两端对齐，中蓝灰正文色。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;color: #5A6B74;">
  <span leaf="">正文内容的前半部分，引出核心概念，</span>
  <span style="border-bottom: 2px solid #B8CDD9;font-weight: 600;color: #3A4A54;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述延展。</span>
</p>
```

**标记原则**：
- 每段选 1～3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4～15 个字，太短没意义，太长失去焦点
- 如果一段没有特别重要的内容，可以不标
- 下划线颜色用浅雾蓝 `#B8CDD9`，温和不抢眼，与风格气质吻合

---

## 组件 7 正文高亮样式（5 种变体 + 使用策略）

> **核心设计理念**：克制用色，雾蓝只在真正需要的锚点出现，整体保持通透宁静。
>
> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 浅雾蓝下划线** —— 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 深雾蓝加粗** —— 普通加粗为主，深雾蓝加粗仅用于极少数锚点
> 3. **7b 浅蓝底深雾蓝字标签** —— 核心概念标签（每篇 2～4 个）
> 4. **7c 浅蓝背景高亮** —— 次要关键词补充
> 5. **7e 荧光笔** —— 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，绝大部分加粗使用此样式。**深雾蓝加粗**仅用于极少数关键锚点（如核心结论、步骤编号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong><span leaf="">普通加粗强调</span></strong>
```

深雾蓝加粗（仅限关键锚点）：
```html
<strong style="color: #5B7F95;"><span leaf="">深雾蓝加粗，仅用于核心结论/步骤/CTA</span></strong>
```

### 7b. 浅蓝底深雾蓝字标签

> 浅蓝底 + 深雾蓝文字，柔和通透。用于核心概念（每篇 2～4 个）

```html
<span style="background: #F0F5F8;color: #5B7F95;padding: 2px 7px;border-radius: 4px;font-weight: 700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅蓝背景高亮

> 更淡的浅蓝背景标注，适用于次要关键词

```html
<span style="background: #F0F5F8;padding: 1px 6px;border-radius: 4px;font-weight: 600;color: #3A4A54;"><span leaf="">浅蓝背景关键词</span></span>
```

### 7d. 浅雾蓝下划线 —— 最常用

> **本风格的标志性标记方式**。颜色为浅雾蓝 `#B8CDD9`，温和不抢眼，适合高频使用，与整体清透气质高度匹配。

```html
<span style="border-bottom: 2px solid #B8CDD9;font-weight: 600;color: #3A4A54;"><span leaf="">浅雾蓝下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;color: #5A6B74;">
  <span leaf="">AI 竞争已进入下半场：上半场拼模型能力，下半场拼</span>
  <span style="border-bottom: 2px solid #B8CDD9;font-weight: 600;color: #3A4A54;"><span leaf="">分发能力</span></span>
  <span leaf="">。微信的策略清晰：不做模型、不限生态，只做一件事——</span>
  <span style="border-bottom: 2px solid #B8CDD9;font-weight: 600;color: #3A4A54;"><span leaf="">把 AI 入口握在手里</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 荧光笔效果

> 底部 40% 浅雾蓝高亮，偶尔用于长句强调，保持整体通透感

```html
<span style="background: linear-gradient(180deg, transparent 60%, #B8CDD9 60%);font-weight: 700;color: #3A4A54;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用高亮块（3 种变体）

### 8a. 浅蓝底左竖条金句引用（视觉焦点最强）

> 浅蓝底 + 雾蓝左竖条，用于核心金句，清透有呼吸感

```html
<section style="background: #F0F5F8;border-radius: 0 10px 10px 0;border-left: 3px solid #7C9EB2;padding: 18px 22px;margin-bottom: 28px;">
  <p style="font-size: 16px;font-weight: 700;color: #3A4A54;margin: 0;line-height: 1.85;">
    <span leaf="">「这里是核心观点或关键金句，清透通风。」</span>
  </p>
</section>
```

### 8b. 白底细线边框引用块（Prompt / 内容块）

> 白底 + 雾蓝细线边框，用于展示 Prompt、引用内容等，干净整洁

```html
<section style="background: #FFFFFF;border-radius: 10px;padding: 18px 20px;margin-bottom: 28px;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
  <p style="font-size: 15px;color: #5A6B74;margin: 0;line-height: 1.85;text-align: justify;">
    <span leaf="">白底细线引用内容，可以包含</span>
    <span style="border-bottom: 2px solid #B8CDD9;font-weight: 600;color: #3A4A54;"><span leaf="">下划线加粗的关键句</span></span>
    <span leaf="">，整体清透宁静。</span>
  </p>
</section>
```

### 8c. 浅灰左竖条引用（轻量旁注）

> 浅灰底 + 浅灰左竖条，用于轻量旁注、附加说明，不抢主体

```html
<section style="border-left: 3px solid #DEE7EC;padding: 14px 20px;margin-bottom: 28px;background: #FAFBFC;border-radius: 0 8px 8px 0;">
  <p style="font-size: 14px;color: #9AAAB2;margin: 0;line-height: 1.85;text-align: justify;">
    <span leaf="">轻量旁注内容，左竖条简洁不抢戏，适合补充说明。</span>
  </p>
</section>
```

---

## 组件 9 提示块（3 种变体）

### 9a. 雾蓝提示条（重要信息）

> 浅蓝底 + 雾蓝左竖条 + 深雾蓝文字，用于重要提醒、核心结论

```html
<section style="background: #F0F5F8;border-left: 3px solid #7C9EB2;border-radius: 0 8px 8px 0;padding: 14px 20px;margin-bottom: 28px;">
  <p style="font-size: 14px;font-weight: 700;color: #5B7F95;margin: 0;line-height: 1.85;">
    <span leaf="">💡 这里是重要提示或核心结论</span>
  </p>
</section>
```

### 9b. 注意事项条（警示）

> 白底 + 浅雾蓝左竖条 + 正文色，用于一般注意事项

```html
<section style="background: #FFFFFF;border-left: 3px solid #B8CDD9;border-radius: 0 8px 8px 0;padding: 14px 20px;margin-bottom: 28px;border: 1px solid #DEE7EC;border-left-width: 3px;">
  <p style="font-size: 14px;color: #5A6B74;margin: 0;line-height: 1.85;">
    <span leaf="">📌 这里是注意事项或附加说明</span>
  </p>
</section>
```

### 9c. 小标签提示行（行内标注）

> 浅蓝底小圆角标签 + 说明文字，适合行内的轻量提示

```html
<p style="margin-bottom: 22px;font-size: 14px;color: #9AAAB2;line-height: 1.85;">
  <span style="display: inline-block;background: #F0F5F8;color: #7C9EB2;font-size: 11px;font-weight: 700;padding: 2px 8px;border-radius: 4px;margin-right: 8px;"><span leaf="">提示</span></span>
  <span leaf="">这里是行内轻量提示内容。</span>
</p>
```

---

## 组件 10 图片容器

```html
<section style="background: #FFFFFF;border-radius: 12px;padding: 6px;border: 1px solid #DEE7EC;box-shadow: 0 4px 14px -4px rgba(92,127,149,0.10);margin-bottom: 10px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width: 100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时，图片 `margin-bottom` 改为 `8px`：

```html
<section style="background: #FFFFFF;border-radius: 12px;padding: 6px;border: 1px solid #DEE7EC;box-shadow: 0 4px 14px -4px rgba(92,127,149,0.10);margin-bottom: 8px;">
  <section style="margin: 0;border-radius: 8px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width: 100%;"></span>
  </section>
</section>
<p style="font-size: 12px;color: #9AAAB2;text-align: center;margin: 0 0 28px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 11 加粗正文段落

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;font-weight: 700;color: #3A4A54;">
  <span leaf="">加粗的结论性短句，深蓝灰色突出重量感。</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;font-weight: 700;color: #3A4A54;">
  <span style="background: linear-gradient(180deg, transparent 60%, #B8CDD9 60%);"><span leaf="">荧光笔标记的结论句，通透雾蓝底色。</span></span>
</p>
```

---

## 组件 12 数据 / 要点卡片组

### 两列版

```html
<section style="display: flex;margin-bottom: 28px;padding: 0;">
  <section style="flex: 1;background: #FFFFFF;border-radius: 12px;padding: 20px 16px;margin-right: 8px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
    <p style="font-size: 28px;font-weight: 900;color: #7C9EB2;margin: 0 0 6px;line-height: 1;"><span leaf="">14亿</span></p>
    <p style="font-size: 12px;color: #9AAAB2;margin: 0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex: 1;background: #FFFFFF;border-radius: 12px;padding: 20px 16px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
    <p style="font-size: 28px;font-weight: 900;color: #7C9EB2;margin: 0 0 6px;line-height: 1;"><span leaf="">3步</span></p>
    <p style="font-size: 12px;color: #9AAAB2;margin: 0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display: flex;margin-bottom: 28px;padding: 0;">
  <section style="flex: 1;background: #FFFFFF;border-radius: 12px;padding: 18px 12px;margin-right: 7px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
    <p style="font-size: 24px;font-weight: 900;color: #7C9EB2;margin: 0 0 6px;line-height: 1;"><span leaf="">98%</span></p>
    <p style="font-size: 12px;color: #9AAAB2;margin: 0;"><span leaf="">用户满意度</span></p>
  </section>
  <section style="flex: 1;background: #FFFFFF;border-radius: 12px;padding: 18px 12px;margin-right: 7px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
    <p style="font-size: 24px;font-weight: 900;color: #7C9EB2;margin: 0 0 6px;line-height: 1;"><span leaf="">50+</span></p>
    <p style="font-size: 12px;color: #9AAAB2;margin: 0;"><span leaf="">应用场景</span></p>
  </section>
  <section style="flex: 1;background: #FFFFFF;border-radius: 12px;padding: 18px 12px;text-align: center;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
    <p style="font-size: 24px;font-weight: 900;color: #7C9EB2;margin: 0 0 6px;line-height: 1;"><span leaf="">∞</span></p>
    <p style="font-size: 12px;color: #9AAAB2;margin: 0;"><span leaf="">可能性</span></p>
  </section>
</section>
```

### 要点列表卡片（带左竖条的内容项）

```html
<section style="background: #FFFFFF;border-radius: 12px;padding: 20px 20px;margin-bottom: 28px;border: 1px solid #DEE7EC;box-shadow: 0 2px 10px -2px rgba(92,127,149,0.08);">
  <section style="display: flex;align-items: flex-start;margin-bottom: 16px;">
    <span style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 11px;font-weight: 800;padding: 2px 8px;border-radius: 4px;margin-right: 12px;margin-top: 2px;flex-shrink: 0;"><span leaf="">01</span></span>
    <p style="font-size: 14px;color: #5A6B74;margin: 0;line-height: 1.85;"><span leaf="">第一个要点的说明文字，简洁有力。</span></p>
  </section>
  <section style="display: flex;align-items: flex-start;margin-bottom: 16px;">
    <span style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 11px;font-weight: 800;padding: 2px 8px;border-radius: 4px;margin-right: 12px;margin-top: 2px;flex-shrink: 0;"><span leaf="">02</span></span>
    <p style="font-size: 14px;color: #5A6B74;margin: 0;line-height: 1.85;"><span leaf="">第二个要点的说明文字，简洁有力。</span></p>
  </section>
  <section style="display: flex;align-items: flex-start;">
    <span style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 11px;font-weight: 800;padding: 2px 8px;border-radius: 4px;margin-right: 12px;margin-top: 2px;flex-shrink: 0;"><span leaf="">03</span></span>
    <p style="font-size: 14px;color: #5A6B74;margin: 0;line-height: 1.85;"><span leaf="">第三个要点的说明文字，简洁有力。</span></p>
  </section>
</section>
```

---

## 组件 13 标签胶囊

### 浅蓝底深雾蓝字（默认）

```html
<span style="display: inline-block;background: #F0F5F8;color: #5B7F95;font-size: 12px;font-weight: 700;padding: 2px 10px;border-radius: 6px;margin-right: 6px;"><span leaf="">标签名</span></span>
```

### 雾蓝细线描边（轻量）

```html
<span style="display: inline-block;border: 1px solid #7C9EB2;color: #7C9EB2;font-size: 12px;font-weight: 600;padding: 1px 10px;border-radius: 6px;margin-right: 6px;"><span leaf="">标签名</span></span>
```

### 雾蓝实底白字（强调）

```html
<span style="display: inline-block;background: #7C9EB2;color: #FFFFFF;font-size: 12px;font-weight: 700;padding: 2px 10px;border-radius: 6px;margin-right: 6px;"><span leaf="">标签名</span></span>
```

---

## 组件 14 END 结尾分割线

```html
<section style="padding: 0 10px;">
  <section style="text-align: center;margin: 0 0 36px;">
    <section style="display: flex;align-items: center;justify-content: center;">
      <span style="height: 1px;width: 60px;background: linear-gradient(to right, transparent, #7C9EB2);margin-right: 14px;"></span>
      <span style="font-size: 11px;color: #7C9EB2;letter-spacing: 4px;font-weight: 600;"><span leaf="">END</span></span>
      <span style="height: 1px;width: 60px;background: linear-gradient(to left, transparent, #7C9EB2);margin-left: 14px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部作者签名区

```html
<section style="padding: 0 10px;">
  <p style="margin-bottom: 20px;font-size: 15px;line-height: 1.85;text-align: justify;color: #5A6B74;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察，AI 干货内容</span>
  </p>
  <p style="margin-bottom: 20px;font-size: 15px;line-height: 1.85;text-align: justify;color: #5A6B74;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color: #5B7F95;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width: 677px;margin: 0 auto;background: #F0F5F8;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #5A6B74;line-height: 1.85;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 1. 开头引言卡片（白底 + 雾蓝左竖条 + 雾蓝引号） -->
  <!-- 组件 2 -->

  <!-- 2. 前言正文（开场白） -->
  <section style="padding: 0 10px 24px;">
    <!-- 组件 6 正文段落 × N -->
  </section>

  <!-- 3. 目录导航 -->
  <!-- 组件 3 浅蓝底目录卡片 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件 4 雾蓝渐变细线 -->

  <!-- 5. 第一章 -->
  <!-- 组件 5（雾蓝编号 01 + 标题 + 细线） -->
  <!--   组件 6 正文 + 组件 7 高亮 + 组件 8 引用 + 组件 9 提示条 + 组件 10 图片 + 组件 12 数据卡片 -->

  <!-- 6. 章节分割线 -->

  <!-- 7. 第二章 -->
  <!-- 组件 5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- 8. 章节分割线 -->

  <!-- 9. 结语章节 -->
  <!-- 组件 5（∞ 变体） -->

  <!-- 10. END 分割线 -->
  <!-- 组件 14 -->

  <!-- 11. 尾部签名 -->
  <!-- 组件 15 -->

</section>
```

---

## 视觉层级设计（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 深雾蓝加粗 `color:#5B7F95` | 核心结论、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 浅雾蓝下划线 `#B8CDD9` | 正文关键词强调 | 每段 1～3 处 |
| **容器层** | 左竖条 + 浅蓝底 / 小标签 | 引用、旁注、提示 | 按需 |

**克制原则**：
- 雾蓝实底白字标签（`bg:#7C9EB2`）**主要用于编号徽章和目录**，正文中用浅蓝底深雾蓝字替代
- 深雾蓝加粗全文不超过 5 处
- 引用/提示统一用左竖条 + 浅底，不用四周虚线框（dashed）
- 渐变雾蓝仅出现在章节分割线和 END 线
- 全局背景用浅蓝 `#F0F5F8`，卡片白底 `#FFFFFF`，形成通透的底卡层次感

---

## Markdown → 雾蓝晴空风排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 白底雾蓝左竖条引言卡片 | 文章开头的引用 |
| `## 章节标题` | 组件 5 章节标题 | 雾蓝编号徽章 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，主动标记关键词下划线 |
| `**加粗文字**` | 组件 7a 普通加粗（默认）或深雾蓝加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 浅蓝底深雾蓝字标签 | 核心概念 |
| `<u>下划线</u>` | 组件 7d 浅雾蓝下划线 | 2px `#B8CDD9` |
| `~~文字~~` | 组件 7e 荧光笔 | 浅雾蓝底部半高亮 |
| `> 引用段落`（金句） | 组件 8a 浅蓝底左竖条 | 核心金句 |
| `> 引用段落`（内容块） | 组件 8b 白底细线边框 | Prompt / 引用内容 |
| `> 引用段落`（旁注） | 组件 8c 浅灰左竖条 | 轻量旁注 |
| `!> 提示文字` | 组件 9a 雾蓝提示条 | 浅蓝底左竖条 |
| `![](图片)` | 组件 10 图片容器 | 白底圆角卡片 + 说明 |
| 数据展示 | 组件 12 数据卡片组 | 雾蓝大号数据 |
| 行内标签 | 组件 13 标签胶囊 | 浅蓝底为默认 |
| `---` | 组件 4 章节分割线 | 雾蓝渐变细线 |
| 文末 | 组件 14 + 15 | END 线 + 签名 |
