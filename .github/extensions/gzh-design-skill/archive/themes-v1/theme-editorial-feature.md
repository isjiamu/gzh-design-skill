# 甲木公众号排版组件库 —— 杂志特稿风（Editorial）

> **使用说明**：本组件库为「杂志特稿风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：高级印刷杂志 / 深度特稿。超大号衬线主标题，首字下沉感，章节上方栏目线 + 栏目名，赭金色细节，强烈的纸质印刷质感与文学气息。
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
主色调（墨黑）：      #1A1A1A（大标题 / 超强锚点）
点缀色（赭金）：      #A87C4F（编号 / 栏目线 / 竖条 / 首字下沉）
点缀色浅：           #C4A47A（金色浅变体，渐变尾色）
点缀色极浅：         #EFE4D3（金色 tint，卡片浅底）
背景色（米白）：      #FBF9F4（全局容器底）
正文色：             #2D2A26（正文段落）
辅助色：             #8A8275（图注 / 时间 / 辅助标签）
分割线色：           #DDD6C9（细线 / 卡片边框）
衬线字体（标题）：   'Noto Serif SC', 'Songti SC', Georgia, serif
正文字体（无衬线）：  -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif
正文字号：           15px
行高：               1.85
字间距（正文）：      0.5px
字间距（标题）：      1px ~ 3px
内容区边距：         0 12px（左右各 12px）
```

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#FBF9F4;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#2D2A26;line-height:1.85;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡（米白底 + 大号衬线斜体 + 左赭金竖线）

> 米白底卡片 + 左侧赭金粗竖线 + 大号衬线斜体金句 + 右下署名。气质沉稳、有杂志报头感。

```html
<section style="margin:16px 12px 36px;background:#FBF9F4;border-radius:2px;border-left:4px solid #A87C4F;padding:28px 28px 22px 30px;box-shadow:0 2px 12px -2px rgba(168,124,79,0.10);">
  <p style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:18px;font-style:italic;font-weight:400;color:#1A1A1A;margin:0 0 18px;line-height:1.9;letter-spacing:1px;">
    <span leaf="">「这里填写文章核心金句——一句话道出全文精髓，令读者停留。」</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#8A8275;margin:0;letter-spacing:2px;font-family:'Noto Serif SC','Songti SC',Georgia,serif;">
    <span leaf="">—— 作者名（按文章作者/主题而定）</span>
  </p>
</section>
```

**效果**：左侧赭金竖线锚定视线，衬线斜体营造印刷杂志的文学质感，无多余装饰。

---

## 组件 3 前言导读区域（栏目线 + 三列目录卡）

> 顶部赭金栏目线 + 英文小标签「CONTENTS」+ 三列米白卡片目录。

```html
<section style="padding:0 12px 36px;">
  <!-- 栏目线 + 栏目名 -->
  <section style="display:flex;align-items:center;margin-bottom:20px;">
    <span style="display:inline-block;width:32px;height:2px;background:#A87C4F;margin-right:10px;"></span>
    <span style="font-size:10px;color:#A87C4F;letter-spacing:4px;font-weight:700;font-family:'Noto Serif SC','Songti SC',Georgia,serif;text-transform:uppercase;"><span leaf="">CONTENTS</span></span>
    <span style="flex:1;height:1px;background:#DDD6C9;margin-left:10px;"></span>
  </section>
  <!-- 三列目录卡 -->
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#FBF9F4;border:1px solid #DDD6C9;border-radius:2px;padding:18px 14px;margin-right:8px;text-align:center;">
      <p style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:20px;font-weight:700;color:#A87C4F;margin:0 0 8px;line-height:1;"><span leaf="">01</span></p>
      <p style="font-size:12px;font-weight:600;color:#1A1A1A;margin:0;line-height:1.6;letter-spacing:0.5px;"><span leaf="">第一个看点</span></p>
    </section>
    <section style="flex:1;background:#FBF9F4;border:1px solid #DDD6C9;border-radius:2px;padding:18px 14px;margin-right:8px;text-align:center;">
      <p style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:20px;font-weight:700;color:#A87C4F;margin:0 0 8px;line-height:1;"><span leaf="">02</span></p>
      <p style="font-size:12px;font-weight:600;color:#1A1A1A;margin:0;line-height:1.6;letter-spacing:0.5px;"><span leaf="">第二个看点</span></p>
    </section>
    <section style="flex:1;background:#FBF9F4;border:1px solid #DDD6C9;border-radius:2px;padding:18px 14px;text-align:center;">
      <p style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:20px;font-weight:700;color:#A87C4F;margin:0 0 8px;line-height:1;"><span leaf="">03</span></p>
      <p style="font-size:12px;font-weight:600;color:#1A1A1A;margin:0;line-height:1.6;letter-spacing:0.5px;"><span leaf="">第三个看点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（赭金渐变细线）

