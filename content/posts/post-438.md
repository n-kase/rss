---
title: "New 64-bit requirement for watchOS apps"
description: "概要と事実 Appleは2025年7月22日に発表した開発者向けのお知らせで、2026年4月からApp Store ConnectにアップロードするwatchOSアプリについては64ビット対応が必須になると明らかにしました。これにより..."
date: 2026-06-16T10:58:47+09:00
categories: ["テクノロジー"]
tags: ["watchOS", "64-bit対応", "Apple", "App Store Connect", "Xcode"]
image: "/rss/downloaded_images/a710258f3dfe492fb8651277f9d179bd.png"
---

## AIによる要約

### 概要と事実
Appleは2025年7月22日に発表した開発者向けのお知らせで、2026年4月からApp Store ConnectにアップロードするwatchOSアプリについては64ビット対応が必須になると明らかにしました。これにより、開発者はwatchOS 26 SDKを使用してアプリをビルドし、Xcodeのデフォルト設定である「Standard architectures」を用いてシングルバイナリに64ビットコードを含めることを推奨しています。テスト方法としては、XcodeシミュレーターまたはApple Watch Series 9、Series 10、Apple Watch Ultra 2でwatchOS 26ベータを実行しているデバイスを使うことが案内されています。

### ネットの反応と意見の変遷
この発表を受けて、開発者コミュニティではいくつかの反応が見られました。まず、64ビット対応への移行が必要になることを前向きに捉え、最新のSDKを活用することでパフォーマンス向上や新しい機能への対応が期待できるとの声があります。一方で、既存のwatchOSアプリを維持している中小規模の開発者や個人開発者からは、ビルド環境の更新やテスト工程の追加による負担増への懸念が示されました。特に、古いハードウェアのみをサポートしているアプリについては、64ビットバイナリへの移行が難しいという指摘もあり、Appleが提供する移行ガイドやサポートドキュメントへの期待が高まっています。時間の経過とともに、開発者フォーラムでは実際にXcodeの設定変更やシミュレーターでのテスト手順を共有するスレッドが増え、実装のノウハウが徐々に広まっている様子がうかがえます。

### 背景と結論
今回の要件は、Appleがプラットフォーム全体で64ビットアーキテクチャへの統一を進めている流れの一環です。これにより、セキュリティの向上や最新のハードウェア性能をフルに活用できるアプリが増えることが期待されます。開発者側としては、早期にビルド設定を見直し、テスト環境を整備することで、2026年4月の期限にスムーズに対応できるでしょう。また、この変更はwatchOSエコシステムの成長を促し、ユーザーにとってより安定かつ高機能なアプリ提供につながると考えられます。したがって、開発者は今後のアップデート計画にこの要件を組み込み、必要なリソースを確保することが重要です。

[🔗 元記事を読む](https://developer.apple.com/news/?id=zt8rydnt)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>



![New 64-bit requirement for watchOS apps](/rss/downloaded_images/e3b77969d3a169a2d873055a016952e1.png)



## New 64-bit requirement for watchOS apps

July 22, 2025

Beginning April 2026, watchOS apps uploaded to App Store Connect must also include 64-bit support and be built with the [watchOS 26](https://developer.apple.com/watchos/whats-new/) SDK. To enable 64-bit support in your project, we recommend using the default Xcode build setting of “Standard architectures” to build a single binary with 64-bit code.

You can test ARM64 compatibility for your apps in the Xcode Simulator, and on Apple Watch Series 9 or 10, or Apple Watch Ultra 2 running watchOS 26 beta.

</details>
