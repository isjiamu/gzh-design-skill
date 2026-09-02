# 甲木公众号排版组件库 —— 数据信息图风（Infographic / Report）

> **使用说明**：本组件库为「数据信息图风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：数据复盘 / 年度报告 / 增长分析。超大号 KPI 数字、占比进度条、统计卡片网格、多色维度区分、图表感。信息密度高但清爽。
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
主色调：         #0891B2（青蓝）
数据橙：         #F97316（橙色维度）
数据绿：         #10B981（绿色维度）
数据紫：         #8B5CF6（紫色维度）
数据玫红：       #EC4899（玫红维度）
浅底背景：       #F8FAFC
卡片底色：       #FFFFFF
标题色：         #0F172A（近黑）
正文色：         #475569（中深灰）
辅助文字色：     #94A3B8（浅灰）
细边颜色：       #E2E8F0
主色极浅底：     #ECFEFF（青蓝极浅）
主色浅底：       #CFFAFE（青蓝浅）
主色中：         #06B6D4（青蓝亮色）
正文字号：       15px
行高：           1.8
字间距：         0.5px
内容区边距：     0 10px（左右各 10px）
```

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#F8FAFC;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#475569;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（数据看板感 + 顶部迷你 KPI 行）

> 白底卡片 + 青蓝顶色条 + 顶部一行 3 个迷你 KPI 数据 + 引言大字 + 右下署名。无 dashed 框，圆角 12px。

```html
<section style="margin:10px 10px 32px;background:#FFFFFF;border-radius:12px;box-shadow:0 4px 24px -4px rgba(8,145,178,0.15);overflow:hidden;">
  <!-- 顶部青蓝色条 -->
  <section style="background:#0891B2;padding:12px 24px;">
    <!-- 迷你 KPI 行：3 个关键数据 -->
    <section style="display:flex;justify-content:space-between;align-items:center;">
      <section style="text-align:center;flex:1;">
        <p style="font-size:22px;font-weight:900;color:#FFFFFF;margin:0;line-height:1.1;">
          <span leaf="">数值1</span>
        </p>
        <p style="font-size:11px;color:rgba(255,255,255,0.8);margin:2px 0 0;letter-spacing:0.5px;">
          <span leaf="">指标标签</span>
        </p>
      </section>
      <section style="width:1px;height:36px;background:rgba(255,255,255,0.3);"></section>
      <section style="text-align:center;flex:1;">
        <p style="font-size:22px;font-weight:900;color:#FFFFFF;margin:0;line-height:1.1;">
          <span leaf="">数值2</span>
        </p>
        <p style="font-size:11px;color:rgba(255,255,255,0.8);margin:2px 0 0;letter-spacing:0.5px;">
          <span leaf="">指标标签</span>
        </p>
      </section>
      <section style="width:1px;height:36px;background:rgba(255,255,255,0.3);"></section>
      <section style="text-align:center;flex:1;">
        <p style="font-size:22px;font-weight:900;color:#FFFFFF;margin:0;line-height:1.1;">
          <span leaf="">数值3</span>
        </p>
        <p style="font-size:11px;color:rgba(255,255,255,0.8);margin:2px 0 0;letter-spacing:0.5px;">
          <span leaf="">指标标签</span>
        </p>
      </section>
    </section>
  </section>
  <!-- 引言正文区 -->
  <section style="padding:24px 24px 20px;">
    <p style="font-size:32px;color:#0891B2;font-weight:900;margin:0 0 4px;line-height:0.8;">
      <span leaf="">"</span>
    </p>
    <p style="font-size:16px;font-weight:700;color:#0F172A;margin:8px 0 12px;line-height:1.75;padding-left:4px;">
      <span style="background:#0891B2;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">核心关键词</span></span>
      <span leaf="">，不是数字本身，而是读懂</span>
      <span style="background:#0891B2;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">数字背后的趋势</span></span>
      <span leaf="">。</span>
    </p>
    <p style="text-align:right;font-size:12px;color:#94A3B8;margin:0;letter-spacing:1px;">
      <span leaf="">—— 作者名（按文章作者/主题而定）</span>
    </p>
  </section>