```html
<section style="padding:0 12px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#A87C4F,#C4A47A,#A87C4F,transparent);margin:0 0 2px;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题（栏目线 + 英文栏目名 + 衬线大编号 + 衬线大标题）

> 上方赭金细栏目线 + 英文栏目名（小字母间距）+ 衬线大号赭金编号 + 衬线大字中文章节标题。这是本主题最具识别性的核心组件。

```html
<section style="margin-top:52px;margin-bottom:28px;padding:0 12px;">
  <!-- 顶部栏目线 + 英文栏目名 -->
  <section style="display:flex;align-items:center;margin-bottom:16px;">
    <span style="display:inline-block;width:24px;height:2px;background:#A87C4F;margin-right:10px;"></span>
    <span style="font-size:10px;color:#A87C4F;letter-spacing:4px;font-weight:700;text-transform:uppercase;font-family:'Noto Serif SC','Songti SC',Georgia,serif;"><span leaf="">CHAPTER ONE</span></span>
    <span style="flex:1;height:1px;background:#DDD6C9;margin-left:10px;"></span>
  </section>
  <!-- 衬线大编号 + 衬线大标题 -->
  <section style="display:flex;align-items:baseline;">
    <span style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:36px;font-weight:700;color:#A87C4F;margin-right:14px;line-height:1;letter-spacing:0;"><span leaf="">01</span></span>
    <h3 style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:22px;font-weight:700;color:#1A1A1A;margin:0;line-height:1.4;letter-spacing:1px;">
      <span leaf="">中文章节标题</span>
    </h3>
  </section>
  <!-- 标题下方细分割线 -->
  <section style="height:1px;background:#DDD6C9;margin-top:14px;"></section>
</section>
```

**结语章节变体**（编号用 ∞，英文标签用 EPILOGUE）：

```html
<section style="margin-top:52px;margin-bottom:28px;padding:0 12px;">
  <section style="display:flex;align-items:center;margin-bottom:16px;">
    <span style="display:inline-block;width:24px;height:2px;background:#A87C4F;margin-right:10px;"></span>
    <span style="font-size:10px;color:#A87C4F;letter-spacing:4px;font-weight:700;text-transform:uppercase;font-family:'Noto Serif SC','Songti SC',Georgia,serif;"><span leaf="">EPILOGUE</span></span>
    <span style="flex:1;height:1px;background:#DDD6C9;margin-left:10px;"></span>
  </section>
  <section style="display:flex;align-items:baseline;">
    <span style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:36px;font-weight:700;color:#A87C4F;margin-right:14px;line-height:1;letter-spacing:0;"><span leaf="">∞</span></span>
    <h3 style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:22px;font-weight:700;color:#1A1A1A;margin:0;line-height:1.4;letter-spacing:1px;">
      <span leaf="">结语章节标题</span>
    </h3>
  </section>
  <section style="height:1px;background:#DDD6C9;margin-top:14px;"></section>
