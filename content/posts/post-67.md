---
title: "AMDの自動更新ツールに見つかったリモートコード実行の脆弱性、報告から公開までに何が起きたのか"
description: "AMDの自動更新ツール「AMD Auto Updater」は、更新情報を取得するときにHTTPSを使っているが、実際にダウンロードする実行ファイルのURLはHTTPで取得し、ダウンロード後のファイルに暗号学的な署名検証を行わない仕組み..."
date: 2026-06-15T14:46:28+09:00
categories: ["テクノロジー"]
tags: ["AI", "Summary"]
image: "/rss/downloaded_images/ef2fcb3126da8318cd5e7ccbc1df7b20.jpg"
---

## 何が起きているのか
AMDの自動更新ツール「AMD Auto Updater」は、更新情報を取得するときにHTTPSを使っているが、実際にダウンロードする実行ファイルのURLはHTTPで取得し、ダウンロード後のファイルに暗号学的な署名検証を行わない仕組みだった。これにより、同じネットワーク上にいる攻撃者や通信経路を改ざんできる立場の者が、正規の更新ファイルを悪意のある実行ファイルに差し替えることが可能になる。セキュリティ研究者のMrBruh氏がこの脆弱性を発見し、2026年1月にAMDへ報告したが、当初はバグ報奨金プログラムの対象外と判断され、後にブログ公開を経て改めて調査が入り、最終的にCVE-2026-40677として公表された。

## それによって何が引き起こされそうなのか
この脆弱性が放置されると、特に公共のWi‑Fiや企業内ネットワークなど、中間者攻撃が起こり得る環境では、ユーザーが見かけ上の通常のアップデートを実行するだけで、スパイウェアやランサムウェアなどが管理者権限で実行されるリスクが高まる。また、AMDが最初に報奨金対象外とした判断に対して、Hacker NewsやYouTubeチャンネルなどで「バグ報奨金制度のルールが不透明」や「更新メカニズム自体に根本的な欠陥がある」といった批判が広がり、ソフトウェア供給チェーンへの信頼が揺らぐ可能性がある。さらに、研究者が指摘するように、現在の緩和策（CRC‑32チェックのみ）では改ざん防止として十分ではなく、根本的な修正が求められている。

## だからどうなのか
ソフトウェアの更新機構では、取得元の通信を常にHTTPSで保護し、ダウンロードしたファイルに対して暗号学的な署名検証を必ず行うべきである。ベンダーは脆弱性報告に対して透明性を持ち、報奨金プログラムの適用基準を明確にし、研究者と協力して迅速に修正を提供する姿勢が求められる。これにより、中間者攻撃による不正実行のリスクを低減し、ユーザーの信頼を維持できる。

---

## 元スレッド・記事本文

# AMDの自動更新ツールに見つかったリモートコード実行の脆弱性、報告から公開までに何が起きたのか

![](/rss/downloaded_images/ef2fcb3126da8318cd5e7ccbc1df7b20.jpg)


AMDの自動更新ツールにリモートコード実行につながる可能性がある脆弱(ぜいじゃく)性が見つかりました。セキュリティ研究者のMrBruh氏はAMDに報告したものの、中間者攻撃を前提とするため報奨金制度の対象外と判断され、その対応を巡って議論が広がっています。


**The RCE that AMD wouldn’t fix! | MrBruh's Epic Blog**

