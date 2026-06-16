---
title: "Upcoming changes to the App Store Receipt Signing Intermediate Certificate"
description: "概要と事実 Appleは、プラットフォームのセキュリティとプライバシーを向上させる取り組みの一環として、App Storeレシート署名の中間証明書をSHA‑256暗号アルゴリズムを使用するものに変更すると発表しました。この変更は202..."
date: 2026-06-16T11:18:16+09:00
categories: ["テクノロジー"]
tags: ["App Store", "SHA-256", "レシート検証", "Apple開発者", "セキュリティアップデート"]
image: "/rss/downloaded_images/acd39502042668968c938927794d07c7.png"
---

## AIによる要約

### 概要と事実
Appleは、プラットフォームのセキュリティとプライバシーを向上させる取り組みの一環として、App Storeレシート署名の中間証明書をSHA‑256暗号アルゴリズムを使用するものに変更すると発表しました。この変更は2025年1月24日から適用され、その日からSHA‑256に対応していないアプリではレシートの検証に失敗する可能性があります。レシート検証に失敗すると、アプリ内のプレミアムコンテンツへのアクセスがブロックされるケースがあります。開発者は、対応する証明書をサポートするようにアプリをアップデートするか、StoreKitのAppTransactionおよびTransaction APIを使ってトランザクションを検証することを推奨されています。

### ネットの反応と意見の変遷
この記事にはネット上の反応やコメントは含まれていませんので、ここでの議論の流れや意見の変遷についてはお伝えできません。

### 背景と結論
今回の証明書更新は、Appleが継続的に行っているセキュリティ強化の一部であり、古い暗号アルゴリズムへの依存を減らす狙いがあります。開発者にとっては、レシート検証の実装を見直し、最新のセキュリティ基準に合わせる良い機会となります。今後も同様のアルゴリズム変更が行われる可能性があるため、定期的に開発ガイドラインを確認し、必要に応じてアップデートを行う姿勢が求められます。これにより、ユーザーは安心してアプリを利用し続けることができ、開発者は信頼性の高いサービスを提供できるでしょう。

[🔗 元記事を読む](https://developer.apple.com/news/?id=b6tejt6f)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>



![Upcoming changes to the App Store Receipt Signing Intermediate Certificate](/rss/downloaded_images/1df3c9b947e5dcde1ae52cfde4a0945b.png)



## Upcoming changes to the App Store Receipt Signing Intermediate Certificate

October 31, 2024

As part of ongoing efforts to improve security and privacy on Apple platforms, the App Store receipt signing intermediate certificate is being updated to use the SHA-256 cryptographic algorithm. This certificate is used to sign App Store receipts, which are the proof of purchase for apps and In-App Purchases.

This update is being completed in [multiple phases](https://developer.apple.com/news/?id=smofnyhj) and some existing apps on the App Store may be impacted by the next update, depending on how they verify receipts.

Starting **January 24, 2025**, if your app performs on-device receipt validation and doesn't support a SHA-256 algorithm, your app will fail to validate the receipt. If your app prevents customers from accessing the app or premium content when receipt validation fails, your customers may lose access to their content.

If your app performs on-device receipt validation, update your app to support certificates that use the SHA-256 algorithm; alternatively, use the [AppTransaction](https://developer.apple.com/documentation/storekit/apptransaction) and [Transaction](https://developer.apple.com/documentation/storekit/transaction) APIs to verify App Store transactions.

For more details, view [TN3138: Handling App Store receipt signing certificate change](https://developer.apple.com/documentation/technotes/tn3138-handling-app-store-receipt-signing-certificate-changes).

</details>
