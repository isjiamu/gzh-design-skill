# 公众号排版组件库 —— 红白色系

> **使用说明**：本组件库为「红白色系」主题（经典编辑风），所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：红白干净 + 克制点睛。淡粉下划线为主标记、左竖条块引用、红色仅在锚点处出现。编号章节 + 引言卡 + 签名区的经典编辑骨架，适合观点、深度分析、盘点、教程、随笔类文章。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（有限）、`linear-gradient`、`border-radius`、`box-shadow`、`<section>/<p>/<span>/<strong>/<img>` 等基础标签
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 所有"装饰性空元素"（红色渐变分割线、END 短线、光晕竖条、数据卡分隔）**必须在内部放 `<span leaf=""><br></span>` 占位**，否则微信会剥掉样式
> - **不要把 `font-size`/`border-bottom` 打在 `<strong>` 上**，也不要在同一个 `<p>` 里混多个不同 `font-size`——微信编辑器会自动"纠正"导致样式被重写。正确做法：拆成多个 `<p>`，每个 `<p>` 只有一个字号；高亮样式统一挂在外层 `<span>` 上
> - 不用 `position:absolute` 做划线/高亮，删除线用 `text-decoration:line-through`
> - 结构化区域（如引言卡右下署名、图片说明）没有内容时**整块删掉**，不留空 section

---

## 设计变量速查表

```
主色调：       #DC2626（正红）
主色调深：     #991B1B（暗红/酒红）
主色调浅：     #FCA5A5（珊瑚红）
主色调极浅：   #FEE2E2（粉白）
主色调背景：   #FEF2F2（极淡红底）
淡粉标记色：   #FECACA（下划线/左竖条专用）
标题色：       #1C1917（近黑）
正文色：       #374151（深灰）
辅助文字色：   #9CA3AF（中灰）
分割线色：     #E5E7EB
灰竖条：       #D6D3D1（灰底引用左竖条）
正文字号：     15px（不可改）
行高：         1.8
字间距：       0.5px
最大宽度：     677px
内容区边距：   0 10px（左右各 10px）
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

## 组件 2 开头引言卡片（白底 + 红色阴影光晕）

> **文案策略（先读，比代码重要）**：
> - 引言卡金句和公众号外标题是**两层**，视角要错开——外标题卖"为什么点开"，引言卡卖"核心观点是什么"
> - 已知外标题时，金句**禁止原样复述**其核心关键词；从文章第一段或核心论点提炼一句有张力的判断句
> - 右下署名按文章实际作者填，未知则整行删掉，**不要固定写"甲木"**
> - 红底白字标签仅在本卡片内使用（视觉焦点），正文中的关键词标签一律用浅红底深红字（组件 7b）

```html
<section style="margin:10px 10px 32px;background:#ffffff;border-radius:12px;box-shadow:0 4px 24px -4px rgba(220,38,38,0.15);padding:28px 24px 22px;overflow:hidden;">
  <p style="font-size:42px;color:#DC2626;font-weight:900;margin:0;line-height:0.6;">
    <span leaf="">"</span>
  </p>
  <p style="font-size:16px;font-weight:800;color:#1C1917;margin:12px 0 8px;line-height:1.75;padding-left:4px;">
    <span style="background:#DC2626;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">{{高亮关键词}}</span></span>
    <span leaf="">{{金句中段}}</span>
    <span style="background:#DC2626;color:#FFFFFF;padding:2px 8px;border-radius:4px;"><span leaf="">{{高亮关键词}}</span></span>
    <span leaf="">{{金句收尾}}</span>
  </p>
  <p style="text-align:right;font-size:12px;color:#9CA3AF;margin:8px 0 0;letter-spacing:1px;">
    <span leaf="">—— {{作者名，未知则删整行}}</span>
  </p>
</section>
```

---

## 组件 3 前言导读区域（本文看点，三列目录卡片）

> 3 个及以上章节时生成。红底白字编号 + 深色标题；展示**精选 3 个核心看点**，不是全量章节列表。

```html
<section style="padding:0 10px 32px;">
  <p style="font-size:14px;color:#9CA3AF;margin:0 0 14px;letter-spacing:1px;">
    <span leaf="">📌 本文看点</span>
  </p>
  <section style="display:flex;justify-content:space-between;">
    <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #FEE2E2;">
      <p style="display:inline-block;background:#DC2626;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">01</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">{{看点一}}</span></p>
    </section>
    <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:16px 12px;margin-right:8px;text-align:center;border:1px solid #FEE2E2;">
      <p style="display:inline-block;background:#DC2626;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">02</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">{{看点二}}</span></p>
    </section>
    <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:16px 12px;text-align:center;border:1px solid #FEE2E2;">
      <p style="display:inline-block;background:#DC2626;color:#FFFFFF;font-size:12px;font-weight:800;padding:2px 10px;border-radius:4px;margin:0 0 8px;"><span leaf="">03</span></p>
      <p style="font-size:13px;font-weight:700;color:#1C1917;margin:0;"><span leaf="">{{看点三}}</span></p>
    </section>
  </section>
