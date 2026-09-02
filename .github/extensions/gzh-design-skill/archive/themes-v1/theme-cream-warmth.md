# 甲木公众号排版组件库 —— 奶油暖阳风（Cream）

> **使用说明**：本组件库为「奶油暖阳风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：奶油米色底 + 暖橘点睛、大圆角圆润舒适、温暖治愈轻杂志感。呼吸感充足，简洁大方，全暖调无冷色。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>` 标签、`<script>` 标签、CSS class
> - ❌ 不支持 `position: fixed/absolute/sticky`、`float`
> - ❌ 不支持 `@media` 媒体查询、`@keyframes` 动画
> - ❌ 不支持 `display: grid`
> - ✅ 支持内联 `style` 属性
> - ✅ 支持 `display: flex`（有限支持）
> - ✅ 支持 `linear-gradient`
> - ✅ 支持 `border-radius`、`box-shadow`
> - ✅ 支持 `<section>`、`<p>`、`<span>`、`<strong>`、`<img>` 等基础标签

---

## 设计变量速查表

```
主色调（暖橘）：    #E8A87C
辅色（暖金）：      #D4A574
辅色（柔棕）：      #C08552
全局背景（奶油底）：#FAF6F0
卡片底色：          #FFFFFF
引用浅底：          #FFF8F2
提示浅底：          #FFF3E8
下划线标记色：      #EDD5B8（暖米下划线，温和不刺眼）
标题色：            #5C4A3A（深暖棕）
正文色：            #6B5D4F（中暖棕）
辅助文字色：        #A89684（浅暖灰棕）
细线色：            #EDE4D8
左竖条主色：        #E8A87C（暖橘）
左竖条辅色：        #D4C4B0（柔米灰，旁注用）
正文字号：          15px
行高：              1.85
字间距：            0.5px
内容区边距：        0 10px（左右各 10px）
圆角（卡片）：      16px
圆角（标签）：      8px
阴影：              0 4px 20px -4px rgba(200,140,90,0.13)
```

---

## 组件 1 全局容器

```html
<section style="max-width: 677px;margin: 0 auto;background: #FAF6F0;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #6B5D4F;line-height: 1.85;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（奶油大圆角 + 暖橘左竖条 + 暖色引号）

> 白底大圆角卡片 + 暖橘左竖条 + 暖色大引号 + 暖橘实底关键词高亮 + 右下署名。温暖质感，呼吸感十足。

```html
<section style="margin: 10px 10px 36px;background: #FFFFFF;border-radius: 16px;box-shadow: 0 4px 20px -4px rgba(200,140,90,0.13);padding: 28px 24px 22px;overflow: hidden;border-left: 5px solid #E8A87C;">
  <p style="font-size: 44px;color: #E8A87C;font-weight: 900;margin: 0;line-height: 0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size: 16px;font-weight: 800;color: #5C4A3A;margin: 14px 0 10px;line-height: 1.8;padding-left: 2px;">
    <span style="background: #E8A87C;color: #FFFFFF;padding: 2px 9px;border-radius: 6px;"><span leaf="">高亮关键词</span></span>
    <span leaf="">，不是模型，而是懂得如何</span>
    <span style="background: #E8A87C;color: #FFFFFF;padding: 2px 9px;border-radius: 6px;"><span leaf="">驾驭</span></span>
    <span leaf="">它们的我们。</span>
  </p>
  <p style="text-align: right;font-size: 12px;color: #A89684;margin: 10px 0 0;letter-spacing: 1px;">
    <span leaf="">—— 作者名（按文章作者/主题而定）</span>
  </p>
</section>
```

**效果**：白底奶油卡片，暖橘左竖条定调，大引号温暖开场，暖橘实底标签点睛，圆角 16px 柔润圆滑。

> **注意**：开头卡片内的关键词高亮保留暖橘底白字（`background:#E8A87C;color:#FFFFFF`）；正文中的关键词标签则用浅橘底深棕字（见组件 7b）。

---

## 组件 3 前言导读区域（暖色三列目录卡片）

> 三列奶油底目录卡片，暖橘编号标签 + 深棕标题，细暖边框。

