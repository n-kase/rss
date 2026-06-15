---
title: "主戦場はクラウドから「手元のAgent AI」へ　COMPUTEXでNVIDIAとIntelが描いた次世代PCの姿"
description: "2026年6月2日から5日まで台北で開催されたCOMPUTEX TAIPEIは、過去最大規模となる来場者11万人以上、1500社・6000ブースが出展し、閉幕しました。会場の雰囲気からは、NVIDIAが主導する次世代のAIハードウェア..."
date: 2026-06-16T08:39:29+09:00
categories: ["テクノロジー"]
tags: ["COMPUTEX", "RTX Spark", "NVIDIA", "AIエージェント", "Windows PC"]
image: "/rss/downloaded_images/860f1173a5066477dec7fed04fc93f66.jpg"
---

## AIによる要約

2026年6月2日から5日まで台北で開催されたCOMPUTEX TAIPEIは、過去最大規模となる来場者11万人以上、1500社・6000ブースが出展し、閉幕しました。会場の雰囲気からは、NVIDIAが主導する次世代のAIハードウェアが注目を集めており、特に開幕前夜のGTC Taipei 2026で発表された「RTX Spark」が最大の話題となりました。RTX SparkはArmベースのCPUとBlackwell世代のGPUを1つのSoCに統合し、NVLink C2Cで高速に結びつけたチップで、消費電力は約140Wながら最大128GBのユニファイドメモリを備え、数十億〜1000億パラメータ級のローカルLLMを動かすことが可能です。このチップは、これまでデータセンターで行われていたCPU・GPU・大容量メモリの一体設計をWindows PCにもたらすもので、NVIDIAは2013年のTegra 4以来約13年ぶりのWindows向けSoC投入となり、ASUS、Dell、HP、Lenovo、Microsoft、MSIなどから今秋以降に搭載PCが登場する見込みです。

会場では実際の動作機はほとんど展示されず、クローズドなデモでホットモックが披露された程度でしたが、参加者の間では期待と不安が交錯しました。当初は「手元で大規模AIを動かせる」という革新性に興奮する声が多く、特にプライバシー保護やオフライン利用の点で歓迎されました。一方で、価格非公開や実際の製品化スケジュールの不透明さから、ハイエンド仕様のMacと競合できる価格帯に収められるのか疑問視する意見も現れました。議論が進むにつれて、エージェント型AI「OpenClaw」のデモが示され、クラウドに依存せず機密データをローカルで処理できる点が再評価され、ビジネスユーザーや開発者からの関心が高まっていく様子が見られました。

このようにRTX Sparkが市場に投入されれば、個人や中小企業でも高性能なAIモデルを手元で実行しやすくなり、データの外部流出リスクを低減できる可能性があります。さらに、WindowsエコシステムにAI専用ハードウェアが浸透すれば、ソフトウェア開発やコンテンツ制作のワークフローが変わり、クラウドサービスへの依存度が低下する傾向が予想されます。一方で、高価なハードウェアが普及すれば、新たなデジタルディバイドが生じる懸念もあり、価格設定やサポート体制が重要な鍵となるでしょう。

したがって、今回のCOMPUTEXでの発表は、AIの利用をクラウドからエッジへとシフトさせる転換点であり、技術革新とともにアクセシビリティとコストへの配慮が求められるということです。今後は、メーカーが価格透明性を高め、幅広いユーザー層に恩恵が届くよう製品戦略を練ることが、健全な市場成長のために不可欠です。

---

<details>
<summary>元スレッド・記事本文</summary>

「AI Together」をテーマに掲げ、6月2日から5日まで台北で開かれた「[COMPUTEX TAIPEI 2026](https://www.itmedia.co.jp/pcuser/articles/2606/01/news093.html)」は、来場者11万人超、3会場で33カ国／地域から1500社／6000ブースと[過去最大規模で閉幕](https://www.itmedia.co.jp/pcuser/articles/2606/06/news028.html)した。

会場を歩いて感じたのは、2026年の主役がNVIDIAであり、その狙いがAgent AI（エージェント型AI）をクラウドではなく手元で動かす点にあったことだ。

2026年のCOMPUTEX最大の注目は、開幕前夜の「GTC Taipei 2026」で発表された「[RTX Spark](https://www.itmedia.co.jp/pcuser/articles/2606/01/news125.html)」だろう。

RTX Sparkは、Arm CPUとBlackwell世代のGPUを1つのパッケージに収めたSoCだ。CPUの設計はMediaTekが担い、Cortex-X925とA725を合わせて20コアを搭載する。GPU側はGeForce RTX 5070と同じ6144基のCUDAコアを積み、両者をNVLink C2Cの高速リンクで結んでいる。

それでいてパッケージ全体の消費電力は140W前後と低い。これまでデータセンターで実施されていたCPU／GPU／大容量メモリの一体設計を、そっくりWindows PCへ持ち込んだチップでもある。

NVIDIAがWindows PC向けSoCを出すのは、2013年のWindows RTタブレット「Surface 2」に載った「Tegra 4」以来、実に13年ぶりだ。そのTegra 4もArmコアで、Arm版Windowsの先駆けとなるSurfaceと共にWindows RTの不発で姿を消したが、改めて市場に挑戦する形となる。

同社のジェンソン・フアンCEOいわく「Windows誕生から40年、MicrosoftとNVIDIAでPCを再発明する」とのことで、搭載PCはASUSTek Computer、Dell Technologies、HP、Lenovo、Microsoft、MSIなどから今秋以降に出てくる見込みだ。

COMPUTEXの会場では動く実機はほぼ展示されず、会期中にクローズドな場でホットモックがお披露目されたようだ。会場内で画面がついていたのはMicrosoftのSurface開発機くらいで、価格感も非公開だった。もっとも、筆者がMSIブースで聞いた感触では、Spark搭載ノートPCはハイエンド仕様のMacに張り合える価格に収めたい意向らしい。

RTX Sparkの肝は、CPUとGPUがメモリを共有するユニファイドメモリ構造だ。ユニファイドメモリは最大128GB搭載可能であり、数十億〜100億パラメータ級のローカルLLMを手元で走らせることができる。

そんなRTX Sparkは、「[DGX Spark](https://www.itmedia.co.jp/pcuser/articles/2605/27/news106.html)」とほぼ同一のものとみられる。DGX Sparkは、NVIDIAがRTX Sparkに先んじて投入していた小型のAI開発機だ。

独自のLinuxを積んだ開発者／エンタープライズ向けのミニPCで、最大2000億パラメータ級のモデルまで手元で走らせられる卓上のスーパーコンピューターをうたう。RTX Sparkは、要するにこの中身をWindowsに載せ替えたものと考えてよいだろう。

NVIDIAの会場では、DGX Sparkを使ったエージェント型AI「OpenClaw」がクラウドにつながず手元で動くデモが示されていた。各ブースの主役も、データを外部に出さず、機密データを抱えたまま自律的にファイルを開き、コードを実行し、結果まで検証する「ローカルAIエージェント」だった。

RTX Sparkでは、こういったユースケースをWindowsのノートやミニデスクトップで実現し、一般のユーザーに届けることができるようになると予測できる。

Copyright © ITmedia, Inc. All Rights Reserved.

</details>