</section>
```

---

## 组件 4 章节分割线（红色渐变）

```html
<section style="padding:0 10px;">
  <section style="height:1px;background:linear-gradient(to right,transparent,#FCA5A5,#DC2626,#FCA5A5,transparent);margin:0;">
    <span leaf=""><br></span>
  </section>
</section>
```

---

## 组件 5 章节标题（红底编号标签 + 标题）

> 红色实底编号标签 + 英文小标签 + 中文大标题，底部红色实线。第一章 `margin-top:16px`，后续章节 `margin-top:48px`。

```html
<section style="margin-top:48px;margin-bottom:28px;padding:0 10px;">
  <section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding-bottom:14px;border-bottom:3px solid #DC2626;">
    <section style="display:flex;align-items:center;">
      <span style="display:inline-block;background:#DC2626;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">01</span></span>
      <section>
        <p style="font-size:10px;color:#DC2626;font-weight:700;letter-spacing:3px;margin:0 0 2px;text-transform:uppercase;">
          <span leaf="">{{ENGLISH TAG}}</span>
        </p>
        <h3 style="font-size:18px;font-weight:800;color:#1C1917;margin:0;letter-spacing:0.5px;">
          <span leaf="">{{中文章节标题}}</span>
        </h3>
      </section>
    </section>
  </section>

  <!-- 本章节正文内容放在这里 -->

</section>
```

**结语章节变体**（编号用 `∞` 替代数字，英文标签用 `THE END` / `EPILOGUE`）：

```html
<span style="display:inline-block;background:#DC2626;color:#FFFFFF;font-size:18px;font-weight:900;padding:4px 14px;border-radius:6px;margin-right:14px;line-height:1.3;"><span leaf="">∞</span></span>
```

---

## 组件 6 正文段落

> **关键规则**：每段主动识别 1~3 个关键短语，用**淡粉下划线（7d）**标记——这是本风格的核心视觉特征，让读者快速扫到每段重点。

**基础段落**：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">{{正文内容}}</span>
</p>
```

**带关键词下划线标记的段落**（推荐默认）：

```html
<p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
  <span leaf="">{{前半句}}</span>
  <span style="border-bottom:2px solid #FECACA;font-weight:600;"><span leaf="">{{需要强调的关键短语}}</span></span>
  <span leaf="">{{后半句}}</span>
</p>
```

**标记原则**：每段选 1~3 个关键短语（4~15 字）加下划线，不要整段都标；优先标核心观点、结论判断、关键数据、专有名词；无重点的段落可不标。

---

## 组件 6b 子标题（`###` 小节标题）

> `###` 子标题用红色左竖条 + 深色标题，**不套用组件 5 的编号章节样式**（编号章节只给 `##`）。

```html
<p style="font-size:15px;font-weight:800;color:#1C1917;margin:28px 0 14px;padding-left:10px;border-left:3px solid #DC2626;line-height:1.4;">
  <span leaf="">{{子标题}}</span>
</p>
```

---

## 组件 7 正文高亮样式（5 种变体 + 使用策略）

> **核心理念**：克制用色，红色只在真正需要的锚点出现。
>
> **优先级**：① 7d 淡粉下划线（正文默认标记）→ ② 7a 普通加粗为主、红色加粗仅锚点 → ③ 7b 浅红底深红字标签（每篇 2~4 个）→ ④ 7c 浅红背景（次要）→ ⑤ 7e 荧光笔（偶尔长句强调）

### 7a. 加粗强调

普通加粗（默认，绝大部分加粗用这个）：

```html
<strong><span leaf="">普通加粗强调</span></strong>
```

红色加粗（仅限产品名/步骤/CTA 等锚点，全文 ≤5 处）：

```html
<strong style="color:#DC2626;"><span leaf="">红色加粗锚点</span></strong>
```

### 7b. 浅红底深红字标签（核心概念，每篇 2~4 个）

