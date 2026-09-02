# 公众号排版组件库 —— 留白禅意风（Zen）

> **使用说明**：本组件库为「留白禅意风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：极简超大留白 + 东方禅意气质、衬线大字金句、细线分层、几乎无色块。靠留白和 1px 细线建立层次，克制、沉静、高级。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>` 标签、`<script>` 标签、CSS class
> - ❌ 不支持 `position: fixed/absolute`、`float`
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
主色调（墨绿）：    #4A5D52（点缀/强调专用，克制使用）
标题色：            #2B2B2B（近黑，衬线大字）
正文色：            #525252（中深灰）
辅助文字色：        #A3A3A3（小字/说明/署名）
细线色：            #E8E8E8（1px 分隔线，贯穿全文）
底色：              #FFFFFF（纯白）
下划线标记色：      #B5C8BC（低饱和墨绿，正文关键词专用）
荧光笔色：          #D6E4DC（极浅墨绿，底部半高亮，偶尔用）
标签底色：          #EEF3F0（极浅墨绿底，胶囊标签用）
标签文字色：        #3D5046（深墨绿，胶囊标签文字）

正文字号：          15px
行高：              1.9
字间距：            0.3px
段落间距：          26px+
章节上下留白：      64px+
内容区边距：        0 16px（左右各 16px，比红白系更宽）

标题字体：          'Noto Serif SC', Georgia, 'Times New Roman', serif（衬线）
正文字体：          -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif
```

---

## 组件 1 全局容器

```html
<section style="max-width: 677px;margin: 0 auto;background: #FFFFFF;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #525252;line-height: 1.9;letter-spacing: 0.3px;overflow-x: hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（纯白 + 居中细线上下边 + 衬线大字金句）

> 纯白底，上下各一条 1px 细线（`#E8E8E8`），衬线字体大字金句居中，右下署名。无边框、无阴影、无色块——完全靠留白和细线传递气质。

```html
<section style="margin: 32px 16px 48px;padding: 40px 24px;border-top: 1px solid #E8E8E8;border-bottom: 1px solid #E8E8E8;text-align: center;">
  <p style="font-family: 'Noto Serif SC', Georgia, 'Times New Roman', serif;font-size: 19px;font-weight: 600;color: #2B2B2B;margin: 0 0 28px;line-height: 1.85;letter-spacing: 0.8px;">
    <span leaf="">这里放开篇金句，衬线字体自带书卷气，</span><span leaf="">留白让文字自己呼吸。</span>
  </p>
  <p style="font-size: 12px;color: #A3A3A3;margin: 0;letter-spacing: 1.5px;">
    <span leaf="">—— 作者名（按文章作者/主题而定）</span>
  </p>
</section>
```

**效果**：纯白无色块，细线框定空间，衬线大字在大留白中极有质感。署名占位不写死品牌名。

---

## 组件 3 前言导读区域（极简目录）

> 无色块目录，用细线分隔，数字编号低调呈现。三列等宽，纯文字 + 细线底边。

