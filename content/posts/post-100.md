---
title: "主戦場はクラウドから「手元のAgent AI」へ　COMPUTEXでNVIDIAとIntelが描いた次世代PCの姿"
description: "2026年6月2日から5日まで台北で開催されたCOMPUTEX TAIPEIは、「AI Together」をテーマに掲げ、過去最大となる11万人以上の来場者と1500社・6000ブースが集まった。その中で注目を集めたのは、NVIDIA..."
date: 2026-06-15T14:56:23+09:00
categories: ["テクノロジー"]
tags: ["AI", "Summary"]
---

## 何が起きているのか
2026年6月2日から5日まで台北で開催されたCOMPUTEX TAIPEIは、「AI Together」をテーマに掲げ、過去最大となる11万人以上の来場者と1500社・6000ブースが集まった。その中で注目を集めたのは、NVIDIAが発表したRTX SparkというSoCで、ArmベースのCPUとBlackwell世代のGPUを1チップに統合し、消費電力を抑えながら大容量のユニファイドメモリを提供する設計だった。このチップはWindows PC向けに今秋以降、主要PCメーカーから発売される見込みで、データセンターで行われていたCPU・GPU・メモリの統合を個人用ノートやミニデスクトップに持ち込む狙いがある。

## それによって何が引き起こされそうなのか
RTX Sparkの登場により、高性能なAIエージェントをクラウドに頼らず手元のPCで動かすことが現実的になる。これにより、機密データを外部に送らずにローカルで処理できるプライバシー重視の利用が広がり、企業や個人のセキュリティ意識が高まる可能性がある。また、ArmベースのWindowsエコシステムが再び活性化し、従来のx86中心のPC市場に競争が生まれ、価格や性能面での選択肢が増えることが予想される。さらに、開発者はローカルで大規模言語モデルを扱いやすくなるため、AIアプリケーションの迅速なプロトタイピングや教育現場での活用が促進されるだろう。

## だからどうなのか
今回の動きは、AI処理をクラウドからエッジへとシフトさせる大きな転換点であり、プライバシー保護と即応性を両立させるために、ハードウェアとソフトウェアの統合が今後さらに進むことを示している。したがって、個人・企業はローカルAIを活用できる環境を早期に整備し、データの機密性を守りながらAIの恩恵を受ける準備をするべきである。

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
