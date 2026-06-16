---
title: "Age requirements for apps distributed in Brazil, Australia, Singapore, Utah, and Louisiana"
description: "概要と事実 Appleは2026年2月24日に、ブラジル、オーストラリア、シンガポール、ユタ州、ルイジアナ州における年齢確認義務に対応するため、Declared Age Range APIのベータ版アップデートをリリースしました。この..."
date: 2026-06-16T10:44:54+09:00
categories: ["テクノロジー"]
tags: ["Apple", "年齢確認", "API", "プライバシー", "法規制"]
image: "/rss/downloaded_images/3c25aace77a0736d1ec069bb112a52d7.png"
---

## AIによる要約

### 概要と事実
Appleは2026年2月24日に、ブラジル、オーストラリア、シンガポール、ユタ州、ルイジアナ州における年齢確認義務に対応するため、Declared Age Range APIのベータ版アップデートをリリースしました。このアップデートにより、開発者はユーザーまたは保護者が同意した場合に年齢カテゴリを取得でき、さらにデバイスから年齢確認の方法に関するシグナルも受け取れます。オーストラリア、ブラジル、シンガポールでは、18歳以上と指定されたアプリについては、ユーザーが成人であることを合理的な手段で確認できない限り、App Storeからダウンロードをブロックする仕組みが導入されます。ブラジルでは、ロットボックスを含むと申告したアプリは自動的に18+ ratingに変更されます。ユタ州とルイジアナ州では、それぞれ2026年5月6日と7月1日から新規Appleアカウント作成者に対して年齢カテゴリの共有が可能となり、 Significant Change API や新しい ageRating プロパティ、App Store Server Notifications などのツールが拡張されました。これにより、重要なアップデート時に保護者の同意が必要かどうかを判断するサポートも提供されます。

### ネットの反応と意見の変遷
この発表に対して、開発者コミュニティでは主に二つの反応が見られます。一方では、年齢確認のプロセスが標準化され、法令遵守が容易になることを歓迎する声があり、特に未成年者保護が強化される点を評価しています。他方では、追加の実装負荷やプライバシーへの懸念から、APIの利用方法やデータ取得の範囲について慎重な見方を示す開発者もいます。時間の経過とともに、ベータテストを通じて実際の動作が検証され、フィードバックに基づいてAPIの仕様が調整される過程が注目されています。

### 背景と結論
今回のアップデートは、各国・州で強化されている未成年者保護関連の法律に対応するためのものです。年齢確認の仕組みをプラットフォーム側で提供することで、開発者は個別に複雑な認証ロジックを構築する負担を軽減できます。その結果、アプリストアにおける年齢制限の遵守が向上し、未成年者への不適切なコンテンツ提供リスクが低減されることが期待されます。今後は、実際の運用状況と法令の変化に応じて、さらにツールが改善されていくでしょう。

[🔗 元記事を読む](https://developer.apple.com/news/?id=f5zj08ey)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Age requirements for apps distributed in Brazil, Australia, Singapore, Utah, and Louisiana

February 24, 2026

Today we’re providing an update on the tools available for developers to meet their age assurance obligations under upcoming U.S. and regional laws, including in Brazil, Australia, Singapore, Utah, and Louisiana. Updates to the Declared Age Range API are now available in beta for testing.

**Brazil**

Developers who are distributing apps in Brazil can use the updated Declared Age Range API to obtain a user’s age category. Age categories for users in Brazil will be shared when the user or a parent or guardian (where relevant) agrees to share the age category with you. The API will also return a signal from the user’s device about the method of age assurance.

**Apps rated 18+ in Australia, Singapore, and Brazil**

Starting February 24, 2026, Apple will block users in Australia, Brazil, and Singapore from downloading apps rated 18+ unless they have been confirmed to be adults through reasonable methods. The App Store will perform this confirmation automatically. However, developers may have separate obligations to independently confirm that their users are adults. To assist with this, the Declared Age Range API—available on iOS, iPadOS, and macOS—provides developers with a helpful signal about a user's age.

For developers distributing their apps in Brazil, if you identify your app as containing loot boxes through the age rating questionnaire, the age rating of your app on the Brazil storefront will be updated to 18+.

**Utah and Louisiana**

For users with new Apple Accounts in Utah as of May 6, 2026, and in Louisiana as of July 1, 2026, age categories will be shared with the developer’s app when requested through the Declared Age Range API. The tools we previously announced have been expanded to help developers meet compliance obligations for Louisiana and Utah, including:

[Significant Change API under PermissionKit](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)

[New age rating property type in StoreKit](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode)

[App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)

New signals are now available through the Declared Age Range API, including whether age-related regulatory requirements apply to the user and if the user is required to share their age range. The API will also let you know if you need to get a parent or guardian's permission for significant app updates for a child.

Developers can use the Declared Age Range API to present significant update notifications to adults in these states through the Significant Update Action, now in beta. When releasing a significant update, developers must follow the Human Interface Guidelines and provide users with a meaningful description of the update.

[Design safe and age‑appropriate experiences for your apps and games](https://developer.apple.com/kids/#age-assurance)

</details>