</section>
```

**英文栏目名参考**（据中文章节主题替换）：

| 章节主题 | 英文栏目名 |
|---|---|
| 背景 / 起源 | ORIGIN |
| 现状 / 分析 | ANALYSIS |
| 方法 / 实践 | PRACTICE |
| 洞察 / 思考 | INSIGHT |
| 结论 / 总结 | SUMMARY |
| 案例 | CASE STUDY |
| 访谈 | INTERVIEW |
| 结语 / 尾声 | EPILOGUE |

---

## 组件 6 正文段落

> **关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**赭金下划线（7d）**进行标记。这是本风格的核心正文标记方式。

**基础段落**：

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.85;text-align:justify;color:#2D2A26;letter-spacing:0.5px;">
  <span leaf="">正文内容，15px 字号，1.85 倍行高，两端对齐。正文底色为米白，与墨黑文字形成印刷质感对比。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.85;text-align:justify;color:#2D2A26;letter-spacing:0.5px;">
  <span leaf="">正文内容的前半部分，引出核心概念，逐渐推进到</span>
  <span style="border-bottom:2px solid #A87C4F;font-weight:600;color:#1A1A1A;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述延伸内容。</span>
</p>
```

**首字下沉变体**（仅用于全文第一段，首字 60px+ 衬线赭金，inline 放大）：

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.85;text-align:justify;color:#2D2A26;letter-spacing:0.5px;">
  <span style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:62px;font-weight:700;color:#A87C4F;line-height:0.85;margin-right:4px;vertical-align:bottom;"><span leaf="">这</span></span><span leaf="">是正文第一段的首字下沉效果。首字用衬线赭金放大，其余文字正常排列，营造高级印刷杂志的阅读入口感。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字，太短没意义，太长失去焦点
- 如果一段没有特别重要的内容，可以不标

---

## 组件 7 正文高亮样式（5 种变体 + 使用策略）

> **核心设计理念**：克制用金，赭金只在真正需要的锚点出现。
>
> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 赭金下划线** —— 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 赭金加粗** —— 普通加粗为主，赭金加粗仅用于极少数锚点
> 3. **7b 金底深字标签** —— 核心概念标签（每篇 2~4 个）
> 4. **7c 米白背景淡底高亮** —— 次要关键词补充
> 5. **7e 荧光笔** —— 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，绝大部分加粗使用此样式。**赭金加粗**仅用于极少数关键锚点（产品名、步骤编号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong style="color:#1A1A1A;"><span leaf="">普通加粗强调</span></strong>
```

赭金加粗（仅限关键锚点）：
```html
<strong style="color:#A87C4F;font-family:'Noto Serif SC','Songti SC',Georgia,serif;"><span leaf="">赭金加粗，仅用于产品名/步骤/CTA</span></strong>
```

### 7b. 金底深字标签

> 极浅金底 + 赭金边框 + 深字，用于核心概念（每篇 2~4 个）

```html
<span style="background:#EFE4D3;color:#7A5832;padding:2px 7px;border-radius:2px;font-weight:700;border:1px solid #C4A47A;"><span leaf="">核心概念标签</span></span>
```

### 7c. 米白淡底高亮

> 比正文背景略深的米色底，轻量标注，适用于次要关键词

```html
<span style="background:#EFE4D3;padding:1px 6px;border-radius:2px;font-weight:600;color:#2D2A26;"><span leaf="">淡底关键词</span></span>
```

### 7d. 赭金下划线 —— 最常用

> **本风格的标志性标记方式**。颜色为赭金 `#A87C4F`，沉稳不刺眼，适合高频使用。

```html
<span style="border-bottom:2px solid #A87C4F;font-weight:600;color:#1A1A1A;"><span leaf="">赭金下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.85;text-align:justify;color:#2D2A26;letter-spacing:0.5px;">
  <span leaf="">深度阅读正在式微，但真正有价值的内容依然稀缺。我们需要的不是</span>
  <span style="border-bottom:2px solid #A87C4F;font-weight:600;color:#1A1A1A;"><span leaf="">更多内容</span></span>
  <span leaf="">，而是</span>
  <span style="border-bottom:2px solid #A87C4F;font-weight:600;color:#1A1A1A;"><span leaf="">更好的判断力</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 荧光笔效果

> 底部 40% 金色高亮，偶尔用于长句强调

```html
<span style="background:linear-gradient(180deg,transparent 60%,#EFE4D3 60%);font-weight:700;color:#1A1A1A;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用块（3 种变体）