</section>
```

**效果**：顶部青蓝数据条 + 3 个迷你 KPI 白字数值，传递「年度报告/数据复盘」的看板感；下方引言区保留品牌感引号与关键词高亮。

---

## 组件 3 前言导读区域（数据看点卡片目录）

> 3 列目录卡片，青蓝渐变编号 + 深色标题 + 浅底卡片。

```html
<section style="padding:0 10px 32px;">
  <p style="font-size:14px;color:#94A3B8;margin:0 0 14px;letter-spacing:1px;">
    <span leaf="">📊 本期数据看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#FFFFFF;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E2E8F0;box-shadow:0 2px 8px -2px rgba(8,145,178,0.08);">
      <p style="display:inline-block;background:#0891B2;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#0F172A;margin:0;line-height:1.5;"><span leaf="">第一个看点</span></p>
    </section>
    <section style="flex:1;background:#FFFFFF;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #E2E8F0;box-shadow:0 2px 8px -2px rgba(8,145,178,0.08);">
      <p style="display:inline-block;background:#0891B2;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#0F172A;margin:0;line-height:1.5;"><span leaf="">第二个看点</span></p>
    </section>
    <section style="flex:1;background:#FFFFFF;border-radius:10px;padding:16px 12px;text-align:center;border:1px solid #E2E8F0;box-shadow:0 2px 8px -2px rgba(8,145,178,0.08);">
      <p style="display:inline-block;background:#0891B2;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#0F172A;margin:0;line-height:1.5;"><span leaf="">第三个看点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（青蓝渐变）

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#06B6D4,#0891B2,#06B6D4,transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题组件（带数据徽章 + 青蓝编号）

> 青蓝实底编号标签 + 英文小标签 + 中文大标题 + 可选数据徽章，底部青蓝线。

**标准版（带数据徽章）**：

```html
<section style="margin-top:48px;margin-bottom:28px;padding:0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #0891B2;">
    <section style="display:flex;align-items:center;">
      <span style="display:inline-block;background:#0891B2;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#0891B2;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size:18px;font-weight:800;color:#0F172A;margin:0;letter-spacing:0.5px;">
          <span leaf="">中文章节标题</span>
        </h3>
      </section>
    </section>
    <!-- 数据徽章（可选）：章节核心数据 -->
    <span style="display:inline-block;background:#ECFEFF;color:#0891B2;font-size:13px;font-weight:800;padding:4px 12px;border-radius:20px;border:1px solid #CFFAFE;white-space:nowrap;">
      <span leaf="">↑ 38%</span>
    </span>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**（编号用 ∞）：

```html
<span style="display:inline-block;background:#0891B2;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

**无徽章精简版**（不需要数据标注时）：

```html
<section style="margin-top:48px;margin-bottom:28px;padding:0 10px;">
  <section style="display:flex;align-items:center;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #0891B2;">
    <span style="display:inline-block;background:#0891B2;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">02</span></span>
    <section>
      <p style="font-size:10px;color:#0891B2;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
        <span leaf="">ENGLISH TAG</span>
      </p>
      <h3 style="font-size:18px;font-weight:800;color:#0F172A;margin:0;letter-spacing:0.5px;">
        <span leaf="">中文章节标题</span>
      </h3>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

---

## 组件 6 正文段落

> **关键规则**：每个正文段落主动识别 1~3 个**关键语句或关键词**，用**青蓝下划线（6d）**进行标记，让读者快速扫到每段重点。

**基础段落**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#475569;">
  <span leaf="">正文内容，15px 字号，1.8 倍行高，两端对齐。</span>
</p>
```

**带关键词下划线标记的段落（推荐默认使用）**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#475569;">
  <span leaf="">正文内容的前半部分，引出核心概念——</span>
  <span style="border-bottom:2px solid #06B6D4;font-weight:600;color:#0F172A;"><span leaf="">这是需要强调的关键语句</span></span>
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

> **核心设计理念**：多色维度区分，青蓝为主线，橙/绿/紫/玫红用于不同数据维度。

> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 青蓝下划线** —— 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 青蓝加粗** —— 普通加粗为主，青蓝加粗仅用于极少数锚点
> 3. **7b 青蓝浅底标签** —— 核心概念标签（每篇 2~4 个）
> 4. **7c 浅底背景高亮** —— 次要关键词补充
> 5. **7e 荧光笔** —— 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，绝大部分加粗使用此样式。**青蓝加粗**仅用于极少数关键锚点（如指标名、步骤编号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong><span leaf="">普通加粗强调</span></strong>
```

青蓝加粗（仅限关键锚点）：
```html
<strong style="color:#0891B2;"><span leaf="">青蓝加粗，仅用于指标名/步骤/CTA</span></strong>
```

### 7b. 青蓝浅底深色字标签

> 青蓝极浅背景 + 深青文字，用于核心概念（每篇 2~4 个）。

```html
<span style="background:#ECFEFF;color:#0E7490;padding:2px 6px;border-radius:3px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅底背景高亮

