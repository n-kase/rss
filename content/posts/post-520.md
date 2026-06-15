---
title: "Reminder: Upcoming Changes to the App Store Receipt Signing Intermediate Certificate"
description: "Appleは、セキュリティ向上のためApp Storeレシート署名の中間証明書をSHA-256アルゴリズムに変更しており、2025年1月24日からデバイス上でレシート検証を行いSHA-256に対応していないアプリは検証に失敗し、コンテ..."
date: 2026-06-15T19:10:41+09:00
categories: ["テクノロジー"]
tags: ["Apple", "App Store", "SHA-256", "レシート検証", "開発者向け更新"]
image: "/rss/downloaded_images/9a06ed283499b7f13b5c9e3be007df56.png"
---

## AIによる要約
Appleは、セキュリティ向上のためApp Storeレシート署名の中間証明書をSHA-256アルゴリズムに変更しており、2025年1月24日からデバイス上でレシート検証を行いSHA-256に対応していないアプリは検証に失敗し、コンテンツへのアクセスがブロックされる可能性がある。これにより、影響を受けるアプリのユーザーが購入した機能やコンテンツを利用できなくなるリスクが高まる。したがって、開発者はアプリをSHA-256に対応させるか、AppTransaction／Transaction APIを使った検証に切り替えることで、サービスの中断を防ぐべきである。





## 和訳本文
![App Store レシート署名中間証明書の今後の変更についてのリマインダー](/rss/downloaded_images/9a06ed283499b7f13b5c9e3be007df56.png)

## App Store レシート署名中間証明書の今後の変更についてのリマインダー

2025年1月16日

Apple プラットフォームのセキュリティとプライバシーを向上させる継続的な取り組みの一環として、App Store レシート署名の中間証明書が SHA-256 暗号アルゴリズムを使用するように更新されています。この証明書は、アプリおよびアプリ内購入の購入証明である App Store レシートに署名するために使用されます。

この更新は[複数のフェーズ](https://developer.apple.com/news/?id=smofnyhj)で行われており、レシートの検証方法によっては、次の更新で App Store 上の既存の一部のアプリに影響が出る可能性があります。

**2025年1月24日** から、デバイス上でレシート検証を行い、SHA-256 アルゴリズムをサポートしていないアプリはレシートの検証に失敗します。検証に失敗したときにアプリまたはプレミアムコンテンツへのアクセスをブロックする仕組みになっているアプリでは、ユーザーがコンテンツにアクセスできなくなる可能性があります。

デバイス上でレシート検証を行うアプリについては、SHA-256 を使用する証明書をサポートするようにアプリを更新してください。あるいは、[AppTransaction](https://developer.apple.com/documentation/storekit/apptransaction) と [Transaction](https://developer.apple.com/documentation/storekit/transaction) API を使って App Store のトランザクションを検証してください。

詳細については、[TN3138: App Store レシート署名証明書の変更への対応](https://developer.apple.com/documentation/technotes/tn3138-handling-app-store-receipt-signing-certificate-changes) を参照してください。

---

## 元スレッド・記事本文

![Reminder: Upcoming Changes to the App Store Receipt Signing Intermediate Certificate](/rss/downloaded_images/9a06ed283499b7f13b5c9e3be007df56.png)

## Reminder: Upcoming Changes to the App Store Receipt Signing Intermediate Certificate

January 16, 2025

As part of ongoing efforts to improve security and privacy on Apple platforms, the App Store receipt signing intermediate certificate is being updated to use the SHA-256 cryptographic algorithm. This certificate is used to sign App Store receipts, which are the proof of purchase for apps and In-App Purchases.

This update is being completed in [multiple phases](https://developer.apple.com/news/?id=smofnyhj) and some existing apps on the App Store may be impacted by the next update, depending on how they verify receipts.

Starting **January 24, 2025**, if your app performs on-device receipt validation and doesn’t support the SHA-256 algorithm, your app will fail to validate the receipt. If your app prevents customers from accessing the app or premium content when receipt validation fails, your customers may lose access to their content.

If your app performs on-device receipt validation, update your app to support certificates that use the SHA-256 algorithm; alternatively, use the [AppTransaction](https://developer.apple.com/documentation/storekit/apptransaction) and [Transaction](https://developer.apple.com/documentation/storekit/transaction) APIs to verify App Store transactions.

For more details, view [TN3138: Handling App Store receipt signing certificate changes](https://developer.apple.com/documentation/technotes/tn3138-handling-app-store-receipt-signing-certificate-changes).
