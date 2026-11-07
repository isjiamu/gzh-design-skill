> 🏠 **メインのリポジトリ：[github.com/isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) ｜ AtomGit のミラー**：[atomgit.com/zuiyn/gzh-design-skill](https://atomgit.com/zuiyn/gzh-design-skill)

> 🤝 **Jiamu × [Moyu Xiaoli（摸鱼小李）](https://mp.weixin.qq.com/s/EMahAzgfAbRQrYukWE7_IQ) の共同プロジェクト** — コンポーネント、テーマのデザイン、品質の基準は、2 人の作者による WeChat 公式アカウントでの実際の発信の経験から形づくられています。Xiaoli に特に感謝します。

<div align="center">

# gzh-design-skill · WeChat のレイアウトスキル

**Markdown を、WeChat のエディターにそのまま貼り付けられる洗練された HTML に変えます**

厳選した 6 つのテーマ + テーマジェネレーター · コードブロック / 画像 / GIF · 節の番号とキーワードのマークを自動で付与 · 2 段階の品質チェック

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/code)
[![Themes](https://img.shields.io/badge/themes-6%20+%20generator-059669)](references/theme-index.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Agents](https://img.shields.io/badge/Claude%20Code%20·%20Codex%20·%20Cursor-supported-8b5cf6.svg)](#-クイックスタート)

[English](README.en.md) ｜ [中文](README.md) ｜ 日本語

</div>

---

AI エージェント（Claude Code / Codex / Cursor …）のためのレイアウトのスキルです。あなたが Markdown を書くと、**WeChat のエディターに貼り付けても崩れない、完全にインライン化したスタイル** の HTML を描画します。節の番号の自動付与、キーワードの下線、導入のカード、コードブロック、画像、統合された作者の署名などに対応し、WeChat のプラットフォームの制限はスクリプトが決定論的に守らせます。

## ✨ 特徴

- **厳選した 6 つのテーマ**：Moyu Green（デフォルト）· Red & White · Graphite Minimal · Zen Whitespace · Moyu Ticket · Olive Journal。どれも自己完結した厚いコンポーネントライブラリです（デザイントークン + 数十のコンポーネント + 視覚的な階層の表 + 記事の種類ごとのレシピの表）。
- **テーマジェネレーター**：合うものがない？ スタイルを 1 行で説明するか、参考の画像を渡すと、新しいコンポーネントライブラリを生成し、再利用できるように保存します（`references/theme-generator.md` をご覧ください）。
- **コンテンツの全面的な対応**：コードブロック（ダーク / ライト、等幅）、画像、GIF（動くことを示すバッジ付き）、インラインコード、引用、リスト、製品のバッジ。
- **賢いレイアウト**：節の番号の自動付与（最後の章は ∞ / ///）、段落ごとに 1～3 個のキーワードの下線、本文から抽出した導入のカードと目次、重複を除いた署名。
- 本文では **全角の CJK の句読点** を使い、コードブロックの中ではそのまま残します。
- **貼り付けても崩れない**：すべてのスタイルをインライン化し、すべてのテキストのノードを `<span leaf="">` で包み、WeChat が取り除いてしまう `<style>/<div>/class/grid/position` を避けます。
- **2 段階の品質チェック**：`component_lint.py`（ライブラリのソース）+ `validate_gzh_html.py`（最終的な出力）で、編集 → 検証 → 修正の再現可能なループを作ります。
- **ワンクリックでコピー**：**Copy** ボタン付きのプレビューページで、クリックするとリッチテキストがコピーされ、WeChat にそのまま貼り付けられます。手で全選択する必要はありません。

## ✅ 向いているもの / ❌ 向いていないもの

**✅ 向いているもの**：意見 / 分析 · チュートリアル / ハウツー · レビュー / ツールのまとめ · 知識のメモ / 方法論 · インタビュー / 特集 · データの振り返り · ライフスタイル / 個人のエッセイ · 事例の研究。Markdown / Word / PDF / プレーンテキストの長文を、貼り付けられる WeChat の HTML に変えます。説明や参考の画像から独自のテーマを生成することもできます。

**❌ 向いていないもの**：一般的な Web / ランディングページ（フロントエンドのスキルを使ってください）· スライド（PPT のスキルを使ってください）· 画像だけのポスター / SNS のカード（ソーシャルカードのスキルを使ってください）· WeChat 以外のレイアウト · **記事を書くこと**（このスキルはレイアウトだけを行うので、先に Markdown を用意してください）。

## 🗂 よくある使い方

| コンテンツ | レイアウトの方法 |
|---|---|
| 意見 / 深い長文 | Red & White か Graphite Minimal。キーワードの下線 + 引用の強調 |
| 製品のレビュー / ツールのまとめ | Moyu Green か Moyu Ticket。手順 / ツールのラベル + カードを、レシピに沿って |
| チュートリアル / ハウツー | Moyu Green。手順のラベル + コードブロック + 番号付きのリスト |
| データの振り返り / 年次レポート | Moyu Green か Olive Journal。データのカード + 表 |
| 禅 / ミニマルなエッセイ | Zen Whitespace。たっぷりの余白 + 中央寄せのセリフ体の引用 |
| 編集後記 / 深いレビュー | Olive Journal。編集者のメモ + 節 + 暗い色のまとめの枠 |
| Word / PDF の下書き → WeChat | 形式を自動で整える → その後、テーマに合わせてテーマを選ぶ |
| 組み込み以外のスタイル | テーマジェネレーター：1 行か 1 枚の画像から作ります |

## 🎨 厳選した 6 つのテーマ

1 本の長文の記事を、6 つのテーマすべてでレイアウトしたものです（実際の画像を使った、元の品質のままのスクリーンショット）。

<table>
<tr>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-green.png?v=1" width="250"><br><sub><b>Moyu Green (default)</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-red-white.png?v=1" width="250"><br><sub><b>Red & White</b></sub></td>
<td width="33%" align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-graphite-minimal.png?v=1" width="250"><br><sub><b>Graphite Minimal</b></sub></td>
</tr>
<tr>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-zen-whitespace.png?v=1" width="250"><br><sub><b>Zen Whitespace</b></sub></td>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-moyu-ticket.png?v=1" width="250"><br><sub><b>Moyu Ticket</b></sub></td>
<td align="center"><img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/lf-olive-journal.png?v=1" width="250"><br><sub><b>Olive Journal</b></sub></td>
</tr>
</table>

> 📚 **6 つのテーマすべて → [docs/all-themes.md](docs/all-themes.md)**　|　または `docs/gallery/index.html` を開くと、インタラクティブな完全版の HTML を見られます。

### テーマの早見表

| | テーマ | 向いているもの |
|---|---|---|
| ![](https://placehold.co/12/059669/059669.png) `#059669` | Moyu Green（デフォルト） | チュートリアル、レビュー、チェックリスト、ツールのまとめ |
| ![](https://placehold.co/12/DC2626/DC2626.png) `#DC2626` | Red & White | 深い分析、意見、はっきりした主張 |
| ![](https://placehold.co/12/52525B/52525B.png) `#52525B` | Graphite Minimal | デザイン、技術の論評、高級なブランド |
| ![](https://placehold.co/12/4A5D52/4A5D52.png) `#4A5D52` | Zen Whitespace | 禅、ミニマルな暮らし、内省的なエッセイ |
| ![](https://placehold.co/12/059669/059669.png) `#059669` | Moyu Ticket | ツールの比較、クリエイティブなレビュー（チケットのモチーフ） |
| ![](https://placehold.co/12/1e1f23/1e1f23.png) `#1e1f23` | Olive Journal | 編集後記、深いレビュー、事例の振り返り |

> 各テーマの英語の識別子、ライブラリのファイル、下線の CSS は、[`references/theme-index.md`](references/theme-index.md) をご覧ください。別のスタイルが必要ですか？ [テーマジェネレーター](references/theme-generator.md)で AI に作ってもらいましょう。

## 🚀 クイックスタート

```bash
# One-line install (recommended)
npx skills add https://github.com/isjiamu/gzh-design-skill

# Or manual clone
git clone https://github.com/isjiamu/gzh-design-skill.git ~/.claude/skills/gzh-design
```

または **どのエージェント**（Claude Code / Codex / Cursor …）にでも、こう頼むだけです。

> https://github.com/isjiamu/gzh-design-skill にあるスキルを見つけてインストールしてください

インストールしたら、エージェントにこう伝えます。

> `article.md` を Moyu Green のテーマで WeChat の HTML にレイアウトしてください。

## 💬 コミュニティ

スキャンして **公式の WeChat Work のグループ** に参加してください（動的な QR コード、自動で招待されます）。WeChat のレイアウトと Agent Skills について話しましょう。

<img src="https://github.com/isjiamu/gzh-design-skill/releases/download/assets-v1/group-qr.png" width="220" alt="WeChat Work のグループの QR コード">

> QR コードの期限が切れていますか？ WeChat で **`zuiyn_soul`** を追加すると（メモに「gzh-design」と書いてください）、招待してもらえます。

## 📖 ワークフロー

1. **テーマを選ぶ** — テーマの内容に最も合うものを自動で提案し、確認を求めます（デフォルトは Moyu Green）。自分で指定するか、新しいテーマを生成することもできます。
2. **ライブラリを読み込む** — 選んだテーマのライブラリ + 共通の増分ライブラリ（コード / 画像 / ラベル）。
3. **Markdown を解析する** — 見出し、章、太字、ハイライト、引用、画像、コード、リスト。
4. **HTML を組み立てる** — 実際のコンポーネントから組み立て、番号、下線、全角の句読点、署名を適用します。
5. **検証する** — `validate_gzh_html.py` を実行し、0 ERROR のときだけ出力します。
6. **出力する** — きれいな断片 + **Copy** ボタン付きのプレビューページです。開いて「Copy to WeChat」をクリックし、エディターに貼り付けます（手で全選択する必要はありません）。

## 🧩 プラットフォームの制限（強制）

出力は次を守ります。`<style>/<script>/<div>`、`class/id`、`position:fixed/absolute/sticky`、`float`、`@media/@keyframes`、`display:grid`、CSS 変数、外部のフォントを使いません。すべてのスタイルをインライン化し、すべてのテキストのノードを `<span leaf="">` で包みます。モデルの規律ではなく、スクリプトで決定論的にチェックします。

## 🔁 検証できるループ

```bash
python3 scripts/component_lint.py .            # source gate: anti-patterns in libraries
python3 scripts/validate_gzh_html.py out.html  # output gate: final HTML compliance
```

ソースの関門では、`white-space:pre`（空白の膨張）、本文の四周を囲む破線の枠、プラットフォームで禁止されている項目を指摘し、0 ERROR でなければなりません。出力の関門では、禁止されたタグ、`<span leaf>` での包み方、半角の句読点を指摘し、0 ERROR / 半角の WARN 0 でなければなりません。

## 💡 こう作った理由

- **自由より制約** — あらかじめ決めた配色 + 固定のコンポーネントで、毎回モデルに即興させるのではなく、品質の下限を固定します。
- **貼り付けても崩れない設計** — スタイルを完全にインライン化し、すべてのテキストのノードを `<span leaf="">` に入れて、WeChat のエディターが取り除くものをまさに避けます。
- **規律ではなくスクリプトで品質を保つ** — 2 つの関門（ソースでの `component_lint` + 出力での `validate_gzh_html`）で、プラットフォームのルールと句読点を決定論的にチェックします。
- **モデルに依存しない** — レイアウトのロジックは、特定のモデルの技ではなく、ライブラリとスクリプトにあります。Claude / GPT / Gemini / 中国のモデルのどれでも同じ結果になります。
- **エージェントにやさしい** — 入力と出力は、どのエージェントでも読み書き、編集、検証できるプレーンテキストの Markdown / HTML で、Claude Code / Codex / Cursor にそのままなじみます。

## 📁 構成

```
gzh-design/
├── SKILL.md                 # layout workflow (agent entry)
├── references/              # 6 theme libs + generator + shared lib + theme-index + eval-cases
├── scripts/                 # validate_gzh_html.py + component_lint.py
├── assets/                  # sample-article.md + theme-previews/
└── docs/gallery/            # browser preview of themes
```

## 🎯 原則

- **自由より制約** — あらかじめ決めた配色と固定のコンポーネントで、品質の下限を保証します。
- **決定論はスクリプトに** — 厳格なルールはリンターに任せ、モデルは内容だけを判断します。
- **破線の枠ではなく小さなラベル** — 強調には左の縦線やピル型のラベルを使い、破線の枠は中央寄せの「素材のプレースホルダー」専用にします。
- **再現できる** — 得た教訓はすべて注意点かチェックになり、検証できるループで守られます。
- **モデルに依存しない** — 有能な LLM ならどれでも動きます（Claude、GPT、Gemini に加え、DeepSeek、Kimi、Qwen、GLM などの中国のモデルも）。レイアウトはライブラリとリンターにあり、モデルに固有の技ではないので、モデルを替えても同じ結果になります。
- **自由な選択よりレシピ** — まずテーマの記事の種類ごとのレシピの表からコンポーネントの組み合わせを選び、それから組み立てます。同じジャンルの記事は見た目の一貫性が保たれます。
- **控えめな色** — メインの色は要所だけに使い（記事あたり 5 か所以下）、大部分は白 + グレーで、色は句読点のように使います。

## 🧠 自分のテーマを作る

### テーマの生成 — 1 行か 1 枚の参考の画像から

組み込みの 6 つでは足りませんか？ AI に作ってもらいましょう。[`references/theme-generator.md`](references/theme-generator.md) の 2 つ目のワークフローで進めます。

1. **好みを集める**（まとめて尋ねます）：テーマの説明は必須です（または参考の画像）。名前 / 色 / フォント / 角の丸み / 影 / 用途は、空欄なら自動で埋められます。
2. **ブロックのライブラリを生成する**：インラインスタイルの完全な HTML のブロックを 45～75 個、`assets/theme-previews/{id}.html` に保存します。ブラウザーでページ全体を一度に確認できます。
3. **変換して登録する**：それを `references/theme-{id}.md` に変換し（`<span leaf>` を追加し、必須の 5 つの節を入れます）、theme-index に登録して、`component_lint.py` を 0 ERROR で通します。
4. **以後は正式なテーマとして**：組み込みのテーマとまったく同じように使えます。

> 試してみてください：*「新しい WeChat のテーマを作って — モノトーンの雑誌風、クラインブルーのアクセント、セリフ体」* または *「この参考の画像からコンポーネントライブラリを作って」*。

### 配色 — AI が自動で埋められる、繰り返し使える配色の構造

どのテーマも、役割が決まった **デザイントークンの配色** の上に作られています。見分けやすい **メインの色**（要所だけ、記事あたり 5 か所以下）、カード / 引用 / ラベルの背景に使う、その **薄い色合い**、ハイライトに使う **対照的なアクセント** 1 色、テキストの約 90% を担う **中間のグレーの階調**、そして段落ごとのキーワードのマークに使う **薄い下線の色** です。控えめにすることが大事で、大部分は白 + グレー、色は句読点としてだけ使い、段落あたりのハイライトは 2 か所以下にします。

メインの色か雰囲気を伝えるだけで、ジェネレーターが読みやすいコントラストを保った調和のとれた配色全体（色合い、枠線、ハイライト、グレー、下線）を導き出します。

> *「#7C9EB2 のミスティーブルーをメインの色にして、爽やかな旅行エッセイ向けの WeChat のテーマを作って。」*

## ❓ FAQ

**WeChat に貼り付けてもスタイルは崩れませんか？** はい。すべてインライン化され、すべてのテキストのノードが `<span leaf="">` で包まれていて、バリデーターがそれを強制します。

**自分のテーマを追加できますか？** 2 つの方法があります。（1）`references/theme-generator.md` を使って AI に生成してもらう。（2）`CONTRIBUTING.md` に従って手で書き、PR を出す。

**一度に複数のテーマで出力できますか？** はい。「これをこれらのテーマでそれぞれレイアウトして」と言えば、選べるようにまとめて作ります。

**どうやって更新しますか？** `npx skills add https://github.com/isjiamu/gzh-design-skill` をもう一度実行するか、インストールしたディレクトリで `git pull` します。

**エージェントの出力が準拠していなかったら？** `scripts/validate_gzh_html.py` を実行し、ERROR が出たら、2 つの関門が両方とも通るまで修正します。それでも解決しなければ、Issue を作成してください。

## ⭐ Star History

このプロジェクトが役に立ったら、Star をいただけるととても励みになります 🙏

<a href="https://www.star-history.com/?repos=isjiamu%2Fgzh-design-skill&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&theme=dark&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=isjiamu/gzh-design-skill&type=date&legend=top-left&sealed_token=OSZCPLO_3NeTUKAtXcnNT6T3HuZwlFsH1HDGh6BcU0G2bdOm-5snTE01rzgYkwgNkF0pvraNI226pwK4jt9zYc4YuJ196yA1fcRRZKmfVQDMWqtE87dHqXn1E4v2q1mCWNFHzXAGJrCMEHx_0wwNmIVOg5nOaNCtRUYS2C_E1IlITdmy_yv7vpyVxqti" />
 </picture>
</a>

## 🤝 コントリビュート · 📄 ライセンス

[CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。**Jiamu × Moyu Xiaoli** の共同制作で、コンポーネントライブラリとテーマのデザインの基準は、2 人の作者の WeChat 公式アカウントでの発信の経験から生まれました。

**AGPL-3.0 © 2026 Jiamu × Moyu Xiaoli.** 主な条件：

1. **帰属の表示が必要** — 著作権と共同作者の表示を残してください。
2. **派生物はオープンソースに** — 変更したバージョン、フォーク、再配布は、完全なソースとともに AGPL-3.0（または互換のライセンス）で公開する必要があります。
3. **ネットワークでの利用も公開が必要** — 変更したバージョンを SaaS / Web サービスとしてデプロイするだけでも（コードを配布しなくても）、ソースの公開が必要です。これが AGPL を GPL と分ける点です。
4. **クローズドソース、独占的、有料限定での配布はできません。**

全文は [LICENSE](LICENSE) にあります。

> 🤝 **AI エージェントとモデルのベンダーとの共創を歓迎します**：gzh-design を自社の製品に組み込みたい、または深く共同で開発したいとお考えですか？ ぜひお願いします。共創の契約については Jiamu にご連絡ください。