> 柔和的背景标注，适用于次要关键词。

```html
<span style="background:#CFFAFE;padding:1px 6px;border-radius:3px;font-weight:600;color:#0891B2;"><span leaf="">浅底背景关键词</span></span>
```

### 7d. 青蓝下划线 —— 最常用

> **本风格的标志性标记方式**。颜色为青蓝 `#06B6D4`，清晰有图表感，适合高频使用。

```html
<span style="border-bottom:2px solid #06B6D4;font-weight:600;color:#0F172A;"><span leaf="">青蓝下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#475569;">
  <span leaf="">数据驱动增长已进入下半场：上半场拼规模指标，下半场拼</span>
  <span style="border-bottom:2px solid #06B6D4;font-weight:600;color:#0F172A;"><span leaf="">转化效率与复购深度</span></span>
  <span leaf="">。真正的增长飞轮，不是流量，而是</span>
  <span style="border-bottom:2px solid #06B6D4;font-weight:600;color:#0F172A;"><span leaf="">用户留存与口碑裂变</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 荧光笔效果

> 底部 40% 青蓝浅高亮，偶尔用于长句强调。

```html
<span style="background:linear-gradient(180deg,transparent 60%,#CFFAFE 60%);font-weight:700;color:#0F172A;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用高亮块（3 种变体）

### 8a. 青蓝底左竖条金句引用（视觉焦点最强）

> 青蓝极浅底 + 青蓝左竖条，用于核心数据金句。

```html
<section style="background:#ECFEFF;border-radius:0 10px 10px 0;border-left:4px solid #0891B2;padding:18px 22px;margin-bottom:24px;">
  <p style="font-size:16px;font-weight:800;color:#0E7490;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心数据观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 浅底引用块（数据说明/背景内容）

> 浅底 + 细边框，用于展示数据来源说明、背景信息等。

```html
<section style="background:#F8FAFC;border-radius:10px;padding:18px 20px;margin-bottom:24px;border:1px solid #E2E8F0;">
  <p style="font-size:15px;color:#475569;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">背景说明内容，可以包含</span>
    <span style="border-bottom:2px solid #06B6D4;font-weight:600;color:#0F172A;"><span leaf="">下划线加粗的关键句</span></span>
  </p>
</section>
```

### 8c. 灰色左竖条引用（轻量旁注）

> 灰色左竖条，用于轻量旁注、数据来源标注等。

```html
<section style="border-left:4px solid #CBD5E1;padding:14px 20px;margin-bottom:24px;background:#F8FAFC;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#475569;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">轻量旁注内容，数据来源标注或补充说明</span>
  </p>
</section>
```

---

## 组件 9 提示/警示条

> 青蓝极浅底 + 青蓝左竖条 + 深青文字，用于数据结论、核心洞察提醒。

```html
<section style="background:#ECFEFF;border-left:4px solid #0891B2;border-radius:0 8px 8px 0;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:700;color:#0E7490;margin:0;line-height:1.8;">
    <span leaf="">💡 这里是数据洞察或核心结论</span>
  </p>
</section>
```

---

## 组件 10 图片容器

```html
<section style="background:#FFFFFF;border-radius:12px;padding:6px;border:1px solid #E2E8F0;box-shadow:0 4px 12px -2px rgba(8,145,178,0.08);margin-bottom:10px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时：

```html
<section style="background:#FFFFFF;border-radius:12px;padding:6px;border:1px solid #E2E8F0;box-shadow:0 4px 12px -2px rgba(8,145,178,0.08);margin-bottom:8px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
<p style="font-size:12px;color:#94A3B8;text-align:center;margin:0 0 24px;">
  <span leaf="">— 图片说明文字</span>
</p>
```

---

## 组件 11 加粗正文段落

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#0F172A;">
  <span leaf="">加粗的结论性短句</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#0F172A;">
  <span style="background:linear-gradient(180deg,transparent 60%,#CFFAFE 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

---

## 组件 12a KPI 大数字卡（核心特色组件）

> **本风格最具辨识度的组件**。48px+ 青蓝超大数字 + 指标标签 + 同比箭头小字。可单列或多列并排。

