---
title: "文章からマンガを生成する東大開発の国産AI「MangaFlow」、軽量0.9Bで巨大モデル超える精度のオープンソース文書解析AI「PaddleOCR-VL-1.6」など生成AI技術5つを解説（生成AIウィークリー） | テクノエッジ TechnoEdge"
description: "概要と事実 今回の「生成AIウィークリー」第147回では、最近注目されているいくつかの生成AI技術が紹介されました。まず、NVIDIAがロボットや自動運転などの物理的なAI向けに開発したオープンソースの世界モデル「Cosmos 3」が..."
date: 2026-06-16T10:00:38+09:00
categories: ["テクノロジー"]
tags: ["生成AI", "NVIDIA", "Google", "マンガ生成", "OCR"]
image: "/rss/downloaded_images/6f26b4af39de83e36909c370f46e23d2.jpg"
---

## AIによる要約

### 概要と事実
今回の「生成AIウィークリー」第147回では、最近注目されているいくつかの生成AI技術が紹介されました。まず、NVIDIAがロボットや自動運転などの物理的なAI向けに開発したオープンソースの世界モデル「Cosmos 3」が発表されました。このモデルは言語、画像、動画、音声、行動という五つの異なるデータタイプを一つの構造で扱えるため、従来は別々に作られていた各種モデルを統合しています。評価ではオープンソースモデルだけでなく、クローズドモデルであるGemini 3.1 Proを上回る性能を示し、いくつかのベンチマークでトップを記録しています。次に、東京大学と香港科技大学（広州）の研究チームが開発した国産AI「MangaFlow」が取り上げられました。このシステムは文章からマンガを自動生成するもので、ストーリー計画、コマ割り、作画、セリフ配置といった作業工程を別々のAIが連携して処理し、キャラクターの一貫性を保つ独自の記憶機能を備えています。さらに、GoogleがノートPCでも動作するマルチモーダルAI「Gemma 4 12B」を発表しました。16GBのメモリがあれば画像や音声も処理でき、従来のエンコーダーを使わない構成により遅延とメモリ消費を抑えながら、性能は大型モデルに近い水準を維持しています。最後に、Baiduが軽量なオープンソース文書解析AI「PaddleOCR-VL-1.6」を公開しました。0.9Bという小さなモデルながら、文書ベンチマークで高い精度を達成し、巨大モデルであるQwen3-VLやGemini 3 Proを上回る結果を示しています。

### ネットの反応と意見の変遷
記事が公開されると、技術系のフォーラムやSNSでは「Cosmos 3」の統合アプローチに対して期待の声が多く上がりました。特にロボット制御や自動運転の分野で、別々に開発されていたモデルを一つにまとめることで開発コストが削減できる点が評価されました。一方で、オープンソースモデルがクローズドモデルを凌駕したという点については、一部のユーザーから「本当に実用レベルで差があるのか」と慎重な見方も見られました。「MangaFlow」については、マンガクリエイターからは「コマ割りやキャラクターのブレを防ぐ仕組みが魅力的」と好意的な反応が多く、実際に試してみたいという声が散見されました。ただし、AIが生成するマンガの著作権やオリジナリティについて懸念する意見もあり、今後のガイドラインが必要だと指摘されるケースもありました。「Gemma 4 12B」は、ノートPCで高性能マルチモーダル処理が可能になるという点で、開発者や学生から「環境を選ばずに実験できる」と歓迎されました。一方で、実際のバッテリー消費や発熱についての疑問も呈され、長時間の使用においては冷却や電源管理が課題になるとの指摘がありました。「PaddleOCR-VL-1.6」については、文書処理の精度が高いことから、企業のバックオフィス作業や行政のデジタル化に役立つと期待する声が多く、特に中小企業向けの導入コストが低い点が強調されました。一方で、特定の言語や特殊なフォーマットに対する適応性については、さらなる検証が必要だとの意見も見受けられました。

### 背景と結論
これらの技術は、AIが単なるデータ処理ツールから、現実世界の様々な領域に直接適用できる実用的なシステムへと進化していることを示しています。統合モデルによる複数モダリティの同時処理は、ロボットや自動運転といった安全性が求められる分野での信頼性向上に寄与する可能性があります。また、創作支援ツールとしての「MangaFlow」は、クリエイターの負担を軽減しながらも芸術性を保つ新しいワークフローを提供するかもしれません。個人デバイスで高性能マルチモーダルAIを動かせる「Gemma 4 12B」は、教育や個人プロジェクトにおけるAIの民主化を促進し、オフライン環境でも高度な処理が可能になる点で、プライバシー保護の観点からも注目されます。さらに、軽量かつ高精度な文書解析AI「PaddleOCR-VL-1.6」は、紙ベースの業務をデジタル化する取り組みを加速させ、特にリソースが限られた現場での導入が容易になるでしょう。全体として、今回紹介された技術は、AIの専門性を高めつつも幅広いユーザー層に使いやすい形で提供される方向性を示しており、今後の社会実装においては、倫理面やセキュリティ面への配慮も同時に進めていく必要があるでしょう。