```html
<section style="padding: 0 10px 36px;">
  <p style="font-size: 13px;color: #A89684;margin: 0 0 14px;letter-spacing: 1px;">
    <span leaf="">📌 本文看点</span>
  </p>
  <section style="display: flex;justify-content: space-between;">
    <section style="flex: 1;background: #FFF8F2;border-radius: 14px;padding: 16px 12px;margin-right: 8px;text-align: center;border: 1px solid #EDE4D8;">
      <p style="display: inline-block;background: #E8A87C;color: #FFFFFF;font-size: 12px;font-weight: 800;padding: 2px 10px;border-radius: 6px;margin: 0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size: 13px;font-weight: 700;color: #5C4A3A;margin: 0;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="flex: 1;background: #FFF8F2;border-radius: 14px;padding: 16px 12px;margin-right: 8px;text-align: center;border: 1px solid #EDE4D8;">
      <p style="display: inline-block;background: #E8A87C;color: #FFFFFF;font-size: 12px;font-weight: 800;padding: 2px 10px;border-radius: 6px;margin: 0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size: 13px;font-weight: 700;color: #5C4A3A;margin: 0;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="flex: 1;background: #FFF8F2;border-radius: 14px;padding: 16px 12px;text-align: center;border: 1px solid #EDE4D8;">
      <p style="display: inline-block;background: #E8A87C;color: #FFFFFF;font-size: 12px;font-weight: 800;padding: 2px 10px;border-radius: 6px;margin: 0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size: 13px;font-weight: 700;color: #5C4A3A;margin: 0;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（暖橘渐变）

```html
<section style="padding: 0 10px;">
  <section style="height: 1px;background: linear-gradient(to right, transparent, #EDD5B8, #E8A87C, #EDD5B8, transparent);margin: 0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题组件（暖橘圆角编号 + 标题）

> 暖橘圆角编号标签 + 英文小标签 + 中文大标题，底部暖金细线，整体简洁大方有呼吸感。

```html
<section style="margin-top: 48px;margin-bottom: 28px;padding: 0 10px;">
  <section style="display: flex;align-items: center;justify-content: space-between;margin-bottom: 20px;padding-bottom: 14px;border-bottom: 2px solid #EDE4D8;">
    <section style="display: flex;align-items: center;">
      <span style="display: inline-block;background: #E8A87C;color: #FFFFFF;font-size: 18px;font-weight: 900;padding: 5px 15px;border-radius: 10px;margin-right: 14px;line-height: 1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size: 10px;color: #E8A87C;font-weight: 700;letter-spacing: 3px;margin: 0 0 3px;text-transform: uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size: 18px;font-weight: 800;color: #5C4A3A;margin: 0;letter-spacing: 0.5px;">
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
<span style="display: inline-block;background: #D4A574;color: #FFFFFF;font-size: 18px;font-weight: 900;padding: 5px 15px;border-radius: 10px;margin-right: 14px;line-height: 1.3;"><span leaf="">∞</span></span>
```

---

## 组件 6 正文段落

> **关键规则**：每个正文段落中，应主动识别 1～3 个**关键语句或关键词**，用**暖米下划线（7d）**进行标记。这是本风格的核心视觉特征——让读者快速扫到每段的重点。

**基础段落**：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;color: #6B5D4F;">
  <span leaf="">正文内容，15px 字号，1.85 倍行高，两端对齐，奶油暖棕色。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;color: #6B5D4F;">
  <span leaf="">正文内容的前半部分，引出核心概念——</span>
  <span style="border-bottom: 2px solid #EDD5B8;font-weight: 600;color: #5C4A3A;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

**标记原则**：
- 每段选 1～3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4～15 个字，太短没意义，太长失去焦点
- 如果一段没有特别重要的内容，可以不标

---

## 组件 7 正文高亮样式（5 种变体 + 使用策略）

> **核心设计理念**：克制用色，暖橘只在真正需要的锚点出现，整体保持奶油温暖底色的呼吸感。
>
> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 暖米下划线** —— 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 暖橘加粗** —— 普通加粗为主，暖橘加粗仅用于极少数锚点
> 3. **7b 浅橘底深棕字标签** —— 核心概念标签（每篇 2～4 个）
> 4. **7c 浅米背景高亮** —— 次要关键词补充
> 5. **7e 暖橘荧光笔** —— 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，绝大部分加粗使用此样式。**暖橘加粗**仅用于极少数关键锚点（如产品名、步骤编号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong style="color: #5C4A3A;"><span leaf="">普通加粗强调</span></strong>
```

暖橘加粗（仅限关键锚点）：
```html
<strong style="color: #C08552;"><span leaf="">暖橘加粗，仅用于产品名/步骤/CTA</span></strong>
```

### 7b. 浅橘底深棕字标签

> 浅橘背景 + 深棕文字，柔和温暖不刺眼。用于核心概念（每篇 2～4 个）

```html
<span style="background: #FCECD9;color: #7A4F2E;padding: 2px 7px;border-radius: 5px;font-weight: 700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅米背景高亮