```html
<section style="padding: 0 16px 48px;">
  <p style="font-size: 11px;color: #A3A3A3;margin: 0 0 20px;letter-spacing: 2px;text-transform: uppercase;">
    <span leaf="">本文脉络</span>
  </p>
  <section style="border-top: 1px solid #E8E8E8;">
    <section style="display: flex;">
      <section style="flex: 1;padding: 18px 12px 18px 0;border-bottom: 1px solid #E8E8E8;border-right: 1px solid #E8E8E8;margin-right: 16px;">
        <p style="font-size: 11px;color: #4A5D52;font-weight: 600;margin: 0 0 6px;letter-spacing: 1px;"><span leaf="">01</span></p>
        <p style="font-size: 13px;color: #2B2B2B;margin: 0;font-weight: 500;line-height: 1.5;"><span leaf="">第一个要点</span></p>
      </section>
      <section style="flex: 1;padding: 18px 12px 18px 0;border-bottom: 1px solid #E8E8E8;border-right: 1px solid #E8E8E8;margin-right: 16px;">
        <p style="font-size: 11px;color: #4A5D52;font-weight: 600;margin: 0 0 6px;letter-spacing: 1px;"><span leaf="">02</span></p>
        <p style="font-size: 13px;color: #2B2B2B;margin: 0;font-weight: 500;line-height: 1.5;"><span leaf="">第二个要点</span></p>
      </section>
      <section style="flex: 1;padding: 18px 0 18px 0;border-bottom: 1px solid #E8E8E8;">
        <p style="font-size: 11px;color: #4A5D52;font-weight: 600;margin: 0 0 6px;letter-spacing: 1px;"><span leaf="">03</span></p>
        <p style="font-size: 13px;color: #2B2B2B;margin: 0;font-weight: 500;line-height: 1.5;"><span leaf="">第三个要点</span></p>
      </section>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（1px 极细线，超大留白）

> 极细线 + 超大上下 margin，靠留白分层，不依赖视觉装饰。

```html
<section style="padding: 0 16px;">
  <section style="height: 1px;background: #E8E8E8;margin: 64px 0 0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题组件（小号墨绿英文 + 大号衬线中文 + 短细线）

> 英文小标签（极小号，墨绿，大字间距）+ 衬线中文大标题 + 标题下方一条短细线（40px 宽，墨绿）。编号低调嵌入英文标签前。无色块，无粗边框。

```html
<section style="margin-top: 64px;margin-bottom: 32px;padding: 0 16px;">
  <p style="font-size: 10px;color: #4A5D52;font-weight: 600;letter-spacing: 4px;margin: 0 0 10px;text-transform: uppercase;">
    <span leaf="">01 · CHAPTER ONE</span>
  </p>
  <h3 style="font-family: 'Noto Serif SC', Georgia, 'Times New Roman', serif;font-size: 22px;font-weight: 700;color: #2B2B2B;margin: 0 0 16px;letter-spacing: 0.5px;line-height: 1.4;">
    <span leaf="">中文章节大标题</span>
  </h3>
  <section style="width: 40px;height: 2px;background: #4A5D52;">
    <span leaf=""><br></span>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**（编号改 ∞，英文改 POSTSCRIPT）：

```html
<p style="font-size: 10px;color: #4A5D52;font-weight: 600;letter-spacing: 4px;margin: 0 0 10px;text-transform: uppercase;">
  <span leaf="">∞ · POSTSCRIPT</span>
</p>
```

---

## 组件 6 正文段落

> **关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**低饱和墨绿下划线（7d）**进行标记。这是本风格的核心视觉特征——在克制中让读者快速锁定每段重点。

**基础段落**：

```html
<p style="margin-bottom: 26px;font-size: 15px;line-height: 1.9;text-align: justify;color: #525252;padding: 0 16px;">
  <span leaf="">正文内容，15px 字号，1.9 倍行高，两端对齐。段落间距 26px+，字里行间充满呼吸感。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom: 26px;font-size: 15px;line-height: 1.9;text-align: justify;color: #525252;padding: 0 16px;">
  <span leaf="">正文内容的前半部分，引出核心概念，</span>
  <span style="border-bottom: 1.5px solid #B5C8BC;font-weight: 500;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字
- 下划线色为低饱和墨绿 `#B5C8BC`，非常克制，不喧宾夺主

---

## 组件 7 正文高亮样式（4 种变体 + 使用策略）

