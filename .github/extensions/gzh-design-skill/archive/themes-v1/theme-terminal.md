# 甲木公众号排版组件库 —— 终端极客风（Terminal / Dark）

> **使用说明**：本组件库为「终端极客风」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计气质**：开发者终端 / 暗色主题。深底卡片 + 终端窗口质感 + 霓虹绿高亮 + 等宽字体点缀。代码块是本风格核心视觉，引言卡模拟终端窗口，章节标题模拟命令行。
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
深底背景色：     #0D1117（全局容器/终端主背景）
次级暗卡色：     #161B22（卡片底/终端内区域）
三级暗卡色：     #1C2128（轻度区分块，如目录项）
霓虹绿主色：     #3FB950（编号/高亮/命令提示符/左竖条）
霓虹绿暗：       #2EA043（按下/次级绿）
青蓝次强调：     #58A6FF（链接感/副标签/次高亮）
正文浅灰：       #C9D1D9（正文主字色）
标题白：         #F0F6FC（大标题/白字）
暗灰辅助：       #8B949E（说明文字/副标签）
边框色：         #30363D（卡片边框/分割线）
终端红点：       #FF5F56
终端黄点：       #FFBD2E
终端绿点：       #27C93F
正文字号：       15px
行高：           1.8
字间距：         0.5px
等宽字体栈：     'SF Mono', Consolas, Monaco, 'Courier New', monospace
无衬线字体栈：   -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif
内容区边距：     0 10px
```

---

## 组件 1 全局容器

> 整体深底 #0D1117，保证所有文字在深色背景上清晰可读。

```html
<section style="max-width:677px;margin:0 auto;background:#0D1117;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#C9D1D9;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;padding-bottom:40px;">

  <!-- 所有组件放在这里 -->

</section>
```

---

## 组件 2 开头引言卡片（终端窗口风格）

> 模拟真实终端窗口：顶部标题栏（三色圆点 + 路径标题）+ 暗卡内容区 + `~/article $` 命令提示符 + 引言正文 + 右下署名。无四周虚线框，只用暗卡底 + 绿色边框点缀。

```html
<section style="margin:16px 10px 32px;border-radius:10px;overflow:hidden;border:1px solid #30363D;box-shadow:0 8px 32px -8px rgba(0,0,0,0.6);">
  <!-- 终端标题栏 -->
  <section style="display:flex;align-items:center;background:#161B22;padding:10px 16px;border-bottom:1px solid #30363D;">
    <span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#FF5F56;margin-right:7px;font-size:0;line-height:0;overflow:hidden;">.</span>
    <span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#FFBD2E;margin-right:7px;font-size:0;line-height:0;overflow:hidden;">.</span>
    <span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:#27C93F;margin-right:12px;font-size:0;line-height:0;overflow:hidden;">.</span>
    <span style="font-size:12px;color:#8B949E;font-family:'SF Mono',Consolas,Monaco,monospace;letter-spacing:1px;"><span leaf="">~/article — zsh</span></span>
  </section>
  <!-- 终端内容区 -->
  <section style="background:#0D1117;padding:22px 24px 20px;">
    <!-- 命令行提示符 -->
    <p style="margin:0 0 14px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;color:#8B949E;line-height:1.5;">
      <span style="color:#3FB950;"><span leaf="">~/article $</span></span>
      <span leaf=""> cat quote.txt</span>
    </p>
    <!-- 引言正文 -->
    <p style="font-size:16px;font-weight:700;color:#F0F6FC;margin:0 0 10px;line-height:1.75;padding-left:4px;">
      <span style="color:#3FB950;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:20px;font-weight:900;"><span leaf="">"</span></span>
      <span leaf=""> </span>
      <span style="border-bottom:2px solid #3FB950;"><span leaf="">核心观点关键词</span></span>
      <span leaf="">，这里是引言金句的主体部分，点出文章核心洞见。</span>
    </p>
    <!-- 署名行 -->
    <p style="text-align:right;font-size:12px;color:#8B949E;margin:10px 0 0;font-family:'SF Mono',Consolas,Monaco,monospace;letter-spacing:1px;">
      <span leaf="">—— 作者名（按文章作者或主题而定，不要固定写"甲木"）</span>
    </p>
  </section>