> 柔和的奶油米背景标注，适用于次要关键词

```html
<span style="background: #FFF3E8;padding: 1px 6px;border-radius: 5px;font-weight: 600;color: #C08552;"><span leaf="">浅米背景关键词</span></span>
```

### 7d. 暖米下划线 —— 最常用

> **本风格的标志性标记方式**。颜色为暖米 `#EDD5B8`，温和不抢眼，适合高频使用。

```html
<span style="border-bottom: 2px solid #EDD5B8;font-weight: 600;color: #5C4A3A;"><span leaf="">暖米下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;color: #6B5D4F;">
  <span leaf="">AI 竞争已进入下半场：上半场拼模型能力，下半场拼</span>
  <span style="border-bottom: 2px solid #EDD5B8;font-weight: 600;color: #5C4A3A;"><span leaf="">分发能力</span></span>
  <span leaf="">。微信的策略清晰：不做模型、不限生态，只做一件事——</span>
  <span style="border-bottom: 2px solid #EDD5B8;font-weight: 600;color: #5C4A3A;"><span leaf="">把 AI 入口握在手里</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 暖橘荧光笔效果

> 底部 40% 暖橘高亮，偶尔用于长句强调，温暖不突兀

```html
<span style="background: linear-gradient(180deg, transparent 60%, #FCECD9 60%);font-weight: 700;color: #5C4A3A;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用高亮块（3 种变体）

### 8a. 奶油底暖橘左竖条块金句引用（视觉焦点最强）

> 暖米底 + 暖橘左竖条块，用于核心金句，温暖大气

```html
<section style="background: #FFF8F2;border-radius: 0 14px 14px 0;border-left: 4px solid #E8A87C;padding: 18px 22px;margin-bottom: 24px;">
  <p style="font-size: 16px;font-weight: 800;color: #7A4F2E;margin: 0;line-height: 1.8;">
    <span leaf="">「这里是核心观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 浅米背景引用块（内容块 / Prompt）

> 浅米底 + 暖米细边框，用于展示 Prompt、引用内容等，自然融入整体暖调

```html
<section style="background: #FFF8F2;border-radius: 14px;padding: 18px 20px;margin-bottom: 24px;border: 1px solid #EDE4D8;">
  <p style="font-size: 15px;color: #6B5D4F;margin: 0;line-height: 1.85;text-align: justify;">
    <span leaf="">浅米引用内容，可以包含</span>
    <span style="border-bottom: 2px solid #EDD5B8;font-weight: 600;color: #5C4A3A;"><span leaf="">下划线加粗的关键句</span></span>
  </p>
</section>
```

### 8c. 柔米左竖条块引用（轻量旁注）

> 浅奶米底 + 柔米灰左竖条块，用于轻量旁注、补充说明等，不抢主文

```html
<section style="border-left: 4px solid #D4C4B0;padding: 14px 20px;margin-bottom: 24px;background: #FDFAF6;border-radius: 0 10px 10px 0;">
  <p style="font-size: 14px;color: #6B5D4F;margin: 0;line-height: 1.85;text-align: justify;">
    <span leaf="">轻量旁注内容，柔米左竖条块简洁不抢戏</span>
  </p>
</section>
```

---

## 组件 9 提示/警示条

> 浅橘底 + 暖橘左竖条块 + 深棕文字，用于重要提醒、核心结论，温暖醒目

```html
<section style="background: #FFF3E8;border-left: 4px solid #E8A87C;border-radius: 0 10px 10px 0;padding: 14px 20px;margin-bottom: 24px;">
  <p style="font-size: 14px;font-weight: 700;color: #7A4F2E;margin: 0;line-height: 1.85;">
    <span leaf="">💡 这里是重要提示或核心结论</span>
  </p>