### 8a. 大号衬线左竖条引用（视觉焦点最强）

> 米白底 + 左侧赭金粗竖线 + 大号衬线斜体正文，用于核心金句。这是本主题最具文学质感的引用方式。

```html
<section style="background:#FBF9F4;border-left:4px solid #A87C4F;border-radius:0 4px 4px 0;padding:22px 26px;margin-bottom:28px;box-shadow:2px 0 0 0 #EFE4D3 inset;">
  <p style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:17px;font-style:italic;font-weight:400;color:#1A1A1A;margin:0;line-height:1.9;letter-spacing:0.8px;">
    <span leaf="">「这里是核心观点或关键金句，衬线斜体令文字自带气质，适合点睛之笔。」</span>
  </p>
</section>
```

### 8b. 浅金底内容引用块（资料/段落型）

> 极浅金底 + 细描边，用于展示摘录、资料引用、数据来源等段落内容

```html
<section style="background:#EFE4D3;border-radius:4px;padding:18px 22px;margin-bottom:28px;border:1px solid #DDD6C9;">
  <p style="font-size:14px;color:#2D2A26;margin:0;line-height:1.85;text-align:justify;letter-spacing:0.5px;">
    <span leaf="">浅金底引用内容，适合引用资料段落、他人观点摘录，</span>
    <span style="border-bottom:2px solid #A87C4F;font-weight:600;color:#1A1A1A;"><span leaf="">关键句同样可以用赭金下划线</span></span>
    <span leaf="">标记重点。</span>
  </p>
</section>
```

### 8c. 灰色左竖条旁注（轻量旁注）

> 细灰线竖条 + 辅助色文字，用于轻量旁注、括注说明、作者按语

```html
<section style="border-left:3px solid #DDD6C9;padding:12px 20px;margin-bottom:24px;">
  <p style="font-size:13px;color:#8A8275;margin:0;line-height:1.8;text-align:justify;font-style:italic;">
    <span leaf="">轻量旁注内容，灰竖线不抢戏，用于编者按、括注说明或作者额外补充。</span>
  </p>
</section>
```

---

## 组件 9 提示块

> 极浅金底 + 赭金左竖线 + 「提示」小标签 + 深字，用于重要提醒或核心结论

```html
<section style="background:#EFE4D3;border-left:4px solid #A87C4F;border-radius:0 4px 4px 0;padding:14px 20px;margin-bottom:26px;">
  <p style="font-size:12px;font-weight:700;color:#A87C4F;margin:0 0 6px;letter-spacing:2px;text-transform:uppercase;font-family:'Noto Serif SC','Songti SC',Georgia,serif;">
    <span leaf="">NOTE</span>
  </p>
  <p style="font-size:14px;font-weight:600;color:#1A1A1A;margin:0;line-height:1.8;">
    <span leaf="">这里是重要提示或核心结论，用赭金标签点出类型，内容简明扼要。</span>
  </p>
</section>
```

---

## 组件 10 图片容器（配衬线图注）

```html
<section style="background:#FBF9F4;border-radius:2px;padding:4px;border:1px solid #DDD6C9;box-shadow:0 4px 14px -2px rgba(26,26,26,0.08);margin-bottom:10px;">
  <section style="margin:0;border-radius:1px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;display:block;"></span>
  </section>
</section>
```

图片 + 衬线图注配合时：

```html
<section style="background:#FBF9F4;border-radius:2px;padding:4px;border:1px solid #DDD6C9;box-shadow:0 4px 14px -2px rgba(26,26,26,0.08);margin-bottom:8px;">
  <section style="margin:0;border-radius:1px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;display:block;"></span>
  </section>
</section>
<p style="font-size:12px;color:#8A8275;text-align:center;margin:0 0 26px;letter-spacing:1px;font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-style:italic;">
  <span leaf="">▲ 衬线斜体图注说明文字</span>
</p>
```

---

