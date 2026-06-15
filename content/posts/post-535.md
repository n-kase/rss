---
title: "Upcoming changes to the App Store Receipt Signing Intermediate Certificate"
description: "Appleはセキュリティ向上のため、App Storeのレシートに署名する中間証明書をSHA-256アルゴリズムに変更し、2025年1月24日から適用します。この変更により、デバイス上でレシートを検証し、SHA-256に対応していない..."
date: 2026-06-15T19:21:45+09:00
categories: ["テクノロジー"]
tags: ["App Store", "証明書更新", "SHA-256", "レシート検証", "開発者向け"]
image: "/rss/downloaded_images/1df3c9b947e5dcde1ae52cfde4a0945b.png"
---

## AIによる要約
Appleはセキュリティ向上のため、App Storeのレシートに署名する中間証明書をSHA-256アルゴリズムに変更し、2025年1月24日から適用します。この変更により、デバイス上でレシートを検証し、SHA-256に対応していないアプリは検証に失敗し、その結果ユーザーがアプリや有料コンテンツにアクセスできなくなる可能性があります。そのため、開発者はアプリをSHA-256に対応させるか、AppTransactionやTransaction APIを使ってトランザクションを検証するよう対応するべきです。





## 和訳本文
![Upcoming changes to the App Store Receipt Signing Intermediate Certificate](/rss/downloaded_images/1df3c9b947e5dcde1ae52cfde4a0945b.png)

## App Store レシート署名中間証明書の今後の変更

2024年10月31日

Apple プラットフォームのセキュリティとプライバシーを向上させる継続的な取り組みの一環として、App Store レシート署名中間証明書が SHA-256 暗号アルゴリズムを使用するように更新されています。この証明書は、アプリおよびアプリ内購入の購入証明である App Store レシートに署名するために使用されます。

この更新は、[複数のフェーズ](https://developer.apple.com/news/?id=smofnyhj) で完了され、レシートの検証方法によっては、次の更新で App Store 上の既存の一部のアプリに影響が出る可能性があります。

**2025年1月24日** から、デバイス上でレシート検証を行い、SHA-256 アルゴリズムをサポートしていないアプリは、レシートの検証に失敗します。レシート検証に失敗するとアプリやプレミアムコンテンツへのアクセスをブロックするアプリの場合、ユーザーはコンテンツへのアクセスを失う可能性があります。

デバイス上でレシート検証を行うアプリは、SHA-256 アルゴリズムを使用する証明書をサポートするようにアプリを更新してください。あるいは、[AppTransaction](https://developer.apple.com/documentation/storekit/apptransaction) と [Transaction](https://developer.apple.com/documentation/storekit/transaction) API を使用して App Store トランザクションを検証してください。

詳細については、[TN3138: App Store レシート署名証明書の変更への対応](https://developer.apple.com/documentation/technotes/tn3138-handling-app-store-receipt-signing-certificate-changes) を参照してください。

---

## 元スレッド・記事本文

![Upcoming changes to the App Store Receipt Signing Intermediate Certificate](/rss/downloaded_images/1df3c9b947e5dcde1ae52cfde4a0945b.png)

## Upcoming changes to the App Store Receipt Signing Intermediate Certificate

October 31, 2024

As part of ongoing efforts to improve security and privacy on Apple platforms, the App Store receipt signing intermediate certificate is being updated to use the SHA-256 cryptographic algorithm. This certificate is used to sign App Store receipts, which are the proof of purchase for apps and In-App Purchases.

This update is being completed in [multiple phases](https://developer.apple.com/news/?id=smofnyhj) and some existing apps on the App Store may be impacted by the next update, depending on how they verify receipts.

Starting **January 24, 2025**, if your app performs on-device receipt validation and doesn't support a SHA-256 algorithm, your app will fail to validate the receipt. If your app prevents customers from accessing the app or premium content when receipt validation fails, your customers may lose access to their content.

If your app performs on-device receipt validation, update your app to support certificates that use the SHA-256 algorithm; alternatively, use the [AppTransaction](https://developer.apple.com/documentation/storekit/apptransaction) and [Transaction](https://developer.apple.com/documentation/storekit/transaction) APIs to verify App Store transactions.

For more details, view [TN3138: Handling App Store receipt signing certificate change](https://developer.apple.com/documentation/technotes/tn3138-handling-app-store-receipt-signing-certificate-changes).