</section>
```

---

## 组件 10 图片容器

```html
<section style="background: #FFFFFF;border-radius: 14px;padding: 6px;border: 1px solid #EDE4D8;box-shadow: 0 4px 16px -4px rgba(200,140,90,0.10);margin-bottom: 10px;">
  <section style="margin: 0;border-radius: 10px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width: 100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时，图片 `margin-bottom` 改为 `8px`：

```html
<section style="background: #FFFFFF;border-radius: 14px;padding: 6px;border: 1px solid #EDE4D8;box-shadow: 0 4px 16px -4px rgba(200,140,90,0.10);margin-bottom: 8px;">
  <section style="margin: 0;border-radius: 10px;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width: 100%;"></span>
  </section>
</section>
<p style="font-size: 12px;color: #A89684;text-align: center;margin: 0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 11 加粗正文段落

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;font-weight: 700;color: #5C4A3A;">
  <span leaf="">加粗的结论性短句</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom: 22px;font-size: 15px;line-height: 1.85;text-align: justify;font-weight: 700;color: #5C4A3A;">
  <span style="background: linear-gradient(180deg, transparent 60%, #FCECD9 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

---

## 组件 12 数据/要点卡片组

### 两列版

```html
<section style="display: flex;margin-bottom: 24px;padding: 0;">
  <section style="flex: 1;background: #FFF8F2;border-radius: 16px;padding: 20px 16px;margin-right: 10px;text-align: center;border: 1px solid #EDE4D8;box-shadow: 0 2px 10px -2px rgba(200,140,90,0.09);">
    <p style="font-size: 28px;font-weight: 900;color: #E8A87C;margin: 0 0 6px;line-height: 1;"><span leaf="">14亿</span></p>
    <p style="font-size: 12px;color: #A89684;margin: 0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex: 1;background: #FFF8F2;border-radius: 16px;padding: 20px 16px;text-align: center;border: 1px solid #EDE4D8;box-shadow: 0 2px 10px -2px rgba(200,140,90,0.09);">
    <p style="font-size: 28px;font-weight: 900;color: #E8A87C;margin: 0 0 6px;line-height: 1;"><span leaf="">3步</span></p>
    <p style="font-size: 12px;color: #A89684;margin: 0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display: flex;margin-bottom: 24px;padding: 0;">
  <section style="flex: 1;background: #FFF8F2;border-radius: 16px;padding: 18px 12px;margin-right: 8px;text-align: center;border: 1px solid #EDE4D8;">
    <p style="font-size: 24px;font-weight: 900;color: #E8A87C;margin: 0 0 5px;line-height: 1;"><span leaf="">95%</span></p>
    <p style="font-size: 12px;color: #A89684;margin: 0;"><span leaf="">满意度</span></p>
  </section>
  <section style="flex: 1;background: #FFF8F2;border-radius: 16px;padding: 18px 12px;margin-right: 8px;text-align: center;border: 1px solid #EDE4D8;">
    <p style="font-size: 24px;font-weight: 900;color: #D4A574;margin: 0 0 5px;line-height: 1;"><span leaf="">200+</span></p>
    <p style="font-size: 12px;color: #A89684;margin: 0;"><span leaf="">实战案例</span></p>
  </section>
  <section style="flex: 1;background: #FFF8F2;border-radius: 16px;padding: 18px 12px;text-align: center;border: 1px solid #EDE4D8;">
    <p style="font-size: 24px;font-weight: 900;color: #C08552;margin: 0 0 5px;line-height: 1;"><span leaf="">48h</span></p>
    <p style="font-size: 12px;color: #A89684;margin: 0;"><span leaf="">平均上手</span></p>
  </section>
