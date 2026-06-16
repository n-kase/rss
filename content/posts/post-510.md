---
title: "Updates to runtime protection in macOS Sequoia"
description: "概要と事実 macOS Sequoiaでは、Gatekeeperによってブロックされる署名が正しくないか、公証されていないソフトウェアを開こうとしたときに、Control‑クリックでこれを無効にするオプションがなくなりました。ユーザー..."
date: 2026-06-16T11:28:08+09:00
categories: ["テクノロジー"]
tags: ["macOS", "Sequoia", "Gatekeeper", "セキュリティ", "公証 notarization"]
image: "/rss/downloaded_images/841ea2bcfa241c9d09d0989721fe479d.jpg"
---

## AIによる要約

### 概要と事実
macOS Sequoiaでは、Gatekeeperによってブロックされる署名が正しくないか、公証されていないソフトウェアを開こうとしたときに、Control‑クリックでこれを無効にするオプションがなくなりました。ユーザーは、システム設定の「プライバシーとセキュリティ」を開き、そこでソフトウェアのセキュリティ情報を確認した上で実行を許可する必要があります。また、Mac App Store以外でソフトウェアを配布する開発者には、Appleの公証サービスにソフトウェアを提出することを推奨しています。このサービスはDeveloper IDで署名されたソフトウェアを自動的にスキャンし、セキュリティチェックを行い、公証が完了するとGatekeeperが認識できるチケットを付与します。これにより、ユーザーは安心してソフトウェアを実行できるようになります。

### 背景と結論
この変更は、誤って危険なソフトウェアを実行してしまうリスクを減らすことを目的としています。Gatekeeperの回避手段を制限することで、マルウェアや改ざんされたアプリの実行を防ぎ、全体的なシステムの安全性が向上します。開発者側は、公証の手順をワークフローに組み込む必要がありますが、それによってユーザーからの信頼を得やすくなり、ソフトウェア配布のハードルが低くなる効果も期待できます。結果として、macOSエコシステム全体のセキュリティが強化され、ユーザーはより安心してアプリを利用できるようになります。

[🔗 元記事を読む](https://developer.apple.com/news/?id=saqachfa)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>



![Updates to runtime protection in macOS Sequoia](/rss/downloaded_images/5e293aba7b1994bda1b47072148e6a31.png)



## Updates to runtime protection in macOS Sequoia

August 6, 2024

In macOS Sequoia, users will no longer be able to Control-click to override [Gatekeeper](https://developer.apple.com/developer-id/) when opening software that isn’t signed correctly or notarized. They’ll need to visit System Settings > Privacy & Security to review security information for software before allowing it to run.

If you distribute software outside of the Mac App Store, we recommend that you submit your software to be notarized. The Apple notary service automatically scans your Developer ID-signed software and performs security checks. When your software is ready for distribution, it’s assigned a ticket to let Gatekeeper know it’s been notarized so customers can run it with confidence.

</details>