### 单个 KPI 卡（白底独立）

```html
<section style="background:#FFFFFF;border-radius:12px;padding:24px 20px;margin-bottom:16px;border:1px solid #E2E8F0;text-align:center;box-shadow:0 4px 16px -4px rgba(8,145,178,0.12);">
  <p style="font-size:52px;font-weight:900;color:#0891B2;margin:0;line-height:1;letter-spacing:-1px;">
    <span leaf="">2,847</span>
  </p>
  <p style="font-size:13px;color:#94A3B8;margin:8px 0 6px;letter-spacing:0.5px;">
    <span leaf="">月活跃用户数（人）</span>
  </p>
  <p style="font-size:12px;font-weight:700;color:#10B981;margin:0;">
    <span leaf="">↑ 同比 +38.6%</span>
  </p>
</section>
```

### 两列 KPI 卡组（并排对比）

```html
<section style="display:flex;margin-bottom:16px;">
  <section style="flex:1;background:#FFFFFF;border-radius:12px;padding:20px 16px;margin-right:8px;border:1px solid #E2E8F0;text-align:center;box-shadow:0 4px 16px -4px rgba(8,145,178,0.10);">
    <p style="font-size:44px;font-weight:900;color:#0891B2;margin:0;line-height:1;letter-spacing:-1px;">
      <span leaf="">87%</span>
    </p>
    <p style="font-size:12px;color:#94A3B8;margin:6px 0 4px;">
      <span leaf="">用户满意度</span>
    </p>
    <p style="font-size:11px;font-weight:700;color:#10B981;margin:0;">
      <span leaf="">↑ +5.2pp</span>
    </p>
  </section>
  <section style="flex:1;background:#FFFFFF;border-radius:12px;padding:20px 16px;border:1px solid #E2E8F0;text-align:center;box-shadow:0 4px 16px -4px rgba(8,145,178,0.10);">
    <p style="font-size:44px;font-weight:900;color:#F97316;margin:0;line-height:1;letter-spacing:-1px;">
      <span leaf="">3.4x</span>
    </p>
    <p style="font-size:12px;color:#94A3B8;margin:6px 0 4px;">
      <span leaf="">ROI 投入产出比</span>
    </p>
    <p style="font-size:11px;font-weight:700;color:#EC4899;margin:0;">
      <span leaf="">↓ -0.2x</span>
    </p>
  </section>
</section>
```

### 三列 KPI 卡组（数据看板）

```html
<section style="display:flex;margin-bottom:24px;">
  <section style="flex:1;background:#FFFFFF;border-radius:10px;padding:16px 10px;margin-right:6px;border:1px solid #E2E8F0;text-align:center;">
    <p style="font-size:36px;font-weight:900;color:#0891B2;margin:0;line-height:1;">
      <span leaf="">1.2亿</span>
    </p>
    <p style="font-size:11px;color:#94A3B8;margin:5px 0 3px;">
      <span leaf="">累计用户</span>
    </p>
    <p style="font-size:11px;font-weight:700;color:#10B981;margin:0;">
      <span leaf="">↑ +22%</span>
    </p>
  </section>
  <section style="flex:1;background:#FFFFFF;border-radius:10px;padding:16px 10px;margin-right:6px;border:1px solid #E2E8F0;text-align:center;">
    <p style="font-size:36px;font-weight:900;color:#8B5CF6;margin:0;line-height:1;">
      <span leaf="">68%</span>
    </p>
    <p style="font-size:11px;color:#94A3B8;margin:5px 0 3px;">
      <span leaf="">次月留存率</span>
    </p>
    <p style="font-size:11px;font-weight:700;color:#10B981;margin:0;">
      <span leaf="">↑ +8pp</span>
    </p>
  </section>
  <section style="flex:1;background:#FFFFFF;border-radius:10px;padding:16px 10px;border:1px solid #E2E8F0;text-align:center;">
    <p style="font-size:36px;font-weight:900;color:#EC4899;margin:0;line-height:1;">
      <span leaf="">4.8分</span>
    </p>
    <p style="font-size:11px;color:#94A3B8;margin:5px 0 3px;">
      <span leaf="">应用商店评分</span>
    </p>
    <p style="font-size:11px;font-weight:700;color:#94A3B8;margin:0;">
      <span leaf="">→ 持平</span>
    </p>
  </section>
</section>
```

---

## 组件 12b 占比进度条（核心特色组件）

