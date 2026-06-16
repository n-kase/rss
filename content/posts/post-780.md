---
title: "Google Chromeの次回のアップデートでついにuBlock Originなど人気の広告ブロッカーが使えなくなる"
description: "概要と事実 GoogleはChromeの拡張機能フレームワークをManifest V2からManifest V3へ移行し、旧仕様のサポートを段階的に終了しています。これにより、uBlock Originなどの主要な広告ブロッカー拡張機..."
date: 2026-06-16T13:23:33+09:00
categories: ["テクノロジー"]
tags: ["Chrome", "Manifest V3", "uBlock Origin", "広告ブロッカー", "セキュリティ"]
image: "/rss/downloaded_images/14659df410a032ff903b325fbc5288b4.png"
---

## AIによる要約

### 概要と事実
GoogleはChromeの拡張機能フレームワークをManifest V2からManifest V3へ移行し、旧仕様のサポートを段階的に終了しています。これにより、uBlock Originなどの主要な広告ブロッカー拡張機能は、従来の柔軟な通信制御が難しくなり、Chrome上での機能が制限される見込みです。具体的には、Manifest V2で利用できていたwebRequestBlockingによるリアルタイムの判定・変更が制限され、declarativeNetRequestに基づくルール方式に従う必要があります。

Googleは2024年頃からManifest V2の段階的廃止を開始し、2025年7月24日にすべてのユーザーでManifest V2拡張機能を無効化しました。さらにChrome 150では「ExtensionManifestV2Disabled」フラグが削除され、Chrome 151以降では残りの関連フラグも順次削除される見通しです。これにより、Manifest V2ベースの広告ブロッカーをChromeで使い続ける余地は大きく狭まっています。

一方で、広告ブロックは単なる利便性だけでなくセキュリティ対策としても重要です。アメリカのサイバーセキュリティ・インフラセキュリティ庁(CISA)は、悪質な広告や危険なサイトへのリダイレクトを減らし、ページ読み込みを改善し、第三者によるデータ収集リスクを下げる手段として広告ブロックソフトの利用を推奨しています。ただし、CISAは広告ブロッカーが高い権限で動作し、データ収集や悪意ある行為のリスクがあることにも注意を促しています。

### 背景と結論
今回の変更は、Chromeの安全性を高めるための技術的整理と、拡張機能の悪用リスクを低減させる狙いがあります。しかし、ユーザーにとっては不要な広告やトラッカーを避ける手段が制限されるため、BraveやFirefoxなど広告ブロッカーがそのまま使えるブラウザへの移行が選択肢として挙げられています。これにより、ブラウザ間の競争が激化し、ユーザーの選択肢が広がる可能性もあります。

結論として、GoogleのManifest V3への移行はセキュリティとプラットフォームの安定性を優先する方針を示していますが、同時にユーザーの広告ブロッキングニーズに応える代替手段の提供が求められています。今後は、広告ブロッカーの機能をManifest V3の枠組み内でどう維持・改善していくかが、ユーザーと開発者の関心の焦点となるでしょう。

[🔗 元記事を読む](https://gigazine.net/news/20260616-google-chrome-update-disable-adblockers/)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

# Google Chromeの次回のアップデートでついにuBlock Originなど人気の広告ブロッカーが使えなくなる



![](/rss/downloaded_images/14659df410a032ff903b325fbc5288b4.png)




Googleは、Chromeの拡張機能フレームワークをManifest V2から** Manifest V3**へ移行し、旧仕様のサポートを段階的に終了しています。この変更により、uBlock Originのような主要な広告ブロック拡張機能は、Chrome上で従来の仕組みを維持しにくくなっています。

**Chrome update will soon disable adblockers for good | Cybernews**


[https://cybernews.com/security/chrome-update-disables-adblockers-manifest-v3/](https://cybernews.com/security/chrome-update-disables-adblockers-manifest-v3/)**Google Chrome update will fully close the door on ad blockers**


[https://9to5google.com/2026/06/15/google-chromes-next-update-will-mark-the-end-of-popular-ad-blockers/](https://9to5google.com/2026/06/15/google-chromes-next-update-will-mark-the-end-of-popular-ad-blockers/)Manifest V3でも広告やトラッカーを表示前に遮断することは可能ですが、Manifest V2で使われていたwebRequestBlockingによる通信ごとの柔軟な判定・変更は制限され、declarativeNetRequestに基づくルール方式に従う必要があります。「どのサイトからどのサイトへの通信か」といった文脈に応じて細かく制御する高度な動的フィルタリングはManifest V2時代ほど柔軟には実現できなくなりました。


Googleは2024年頃からManifest V2を段階的に廃止し、2025年7月24日にすべてのユーザーでManifest V2の拡張機能を** 無効化**しました。


[Googleが拡張機能仕様「Manifest V2」の段階的廃止を開始 - GIGAZINE](https://gigazine.net/news/20240601-google-manifest-v2-phase-out-begins/)

![](/rss/downloaded_images/0c600a0b5337b77aaa632560c7e72757.png)




そして、Chrome 150では「ExtensionManifestV2Disabled」というフラグが削除される見通しとなっています。このフラグはManifest V2ベースの広告ブロッカーを使い続けるための事実上の回避手段として残っていましたが、Chrome側ではManifest V2拡張機能がすでにサポート対象外になっているため、不要なコードとして整理されます。


Chrome 150以降も限定的なDevTools経由の方法は残るとされていますが、利用のたびに手作業でページ要素を修正する必要があり、日常利用には向かないとのこと。さらにChrome 151では「ExtensionManifestV2Unsupported」「ExtensionManifestV2Availability」「AllowLegacyMV2Extensions」など残りの関連フラグも削除される** 見通し**で、Manifest V2ベースの広告ブロッカーをChromeで使い続ける余地は大きく狭まります。

Googleのエンジニアのデブリン・クローニン氏はChromiumのイシューで「Manifest V2の維持には複雑さや技術的負債、セキュリティリスクがある」と

**しています。実際にChrome拡張機能では、所有者変更後に悪意あるコードが入った事例や、バックドアを仕込むマルウェアを含む拡張機能、秘密の追跡コードを含む58件の人気拡張機能が確認されたとされています。**

[説明](https://chromium-review.googlesource.com/c/chromium/src/+/7813942)

![](/rss/downloaded_images/f2198ab05cc1aaad17a664cd430b80bc.png)




一方で、広告ブロックは単なる利便性の機能ではなく、セキュリティ対策としての意味もあります。アメリカのサイバーセキュリティ・インフラセキュリティ庁(CISA)は悪質な広告や危険なサイトへのリダイレクトを減らし、ページ読み込みを改善し、第三者によるデータ収集のリスクを下げる手段として広告ブロックソフトの利用を**(PDFファイル) 推奨**しています。ただし、CISAは「広告ブロックブラウザ拡張機能は高い権限で動作し、クライアントとネットワーク間のすべてのデータトラフィックにアクセスできるため、データの収集やその他の潜在的に悪意のある行為を行うことができます」と述べており、広告ブロッカーの権限が高すぎる危険性にも注意を促しています。

今回の移行はChromeの安全性を高める施策であると同時に、広告表示をめぐるユーザーの選択肢を狭める変更でもあります。不要な広告やコンテンツを避けたい開発者や利用者の間では、BraveやFirefoxへの移行も選択肢となっています。

</details>