## 组件 11 加粗正文段落

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.85;text-align:justify;font-weight:700;color:#1A1A1A;letter-spacing:0.5px;">
  <span leaf="">加粗的结论性短句，适合用在段落末尾或章节收束处。</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom:22px;font-size:15px;line-height:1.85;text-align:justify;font-weight:700;color:#1A1A1A;letter-spacing:0.5px;">
  <span style="background:linear-gradient(180deg,transparent 60%,#EFE4D3 60%);"><span leaf="">荧光笔标记的加粗结论句</span></span>
</p>
```

---

## 组件 12 数据 / 要点卡片组

### 两列版（数据型）

```html
<section style="display:flex;margin-bottom:28px;padding:0;">
  <section style="flex:1;background:#FBF9F4;border:1px solid #DDD6C9;border-radius:2px;padding:20px 16px;margin-right:8px;text-align:center;">
    <p style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:30px;font-weight:700;color:#A87C4F;margin:0 0 6px;line-height:1;letter-spacing:0;"><span leaf="">14亿</span></p>
    <p style="font-size:11px;color:#8A8275;margin:0;letter-spacing:1px;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#FBF9F4;border:1px solid #DDD6C9;border-radius:2px;padding:20px 16px;text-align:center;">
    <p style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:30px;font-weight:700;color:#A87C4F;margin:0 0 6px;line-height:1;letter-spacing:0;"><span leaf="">3步</span></p>
    <p style="font-size:11px;color:#8A8275;margin:0;letter-spacing:1px;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 要点列表卡（单列带编号）

```html
<section style="background:#FBF9F4;border:1px solid #DDD6C9;border-radius:2px;padding:20px 22px;margin-bottom:28px;">
  <section style="display:flex;align-items:baseline;margin-bottom:14px;">
    <span style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:16px;font-weight:700;color:#A87C4F;margin-right:12px;min-width:24px;"><span leaf="">①</span></span>
    <p style="font-size:14px;color:#2D2A26;margin:0;line-height:1.8;"><span leaf="">第一个要点内容，简洁说明核心价值。</span></p>
  </section>
  <section style="display:flex;align-items:baseline;margin-bottom:14px;">
    <span style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:16px;font-weight:700;color:#A87C4F;margin-right:12px;min-width:24px;"><span leaf="">②</span></span>
    <p style="font-size:14px;color:#2D2A26;margin:0;line-height:1.8;"><span leaf="">第二个要点内容，与上条保持平行结构。</span></p>
  </section>
  <section style="display:flex;align-items:baseline;">
    <span style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:16px;font-weight:700;color:#A87C4F;margin-right:12px;min-width:24px;"><span leaf="">③</span></span>
    <p style="font-size:14px;color:#2D2A26;margin:0;line-height:1.8;"><span leaf="">第三个要点内容，收尾可略带总结语气。</span></p>
  </section>
</section>
```

---

## 组件 13 标签胶囊

### 赭金描边（默认）

```html
<span style="display:inline-block;border:1px solid #A87C4F;color:#A87C4F;font-size:11px;font-weight:600;padding:2px 10px;border-radius:2px;margin-right:6px;letter-spacing:1px;"><span leaf="">标签名</span></span>
```

### 金底深字（强调型）

```html
<span style="display:inline-block;background:#EFE4D3;color:#7A5832;font-size:11px;font-weight:700;padding:2px 10px;border-radius:2px;margin-right:6px;border:1px solid #C4A47A;letter-spacing:1px;"><span leaf="">强调标签</span></span>
```

### 墨黑底白字（最强锚点，每篇 ≤ 2 个）

```html
<span style="display:inline-block;background:#1A1A1A;color:#FBF9F4;font-size:11px;font-weight:700;padding:2px 10px;border-radius:2px;margin-right:6px;letter-spacing:1px;"><span leaf="">核心标签</span></span>
```

---

## 组件 14 END 结尾分割线

