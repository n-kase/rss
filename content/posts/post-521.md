---
title: "Algorithm changes to server connections for Apple Pay on the Web"
description: "Appleは2025年2月4日より、Apple Pay on the Webのサーバー接続を保護するアルゴリズムを変更し、対応する六つの暗号スイートのうち少なくとも一つをサポートするよう求めている。この変更は、決済セッションの取得やド..."
date: 2026-06-15T19:11:26+09:00
categories: ["テクノロジー"]
tags: ["Apple Pay", "アルゴリズム変更", "サーバーセキュリティ", "Web決済", "2025年2月"]
image: "/rss/downloaded_images/682546ced730d2d1af5bd53dc79bbe57.png"
---

## AIによる要約
Appleは2025年2月4日より、Apple Pay on the Webのサーバー接続を保護するアルゴリズムを変更し、対応する六つの暗号スイートのうち少なくとも一つをサポートするよう求めている。この変更は、決済セッションの取得やドメイン確認の更新、マーチャントトークン通知の処理、Wallet Ordersの作成・更新、そしてApple Pay Web Merchant Registration APIを通じたマーチャントオンボーディングなど、Apple Payのウェブ統合におけるすべてのセキュアな接続に影響する。対応が遅れるとサービスの中断リスクが高まるため、事業者は早めにサーバー設定を見直し、必要な暗号スイートを導入すべきである。これにより、決済の継続性とセキュリティを確保し、利用者への信頼を維持できるだろう。





## 和訳本文
![Apple Pay on the Webのサーバー接続アルゴリズム変更](/rss/downloaded_images/682546ced730d2d1af5bd53dc79bbe57.png)

## Apple Pay on the Webのサーバー接続アルゴリズム変更

2025年1月9日

来月から、AppleはApple Pay on the Webのサーバー接続を保護するサポートアルゴリズムを変更します。サービスの中断を避けるため、**2025年2月4日**以前に、[指定された六つの暗号スイート](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server#overview)のうち1つ以上をサポートするよう、本番サーバーの準備をしてください。

これらのアルゴリズム変更は、Apple Payへの統合の一部として確立したすべてのセキュアな接続に影響し、以下のタッチポイントが対象となります：

- [Apple Pay支払いセッションのリクエスト](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session)（Apple Pay on the Webのみ）
- [ドメイン確認の更新](https://developer.apple.com/documentation/apple_pay_on_the_web/maintaining_your_environment#3179140)（Apple Pay on the Webのみ）
- [定期、延期、自動リロード取引のマーチャントトークン通知の受信と処理](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications)（Apple Pay on the Webおよびアプリ）
- [Wallet Ordersの作成と更新](https://developer.apple.com/documentation/walletorders)（Apple Pay on the Webおよびアプリ）
- [Apple Pay Web Merchant Registration APIを介したマーチャントオンボーディングの管理](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi)（決済サービスプロバイダー（PSP）および電子商取引プラットフォームのみ)

---

## 元スレッド・記事本文

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