> **纯 flex 实现**，两个子 section 拼宽度比例，左实色右浅底，标百分比标签。绝对不用 display:grid。

### 单条占比进度条

```html
<section style="margin-bottom:20px;">
  <section style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
    <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">指标名称</span></p>
    <p style="font-size:13px;font-weight:800;color:#0891B2;margin:0;"><span leaf="">72%</span></p>
  </section>
  <section style="display:flex;height:10px;border-radius:5px;overflow:hidden;background:#E2E8F0;">
    <section style="width:72%;background:#0891B2;border-radius:5px 0 0 5px;"></section>
    <section style="width:28%;background:#E2E8F0;"></section>
  </section>
</section>
```

### 多维度进度条组（不同颜色区分维度）

```html
<section style="background:#FFFFFF;border-radius:12px;padding:20px;margin-bottom:24px;border:1px solid #E2E8F0;">
  <p style="font-size:13px;font-weight:700;color:#94A3B8;margin:0 0 16px;letter-spacing:1px;text-transform:uppercase;">
    <span leaf="">维度占比分析</span>
  </p>

  <!-- 维度 1：青蓝 -->
  <section style="margin-bottom:14px;">
    <section style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
      <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">产品研发</span></p>
      <p style="font-size:13px;font-weight:800;color:#0891B2;margin:0;"><span leaf="">42%</span></p>
    </section>
    <section style="display:flex;height:8px;border-radius:4px;overflow:hidden;background:#E2E8F0;">
      <section style="width:42%;background:#0891B2;border-radius:4px 0 0 4px;"></section>
      <section style="width:58%;background:#E2E8F0;"></section>
    </section>
  </section>

  <!-- 维度 2：橙色 -->
  <section style="margin-bottom:14px;">
    <section style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
      <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">市场营销</span></p>
      <p style="font-size:13px;font-weight:800;color:#F97316;margin:0;"><span leaf="">28%</span></p>
    </section>
    <section style="display:flex;height:8px;border-radius:4px;overflow:hidden;background:#E2E8F0;">
      <section style="width:28%;background:#F97316;border-radius:4px 0 0 4px;"></section>
      <section style="width:72%;background:#E2E8F0;"></section>
    </section>
  </section>

  <!-- 维度 3：绿色 -->
  <section style="margin-bottom:14px;">
    <section style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
      <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">用户运营</span></p>
      <p style="font-size:13px;font-weight:800;color:#10B981;margin:0;"><span leaf="">18%</span></p>
    </section>
    <section style="display:flex;height:8px;border-radius:4px;overflow:hidden;background:#E2E8F0;">
      <section style="width:18%;background:#10B981;border-radius:4px 0 0 4px;"></section>
      <section style="width:82%;background:#E2E8F0;"></section>
    </section>
  </section>

  <!-- 维度 4：紫色 -->
  <section style="margin-bottom:0;">
    <section style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
      <p style="font-size:13px;font-weight:600;color:#0F172A;margin:0;"><span leaf="">基础设施</span></p>
      <p style="font-size:13px;font-weight:800;color:#8B5CF6;margin:0;"><span leaf="">12%</span></p>
    </section>
    <section style="display:flex;height:8px;border-radius:4px;overflow:hidden;background:#E2E8F0;">
      <section style="width:12%;background:#8B5CF6;border-radius:4px 0 0 4px;"></section>
      <section style="width:88%;background:#E2E8F0;"></section>
    </section>
  </section>

</section>
```

---

## 组件 12c 横向柱状对比（核心特色组件）

> 多行对比，每行 label + flex 比例条 + 数值。纯 flex 实现，无 grid。用于多项目横向对比（如渠道对比、产品对比、时间段对比）。