</section>
```

**效果**：完整终端窗口质感，顶部三色圆点，命令行提示符 `~/article $`，霓虹绿引号 + 绿色下划线关键词，深底浅字，边框 + 阴影使卡片有浮起感。

---

## 组件 3 前言导读区域（暗卡目录）

> 三列目录卡片，霓虹绿编号 + 暗卡底 + 边框，命令行风格编号前缀。

```html
<section style="padding:0 10px 32px;">
  <p style="font-size:13px;color:#8B949E;margin:0 0 14px;font-family:'SF Mono',Consolas,Monaco,monospace;letter-spacing:2px;">
    <span style="color:#3FB950;"><span leaf="">#</span></span>
    <span leaf=""> 本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#161B22;border-radius:8px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #30363D;">
      <p style="font-size:18px;font-weight:900;color:#3FB950;margin:0 0 8px;font-family:'SF Mono',Consolas,Monaco,monospace;line-height:1;"><span leaf="">01</span></p>
      <p style="font-size:12px;font-weight:700;color:#C9D1D9;margin:0;line-height:1.5;"><span leaf="">第一个要点</span></p>
    </section>
    <section style="flex:1;background:#161B22;border-radius:8px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #30363D;">
      <p style="font-size:18px;font-weight:900;color:#3FB950;margin:0 0 8px;font-family:'SF Mono',Consolas,Monaco,monospace;line-height:1;"><span leaf="">02</span></p>
      <p style="font-size:12px;font-weight:700;color:#C9D1D9;margin:0;line-height:1.5;"><span leaf="">第二个要点</span></p>
    </section>
    <section style="flex:1;background:#161B22;border-radius:8px;padding:16px 12px;text-align:center;border:1px solid #30363D;">
      <p style="font-size:18px;font-weight:900;color:#3FB950;margin:0 0 8px;font-family:'SF Mono',Consolas,Monaco,monospace;line-height:1;"><span leaf="">03</span></p>
      <p style="font-size:12px;font-weight:700;color:#C9D1D9;margin:0;line-height:1.5;"><span leaf="">第三个要点</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（霓虹绿渐变）

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right, transparent, #3FB950, #58A6FF, #3FB950, transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题（命令行风格，自动编号）

> 命令行 `$` 提示符 + 霓虹绿编号 + 等宽大标题 + 英文标签。底部绿色边框线。

```html
<section style="margin-top:48px;margin-bottom:28px;padding:0 10px;">
  <section style="border-bottom:2px solid #3FB950;margin-bottom:20px;padding-bottom:14px;">
    <section style="display:flex;align-items:center;">
      <!-- 命令提示符 + 编号 -->
      <span style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:22px;font-weight:900;color:#3FB950;margin-right:10px;line-height:1;"><span leaf="">$</span></span>
      <span style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:20px;font-weight:900;color:#3FB950;margin-right:16px;line-height:1;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#58A6FF;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;font-family:'SF Mono',Consolas,Monaco,monospace;">
          <span leaf="">ENGLISH TAG</span>
        </p>
        <h3 style="font-size:18px;font-weight:800;color:#F0F6FC;margin:0;letter-spacing:0.5px;">
          <span leaf="">中文章节标题</span>
        </h3>
      </section>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**（用 `~` 替代数字编号，表示 home/结语）：

```html
<span style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:22px;font-weight:900;color:#3FB950;margin-right:10px;line-height:1;"><span leaf="">$</span></span>
<span style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:20px;font-weight:900;color:#3FB950;margin-right:16px;line-height:1;"><span leaf="">~</span></span>
```

或使用 `///` 变体（更有终端注释感）：

