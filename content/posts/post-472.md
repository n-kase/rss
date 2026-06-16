---
title: "Reminder: Upcoming Changes to the App Store Receipt Signing Intermediate Certificate"
description: "概要と事実 Appleは2025年1月16日に、App Storeレシート署名の中間証明書をSHA-256暗号アルゴリズムを使用するように更新すると発表しました。この証明書はアプリやアプリ内購入の購入証明であるレシートに署名するために..."
date: 2026-06-16T11:12:42+09:00
categories: ["テクノロジー"]
tags: ["App Store", "レシート署名", "SHA-256", "開発者向け", "セキュリティアップデート"]
image: "/rss/downloaded_images/acd39502042668968c938927794d07c7.png"
---

## AIによる要約

### 概要と事実
Appleは2025年1月16日に、App Storeレシート署名の中間証明書をSHA-256暗号アルゴリズムを使用するように更新すると発表しました。この証明書はアプリやアプリ内購入の購入証明であるレシートに署名するために使われます。更新は複数のフェーズで行われ、2025年1月24日からSHA-256に対応していないデバイス上でのレシート検証を行うアプリは検証に失敗する可能性があります。検証に失敗すると、アプリ内のプレミアムコンテンツへのアクセスがブロックされるケースがあります。開発者には、SHA-256をサポートするようにアプリを更新するか、AppTransactionやTransaction APIを使ってトランザクションを検証するよう推奨されています。詳細はTN3138テクニカルノートを参照してください。

### ネットの反応と意見の変遷
この記事にはネットの反応は含まれていません。

### 背景と結論
Appleはプラットフォームのセキュリティとプライバシーを継続的に向上させるため、証明書のアルゴリズムを古いSHA-1からより強固なSHA-256へ移行させています。この変更は、将来的な攻撃リスクを低減し、ユーザーの購入情報をより安全に保つことを目的としています。開発者は早めに対応を行わなければ、ユーザーが正当に購入したコンテンツにアクセスできなくなるリスクがあります。したがって、適切なアップデートやAPIの利用により、サービスの継続性を確保し、セキュリティ基準に合わせることが求められます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=rzloycgp)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>



![Reminder: Upcoming Changes to the App Store Receipt Signing Intermediate Certificate](/rss/downloaded_images/9a06ed283499b7f13b5c9e3be007df56.png)



## Reminder: Upcoming Changes to the App Store Receipt Signing Intermediate Certificate

January 16, 2025

As part of ongoing efforts to improve security and privacy on Apple platforms, the App Store receipt signing intermediate certificate is being updated to use the SHA-256 cryptographic algorithm. This certificate is used to sign App Store receipts, which are the proof of purchase for apps and In-App Purchases.

This update is being completed in [multiple phases](https://developer.apple.com/news/?id=smofnyhj) and some existing apps on the App Store may be impacted by the next update, depending on how they verify receipts.

Starting **January 24, 2025**, if your app performs on-device receipt validation and doesn’t support the SHA-256 algorithm, your app will fail to validate the receipt. If your app prevents customers from accessing the app or premium content when receipt validation fails, your customers may lose access to their content.

If your app performs on-device receipt validation, update your app to support certificates that use the SHA-256 algorithm; alternatively, use the [AppTransaction](https://developer.apple.com/documentation/storekit/apptransaction) and [Transaction](https://developer.apple.com/documentation/storekit/transaction) APIs to verify App Store transactions.

For more details, view [TN3138: Handling App Store receipt signing certificate changes](https://developer.apple.com/documentation/technotes/tn3138-handling-app-store-receipt-signing-certificate-changes).

</details>