```html
<section style="padding:0 12px;">
  <section style="text-align:center;margin:0 0 36px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:50px;background:linear-gradient(to right,transparent,#A87C4F);margin-right:14px;"></span>
      <span style="font-family:'Noto Serif SC','Songti SC',Georgia,serif;font-size:12px;color:#A87C4F;letter-spacing:5px;font-weight:400;"><span leaf="">· END ·</span></span>
      <span style="height:1px;width:50px;background:linear-gradient(to left,transparent,#A87C4F);margin-left:14px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部签名区

```html
<section style="padding:0 12px;">
  <p style="margin-bottom:20px;font-size:15px;line-height:1.85;text-align:justify;color:#2D2A26;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察，AI 干货内容</span>
  </p>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.85;text-align:justify;color:#2D2A26;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#A87C4F;font-family:'Noto Serif SC','Songti SC',Georgia,serif;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#FBF9F4;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#2D2A26;line-height:1.85;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 开头引言卡（米白底 + 左赭金竖线 + 衬线斜体金句） -->
  <!-- 组件 2 -->

  <!-- 2. 前言正文（开场白，首段用首字下沉变体） -->
  <section style="padding:0 12px 20px;">
    <!-- 组件 6 首字下沉变体 -->
    <!-- 组件 6 正文段落 x N -->
  </section>

  <!-- 3. 目录导读 -->
  <!-- 组件 3 栏目线 + 三列目录卡 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件 4 赭金渐变细线 -->

  <!-- 5. 第一章 -->
  <!-- 组件 5（栏目线 + CHAPTER ONE + 编号 01 + 衬线大标题） -->
  <!--   组件 6 正文 + 组件 7 高亮 + 组件 8 引用 + 组件 9 提示 + 组件 10 图片 + 组件 12 卡片 -->

  <!-- 6. 章节分割线 -->
  <!-- 组件 4 -->

  <!-- 7. 第二章 -->
  <!-- 组件 5（02） -->

  <!-- ... 更多章节 ... -->

  <!-- 8. 章节分割线 -->
  <!-- 组件 4 -->

  <!-- 9. 结语章节 -->
  <!-- 组件 5（∞ 变体 + EPILOGUE） -->

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
| **锚点层** | 赭金加粗 `color:#A87C4F` / 墨黑底白字胶囊 | 产品名、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 赭金下划线 `#A87C4F` | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 左竖条 + 浅底 / 小标签 | 引用、旁注、提示 | 按需 |

**克制原则**：
- 墨黑底白字胶囊（组件 13 强调型）**全篇 ≤ 2 个**，极致锚点专用
- 赭金加粗全文不超过 5 处
- 引用 / 提示统一用左竖条 + 浅底，不用四周虚线框（dashed）
- 渐变金色仅出现在分割线和 END 线
- 衬线字体集中在标题、编号、图注、END 线处，正文使用无衬线保持可读性

---

## Markdown → 杂志特稿排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 引言卡（米白底 + 左赭金竖线） | 文章开头的核心金句 |
| `## 章节标题` | 组件 5 章节标题 | 栏目线 + 英文栏目名 + 衬线编号 01/02/03，结语用 ∞ + EPILOGUE |
| 普通段落（首段） | 组件 6 首字下沉变体 | 首字 62px 衬线赭金，仅全文第一段使用 |
| 普通段落 | 组件 6 正文段落 | 默认样式，主动标记赭金下划线关键词 |
| `**加粗文字**` | 组件 7a 普通加粗（默认）或赭金加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 金底深字标签 | 核心概念 |
| `<u>下划线</u>` | 组件 7d 赭金下划线 | 2px `#A87C4F` |
| `> 引用段落`（金句） | 组件 8a 大号衬线左竖条 | 衬线斜体核心金句 |
| `> 引用段落`（旁注） | 组件 8c 灰竖条旁注 | 轻量旁注 |
| `!> 提示文字` | 组件 9 提示块 | 极浅金底 + 赭金竖线 + NOTE 标签 |
| `![](图片)` | 组件 10 图片容器 | 细描边卡片 + 衬线斜体图注 |
| 数据展示 | 组件 12 两列数据卡 | 衬线大号赭金数据 |
| 要点列表 | 组件 12 要点列表卡 | 衬线圆圈编号 ①②③ |
| 行内标签 | 组件 13 赭金描边胶囊 | 赭金描边为默认 |
| `---` | 组件 4 章节分割线 | 赭金渐变细线 |
| 文末 | 组件 14 + 15 | END 线 + 签名 |