```html
<span style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:16px;font-weight:900;color:#3FB950;margin-right:12px;line-height:1;"><span leaf="">///</span></span>
```

---

## 组件 6 正文段落

> **关键规则**：每个正文段落中，应主动识别 1~3 个**关键语句或关键词**，用**霓虹绿下划线（7d）**进行标记。深底 + 浅灰正文，字号 15px，行高 1.8。

**基础段落**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#C9D1D9;padding:0 10px;">
  <span leaf="">正文内容，深底浅灰字，15px 字号，1.8 倍行高，两端对齐。</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认使用）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#C9D1D9;padding:0 10px;">
  <span leaf="">正文内容的前半部分，引出核心概念——</span>
  <span style="border-bottom:2px solid #3FB950;font-weight:600;color:#F0F6FC;"><span leaf="">这是需要强调的关键语句</span></span>
  <span leaf="">，后半部分继续阐述。</span>
</p>
```

**标记原则**：
- 每段选 1~3 个关键短语加下划线，**不要整段都标**
- 优先标记：核心观点、结论性判断、关键数据、专有名词
- 标记的词组长度建议 4~15 个字
- 深色背景下，下划线用霓虹绿 `#3FB950`，标记文字颜色提亮为 `#F0F6FC`

---

## 组件 7 正文高亮样式（5 种变体 + 使用策略）

> **核心设计理念**：深底背景下克制用绿，霓虹绿只在真正需要的锚点出现。
>
> **使用优先级**（从最常用到偶尔使用）：
> 1. **7d 霓虹绿下划线** —— 正文默认标记方式，每段都应考虑使用
> 2. **7a 普通加粗 / 绿色加粗** —— 普通加粗为主，绿色加粗仅用于极少数锚点
> 3. **7b 暗卡绿字标签** —— 核心概念标签（每篇 2~4 个）
> 4. **7c 暗绿背景高亮** —— 次要关键词补充
> 5. **7e 荧光笔效果** —— 偶尔用于长句强调

### 7a. 加粗强调

> **普通加粗**为默认，白色提亮。**霓虹绿加粗**仅用于极少数关键锚点（如命令名、步骤标号、CTA），全文不超过 5 处。

普通加粗（默认）：
```html
<strong style="color:#F0F6FC;"><span leaf="">普通加粗强调</span></strong>
```

霓虹绿加粗（仅限关键锚点）：
```html
<strong style="color:#3FB950;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">绿色加粗，仅用于命令名/步骤/CTA</span></strong>
```

### 7b. 暗卡绿字标签

> 暗卡背景 + 霓虹绿文字 + 绿色边框，代码感十足。用于核心概念（每篇 2~4 个）。

```html
<span style="background:#161B22;color:#3FB950;padding:2px 8px;border-radius:4px;font-weight:700;border:1px solid #30363D;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;"><span leaf="">关键词标签</span></span>
```

### 7c. 暗绿背景高亮

> 深绿底 + 绿字，适合次要关键词补充标注。

```html
<span style="background:rgba(63,185,80,0.12);color:#3FB950;padding:1px 6px;border-radius:3px;font-weight:600;"><span leaf="">暗绿背景关键词</span></span>
```

### 7d. 霓虹绿下划线 —— 最常用

> **本风格的标志性标记方式**。颜色为霓虹绿 `#3FB950`，配合字色提亮 `#F0F6FC`，在深底背景下清晰醒目，适合高频使用。

```html
<span style="border-bottom:2px solid #3FB950;font-weight:600;color:#F0F6FC;"><span leaf="">霓虹绿下划线标记的关键词</span></span>
```