```html
<section style="background:#FFFFFF;border-radius:12px;padding:20px;margin-bottom:24px;border:1px solid #E2E8F0;">
  <p style="font-size:13px;font-weight:700;color:#94A3B8;margin:0 0 16px;letter-spacing:1px;">
    <span leaf="">渠道获客量对比（月）</span>
  </p>

  <!-- 行 1：青蓝 -->
  <section style="display:flex;align-items:center;margin-bottom:12px;">
    <p style="font-size:12px;color:#475569;margin:0;width:56px;flex-shrink:0;"><span leaf="">自然搜索</span></p>
    <section style="flex:1;display:flex;align-items:center;margin:0 10px;">
      <section style="display:flex;height:18px;border-radius:3px;overflow:hidden;width:100%;">
        <section style="width:80%;background:#0891B2;border-radius:3px 0 0 3px;"></section>
        <section style="width:20%;background:#E2E8F0;"></section>
      </section>
    </section>
    <p style="font-size:12px;font-weight:700;color:#0891B2;margin:0;width:40px;text-align:right;flex-shrink:0;"><span leaf="">8,240</span></p>
  </section>

  <!-- 行 2：橙色 -->
  <section style="display:flex;align-items:center;margin-bottom:12px;">
    <p style="font-size:12px;color:#475569;margin:0;width:56px;flex-shrink:0;"><span leaf="">付费广告</span></p>
    <section style="flex:1;display:flex;align-items:center;margin:0 10px;">
      <section style="display:flex;height:18px;border-radius:3px;overflow:hidden;width:100%;">
        <section style="width:55%;background:#F97316;border-radius:3px 0 0 3px;"></section>
        <section style="width:45%;background:#E2E8F0;"></section>
      </section>
    </section>
    <p style="font-size:12px;font-weight:700;color:#F97316;margin:0;width:40px;text-align:right;flex-shrink:0;"><span leaf="">5,620</span></p>
  </section>

  <!-- 行 3：绿色 -->
  <section style="display:flex;align-items:center;margin-bottom:12px;">
    <p style="font-size:12px;color:#475569;margin:0;width:56px;flex-shrink:0;"><span leaf="">社交裂变</span></p>
    <section style="flex:1;display:flex;align-items:center;margin:0 10px;">
      <section style="display:flex;height:18px;border-radius:3px;overflow:hidden;width:100%;">
        <section style="width:38%;background:#10B981;border-radius:3px 0 0 3px;"></section>
        <section style="width:62%;background:#E2E8F0;"></section>
      </section>
    </section>
    <p style="font-size:12px;font-weight:700;color:#10B981;margin:0;width:40px;text-align:right;flex-shrink:0;"><span leaf="">3,910</span></p>
  </section>

  <!-- 行 4：紫色 -->
  <section style="display:flex;align-items:center;margin-bottom:12px;">
    <p style="font-size:12px;color:#475569;margin:0;width:56px;flex-shrink:0;"><span leaf="">合作伙伴</span></p>
    <section style="flex:1;display:flex;align-items:center;margin:0 10px;">
      <section style="display:flex;height:18px;border-radius:3px;overflow:hidden;width:100%;">
        <section style="width:22%;background:#8B5CF6;border-radius:3px 0 0 3px;"></section>
        <section style="width:78%;background:#E2E8F0;"></section>
      </section>
    </section>
    <p style="font-size:12px;font-weight:700;color:#8B5CF6;margin:0;width:40px;text-align:right;flex-shrink:0;"><span leaf="">2,280</span></p>
  </section>

  <!-- 行 5：玫红 -->
  <section style="display:flex;align-items:center;margin-bottom:0;">
    <p style="font-size:12px;color:#475569;margin:0;width:56px;flex-shrink:0;"><span leaf="">口碑推荐</span></p>
    <section style="flex:1;display:flex;align-items:center;margin:0 10px;">
      <section style="display:flex;height:18px;border-radius:3px;overflow:hidden;width:100%;">
        <section style="width:14%;background:#EC4899;border-radius:3px 0 0 3px;"></section>
        <section style="width:86%;background:#E2E8F0;"></section>
      </section>
    </section>
    <p style="font-size:12px;font-weight:700;color:#EC4899;margin:0;width:40px;text-align:right;flex-shrink:0;"><span leaf="">1,430</span></p>
  </section>

</section>
```

---

## 组件 13 标签胶囊

### 青蓝浅底深色字（默认）

```html
<span style="display:inline-block;background:#ECFEFF;color:#0E7490;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;border:1px solid #CFFAFE;"><span leaf="">标签名</span></span>
```

### 数据多色维度标签（按维度选色）

橙色维度：
```html
<span style="display:inline-block;background:#FFF7ED;color:#C2410C;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;border:1px solid #FED7AA;"><span leaf="">增长</span></span>
```

绿色维度：
```html
<span style="display:inline-block;background:#ECFDF5;color:#065F46;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;border:1px solid #A7F3D0;"><span leaf="">健康</span></span>
```

紫色维度：
```html
<span style="display:inline-block;background:#F5F3FF;color:#5B21B6;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;border:1px solid #DDD6FE;"><span leaf="">创新</span></span>
```