[🔗 元記事を読む](https://www.techno-edge.net/article/2026/06/15/5182.html)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

この1週間の気になる生成AI技術・研究をいくつかピックアップして解説する今回の「生成AIウィークリー」（第147回）は、NVIDIA開発の物理AI向けオープンソースの世界モデル「Cosmos 3」や、ノートPCで動くGoogleのマルチモーダルAI「Gemma 4 12B」を取り上げます。

また、文章からマンガを生成する国産AI「MangaFlow」や、Baiduが開発した軽量なオープンソース文書解析AI「PaddleOCR-VL-1.6」をご紹介します。

そして、生成AIウィークリーの中でも特に興味深いAI技術や研究にスポットライトを当てる「生成AIクローズアップ」では、使うほど育つ自己改善型AIエージェント「Hermes Agent」の専用デスクトップアプリ「Hermes Desktop」を別の単体記事で取り上げています。

[使うほど育つオープンソースの自律型AI「Hermes Agent」にデスクトップアプリ登場。ターミナル操作不要（生成AIクローズアップ） | テクノエッジ TechnoEdge今回は、Nous Researchが自己改善型AIエージェント「Hermes Agent」の専用デスクトップアプリ「Hermes Desktop」（パブリックプレビュー）を取り上げます。 https://www.techno-edge.net/article/2026/06/08/5153.html続きを読む »](https://www.techno-edge.net/article/2026/06/08/5153.html?utm_source=techno-edge.net&utm_medium=article&utm_content=linkcard_2O48RJUA)



![画像](/rss/downloaded_images/9274a01aa535527a139c705bdc73e622.jpg)



**NVIDIA、物理AI向けオープンソースの世界モデル「Cosmos 3」発表　言語・画像・動画・音声・行動を単一構造で統合**

NVIDIAはロボットや自動運転といったPhysical AI向けのモデル「Cosmos 3」を発表しました。これは言語・画像・動画・音声・行動という5つのモダリティを、単一のアーキテクチャでまとめて処理・生成できる世界モデルです。

これまで、状況を理解する視覚言語モデル、未来を映像で予測する動画生成モデル、動きを決める行動予測モデルは別々に作られてきましたが、Cosmos 3はそれらを一つの枠組みに統合しました。

評価面では、スマートインフラや自動運転の各ドメインではオープンソースモデルだけでなくGemini 3.1 Proなどのクローズドモデルも上回りました。

後処理済みモデルは、Artificial AnalysisのリーダーボードでオープンウェイトのText-to-Image・Image-to-Video部門でいずれも1位、ロボット制御ではRoboLab・RoboArenaの両ベンチマークで1位を獲得しました。

モデルは「Edge」「Nano」「Super」の3サイズが用意され、今回はNanoとSuperが公開されています。



![](/rss/downloaded_images/06f5b606193bad04408aa80984fd4afe.jpg)



**文章からマンガを生成する国産AI「MangaFlow」を東大などが開発**

東京大学と香港科技大学（広州）の研究チームが、文章から一貫性のあるマンガを自動生成するAIシステム「MangaFlow」を発表しました。

従来の画像生成AIでは、マンガのページ全体を一度に出力しようとするため、指定したコマ割りが崩れたり、ページが変わるとキャラクターの見た目まで変わってしまうという大きな課題がありました。

この問題を解決するため、MangaFlowはマンガ制作を人間の作業のように分割しているのが特徴。「ストーリー計画」「コマ割り」「作画」「セリフ配置」などを別々のAIが連携して処理します。

さらに独自の記憶機能を採用し、特定のシーンにおける登場人物のキャラ・シーン・オブジェクトなどの設定をAIが保持することで、複数のコマにわたってキャラクターの姿がブレるのを防いでいます。

また、コマの配置やサイズをユーザーが自由に指定したり、参考となる既存のマンガの構図をそのまま流用したりと、クリエイターの意図を反映した細かな調整ができます。



![](/rss/downloaded_images/3c269a0eeb28fd47424d8cc7c22d76fc.jpg)





![](/rss/downloaded_images/be5b53fbe47b54f971a24b5f4deb3563.jpg)





![](/rss/downloaded_images/f492457a6ec8e78758d3c268eb3a32e8.jpg)





![](/rss/downloaded_images/ade9d5d30840a717219f09445b0c5dc7.jpg)





![](/rss/downloaded_images/111201b97afce346c85e905a6c6b25aa.jpg)





![](/rss/downloaded_images/45dac9eea01bf4ff5f1c72e981b8fcf0.jpg)



**MangaFlow: An End-to-End Agentic Framework for Controllable Story to Manga Generation**

Muyao Wang, Zeke Xie, Yanhao Chen, Lixin Xiu, Hideki Nakayama[Paper](https://arxiv.org/abs/2605.28173)

**Google、ノートPCで動くマルチモーダルAI「Gemma 4 12B」公開**

GoogleはAIモデル「Gemma 4 12B」を発表しました。クラウドに頼らず手元のノートパソコンで動かせるのが特徴で、画像や音声も扱えるマルチモーダルAIでありながら、16GBのメモリがあれば動作します。

小型のE4Bと上位の26B MoEモデルの中間にあたり、中型モデルとしては音声入力に標準対応しました。

従来のマルチモーダルAIは画像や音声を専用のエンコーダーを通してから言語モデルに渡していましたが、これは処理が重くメモリも多く消費します。Gemma 4 12Bはこのエンコーダーを使わず、画像や音声を直接言語モデルに取り込む構成にすることで、動作を軽く、速くしました。

性能は26Bモデルに迫る一方、メモリ消費は半分以下です。オフラインでも音声の文字起こしや翻訳ができ、複雑な処理も手元のパソコンでこなせます。

ライセンスはApache 2.0で自由に利用できます。

[16GB RAMで高性能エージェントが動くGemma 4 12B、Google DeepMindが公開　26B MoEに迫る推論性能、エンコーダなしのマルチモーダル | テクノエッジ TechnoEdge・Gemma 4 12Bはノート PC上で動作可能な高性能マルチモーダルAIモデルで、16GBのVRAMまたは統合メモリで動作する ・エンコーダーフリーのユニファイドアーキテクチャを採用し、視覚・音声入力をLLMバックボーンに直接統合することで低遅延・低メモリを実現 ・Apache 2.0ライセンスで公開され、Hugging Face・Kaggle・各種推論フレームワークに対応 https://www.techno-edge.net/article/2026/06/04/5144.html続きを読む »](https://www.techno-edge.net/article/2026/06/04/5144.html?utm_source=techno-edge.net&utm_medium=article&utm_content=linkcard_88YEVQ0J)



![画像](/rss/downloaded_images/f5853112d37ec3eccd17cfae71d93649.jpg)





![](/rss/downloaded_images/47549f53ce0b371910dbc4e2f22706c2.png)





![](/rss/downloaded_images/6ff4bde7500150e1e726a22ed3b450f3.png)



**Gemma 4 12B**

Google[GitHub](https://github.com/google-gemma) | [Blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) | [Hugging Face](https://huggingface.co/collections/google/gemma-4)

**軽量なオープンソース文書解析AI「PaddleOCR-VL-1.6」をBaiduが発表。0.9Bで巨大モデル超えの精度**

「PaddleOCR-VL-1.6」は、Baiduが発表した文書解析向けの軽量AIモデルです。前バージョンの1.5を改良したもので、0.9Bというコンパクトさを保ちながら、文書ベンチマークのOmniDocBench v1.6で96.33%という最高水準のスコアを達成しました。

ポイントは、学習データをただ増やすのではなく、前モデルが苦手な部分だけを狙って補強したことです。具体的には、画像が少しずれただけで答えが変わる不安定な箇所、似た例が少なくて学習しきれていない箇所、そもそも正解ラベル自体が間違っている箇所、という3つの弱点を見つけ出して重点的に直しました。

結果として、表の認識精度が伸び、実世界に近い条件の文書解析テスト「Real5-OmniDocBench」でも首位になりました。また、235BのQwen3-VLやGemini 3 Proといった大きなモデルすら上回りました。



![](/rss/downloaded_images/6cbec2f604d5b20cdb88c7caa5e7d203.jpg)





![](/rss/downloaded_images/46195274691617e121be2551b2a2f5ef.jpg)





![](/rss/downloaded_images/7443b791d626cc597e6c1260e5fd1459.jpg)



**PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training**

Zelun Zhang, Hongen Liu, Suyin Liang, Yubo Zhang, Yiqing Xiang, Jiaxuan Liu, Ting Sun, Manhui Lin, Yue Zhang, Changda Zhou, Tingquan Gao, Cheng Cui, Yi Liu, Dianhai Yu, Yanjun Ma[Paper](https://arxiv.org/abs/2606.03264) |[ GitHub](https://github.com/PADDLEPADDLE/PADDLEOCR) | [Hugging Face](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6)

</details>