**在段落中的实际效果**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;color:#C9D1D9;padding:0 10px;">
  <span leaf="">AI 竞争已进入下半场：上半场拼模型能力，下半场拼</span>
  <span style="border-bottom:2px solid #3FB950;font-weight:600;color:#F0F6FC;"><span leaf="">分发能力</span></span>
  <span leaf="">。微信的策略清晰：不做模型、不限生态，只做一件事——</span>
  <span style="border-bottom:2px solid #3FB950;font-weight:600;color:#F0F6FC;"><span leaf="">把 AI 入口握在手里</span></span>
  <span leaf="">。</span>
</p>
```

### 7e. 荧光笔效果（深底适配版）

> 底部 40% 霓虹绿半透明高亮，偶尔用于长句强调。深底下用透明渐变避免太刺眼。

```html
<span style="background:linear-gradient(180deg, transparent 60%, rgba(63,185,80,0.3) 60%);font-weight:700;color:#F0F6FC;"><span leaf="">荧光笔效果的重要长句</span></span>
```

---

## 组件 8 引用高亮块（3 种变体）

### 8a. 暗卡左绿竖条块金句引用（视觉焦点最强）

> 暗卡底 + 霓虹绿左竖条 + 浅白字，用于核心金句。

```html
<section style="background:#161B22;border-radius:0 10px 10px 0;border-left:4px solid #3FB950;padding:18px 22px;margin:0 10px 24px;">
  <p style="font-size:16px;font-weight:800;color:#F0F6FC;margin:0;line-height:1.8;">
    <span leaf="">「这里是核心观点或关键金句。」</span>
  </p>
</section>
```

### 8b. 暗卡边框引用块（内容/Prompt 块）

> 暗卡底 + 绿色细边框，用于展示 Prompt、引用内容、命令输出等。

```html
<section style="background:#161B22;border-radius:8px;padding:18px 20px;margin:0 10px 24px;border:1px solid #30363D;border-left:3px solid #58A6FF;">
  <p style="font-size:15px;color:#C9D1D9;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">青蓝左竖条引用内容，可以包含</span>
    <span style="border-bottom:2px solid #3FB950;font-weight:600;color:#F0F6FC;"><span leaf="">下划线加粗的关键句</span></span>
    <span leaf="">。</span>
  </p>
</section>
```

### 8c. 暗灰左竖条块引用（轻量旁注）

> 暗卡底 + 暗灰左竖条，用于轻量旁注、补充说明。

```html
<section style="border-left:4px solid #30363D;padding:14px 20px;margin:0 10px 24px;background:#161B22;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#8B949E;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">轻量旁注内容，暗灰竖条低调不抢戏</span>
  </p>
</section>
```

---

## 组件 9 提示/警示条

> 暗卡底 + 霓虹绿左竖条 + 类型小标签 + 浅灰正文，用于重要提醒、核心结论、注意事项。

```html
<section style="background:#161B22;border-left:4px solid #3FB950;border-radius:0 8px 8px 0;padding:14px 20px;margin:0 10px 24px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;background:#3FB950;color:#0D1117;font-size:11px;font-weight:700;padding:2px 10px;border-radius:4px;letter-spacing:1px;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">提示</span></span>
  </p>
  <p style="font-size:14px;font-weight:600;color:#C9D1D9;margin:0;line-height:1.8;">
    <span leaf="">这里是重要提示或核心结论，霓虹绿标签 + 暗卡底。</span>
  </p>
</section>
```

标签文字可换：`提示` / `注意` / `重点` / `WARNING` / `旁注` 等。

---

## 组件 10 图片容器（深框版）

> 深色边框 + 暗卡内边距 + 圆角，与整体深色主题协调。

```html
<section style="background:#161B22;border-radius:10px;padding:6px;border:1px solid #30363D;box-shadow:0 4px 16px -4px rgba(0,0,0,0.5);margin:0 10px 10px;">
  <section style="margin:0;border-radius:6px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
```

图片 + 说明文字配合时，图片 `margin-bottom` 改为 `8px`：

```html
<section style="background:#161B22;border-radius:10px;padding:6px;border:1px solid #30363D;box-shadow:0 4px 16px -4px rgba(0,0,0,0.5);margin:0 10px 8px;">
  <section style="margin:0;border-radius:6px;overflow:hidden;">
    <span leaf=""><img src="图片URL" style="max-width:100%;"></span>
  </section>
