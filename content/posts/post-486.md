---
title: "New 64-bit requirement for watchOS apps"
description: "Appleは2025年7月22日に、2026年4月からApp Store ConnectにアップロードするすべてのwatchOSアプリには64ビットサポートが必須となり、watchOS 26 SDKでビルドする必要があると発表しました..."
date: 2026-06-15T18:38:50+09:00
categories: ["テクノロジー"]
tags: ["watchOS", "64ビット", "Apple", "App Store Connect", "Xcode"]
image: "/rss/downloaded_images/e3b77969d3a169a2d873055a016952e1.png"
---

## AIによる要約
Appleは2025年7月22日に、2026年4月からApp Store ConnectにアップロードするすべてのwatchOSアプリには64ビットサポートが必須となり、watchOS 26 SDKでビルドする必要があると発表しました。開発者はXcodeの「Standard architectures」設定を使うことで単一の64ビットバイナリを作成でき、XcodeシミュレータやApple Watch Series 9/10およびUltra 2でwatchOS 26ベータを実行したデバイスでARM64互換性をテストできます。この変更により、古いApple Watchモデルへの対応を見直す必要が出てきたり、開発作業が増える可能性がありますが、アプリのパフォーマンス向上や今後のOSアップデートへの対応が容易になります。したがって、開発者は今すぐ64ビット対応の準備を進め、ベータ版でのテストを経て期限前にアプリを更新するべきです。





## 和訳本文
![watchOSアプリの新しい64ビット要件](/rss/downloaded_images/e3b77969d3a169a2d873055a016952e1.png)

## watchOSアプリの新しい64ビット要件

2025年7月22日

2026年4月から、App Store ConnectにアップロードするwatchOSアプリには64ビットサポートも含め、[watchOS 26](https://developer.apple.com/watchos/whats-new/) SDKでビルドする必要があります。プロジェクトで64ビットサポートを有効にするには、デフォルトのXcodeビルド設定である「Standard architectures」を使って、64ビットコードを含む単一のバイナリをビルドすることをお勧めします。

XcodeシミュレータでARM64互換性をテストでき、さらにApple Watch Series 9または10、またはApple Watch Ultra 2でwatchOS 26ベータを実行しているデバイスでもテスト可能です。

---

## 元スレッド・記事本文

![New 64-bit requirement for watchOS apps](/rss/downloaded_images/e3b77969d3a169a2d873055a016952e1.png)

## New 64-bit requirement for watchOS apps

July 22, 2025

Beginning April 2026, watchOS apps uploaded to App Store Connect must also include 64-bit support and be built with the [watchOS 26](https://developer.apple.com/watchos/whats-new/) SDK. To enable 64-bit support in your project, we recommend using the default Xcode build setting of “Standard architectures” to build a single binary with 64-bit code.

You can test ARM64 compatibility for your apps in the Xcode Simulator, and on Apple Watch Series 9 or 10, or Apple Watch Ultra 2 running watchOS 26 beta.