> **核心设计理念**：克制留白，墨绿只在真正需要的锚点出现。整体气质冷静，避免一切鲜艳色彩。
>
> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 低饱和墨绿下划线** —— 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 墨绿加粗** —— 普通加粗为主，墨绿加粗仅用于极少数锚点
> 3. **7b 浅墨绿底深色字标签** —— 核心概念标签（每篇 2~4 个）
> 4. **7e 极浅墨绿荧光笔** —— 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，绝大部分加粗使用此样式。**墨绿加粗**仅用于极少数关键锚点（如核心概念首次出现、步骤编号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong style="color: #2B2B2B;"><span leaf="">普通加粗强调</span></strong>
```

墨绿加粗（仅限关键锚点）：
```html
<strong style="color: #4A5D52;"><span leaf="">墨绿加粗，仅用于核心概念/步骤/CTA</span></strong>
```

### 7b. 浅墨绿底深字标签

> 极浅墨绿底 + 深墨绿字，低调不刺眼。用于核心概念（每篇 2~4 个）。

```html
<span style="background: #EEF3F0;color: #3D5046;padding: 2px 6px;border-radius: 2px;font-weight: 600;font-size: 14px;"><span leaf="">关键词标签</span></span>
```

### 7c. 留空（本风格不设此变体，保持克制）

> 本风格不设浅色背景高亮块——色块与禅意留白气质相悖。需要次要强调时，优先用 7d 下划线或 7a 普通加粗。

### 7d. 低饱和墨绿下划线 —— 最常用

> **本风格的标志性标记方式**。颜色为低饱和墨绿 `#B5C8BC`，1.5px 实线，温和克制，适合高频使用。

```html
<span style="border-bottom: 1.5px solid #B5C8BC;font-weight: 500;"><span leaf="">下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom: 26px;font-size: 15px;line-height: 1.9;text-align: justify;color: #525252;padding: 0 16px;">
  <span leaf="">这个时代的竞争，拼的不是速度，而是</span>
  <span style="border-bottom: 1.5px solid #B5C8BC;font-weight: 500;"><span leaf="">深度思考的能力</span></span>
  <span leaf="">。真正的高手，往往在别人仰望风口时，已经悄悄</span>
  <span style="border-bottom: 1.5px solid #B5C8BC;font-weight: 500;"><span leaf="">找到了下一片旷野</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 极浅墨绿荧光笔效果

> 底部 40% 极浅绿色高亮，偶尔用于长句强调，仍保持克制。

```html
<span style="background: linear-gradient(180deg, transparent 60%, #D6E4DC 60%);font-weight: 600;color: #2B2B2B;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用块（3 种变体）

### 8a. 居中衬线大字引用（核心金句，视觉焦点最强）

> 纯白底，上下各一条 1px 细线，衬线字体居中，大留白。这是禅意风最具特色的引用形式——不用色块，靠留白和字体传递力量。

```html
<section style="margin: 40px 16px;padding: 36px 20px;border-top: 1px solid #E8E8E8;border-bottom: 1px solid #E8E8E8;text-align: center;">
  <p style="font-family: 'Noto Serif SC', Georgia, 'Times New Roman', serif;font-size: 17px;font-weight: 600;color: #2B2B2B;margin: 0;line-height: 1.9;letter-spacing: 0.8px;">
    <span leaf="">「这里是核心金句，衬线字体 + 大留白 + 细线框定。」</span>
  </p>
</section>
```

### 8b. 左竖条轻量引用（次要旁注 / 补充说明）

> 极细左竖条（`#4A5D52`，2px），无底色，大 padding，适合旁注和补充说明。

```html
<section style="border-left: 2px solid #4A5D52;padding: 10px 20px 10px 20px;margin: 0 16px 30px;background: #FFFFFF;">
  <p style="font-size: 14px;color: #525252;margin: 0;line-height: 1.9;text-align: justify;">
    <span leaf="">旁注或补充说明内容，左侧细竖线划定边界，无色块，保持呼吸感。</span>
  </p>
</section>
```

### 8c. 极细线旁注（最轻量，几乎无存在感）

> 仅左侧 1px 浅灰线，字号稍小，颜色略淡，用于最轻量的旁注或个人感想。