</section>
<p style="font-size:12px;color:#8B949E;text-align:center;margin:0 10px 24px;font-family:'SF Mono',Consolas,Monaco,monospace;">
  <span leaf="">// 图片说明文字</span>
</p>
```

---

## 组件 11 加粗正文段落

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#F0F6FC;padding:0 10px;">
  <span leaf="">加粗的结论性短句，深底用白色提亮。</span>
</p>
```

结合荧光笔的变体：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;font-weight:700;color:#F0F6FC;padding:0 10px;">
  <span style="background:linear-gradient(180deg, transparent 60%, rgba(63,185,80,0.3) 60%);"><span leaf="">荧光笔标记的结论句</span></span>
</p>
```

---

## 组件 12 数据/要点卡片组

> 霓虹绿大号数字 + 暗卡底 + 边框，视觉冲击感强。

### 两列版

```html
<section style="display:flex;margin:0 10px 24px;">
  <section style="flex:1;background:#161B22;border-radius:10px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #30363D;">
    <p style="font-size:28px;font-weight:900;color:#3FB950;margin:0 0 4px;line-height:1;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">14亿</span></p>
    <p style="font-size:12px;color:#8B949E;margin:0;"><span leaf="">覆盖用户</span></p>
  </section>
  <section style="flex:1;background:#161B22;border-radius:10px;padding:18px 16px;text-align:center;border:1px solid #30363D;">
    <p style="font-size:28px;font-weight:900;color:#3FB950;margin:0 0 4px;line-height:1;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">3步</span></p>
    <p style="font-size:12px;color:#8B949E;margin:0;"><span leaf="">快速接入</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display:flex;margin:0 10px 24px;">
  <section style="flex:1;background:#161B22;border-radius:10px;padding:16px 10px;margin-right:8px;text-align:center;border:1px solid #30363D;">
    <p style="font-size:22px;font-weight:900;color:#3FB950;margin:0 0 4px;line-height:1;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">99%</span></p>
    <p style="font-size:11px;color:#8B949E;margin:0;"><span leaf="">准确率</span></p>
  </section>
  <section style="flex:1;background:#161B22;border-radius:10px;padding:16px 10px;margin-right:8px;text-align:center;border:1px solid #30363D;">
    <p style="font-size:22px;font-weight:900;color:#58A6FF;margin:0 0 4px;line-height:1;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">200ms</span></p>
    <p style="font-size:11px;color:#8B949E;margin:0;"><span leaf="">响应时间</span></p>
  </section>
  <section style="flex:1;background:#161B22;border-radius:10px;padding:16px 10px;text-align:center;border:1px solid #30363D;">
    <p style="font-size:22px;font-weight:900;color:#3FB950;margin:0 0 4px;line-height:1;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">∞</span></p>
    <p style="font-size:11px;color:#8B949E;margin:0;"><span leaf="">可扩展</span></p>
  </section>
</section>
```

---

## 组件 13 标签胶囊

### 霓虹绿底黑字（强调，默认）

```html
<span style="display:inline-block;background:#3FB950;color:#0D1117;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">标签名</span></span>
```

### 暗卡绿描边（轻量）

```html
<span style="display:inline-block;border:1px solid #3FB950;color:#3FB950;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">标签名</span></span>
```

### 青蓝描边（次强调）

```html
<span style="display:inline-block;border:1px solid #58A6FF;color:#58A6FF;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">标签名</span></span>
```

---

## 组件 14 END 结尾分割线

> 终端风格结尾，霓虹绿渐变线 + `EOF` 标识（终端脚本结束标记）。

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:1px;width:60px;background:linear-gradient(to right,transparent,#3FB950);margin-right:12px;"></span>
      <span style="font-size:11px;color:#3FB950;letter-spacing:3px;font-weight:700;font-family:'SF Mono',Consolas,Monaco,monospace;"><span leaf="">EOF</span></span>
      <span style="height:1px;width:60px;background:linear-gradient(to left,transparent,#3FB950);margin-left:12px;"></span>
    </section>
  </section>
</section>
```

