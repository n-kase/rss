---
title: "日本語対応の音声クローンAI「ZONOS2」が登場、トランプ大統領の声でエヴァンゲリオンについて語らせるデモもあり"
description: "AI企業Zyphraが日本語にも対応したリアルタイム音声合成モデルZONOS2を発表し、トランプ元大統領の声でエヴァンゲリオンのキャラクターについて話すデモなどを公開した。この技術は高精度の声クローンと多言語対応により、エンタメやコン..."
date: 2026-06-15T15:21:58+09:00
categories: ["テクノロジー"]
tags: ["音声合成", "AI", "オープンソース", "デモ", "言語対応"]
image: "/rss/downloaded_images/8ca499045940521c75364cc349b1d0a1.png"
---

## AIによる要約
AI企業Zyphraが日本語にも対応したリアルタイム音声合成モデルZONOS2を発表し、トランプ元大統領の声でエヴァンゲリオンのキャラクターについて話すデモなどを公開した。この技術は高精度の声クローンと多言語対応により、エンタメやコンテンツ制作の現場で個人の声を自由に再現できる可能性が高まり、著作権やなりすましへの懸念も高まっている。したがって、技術の進歩を楽しむ一方で、利用ガイドラインや法的枠組みを整備し、悪用を防ぐ仕組みを早期に構築すべきである。

---

## 元スレッド・記事本文

# 日本語対応の音声クローンAI「ZONOS2」が登場、トランプ大統領の声でエヴァンゲリオンについて語らせるデモもあり

![](/rss/downloaded_images/8ca499045940521c75364cc349b1d0a1.png)


AI開発企業の** Zyphra**が音声合成AI「

**ZONOS2**」を2026年6月12日に発表しました。ZONOS2は人物の声や録音状況を再現しつつ任意のセリフをリアルタイム合成することが可能。日本語にも対応しており、オープンモデルとして公開されています。

**ZONOS2: Real-time TTS with High-Fidelity Voice Cloning**


[https://www.zyphra.com/our-work/zonos2](https://www.zyphra.com/our-work/zonos2)Today we're releasing ZONOS2, our next-generation real-time TTS model with high-fidelity voice cloning.

— Zyphra (@ZyphraAI)

ZONOS2 is the most expressive open-source TTS model, released under Apache 2.0 and available on Zyphra Cloud on[@AMD](https://x.com/AMD?ref_src=twsrc%5Etfw). 🧵[pic.twitter.com/WvI7PXS80M](https://t.co/WvI7PXS80M)[June 12, 2026](https://x.com/ZyphraAI/status/2065498869954490846?ref_src=twsrc%5Etfw)


ZONOS2は人物の音声を再現して任意の文章を読み上げさせる「音声クーロン」が可能な音声合成AIモデルです。総パラメーター数80億、アクティブパラメーター数9億のMoEモデルとして設計されており、旧世代モデルの** Zonos-v0.1**と比べてモデルの規模を大型化しつつ、リアルタイムスループットを4倍に向上させることに成功しています。

ZONOS-v0.1 Betaは合計約60万時間の音声データセットでトレーニングされていましたが、ZONOS2のデータセットは合計200万時間以上に増加しました。これにより、幅広い「言語」「録音条件」「テキスト領域」に対応し、ノイズや非定型的な発話パターンに対する耐性も向上しています。さらに、テキスト入力をUTF-8の生データとして扱うことで日本語・中国語・韓国語といった非ヨーロッパ言語での性能が大幅に向上しています。

ZONOS2の対応言語は以下のとおり。日本語は英語や中国語と並んでティア1言語として位置付けられています。

| ティア | 言語 |
|---|---|
| ティア1 | 英語、中国語、日本語 |
| ティア2 | 韓国語、ロシア語、イタリア語、ポルトガル語、フランス語、 スペイン語、ベトナム語、ドイツ語、ヘブライ語、オランダ語 |
| ティア3 | スウェーデン語、ヒンディー語、タミル語、テルグ語、タイ語、 ノルウェー語、ベンガル語、タガログ語、アラビア語、デンマーク語、 インドネシア語、ポーランド語、ウクライナ語、ルーマニア語、 フィンランド語、ハンガリー語、リトアニア語、エストニア語、 スロバキア語、クロアチア語、ラトビア語 |


音声合成モデルのベンチマークは機械的な評価によって「音声認識モデル(文字起こしモデル)で認識しやすいクリアな音声」が高く評価されがちです。このため、ベンチマークスコアと人間の聴覚での評価が一致しないことがあります。ZONOS2はベンチマーク上のスコアよりも人間にとって自然な音声を重視して設計されています。具体的には、参考音声に含まれる「背景ノイズ」「不自然な声」「その他の歪み」などの再現を重視しているとのこと。



ZyphraはZONOS2の生成例として「ドナルド・トランプ大統領の声で碇シンジや碇ゲンドウについて語らせる」というデモ音声を公開しています。


[リアルタイム音声合成AI「ZONOS2」でドナルド・トランプ大統領に碇シンジや碇ゲンドウについて語らせる例 - YouTube](https://www.youtube.com/watch?v=e9aNZhI-Nds)


![](/rss/downloaded_images/f3802f6244105760ef3b3e10467e5b63.jpg)


「バラク・オバマ元大統領にアメリカ製ガンダム開発計画について語らせる」というデモ音声もあります。


[リアルタイム音声合成AI「ZONOS2」でバラク・オバマ元大統領にガンダム開発計画について語らせる例 - YouTube](https://www.youtube.com/watch?v=CF_iclrgGU4)


![](/rss/downloaded_images/f25f33d243a6486432b35141f04177d4.jpg)


ZONOS2は以下のリンク先でオープンモデルとして公開されています。ライセンスは** Apache License 2.0**です。また、AMDのAIチップを活用したクラウドサービス「Zyphra Cloud」でも利用可能です。

**Zyphra/ZONOS2 · Hugging Face**


[https://huggingface.co/Zyphra/ZONOS2](https://huggingface.co/Zyphra/ZONOS2)![](/rss/downloaded_images/f7e87920621ea3ab2a81a468d4fb7041.png)
