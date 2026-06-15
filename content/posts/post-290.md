---
title: "文章からマンガを生成する東大開発の国産AI「MangaFlow」、軽量0.9Bで巨大モデル超える精度のオープンソース文書解析AI「PaddleOCR-VL-1.6」など生成AI技術5つを解説（生成AIウィークリー） | テクノエッジ TechnoEdge"
description: "今回の「生成AIウィークリー」では、NVIDIAが物理AI向けに言語・画像・動画・音声・行動を一つのアーキテクチャで統合したオープンソース世界モデル「Cosmos 3」を発表し、東京大学などが文章から一貫性のあるマンガを生成する国産A..."
date: 2026-06-15T16:43:23+09:00
categories: ["テクノロジー"]
tags: ["生成AI", "NVIDIA", "Gemma 4 12B", "MangaFlow"]
image: "/rss/downloaded_images/9274a01aa535527a139c705bdc73e622.jpg"
---

## AIによる要約
今回の「生成AIウィークリー」では、NVIDIAが物理AI向けに言語・画像・動画・音声・行動を一つのアーキテクチャで統合したオープンソース世界モデル「Cosmos 3」を発表し、東京大学などが文章から一貫性のあるマンガを生成する国産AI「MangaFlow」を公開、GoogleがノートPCで動作するマルチモーダルAI「Gemma 4 12B」をリリース、Baiduが0.9Bの軽量ながら大規模モデルに匹敵する精度を実現した文書解析AI「PaddleOCR-VL-1.6」を明らかにしました。これらの動向は、モダリティを統合しつつ軽量化・ローカル実行を進める傾向を示しており、ロボットや自動運転、クリエイティブ作業、日常のドキュメント処理など幅広い分野でのAI活用が加速し、オープンソースエコシステムの拡張や開発ハードルの低下が期待されます。したがって、開発者は複数の入力を直接扱える統合アーキテクチャと、エッジデバイスでも動作する効率的なモデル設計を優先すべきであり、これにより実用的なイノベーションが促進され、社会全体へのAIの浸透がさらに進むでしょう。

---

## 元スレッド・記事本文

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
