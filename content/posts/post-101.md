---
title: "主戦場はクラウドから「手元のAgent AI」へ　COMPUTEXでNVIDIAとIntelが描いた次世代PCの姿"
description: "2026年6月に台北で開催されたCOMPUTEX TAIPEIは、過去最大規模の来場者数を記録し、NVIDIAが発表したArm CPUとBlackwell GPUを統合したSoC「RTX Spark」が注目を集めた。このチップはデータ..."
date: 2026-06-15T15:46:48+09:00
categories: ["テクノロジー"]
tags: ["NVIDIA", "RTX Spark", "COMPUTEX", "Windows PC", "AIエージェント"]
---

## AIによる要約
2026年6月に台北で開催されたCOMPUTEX TAIPEIは、過去最大規模の来場者数を記録し、NVIDIAが発表したArm CPUとBlackwell GPUを統合したSoC「RTX Spark」が注目を集めた。

このチップはデータセンター向けの統合設計をWindows PCに持ち込み、ユニファイドメモリによりローカルで大規模言語モデルを動かすことが可能となり、エージェント型AIのデモも披露された。

これにより、クラウドに依存しないプライベートAI利用が広がり、セキュリティや遅延の懸念が緩和される一方、ハードウェアの高度化が一般ユーザーにも届く可能性が示された。

したがって、今後はハードウェアとソフトウェアの統合が進む中で、プライバシーを守りながら高度なAIを手軽に使える環境整備が求められるという教訓が得られる。\n

---

## 元スレッド・記事本文

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