```html
<section style="border-left: 1px solid #E8E8E8;padding: 8px 16px;margin: 0 16px 28px;">
  <p style="font-size: 13px;color: #A3A3A3;margin: 0;line-height: 1.9;text-align: justify;font-style: italic;">
    <span leaf="">极轻量旁注，颜色浅、字号小，几乎不打扰主文节奏。</span>
  </p>
</section>
```

---

## 组件 9 提示块（左竖条 + 小标签 + 大留白）

> 用墨绿左竖条 + 「提示」小标签区分，无色块底色。保持留白气质，不用醒目色块警示。

```html
<section style="margin: 0 16px 32px;padding: 18px 20px;border-left: 2px solid #4A5D52;">
  <p style="font-size: 10px;color: #4A5D52;font-weight: 600;letter-spacing: 2px;margin: 0 0 8px;text-transform: uppercase;">
    <span leaf="">NOTE</span>
  </p>
  <p style="font-size: 14px;color: #525252;margin: 0;line-height: 1.9;">
    <span leaf="">这里是重要提示或核心结论，用小标签「NOTE」区分，不用色块。</span>
  </p>
</section>
```

---

## 组件 10 图片容器

```html
<section style="margin: 0 16px 10px;border: 1px solid #E8E8E8;">
  <section style="margin: 0;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width: 100%;display: block;"></span>
  </section>
</section>
```

图片 + 说明文字配合（说明文字用辅助色，居中，大留白）：

```html
<section style="margin: 0 16px 8px;border: 1px solid #E8E8E8;">
  <section style="margin: 0;overflow: hidden;">
    <span leaf=""><img src="图片URL" style="max-width: 100%;display: block;"></span>
  </section>
</section>
<p style="font-size: 12px;color: #A3A3A3;text-align: center;margin: 8px 16px 32px;letter-spacing: 0.5px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 11 加粗结论段落

```html
<p style="margin-bottom: 26px;font-size: 15px;line-height: 1.9;text-align: justify;font-weight: 600;color: #2B2B2B;padding: 0 16px;">
  <span leaf="">加粗的结论性短句，字色加深到近黑，靠字重而非色彩传达重量。</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom: 26px;font-size: 15px;line-height: 1.9;text-align: justify;font-weight: 600;color: #2B2B2B;padding: 0 16px;">
  <span style="background: linear-gradient(180deg, transparent 60%, #D6E4DC 60%);"><span leaf="">荧光笔标记的结论句，极浅墨绿底，克制温柔。</span></span>
</p>
```

---

## 组件 12 数据/要点卡片组

### 两列版（用细线边框替代色块）

```html
<section style="display: flex;margin: 0 16px 32px;">
  <section style="flex: 1;border: 1px solid #E8E8E8;padding: 24px 16px;margin-right: 12px;text-align: center;">
    <p style="font-family: 'Noto Serif SC', Georgia, 'Times New Roman', serif;font-size: 32px;font-weight: 700;color: #2B2B2B;margin: 0 0 8px;line-height: 1;"><span leaf="">14亿</span></p>
    <p style="font-size: 11px;color: #A3A3A3;margin: 0;letter-spacing: 1px;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex: 1;border: 1px solid #E8E8E8;padding: 24px 16px;text-align: center;">
    <p style="font-family: 'Noto Serif SC', Georgia, 'Times New Roman', serif;font-size: 32px;font-weight: 700;color: #2B2B2B;margin: 0 0 8px;line-height: 1;"><span leaf="">3步</span></p>
    <p style="font-size: 11px;color: #A3A3A3;margin: 0;letter-spacing: 1px;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 要点列表版（竖排，细线分隔）

