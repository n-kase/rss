---
title: "複数のAIを組み合わせてClaude Fable超えの性能を実現するシステム「Fusion」をOpenRouterがリリース"
description: "概要と事実 OpenRouterは、異なるAIモデルを組み合わせて実行できる新しいシステム「Fusion」をリリースしました。このシステムは、ユーザーの入力を複数のモデルに並行して送信し、それぞれの応答を審査モデルで読み取って構造化さ..."
date: 2026-06-16T14:06:17+09:00
categories: ["テクノロジー"]
tags: ["Fusion", "OpenRouter", "AIモデル", "ベンチマーク", "バグ修正"]
image: "/rss/downloaded_images/65650910c43ccbb68d392679b5408994.png"
---

## AIによる要約

### 概要と事実
OpenRouterは、異なるAIモデルを組み合わせて実行できる新しいシステム「Fusion」をリリースしました。このシステムは、ユーザーの入力を複数のモデルに並行して送信し、それぞれの応答を審査モデルで読み取って構造化された分析結果を作成し、その結果に基づいて呼び出しモデルが最終的な回答を生成する仕組みです。具体的には、「Claude Opus 4.8とGPT-5.5」や「Claude Opus 4.8とGPT-5.5とGemini 3.1 Pro」などの組み合わせが可能で、これらの組み合わせはベンチマークにおいてAnthropicが最高性能と主張するClaude Fable 5のスコアを上回ることが確認されています。また、コストと性能を示すグラフでは、「Gemini 3 FlashとKimi K2.6とDeepSeek V4 Pro」の組み合わせがClaude Fable 5の約半分のコストでほぼ同等のスコアを達成していることが示されています。Fusionの詳細なドキュメントと試用リンクも公開されており、OpenRouterのアカウントがあればすぐに体験できます。

### ネットの反応と意見の変遷
Fusionのリリース直後、一部のユーザーから審査モデルに意図せずClaude Opus 4.8が呼び出される現象が報告されました。特に、DeepSeek V4 ProとDeepSeek V4 Flash、Kimi K2.6を指定したにもかかわらず、審査モデルとしてClaude Opus 4.8が使われていたことがAPIログから判明し、これがバグではないかと指摘されました。この指摘に対し、OpenRouterの開発者であるToven氏はフロントエンドのバグであることを認め、APIを直接使う場合は問題なく動作すると説明し、修正を約束しました。これにより、当初の期待通りに低コストのオープンモデルだけで高い推論性能を得たいというニーズに応えるための改善が求められる状況となりました。

### 背景と結論
Fusionの登場は、単一の巨大モデルに依存せず、複数の特化したモデルを組み合わせることで性能とコストのバランスを最適化しようとする業界の動きを反映しています。ベンチマーク結果が既存のトップモデルを上回ることから、モデルのアンサンブル手法が実用的な選択肢として注目される可能性が高まります。一方で、審査モデルの固定化というバグは、システムの透明性とユーザーの期待に応えるための重要な課題となります。今後の修正と改善により、Fusionはより柔軟で信頼性の高いマルチモデルAIプラットフォームとして発展していくことが期待されます。

[🔗 元記事を読む](https://gigazine.net/news/20260616-openrouter-ai-fusion/)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

# 複数のAIを組み合わせてClaude Fable超えの性能を実現するシステム「Fusion」をOpenRouterがリリース



![](/rss/downloaded_images/5d62a9728db8bd97005541713ebf010f.png)




AIモデルのAPI提供サービスを展開するOpenRouterが異なるAIを組み合わせて実行できるシステム「**Fusion**」をリリースしました。Fusionは「Claude Opus 4.8とGPT-5.5」「Claude Opus 4.8とGPT-5.5とGemini 3.1 Pro」といったように高性能モデル同士を組み合わせて実行可能で、** Claude Fable 5**を超えるベンチマークスコアをたたき出すことにも成功しています。

**Surpassing Frontier Performance with Fusion — OpenRouter Blog**


[https://openrouter.ai/blog/announcements/fusion-beats-frontier/](https://openrouter.ai/blog/announcements/fusion-beats-frontier/)Fusionは「ユーザーの入力を複数のモデルに並列送信し、各モデルの応答を審査モデルで読み取って構造化された分析結果を生成し、呼び出しモデルで分析結果に基づいた最終的な回答を生成する」という仕組みで動作します。

組み合わせごとのベンチマークスコアを並べたグラフが以下。青色がFusionを用いて複数モデルを組み合わせた結果で、オレンジ色が単一モデルの結果を示しています。「Claude Opus 4.8とGPT-5.5とGemini 3.1 Pro」「Claude Opus 4.8とGPT-5.5」「Claude Opus 4.8を2つ実行」という組み合わせでAnthropicが史上最高モデルとアピールしているClaude Fable 5のスコアを上回りました。



![](/rss/downloaded_images/f9a74296f1e42631443a0d2e18f35304.png)




以下のグラフは横軸がコスト、縦軸がベンチマークスコアを示しています。「Gemini 3 FlashとKimi K2.6とDeepSeek V4 Pro」という組み合わせではClaude Fable 5の半分のコストでベンチマークスコア1％差まで迫っています。




![](/rss/downloaded_images/4531b2330fb6114cd469dd8cb126604c.png)




Fusionのドキュメントは以下のリンク先で公開されています。


**Fusion Server Tool | Multi-model AI Analysis with OpenRouter | OpenRouter | Documentation**

[https://openrouter.ai/docs/guides/features/server-tools/fusion](https://openrouter.ai/docs/guides/features/server-tools/fusion)


また、OpenRouterのアカウントがあれば、以下のリンク先でFusionを用いたチャットを試すことができます。


**Model Fusion | OpenRouter**

[https://openrouter.ai/fusion](https://openrouter.ai/fusion)


なお、Fusionの公開直後の2026年6月14日には「DeepSeek V4 ProとDeepSeek V4 FlashとKimi K2.6」を指定したのに審査モデルとしてClaude Opus 4.8が使われるという事象が報告されていました。


I have tried to use OpenRouter Fusion API with cheap open models only, and saw reasoning that surpasses any of them individually. Then I looked into API logs and saw that this "Fusion" still calls Opus 4.8 as a judge.

— Teortaxes▶️ (DeepSeek 推特🐋铁粉 2023 – ∞) (@teortaxesTex)

I see no way to disable it.

Not cool, OpenRouter. Not cool.[https://t.co/CjC2NjMMNh](https://t.co/CjC2NjMMNh)[pic.twitter.com/ZYUFO95OvB](https://t.co/ZYUFO95OvB)[June 14, 2026](https://x.com/teortaxesTex/status/2066045540031234516?ref_src=twsrc%5Etfw)


OpenRouterの開発者である** Toven**氏は現象がバグであることを認めており、修正を約束しています。

this just seems like a frontend bug and we’ll fix it! using it over the API is the thing we launched yesterday and is much more flexible

— Toven (@pingToven)[June 14, 2026](https://x.com/pingToven/status/2066145112409735581?ref_src=twsrc%5Etfw)

</details>
