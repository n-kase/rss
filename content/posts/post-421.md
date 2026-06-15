---
title: "Deprecation of the ImageCreator class"
description: "Appleは、画像生成のために提供していたImageCreatorクラスを非推奨とし、iOS 27、iPadOS 27、macOS 27、visionOS 27以降では動作しなくなると発表しました。これにより、ベータ版OSではコンパイ..."
date: 2026-06-15T17:46:41+09:00
categories: ["テクノロジー"]
tags: ["ImageCreator", "iOS 27", "デプレケーション", "アップデート", "画像生成"]
image: "/rss/downloaded_images/3c25aace77a0736d1ec069bb112a52d7.png"
---

## AIによる要約
Appleは、画像生成のために提供していたImageCreatorクラスを非推奨とし、iOS 27、iPadOS 27、macOS 27、visionOS 27以降では動作しなくなると発表しました。これにより、ベータ版OSではコンパイルは通るもののXcodeで警告が出始め、TestFlightビルドでは実行時エラーが発生し、正式リリースではコンパイルエラーとなり、該当機能を使っているアプリはユーザーに正常に動作しなくなる可能性があります。したがって、影響を受けるアプリは、公式リリース前に実装を見直し、Image Playgroundシートへの移行または別の画像生成サービスへの切替を行うことが求められ、これによりユーザー体験の途切れを防ぐことができます。





## 和訳本文
## ImageCreatorクラスの非推奨

2026年6月11日

画像生成へのアプローチをさらに洗練させ続ける中で、ImageCreatorクラスは非推奨となり、iOS 27、iPadOS 27、macOS 27、visionOS 27以降では動作しなくなります。Image Playgroundフレームワークを導入した際、このImageCreatorクラスは、オンデバイス画像生成モデルを使用してアプリがプログラム的に画像を生成する手段として組み込まれました。

**あなたのアプリがImageCreatorクラスを使用している場合、以下のことが予想されます：**

- **ベータ版OSリリース：**コードは引き続きコンパイルされますが、Xcodeで警告が表示され始めます。ImageCreatorを使用しているアプリはTestFlightビルドでは機能せず、ランタイムエラーが発生します。
- **公式OSリリース：**コードはコンパイルされず、ImageCreatorを使用しているアプリの機能は、あなたのアプリを利用する人々にとって動作しなくなります。

**必要な対応：**

あなたのアプリがImageCreatorを使用している場合、iOS 27、iPadOS 27、macOS 27、visionOS 27の公式リリース前に実装を更新し、画像生成機能が引き続き機能し、ユーザーに影響を与えないようにしてください。

- **あなたのアプリがImageCreatorを使用している場合：**Image Playgroundシートを表示するように移行してください。これにより、システムが管理する一貫した画像生成体験が提供されます。あるいは、他の好きな画像生成サービスを統合することもできます。
- **すでに移行済みの場合：**さらなる対応は必要ありません。

**リソース：**

---

## 元スレッド・記事本文

## Deprecation of the ImageCreator class

June 11, 2026

As we continue to refine our approach to image generation, the ImageCreator class is being discontinued and will no longer work in iOS 27, iPadOS 27, macOS 27, and visionOS 27 or later. When we introduced the Image Playground framework, we included the ImageCreator class as a way for apps to generate images programmatically using the on-device image generation model.

**If your app uses the ImageCreator class, here's what to expect:**

- **Beta OS releases:**Your code will continue to compile, but you’ll begin to receive warnings in Xcode. Apps using ImageCreator will not function in TestFlight builds and will cause a runtime error.
- **Public OS releases:**Your code won’t compile, and any features in your app that use ImageCreator won’t work for people using your app.

**What you need to do:**

If your app uses ImageCreator, update your implementation before the public release of iOS 27, iPadOS 27, macOS 27, and visionOS 27 to ensure your image generation features continue to work and people using your app won't be affected.

- **If your app uses ImageCreator:**Transition to presenting the Image Playground sheet, which provides a consistent, system-managed image generation experience. Alternatively, you can integrate another image generation service of your choice.
- **If you’ve already migrated:**No further action is required.

**Resources:**