```html
<span style="background:#FEE2E2;color:#991B1B;padding:2px 6px;border-radius:3px;font-weight:700;"><span leaf="">关键词标签</span></span>
```

### 7c. 浅红背景高亮（次要关键词）

```html
<span style="background:#FEE2E2;padding:1px 6px;border-radius:3px;font-weight:600;color:#991B1B;"><span leaf="">浅红背景关键词</span></span>
```

### 7d. 淡粉下划线（最常用，本风格标志性标记）

```html
<span style="border-bottom:2px solid #FECACA;font-weight:600;"><span leaf="">淡粉下划线关键词</span></span>
```

### 7e. 荧光笔效果（偶尔用于长句强调）

```html
<span style="background:linear-gradient(180deg,transparent 60%,#FECACA 60%);font-weight:700;color:#1C1917;"><span leaf="">荧光笔效果的重要长句</span></span>
```

### 7f. 行内代码

```html
<span style="background:#F3F4F6;color:#1F2937;padding:2px 6px;border-radius:4px;font-size:14px;font-weight:600;"><span leaf="">code</span></span>
```

---

## 组件 8 引用高亮块（3 种变体）

### 8a. 粉底左竖条金句引用（视觉焦点最强，核心金句）

```html
<section style="background:#FEF2F2;border-radius:0 10px 10px 0;border-left:4px solid #DC2626;padding:18px 22px;margin-bottom:24px;">
  <p style="font-size:16px;font-weight:800;color:#991B1B;margin:0;line-height:1.8;">
    <span leaf="">「{{核心观点或关键金句}}」</span>
  </p>
</section>
```

### 8b. 浅红背景引用块（Prompt / 引用内容）

```html
<section style="background:#FEF2F2;border-radius:10px;padding:18px 20px;margin-bottom:24px;border:1px solid #FECACA;">
  <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    {{引用内容，可含 7d 下划线等内联样式}}
  </p>
</section>
```

### 8c. 灰色左竖条引用（轻量旁注、个人吐槽）

```html
<section style="border-left:4px solid #D6D3D1;padding:14px 20px;margin-bottom:24px;background:#FAFAFA;border-radius:0 8px 8px 0;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;text-align:justify;">
    <span leaf="">{{轻量旁注内容}}</span>
  </p>
</section>
```

### 8d. 居中金句分隔（章节间的过渡金句）

```html
<p style="font-size:15px;margin:0 0 24px;text-align:center;color:#DC2626;font-weight:700;letter-spacing:1px;border-top:1px solid #FEE2E2;border-bottom:1px solid #FEE2E2;padding:14px 10px;">
  <span leaf="">{{居中金句}}</span>
</p>
```

---

## 组件 9 提示 / 警示条

### 9a. 红色提示条（重要提醒、核心结论）

```html
<section style="background:#FEF2F2;border-left:4px solid #DC2626;border-radius:0 8px 8px 0;padding:14px 20px;margin-bottom:24px;">
  <p style="font-size:14px;font-weight:700;color:#991B1B;margin:0;line-height:1.8;">
    <span leaf="">💡 {{重要提示或核心结论}}</span>
  </p>
</section>
```

### 9b. 踩坑提示（灰底，风险/注意事项）

```html
<section style="padding:6px 0 4px;margin-bottom:16px;">
  <p style="margin-bottom:6px;font-size:12px;font-weight:700;color:#9CA3AF;letter-spacing:1px;">
    <span style="color:#DC2626;"><span leaf="">！踩坑提示 🕳</span></span>
  </p>
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.7;">
    <span leaf="">{{提示内容}}</span>
  </p>
</section>
```

---

## 组件 10 内容标签组（STEP / SKILL / TOOL / CASE）

> 教程用 STEP、盘点用 SKILL/TOOL、案例用 CASE。红底白字编号标签 + 标题。

### 10a. step-label（教程步骤）

```html
<section style="margin-bottom:22px;">
  <section style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
    <span style="display:inline-block;background:#DC2626;color:#fff;font-size:11px;font-weight:700;padding:2px 8px;border-radius:4px;"><span leaf="">STEP 01</span></span>
    <span style="font-size:15px;font-weight:800;color:#1C1917;"><span leaf="">{{步骤标题}}</span></span>
  </section>
  <p style="font-size:15px;margin:0 0 16px;color:#374151;line-height:1.8;text-align:justify;">
    {{步骤内容}}
  </p>
</section>
```