```html
<section style="margin: 0 16px 32px;border-top: 1px solid #E8E8E8;">
  <section style="display: flex;align-items: baseline;padding: 16px 0;border-bottom: 1px solid #E8E8E8;">
    <p style="font-size: 11px;color: #4A5D52;font-weight: 600;letter-spacing: 1px;margin: 0;min-width: 28px;"><span leaf="">01</span></p>
    <p style="font-size: 14px;color: #2B2B2B;margin: 0;line-height: 1.7;padding-left: 12px;"><span leaf="">要点一：简明扼要的核心内容</span></p>
  </section>
  <section style="display: flex;align-items: baseline;padding: 16px 0;border-bottom: 1px solid #E8E8E8;">
    <p style="font-size: 11px;color: #4A5D52;font-weight: 600;letter-spacing: 1px;margin: 0;min-width: 28px;"><span leaf="">02</span></p>
    <p style="font-size: 14px;color: #2B2B2B;margin: 0;line-height: 1.7;padding-left: 12px;"><span leaf="">要点二：简明扼要的核心内容</span></p>
  </section>
  <section style="display: flex;align-items: baseline;padding: 16px 0;border-bottom: 1px solid #E8E8E8;">
    <p style="font-size: 11px;color: #4A5D52;font-weight: 600;letter-spacing: 1px;margin: 0;min-width: 28px;"><span leaf="">03</span></p>
    <p style="font-size: 14px;color: #2B2B2B;margin: 0;line-height: 1.7;padding-left: 12px;"><span leaf="">要点三：简明扼要的核心内容</span></p>
  </section>
</section>
```

---

## 组件 13 标签胶囊

### 浅墨绿底深字（默认）

```html
<span style="display: inline-block;background: #EEF3F0;color: #3D5046;font-size: 11px;font-weight: 600;padding: 2px 10px;border-radius: 2px;margin-right: 6px;letter-spacing: 0.5px;"><span leaf="">标签名</span></span>
```

### 细线描边（轻量，更透气）

```html
<span style="display: inline-block;border: 1px solid #B5C8BC;color: #4A5D52;font-size: 11px;font-weight: 500;padding: 2px 10px;border-radius: 2px;margin-right: 6px;letter-spacing: 0.5px;"><span leaf="">标签名</span></span>
```

---

## 组件 14 END 结尾分割线

> 居中极细线 + 「END」字样，低调收尾。墨绿细线 + 小号字母，不用渐变装饰。

```html
<section style="padding: 0 16px;">
  <section style="text-align: center;margin: 48px 0 40px;">
    <section style="display: flex;align-items: center;justify-content: center;">
      <span style="height: 1px;width: 48px;background: #E8E8E8;margin-right: 16px;"></span>
      <span style="font-size: 10px;color: #A3A3A3;letter-spacing: 4px;font-weight: 400;"><span leaf="">END</span></span>
      <span style="height: 1px;width: 48px;background: #E8E8E8;margin-left: 16px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部作者签名区

```html
<section style="padding: 0 16px 40px;">
  <p style="margin-bottom: 26px;font-size: 15px;line-height: 1.9;text-align: justify;color: #525252;">
    <span leaf="">我是 {{作者名}}，{{一句话简介，如：热衷于分享 AI 观察与干货}}。</span>
  </p>
  <p style="margin-bottom: 26px;font-size: 15px;line-height: 1.9;text-align: justify;color: #525252;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color: #4A5D52;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见。</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width: 677px;margin: 0 auto;background: #FFFFFF;font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;color: #525252;line-height: 1.9;letter-spacing: 0.3px;overflow-x: hidden;">

  <!-- 1. 开头引言卡片（纯白 + 上下细线 + 衬线大字） -->
  <!-- 组件 2 -->

  <!-- 2. 前言正文（开场白） -->
  <section style="padding: 0 0 20px;">
    <!-- 组件 6 正文段落 × N -->
  </section>

  <!-- 3. 目录导读 -->
  <!-- 组件 3 极简目录 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件 4 1px 极细线 -->

  <!-- 5. 第一章 -->
  <!-- 组件 5（编号 01 · CHAPTER ONE + 衬线大标题 + 短墨绿线） -->
  <!--   组件 6 正文 + 组件 7 高亮 + 组件 8 引用 + 组件 9 提示 + 组件 10 图片 + 组件 12 数据卡片 -->

  <!-- 6. 章节分割线 -->

  <!-- 7. 第二章 -->
  <!-- 组件 5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- 8. 章节分割线 -->

  <!-- 9. 结语章节 -->
  <!-- 组件 5（∞ · POSTSCRIPT 变体） -->

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
| **锚点层** | 墨绿加粗 `color:#4A5D52` | 核心概念首次出现、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 低饱和墨绿下划线 `#B5C8BC` | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 细线 + 大留白 / 左竖条 / 小标签 | 引用、旁注、提示 | 按需 |