</section>
```

---

## 组件 13 标签胶囊

### 浅橘底深棕字（默认）

```html
<span style="display: inline-block;background: #FCECD9;color: #7A4F2E;font-size: 12px;font-weight: 700;padding: 3px 11px;border-radius: 8px;margin-right: 6px;"><span leaf="">标签名</span></span>
```

### 暖橘描边（轻量）

```html
<span style="display: inline-block;border: 1px solid #E8A87C;color: #C08552;font-size: 12px;font-weight: 600;padding: 2px 10px;border-radius: 8px;margin-right: 6px;"><span leaf="">标签名</span></span>
```

### 暖金实底（强调）

```html
<span style="display: inline-block;background: #E8A87C;color: #FFFFFF;font-size: 12px;font-weight: 700;padding: 3px 11px;border-radius: 8px;margin-right: 6px;"><span leaf="">核心标签</span></span>
```

---

## 组件 14 END 结尾分割线

```html
<section style="padding: 0 10px;">
  <section style="text-align: center;margin: 0 0 36px;">
    <section style="display: flex;align-items: center;justify-content: center;">
      <span style="height: 1px;width: 56px;background: linear-gradient(to right, transparent, #D4A574);margin-right: 14px;"></span>
      <span style="font-size: 11px;color: #C08552;letter-spacing: 4px;font-weight: 700;"><span leaf="">END</span></span>
      <span style="height: 1px;width: 56px;background: linear-gradient(to left, transparent, #D4A574);margin-left: 14px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部作者签名区

```html
<section style="padding: 0 10px;">
  <p style="margin-bottom: 20px;font-size: 15px;line-height: 1.85;text-align: justify;color: #6B5D4F;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察，AI 干货内容</span>
  </p>
  <p style="margin-bottom: 20px;font-size: 15px;line-height: 1.85;text-align: justify;color: #6B5D4F;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color: #C08552;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width: 677px;margin: 0 auto;background: #FAF6F0;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #6B5D4F;line-height: 1.85;letter-spacing: 0.5px;overflow-x: hidden;">

  <!-- 1. 开头引言卡片（奶油白底 + 暖橘左竖条 + 大圆角） -->
  <!-- 组件2 -->

  <!-- 2. 前言正文（开场白） -->
  <section style="padding: 0 10px 20px;">
    <!-- 组件6 正文段落 x N -->
  </section>

  <!-- 3. 目录导航 -->
  <!-- 组件3 暖色三列目录卡片 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件4 暖橘渐变分割线 -->

  <!-- 5. 第一章 -->
  <!-- 组件5（暖橘圆角编号 01 + 标题） -->
  <!--   组件6正文 + 组件7高亮 + 组件8引用 + 组件9提示条 + 组件10图片 + 组件12数据卡片 -->

  <!-- 6. 章节分割线 -->

  <!-- 7. 第二章 -->
  <!-- 组件5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- 8. 章节分割线 -->

  <!-- 9. 结语章节 -->
  <!-- 组件5（∞ 变体，暖金底） -->

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
| **锚点层** | 暖橘加粗 `color:#C08552` | 产品名、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 暖米下划线 `#EDD5B8` | 正文关键词强调 | 每段 1～3 处 |
| **容器层** | 左竖条 + 浅底 / 小标签 | 引用、旁注、提示 | 按需 |

**克制原则**：
- 暖橘实底白字标签（`bg:#E8A87C`）**仅在开头卡片内使用**，正文中用浅橘底深棕字替代
- 暖橘加粗全文不超过 5 处
- 引用/提示统一用左竖条 + 浅底，不用四周虚线框（dashed）
- 渐变暖橘仅出现在分割线和 END 线
- 全文无冷色，所有色值均在暖调范围内

---

## Markdown → 奶油暖阳排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 奶油大圆角引言卡片 | 文章开头，暖橘左竖条 + 大引号 |
| `## 章节标题` | 组件 5 章节标题 | 暖橘圆角编号 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，主动标记关键词暖米下划线 |
| `**加粗文字**` | 组件 7a 普通加粗（默认）或暖橘加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 浅橘底深棕字标签 | 核心概念 |
| `<u>下划线</u>` | 组件 7d 暖米下划线 | 2px `#EDD5B8` |
| `~~文字~~` | 组件 7e 暖橘荧光笔 | 底部半高亮长句强调 |
| `> 引用段落`（金句） | 组件 8a 奶油底暖橘左竖条块 | 核心金句 |
| `> 引用段落`（旁注） | 组件 8c 柔米灰左竖条块 | 轻量旁注 |
| `!> 提示文字` | 组件 9 提示条 | 浅橘底暖橘左竖条块 |
| `![](图片)` | 组件 10 图片容器 | 圆角卡片 + 说明 |
| 数据展示 | 组件 12 数据卡片组 | 暖橘大号数据 |
| 行内标签 | 组件 13 标签胶囊 | 浅橘底为默认 |
| `---` | 组件 4 章节分割线 | 暖橘渐变 |
| 文末 | 组件 14 + 15 | END线 + 签名 |