`STEP 01` 可替换为 `SKILL 1`、`TOOL 摄像机`、`CASE 01`（盘点/案例场景）；盘点场景标签底色可改灰 `#E5E7EB`+字 `#991B1B` 做次级层次。

### 10b. tool-card（工具/条目说明卡）

```html
<section style="background:#fff;border-radius:12px;padding:16px 20px;box-shadow:0 4px 16px rgba(220,38,38,0.10);margin-bottom:24px;">
  <p style="font-size:14px;color:#374151;margin:0;line-height:1.8;">
    {{条目说明内容}}
  </p>
</section>
```

---

## 组件 11 列表组件

### 11a. ordered-list（红色圆标数字编号列表）

```html
<section style="margin-bottom:24px;">
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#DC2626;color:#fff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">1</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#DC2626;color:#fff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">2</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
  <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">
    <span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#DC2626;color:#fff;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;"><span leaf="">3</span></span>
    <p style="font-size:15px;color:#374151;margin:0;line-height:1.8;flex:1;"><span leaf="">{{列表项内容}}</span></p>
  </section>
</section>
```

### 11b. pill-list（无序要点，红点前缀 + 说明）

```html
<section style="margin-bottom:14px;">
  <p style="margin:0 0 6px;">
    <span style="display:inline-block;font-size:14px;font-weight:700;color:#991B1B;background:#FEE2E2;padding:3px 10px;border-radius:999px;"><span style="display:inline-block;width:6px;height:6px;background:#DC2626;border-radius:50%;margin-right:5px;vertical-align:middle;"><span leaf=""><br></span></span><span leaf="">{{要点标题}}</span></span>
  </p>
  <p style="font-size:14px;color:#4B5563;margin:0;line-height:1.7;text-align:justify;">
    <span leaf="">{{要点说明}}</span>
  </p>
</section>
```

### 11c. timeline（时间线 / 递进脉络，访谈经历、案例演进）

```html
<section style="display:flex;margin-bottom:24px;">
  <section style="display:flex;flex-direction:column;align-items:center;margin-right:16px;flex-shrink:0;">
    <section style="width:14px;height:14px;border-radius:50%;border:3px solid #DC2626;background:#fff;margin-top:4px;"><span leaf=""><br></span></section>
    <section style="width:2px;background:#FEE2E2;flex:1;margin-top:4px;min-height:44px;"><span leaf=""><br></span></section>
  </section>
  <section style="flex:1;padding-bottom:12px;">
    <p style="margin:0 0 6px;font-size:15px;font-weight:800;color:#1C1917;"><span leaf="">{{节点标题}}</span></p>
    <p style="font-size:15px;margin:0;color:#374151;line-height:1.8;text-align:justify;">{{节点内容}}</p>
  </section>
</section>
```

最后一个节点去掉竖线段。

---

## 组件 12 数据 / 要点卡片组

### 两列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:18px 16px;margin-right:8px;text-align:center;border:1px solid #FEE2E2;">
    <p style="font-size:28px;font-weight:900;color:#DC2626;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
  <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:18px 16px;text-align:center;border:1px solid #FEE2E2;">
    <p style="font-size:28px;font-weight:900;color:#DC2626;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:12px;color:#9CA3AF;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 三列版

```html
<section style="display:flex;margin-bottom:24px;padding:0;">
  <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:16px 10px;margin-right:8px;text-align:center;border:1px solid #FEE2E2;">
    <p style="font-size:24px;font-weight:900;color:#DC2626;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
  <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:16px 10px;margin-right:8px;text-align:center;border:1px solid #FEE2E2;">
    <p style="font-size:24px;font-weight:900;color:#DC2626;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
  <section style="flex:1;background:#FEF2F2;border-radius:10px;padding:16px 10px;text-align:center;border:1px solid #FEE2E2;">
    <p style="font-size:24px;font-weight:900;color:#DC2626;margin:0 0 4px;line-height:1;"><span leaf="">{{数字}}</span></p>
    <p style="font-size:11px;color:#9CA3AF;margin:0;"><span leaf="">{{说明}}</span></p>
  </section>
</section>
```

### 表格（真实数据表用）