**克制原则**：
- 墨绿色（`#4A5D52`）**全文出现频率极低**：仅用于编号小字、章节短线、竖条、加粗锚点、CTA
- 不用色块底色——引用/提示统一用细线 + 大留白 + 类型小标签，无背景色
- 数据卡片用细线边框而非色块，数字用衬线字体提气质
- 所有圆角极小（2px）或不用圆角——方形细线更符合禅意气质

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方。本主题以留白为魂：**核心组件之外尽量少加东西**，一篇文章点缀组件种类 ≤2。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 观点/深度随笔（本主题最佳场景） | 正文 6 + 居中衬线引用 8a + 加粗结论段 11 | 极细线旁注 8c |
| 生活/情感/禅意冥想 | 正文 6 + 居中衬线引用 8a | 左竖条引用 8b |
| 读书笔记/知识整理 | 正文 6 + 要点列表 12 + 浅墨绿标签 7b | 提示块 9 |
| 教程/清单（弱契合，建议换主题） | 正文 6 + 要点列表 12 + 提示块 9 | 数据卡片 12 |
| 访谈/人物特稿 | 正文 6 + 左竖条引用 8b（引语）+ 居中衬线引用 8a（金句） | 极细线旁注 8c |
| 数据复盘 | 正文 6 + 数据卡片组 12 | 加粗结论段 11 |

所有类型共用固定结构：引言卡 2 + 目录 3 + 章节标题 5 + 分割线 4 + END 14 + 签名 15。教程、盘点、强运营类内容与本主题气质不符，选主题时应主动提示用户换摸鱼绿等信息密度更高的主题。

---

## Markdown → 留白禅意风排版映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 纯白细线引言卡片 | 文章开头，衬线大字居中 |
| `## 章节标题` | 组件 5 章节标题 | 小号墨绿英文 + 衬线中文 + 短细线，编号 01/02/03，结语用 ∞ |
| 普通段落 | 组件 6 正文段落 | 默认样式，主动标记关键词下划线 |
| `**加粗文字**` | 组件 7a 普通加粗（默认）或墨绿加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 浅墨绿底深字标签 | 核心概念 |
| `<u>下划线</u>` | 组件 7d 低饱和墨绿下划线 | 1.5px `#B5C8BC` |
| `~~荧光笔~~` | 组件 7e 极浅墨绿荧光笔 | 底部半高亮，偶尔用 |
| `> 引用段落`（金句） | 组件 8a 居中衬线细线引用 | 核心金句，衬线居中最有力 |
| `> 引用段落`（旁注） | 组件 8b 左竖条轻量引用 | 补充说明 |
| 极轻量旁注 | 组件 8c 极细线旁注 | 个人感想，字色最浅 |
| `!> 提示文字` | 组件 9 提示块 | 墨绿左竖条 + NOTE 小标签 |
| `![](图片)` | 组件 10 图片容器 | 细线边框，有说明才加说明 |
| 数据展示 | 组件 12 数据卡片组 | 衬线大号数字，细线边框 |
| 要点列表 | 组件 12 要点列表版 | 竖排，编号 + 细线分隔 |
| 行内标签 | 组件 13 标签胶囊 | 浅墨绿底为默认，描边为轻量 |
| `---` | 组件 4 章节分割线 | 1px 极细线 + 64px 留白 |
| 文末 | 组件 14 + 15 | END 细线 + 签名 |