[https://mrbruh.com/amd2/](https://mrbruh.com/amd2/)


問題となったのは自動更新ツールである** AMD Auto Updater**が更新情報の取得にHTTPSを使っている一方で、実際にダウンロードする実行ファイルのURLにはHTTPが使われていたという点です。さらにMrBruh氏が逆コンパイルして確認したところ、ダウンロードした実行ファイルに対する暗号学的な署名検証は行われず、そのまま実行される仕組みだったとのこと。

この問題により、攻撃者が同じネットワーク上にいる場合や通信経路上でデータを書き換えられる立場にある場合、正規の更新ファイルを悪意ある実行ファイルに差し替えられる可能性があります。特にユーザー側から見ると通常の自動更新に見えるため、スパイウェアやランサムウェアなどが管理者権限で実行されるケースも考えられます。

![](/rss/downloaded_images/84eafd8cdd52788d4101529b6b57b20f.jpg)


MrBruh氏は2026年1月27日にこの脆弱性を発見し、2月6日にAMDへ報告しました。しかし、AMDのバグ報奨金プログラムを担当する** Intigriti**は同日、この報告を「修正対象外かつ報奨金対象外」としてクローズしたとのこと。

その後、MrBruh氏がブログ記事を公開してHacker Newsで話題になると、AMDのPSIRTは改めて調査すると連絡しました。AMD側は「Intigritiが報奨金対象外と判断しても、社内では脆弱性としての妥当性を確認する」と説明し、さらにCVEの発行や修正、研究者としてのクレジット付与を行う方針を示したとされています。


一方で、AMDはMrBruh氏に対してブログ記事の削除を要求し、正式対応が終わるまで公開を待つよう求めました。MrBruh氏はこれに応じたものの、その後の連絡は積極的ではなく、最終的に初回報告から124日後の2026年6月9日が公開日になったと説明しています。


AMDは最終的にこの問題を「** AMD Auto Updater Vulnerability**」として公表し、CVE-2026-40677を割り当てました。AMDは影響を受ける製品として

**や**

[AMD Management Console](https://www.amd.com/en/support/downloads/manageability-tools.html)**、**

[AMD Ryzen Master](https://www.amd.com/ja/products/software/ryzen-master.html)**を挙げています。緩和策としてAMD Management Consoleはバージョン14.0.0、AMD Ryzen Masterはバージョン2.14.3、AMD µProfはバージョン5.3以降への更新が推奨されています。**

[AMD µProf](https://www.amd.com/en/developer/uprof.html)![](/rss/downloaded_images/d8a9525fa02c8902eba20659d738e1cb.jpg)


ただし、MrBruh氏はAMDから「Ryzen Masterでは自動更新機能をインストーラーからアプリケーション層へ移し、更新通信はHTTPSで保護され、更新ファイルは署名検証を受ける」と説明されたものの、実際に確認できたのはCRC-32チェックだったと主張しています。CRC-32はデータ破損の検出には使えますが、攻撃者による改ざんを防ぐための暗号学的な署名検証とは異なるため、MrBruh氏はAMDの説明は正確ではないと批判しています。


さらにMrBruh氏は別の問題としてAMD Auto Updaterがati.comからdrivers.amd.comへのリダイレクトを処理できず、更新処理がクラッシュまたは停止する可能性にも触れています。このため、脆弱性が実際には悪用可能な段階まで到達しない可能性がある一方で、脆弱な更新機構を修正するにはその更新機構自体を更新しなければならないという矛盾した状態になっていたと指摘しています。


ソーシャルニュースサイトの** Hacker News**では、中間者攻撃を理由に報奨金対象外とする判断への批判が相次ぎました。特にHTTPで実行ファイルを配布し追加の署名検証もない場合は単なる特殊条件ではなく、ソフトウェア更新機構として重大な欠陥だという見方が示されています。

また、Hacker Newsでは「バグ報奨金制度の対象外という判断は必ずしも脆弱性としての影響がないことを意味しない」という

**も示されました。**

[見方](https://news.ycombinator.com/item?id=48492487)**では「中間者攻撃は『PCを乗っ取るという観点で対象外』なのではなく、あくまで特定のバグ報奨金プログラムの目的から外れているという意味だ」と指摘されています。**

[あるコメント](https://news.ycombinator.com/item?id=48495932)![](/rss/downloaded_images/ec45d163b7103b997a1d130ce7802db3.jpg)


ゲーミングPCなどのハードウェアに関する話題を扱うYouTubeチャンネル・Gamers Nexusもこの件を取り上げ、「AMDが研究者に対して不誠実な対応を取り、後からルールを変更したかのように見える」と批判しました。


[AMD Gaslights Security Researcher, Changes Rules Retroactively - YouTube](https://www.youtube.com/watch?v=4HjWHNLRMB0)


![](/rss/downloaded_images/6877bba9432b263f710ce1665976258f.jpg)


**・関連記事**

[AMDがハッキングでデータを盗まれたことを認める、重要な情報は流出しておらずビジネスに大きな影響はないと主張 - GIGAZINE](https://gigazine.net/news/20240621-amd-hack-material-impact-on-business)


[AMD製CPUにセキュリティ上の脆弱性があることをGoogleが報告 - GIGAZINE](https://gigazine.net/news/20250204-amd-security-vulnerability)


[パスワードマネージャーのDashlaneがサイバー攻撃を受け暗号化パスワード保管庫を盗まれた経緯を説明 - GIGAZINE](https://gigazine.net/news/20260605-dashlane-how-attackers-managed-encrypted-password)


[Microsoft Defenderの新たなゼロデイ脆弱性「RoguePlanet」、2026年6月10日のWindows Updateのパッチを全て当てた状態でも攻撃されてしまう結果に - GIGAZINE](https://gigazine.net/news/20260610-microsoft-defender-rogueplanet)


[数多くのAMD製CPUで深刻な脆弱性「Sinkclose」が発見される、AMDは修正パッチを配布するも一部の古いモデルには適用されず - GIGAZINE](https://gigazine.net/news/20240813-amd-sinkclose)

**・関連コンテンツ**

in  [ソフトウェア](https://gigazine.net/news/C4/),   [セキュリティ](https://gigazine.net/news/C14/),  Posted by log1i_yk

You can read the machine translated English article ** What happened from the reporting to the …**.