```html
<section style="margin-bottom:24px;overflow-x:auto;">
  <table style="width:100%;border-collapse:collapse;font-size:14px;">
    <thead>
      <tr>
        <th style="background:#DC2626;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题}}</span></th>
        <th style="background:#DC2626;color:#fff;font-weight:700;padding:8px 12px;text-align:left;"><span leaf="">{{列标题}}</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #FEE2E2;color:#374151;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #FEE2E2;color:#374151;"><span leaf="">{{内容}}</span></td>
      </tr>
      <tr>
        <td style="padding:8px 12px;border-bottom:1px solid #FEE2E2;color:#374151;background:#FEF2F2;"><span leaf="">{{内容}}</span></td>
        <td style="padding:8px 12px;border-bottom:1px solid #FEE2E2;color:#374151;background:#FEF2F2;"><span leaf="">{{内容}}</span></td>
      </tr>
    </tbody>
  </table>
</section>
```

---

## 组件 13 标签胶囊

浅红底深红字（默认）：

```html
<span style="display:inline-block;background:#FEE2E2;color:#991B1B;font-size:12px;font-weight:700;padding:2px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

红色描边（轻量）：

```html
<span style="display:inline-block;border:1px solid #DC2626;color:#DC2626;font-size:12px;font-weight:600;padding:1px 10px;border-radius:4px;margin-right:6px;"><span leaf="">标签名</span></span>
```

---

## 组件 14 图片容器

```html
<section style="background:#FFF;border-radius:12px;padding:6px;border:1px solid #E5E7EB;box-shadow:0 4px 12px -2px rgba(0,0,0,0.08);margin-bottom:10px;">
  <section style="margin:0;border-radius:8px;overflow:hidden;">
    <span leaf=""><img src="{{图片URL}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
</section>
```

带说明文字时，图片 `margin-bottom` 改 `8px`，其后加：

```html
<p style="font-size:12px;color:#9CA3AF;text-align:center;margin:0 0 24px;">
  <span leaf="">— {{图片说明}}</span>
</p>
```

多行代码块用通用增量库 `common-components.md` 的 1a 深色 / 1b 浅色（左竖条换 `#DC2626`），禁 `white-space:pre`。

---

## 组件 15 END 结尾分割线

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin:0 0 32px;">
    <section style="display:flex;align-items:center;justify-content:center;">
      <span style="height:2px;width:60px;background:linear-gradient(to right,transparent,#DC2626);margin-right:12px;"><span leaf=""><br></span></span>
      <span style="font-size:11px;color:#DC2626;letter-spacing:3px;font-weight:700;"><span leaf="">END</span></span>
      <span style="height:2px;width:60px;background:linear-gradient(to left,transparent,#DC2626);margin-left:12px;"><span leaf=""><br></span></span>
    </section>
  </section>
</section>
```

---

## 组件 16 尾部作者签名区

> 固定签名文案以正文段落形式呈现；有个人名片/引导图素材才放图，无素材整块删。

```html
<section style="padding:0 10px;">
  <section style="text-align:center;margin-bottom:10px;border-radius:12px;overflow:hidden;">
    <span leaf=""><img src="{{个人名片或引导图URL，无则删本 section}}" style="max-width:100%;height:auto;display:block;margin:0 auto;"></span>
  </section>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
    <span leaf="">我是 {{作者名}}，{{一句话简介，如：热衷于分享 AI 观察与干货}}。</span>
  </p>
  <p style="margin-bottom:20px;font-size:15px;line-height:1.8;text-align:justify;">
    <span leaf="">如果你觉得今天这篇有收获，欢迎</span>
    <strong style="color:#DC2626;"><span leaf="">点赞、在看、转发</span></strong>
    <span leaf="">三连，我们下篇见。</span>
  </p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">

  <!-- 1. 开头引言卡片（组件2，白底红色光晕） -->

  <!-- 2. 前言正文（组件6 段落 × N，放 0 10px 边距 section，第一章之前的开场白） -->

  <!-- 3. 前言导读（组件3，3+ 章节时生成，精选 3 看点） -->

  <!-- 4. 第一章（组件5 章节标题，margin-top:16px） -->
  <!--    章内：组件6 正文 + 6b 子标题 + 7 行内高亮 + 8 引用 + 9 提示 + 10 标签组 + 11 列表 + 12 数据 + 14 图片 -->

  <!-- 5. 章节分割线（组件4）+ 第二章…第N章（组件5，margin-top:48px） -->

  <!-- 6. 结语章（组件5 变体：编号 ∞，英文 THE END） -->

  <!-- 7. END 分割线（组件15） -->

  <!-- 8. 尾部签名（组件16） -->