---

## 组件 15 尾部作者签名区

```html
<section style="padding:0 10px;">
  <section style="background:#161B22;border-radius:10px;padding:20px 24px;border:1px solid #30363D;margin-bottom:16px;">
    <p style="font-family:'SF Mono',Consolas,Monaco,monospace;font-size:12px;color:#8B949E;margin:0 0 10px;">
      <span style="color:#3FB950;"><span leaf="">$</span></span>
      <span leaf=""> whoami</span>
    </p>
    <p style="margin-bottom:14px;font-size:15px;line-height:1.8;color:#C9D1D9;">
      <span leaf="">我是甲木，热衷于分享一些 AI 观察，AI 干货内容。</span>
    </p>
    <p style="margin-bottom:0;font-size:15px;line-height:1.8;color:#C9D1D9;">
      <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
      <strong style="color:#3FB950;"><span leaf="">点赞、在看、转发</span></strong>
      <span leaf="">三连，我们下篇见。</span>
    </p>
  </section>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#0D1117;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#C9D1D9;line-height:1.8;letter-spacing:0.5px;overflow-x:hidden;padding-bottom:40px;">

  <!-- 1. 开头引言卡片（终端窗口风格） -->
  <!-- 组件 2 -->

  <!-- 2. 前言正文（开场白） -->
  <section style="padding:0 0 20px;">
    <!-- 组件 6 正文段落 x N -->
  </section>

  <!-- 3. 目录导航 -->
  <!-- 组件 3 暗卡目录 -->

  <!-- 4. 章节分割线 -->
  <!-- 组件 4 霓虹绿渐变分割线 -->

  <!-- 5. 第一章 -->
  <!-- 组件 5（$ 01 + 标题） -->
  <!--   组件 6 正文 + 组件 7 高亮 + 组件 8 引用 + 组件 9 提示条 + 组件 10 图片 + 组件 12 数据卡片 -->

  <!-- 6. 章节分割线 -->
  <!-- 组件 4 -->

  <!-- 7. 第二章 -->
  <!-- 组件 5（$ 02） -->

  <!-- ... 更多章节 ... -->

  <!-- 8. 章节分割线 -->
  <!-- 组件 4 -->

  <!-- 9. 结语章节 -->
  <!-- 组件 5（$ ~ 变体 或 /// 变体） -->

  <!-- 10. END 分割线 -->
  <!-- 组件 14（EOF 标识） -->

  <!-- 11. 尾部签名 -->
  <!-- 组件 15 -->

</section>
```

---

## 与通用增量库的协调说明

本风格（终端极客风）与通用库（代码块·图片·小标签）深度协调：

- **代码块 1a（深色）**：通用库 1a 代码块与本风格完全一致（均为深底 `#0F172A` 顶栏 + `#1E293B` 正文区），**直接使用无需修改**。是本风格最核心的视觉组件。
- **代码块 1b（浅色）**：本风格不推荐使用 1b 浅色代码块，深色主题下会打破视觉一致性。如需简单代码行，改用本风格的 8b 引用块（暗卡 + 青蓝左竖条）。
- **行内代码 1c**：底色改为暗卡 `#161B22`，字色改为霓虹绿 `#3FB950`：
  ```html
  <span style="background:#161B22;color:#3FB950;padding:1px 6px;border-radius:4px;font-family:'SF Mono',Consolas,Monaco,monospace;font-size:13px;border:1px solid #30363D;"><span leaf="">code</span></span>
  ```