玫红维度：
```html
<span style="display:inline-block;background:#FDF2F8;color:#9D174D;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;border:1px solid #FBCFE8;"><span leaf="">风险</span></span>
```

### 青蓝描边（轻量）

```html
<span style="display:inline-block;border:1px solid #0891B2;color:#0891B2;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 14 END 结尾分割线

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:2px;width:60px;background:linear-gradient(to right,transparent,#0891B2);margin-right:12px;"></span>
      <span style="font-size:11px;color:#0891B2;letter-spacing:3px;font-weight:700;"><span leaf="">END</span></span>
      <span style="height:2px;width:60px;background:linear-gradient(to left,transparent,#0891B2);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部作者签名区

```html
<section style="padding:0 10px;">
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#475569;">
    <span leaf="">我是甲木，热衷于分享一些 AI 观察，AI 干货内容</span>
  </p>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#475569;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#0891B2;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#F8FAFC;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#475569;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 开头引言卡片（青蓝顶色条 + 迷你 KPI 行） -->
  <!-- 组件 2 -->

  <!-- 2. 前言正文（开场白） -->
  <section style="padding:0 10px 20px;">
    <!-- 组件 6 正文段落 x N -->
  </section>

  <!-- 3. 目录导航 -->
  <!-- 组件 3 数据看点卡片目录 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件 4 青蓝渐变分割线 -->

  <!-- 5. 第一章 -->
  <!-- 组件 5（青蓝编号 01 + 标题 + 数据徽章） -->
  <!--   组件 6 正文 + 组件 7 高亮 + 组件 8 引用 + 组件 9 提示条 -->
  <!--   组件 10 图片 + 组件 12a KPI 大数字卡 + 组件 12b 占比进度条 + 组件 12c 横向柱状对比 -->

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
| **锚点层** | 青蓝加粗 `color:#0891B2` | 指标名、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 青蓝下划线 `#06B6D4` | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 左竖条 + 浅底 / 数据卡 / 进度条 | KPI卡、引用、旁注、提示 | 按需 |

**克制原则**：
- 青蓝底白字标签（`bg:#0891B2`）**仅在开头卡片顶色条和引言关键词内使用**，正文中用浅青底深青字替代
- 青蓝加粗全文不超过 5 处
- 引用/提示统一用左竖条 + 浅底 + 类型小标签，不用四周 dashed 框
- 多色（橙/绿/紫/玫红）只用于数据维度区分，同一语义维度全文用同一颜色
- 进度条和横向柱状图全程用 `display:flex` 实现，禁用 `display:grid`

---

## Markdown → 数据信息图风排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 引言卡片（顶部迷你 KPI 行 + 引言） | 文章开头引用；KPI 数据从正文提取 |
| `## 章节标题` | 组件 5 章节标题 | 青蓝编号 01/02/03，结语用 ∞；可带数据徽章 |
| 普通段落 | 组件 6 正文段落 | 默认样式，主动标记青蓝下划线关键词 |
| `**加粗文字**` | 组件 7a 普通加粗（默认）或青蓝加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 青蓝浅底深色字标签 | 核心概念 |
| `<u>下划线</u>` | 组件 7d 青蓝下划线 | 2px `#06B6D4` |
| `~~荧光~~` | 组件 7e 荧光笔 | 底部半高亮 `#CFFAFE` |
| `> 引用段落`（金句） | 组件 8a 青蓝底左竖条 | 核心数据金句 |
| `> 引用段落`（旁注） | 组件 8c 灰底左竖条 | 轻量旁注/数据来源 |
| `!> 提示文字` | 组件 9 提示条 | 青蓝底左竖条洞察结论 |
| `![](图片)` | 组件 10 图片容器 | 圆角卡片 + 说明 |
| KPI 数据（单个） | 组件 12a 单个/两列/三列 KPI 卡 | 超大青蓝数字 + 标签 + 同比箭头 |
| 占比/百分比数据 | 组件 12b 占比进度条 | 纯 flex 比例条，多维度用多色 |
| 多项横向对比 | 组件 12c 横向柱状对比 | label + flex 条 + 数值，多维度多色 |
| 行内标签 | 组件 13 标签胶囊 | 青蓝浅底为默认，多色可选 |
| `---` | 组件 4 章节分割线 | 青蓝渐变 |
| 文末 | 组件 14 + 15 | END 线 + 签名 |