</section>
```

**骨架铁律**：引言卡在最前；导读区在前言正文之后、第一章之前；章节之间用组件 4 红色渐变线分隔；一篇只有一个 END + 一个签名区。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 红色加粗 7a / 红底白字（仅引言卡）/ 金句引用 8a | 产品名、关键结论、核心金句 | 全文 ≤5 处 |
| **标记层** | 淡粉下划线 7d（默认）/ 浅红底标签 7b | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 左竖条引用 8x / 提示 9x / 标签组 10 / 卡片 11-12 | 引用、旁注、提示、结构化信息 | 按需 |

**克制原则**：
- 红底白字标签（`bg:#DC2626`）**仅在引言卡内**，正文关键词标签用浅红底深红字 7b
- 红色加粗全文 ≤5 处
- 引用/提示统一用左竖条 + 浅底 + 类型小标签，**不用四周虚线框**（dashed）
- 渐变红仅出现在章节分割线 4 和 END 线 15

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3，避免花哨。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 观点/深度分析 | 正文6 + 金句引用8a + 居中金句8d | 浅红引用8b、踩坑提示9b |
| 教程/操作指南 | step-label 10a + 代码块（通用库1a）+ ordered-list 11a | 红色提示9a、tool-card 10b |
| 盘点/工具清单 | skill/tool-label 10a + tool-card 10b + pill-list 11b | 数据卡12、标签胶囊13 |
| 访谈/人物特稿 | 正文6 + 金句引用8a（引语）+ timeline 11c（经历脉络） | 居中金句8d、灰底旁注8c |
| 数据复盘/报告 | 数据卡12（两列/三列）+ 表格12 + ordered-list 11a | 红色提示9a、荧光笔7e |
| 生活/情感随笔 | 正文6 + 居中金句8d + 灰底旁注8c | 金句引用8a（少量） |
| 案例实战 | case-label 10a / timeline 11c + step-label 10a | 浅红引用8b、踩坑提示9b |

所有类型共用固定结构：引言卡 2 + 导读 3（3+ 章节）+ 编号章节 5 + END 15 + 签名 16。

---

## Markdown → 红白排版 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 不使用 | 公众号文章标题在平台设置 |
| 文章开头 `> 引言金句` | 组件 2 白底红色光晕引言卡 | 视角与外标题错开 |
| `## 章节标题` | 组件 5 章节标题 | 红底编号 01/02…，末章 ∞ + THE END |
| `### 子标题` | 组件 6b 红色左竖条小标题 | 不套编号章节样式 |
| 普通段落 | 组件 6 正文段落 | 每段主动标 1~3 处淡粉下划线 7d |
| `**加粗文字**` | 组件 7a 普通加粗（默认）/ 红色加粗（锚点 ≤5） | 普通加粗为主 |
| `==高亮文字==` | 组件 7b 浅红底深红字标签 | 核心概念 |
| `<u>下划线</u>` / `++文字++` | 组件 7d 淡粉下划线 | 次要强调 |
| `~~删除线~~` | `text-decoration:line-through` + 灰字 | 被淘汰概念 |
| 行内 `` `code` `` | 组件 7f 行内代码 | |
| `> 引用段落`（金句） | 组件 8a 粉底左竖条 | 核心金句 |
| `> 引用段落`（旁注） | 组件 8c 灰底左竖条 | 轻量旁注 |
| 核心金句 | 组件 8a / 8d 居中金句 | 视觉焦点 |
| 操作步骤 | 组件 10a step-label | STEP 01/02… |
| 技能/工具清单 | 组件 10a skill/tool-label + 10b tool-card | |
| 案例/经历脉络 | 组件 10a case-label / 11c timeline | |
| Prompt 提示词 | 组件 8b 浅红引用块 / 通用库 1a（长多行） | |
| ` ``` 多行代码块 ``` ` | 通用库 1a 深色 / 1b 浅色（左竖条换 #DC2626） | 每行一个 `<p style="margin:0">` |
| 并列要点 | 组件 11b pill-list | |
| `1. 2. 3.` 编号列表 | 组件 11a ordered-list | 红色圆标 |
| 数据展示 | 组件 12 数据卡片组 / 表格 | 红色大号数据 |
| Markdown 表格 | 组件 12 表格 | 偶数行浅红底 |
| 注意/警告 | 组件 9a 红色提示 / 9b 踩坑提示 | |
| 行内标签 | 组件 13 标签胶囊 | 浅红底默认 |
| `---` | 组件 4 章节分割线 | 红色渐变 |
| `![](图片)` | 组件 14 图片容器 | 圆角卡片 + 说明 |
| 文末 | 组件 15 END + 16 签名 | |