- **图片组件 2a/2b**：容器色改为 `#161B22`，边框改为 `#30363D`（即组件 10）。
- **小标签组件 3a**（左竖条小标题）：左竖条色改为 `#3FB950`，标题色改为 `#F0F6FC`，背景保持 `#0D1117`（全局容器色）：
  ```html
  <p style="margin:28px 0 14px;font-size:16px;font-weight:800;color:#F0F6FC;line-height:1.5;border-left:4px solid #3FB950;padding-left:12px;">
    <span leaf="">小标题文字</span>
  </p>
  ```
- **药丸标签 3b**：底色 `#3FB950`，字色 `#0D1117`（深底反色）。
- **序号药丸 3c**：底色 `#161B22`，字色 `#3FB950`，边框 `#30363D`。
- **金句块 3d**：与本风格 8a 对应，使用暗卡底 `#161B22` + 绿色左竖条 `#3FB950`。
- **提示块 3e**：与本风格组件 9 对应。

---

## 视觉层级设计（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 霓虹绿加粗 `color:#3FB950` + 等宽字体 | 命令名、步骤编号、CTA | 全文 ≤5 处 |
| **标记层** | 绿色下划线 `#3FB950` + 字色提亮 `#F0F6FC` | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 暗卡底 + 绿色左竖条 + 类型标签 | 引用、旁注、提示 | 按需 |

**克制原则**：
- 霓虹绿底黑字标签（`bg:#3FB950`）仅在开头卡片内和 END 线使用；正文中用暗卡绿字标签替代
- 绿色加粗全文不超过 5 处
- 引用/提示统一用左竖条 + 暗卡底 + 类型小标签，不用四周虚线框（dashed）
- 渐变绿色仅出现在分割线和 END 线
- 所有正文保持 `#C9D1D9` 基础字色，关键词才提亮至 `#F0F6FC`

---

## Markdown → 终端极客风 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| `> 引言金句` | 组件 2 终端窗口引言卡 | 文章开头，带三色圆点标题栏 |
| `## 章节标题` | 组件 5 命令行标题 | `$ 01` 绿色等宽编号，结语用 `$ ~` 或 `///` |
| 普通段落 | 组件 6 正文段落 | 深底浅灰字，主动标记绿色下划线关键词 |
| `**加粗文字**` | 组件 7a 普通加粗（`#F0F6FC`）或绿色加粗（锚点） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 暗卡绿字标签 | 核心概念，等宽字体 |
| `<u>下划线</u>` | 组件 7d 霓虹绿下划线 | 2px `#3FB950` + 字色提亮 |
| `~~文字~~` | 组件 7e 荧光笔 | 底部半透明绿色，偶尔用于长句 |
| `> 引用段落`（金句） | 组件 8a 暗卡左绿竖条 | 核心金句 |
| `> 引用段落`（内容） | 组件 8b 暗卡青蓝竖条 | Prompt/引用内容 |
| `> 引用段落`（旁注） | 组件 8c 暗卡暗灰竖条 | 轻量旁注 |
| `!> 提示文字` | 组件 9 提示条 | 暗卡底 + 绿色左竖条 + 类型标签 |
| ` ``` 代码/命令/Prompt ``` ` | 通用库 1a 深色代码块 | 本风格核心，与整体深色协调，直接用无需改色 |
| 行内 `` `code` `` | 本风格行内代码（见协调说明） | 暗卡底 + 霓虹绿字 + 边框 |
| `![](图片)` | 组件 10 图片容器 | 深框暗卡底 |
| 数据展示 | 组件 12 数据卡片组 | 暗卡 + 霓虹绿大号等宽数字 |
| 行内标签 | 组件 13 标签胶囊 | 霓虹绿实底（强调）或暗卡描边（轻量）|
| 小标题/强调 | 通用库 3a 左竖条（改绿色）/ 3b 药丸 | 不要用虚线框 |
| `---` | 组件 4 分割线 | 霓虹绿渐变 |
| 文末 | 组件 14 + 15 | EOF 线 + 终端签名区 |
