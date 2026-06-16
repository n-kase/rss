---
title: "Algorithm changes to server connections for Apple Pay on the Web"
description: "概要と事実 Appleは2025年2月4日から、ウェブでのApple Payにおけるサーバー接続を保護するアルゴリズム（暗号スイート）を変更すると発表しました。この変更により、現在のサーバーがサポートしている暗号スイートのうち、指定さ..."
date: 2026-06-16T11:12:52+09:00
categories: ["テクノロジー"]
tags: ["Apple Pay", "アルゴリズム変更", "サーバーセキュリティ", "Web決済", "2025年2月"]
image: "/rss/downloaded_images/8c1da85463868e652e5053b8cc62207e.jpg"
---

## AIによる要約

### 概要と事実
Appleは2025年2月4日から、ウェブでのApple Payにおけるサーバー接続を保護するアルゴリズム（暗号スイート）を変更すると発表しました。この変更により、現在のサーバーがサポートしている暗号スイートのうち、指定された六種類のうちいずれか一つ以上をサポートしている必要があります。対象となる接続ポイントは、Apple Payの支払いセッションのリクエスト、ドメイン検証の更新、定期・延期・自動リロード取引のマーチャントトークン通知の受信・処理、Wallet Ordersの作成・更新、およびApple Pay Webマーチャント登録APIを通じたマーチャントオンボーディング管理です。開発者は、2025年2月4日までに本番サーバーがこれらのアルゴリズムに対応していることを確認し、サービスの中断を防ぐ必要があります。

### ネットの反応と意見の変遷
この記事にはネットの反応やコメントは含まれていませんので、推測による記載は行いません。

### 背景と結論
アルゴリズムの更新は、セキュリティ基準の進化に合わせて行われる定期的な対応であり、ウェブ決済サービスの安全性を維持するために必要です。開発者側では、サーバー設定の見直しやテストを早期に実施することで、移行期間中に発生しうる接続エラーを防ぐことができます。このような変更は、決済インフラ全体の信頼性向上に寄与し、利用者にとっても安心してサービスを利用できる環境を支えるものです。

[🔗 元記事を読む](https://developer.apple.com/news/?id=2x8awlvm)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>



![Algorithm changes to server connections for Apple Pay on the Web](/rss/downloaded_images/682546ced730d2d1af5bd53dc79bbe57.png)



## Algorithm changes to server connections for Apple Pay on the Web

January 9, 2025

Starting next month, Apple will change the supported algorithms that secure server connections for Apple Pay on the Web. In order to maintain uninterrupted service, you’ll need to ensure that your production servers support one or more of the [designated six ciphers](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server#overview) before **February 4, 2025.**

These algorithm changes will affect any secure connection you’ve established as part of your Apple Pay integration, including the following touchpoints:

- [Requesting an Apple Pay payment session](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session)(Apple Pay on the Web only)
- [Renewing your domain verification](https://developer.apple.com/documentation/apple_pay_on_the_web/maintaining_your_environment#3179140)(Apple Pay on the Web only)
- [Receiving and handling merchant token notifications](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications)for recurring, deferred, and automatic-reload transactions (Apple Pay on the Web and in app)
- Creating and updating [Wallet Orders](https://developer.apple.com/documentation/walletorders)(Apple Pay on the Web and in app)
- Managing merchant onboarding via the [Apple Pay Web Merchant Registration API](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi)(payment service provider (PSP) and e-commerce platforms only)

</details>
