---
title: "New requirement for apps using Sign in with Apple for account creation"
description: "2026年1月1日から、韓国に拠点を置く開発者は、Sign in with Appleを使ったウェブサイト連携のためのServices IDの新規登録または更新時に、サーバー間通知エンドポイントを提供しなければならなくなる。この通知に..."
date: 2026-06-15T18:29:37+09:00
categories: ["テクノロジー"]
tags: ["Apple", "Sign in with Apple", "デベロッパー", "プライバシー", "アカウント管理"]
image: "/rss/downloaded_images/7ea03cb4a58f68f88a1498bc8b09f602.png"
---

## AIによる要約
2026年1月1日から、韓国に拠点を置く開発者は、Sign in with Appleを使ったウェブサイト連携のためのServices IDの新規登録または更新時に、サーバー間通知エンドポイントを提供しなければならなくなる。この通知により、メール転送設定の変更やアカウント削除、Appleアカウントの永久削除など、ユーザーのアカウント状況の重要な変化をリアルタイムで把握できるようになり、開発者はアプリ内の関連データやサーバーインフラストラクチャを速やかに更新して、個人データの管理とユーザーのコントロールを強化することが求められる。したがって、開発者は今すぐガイドラインを確認し、必要なエンドポイントを実装し、プライバシー保護と法令遵守のための対応を進めるべきである。





## 和訳本文
![Appleでのサインインを使用したアカウント作成のための新しい要件](/rss/downloaded_images/7ea03cb4a58f68f88a1498bc8b09f602.png)

## Appleでのサインインを使用したアカウント作成のための新しい要件

2025年10月9日

2026年1月1日から、大韓民国に拠点を置く開発者は、新しいServices IDを登録するか、既存のServices IDを更新して、[Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)を使ったウェブサイトとアプリの連携を行う際に、[サーバー間通知エンドポイント](https://developer.apple.com/help/account/capabilities/enabling-server-to-server-notifications)を提供しなければならない。

リマインダーとして、通知エンドポイントを登録すると、Appleからアプリを利用する人々とそのアカウント状況に関する重要な更新情報を受け取ることができるようになります。具体的には以下のような変更が含まれます：

- メール転送設定の変更。
- アプリ内でのアカウント削除。
- Appleアカウントの永久削除。

サーバー間通知について詳しくは、[WWDC20 セッション 10173: Sign in with Appleを最大限に活用する](https://developer.apple.com/videos/play/wwdc2020/10173/)を参照してください。

これらの通知を受け取ったら、アカウント変更に関連したアプリ内のデータおよび必要なサーバーインフラストラクチャをすぐに更新し、ユーザーが共有した個人データに対するコントロールを高める必要があります。詳細については、[Sign in with Appleアカウントの変更処理](https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts)を参照してください。

App Storeに新しいアプリを提出する前に、または既存のアプリ設定を更新して新しいServices IDを登録したり、既存のServices IDを変更する前に、以下のガイドラインを必ずお読みください。

### アカウント変更ガイダンス

アカウント変更はユーザーのプライバシーと個人データの管理に直接関係しており、アカウント変更の確認はシンプルかつ透明であるべきです。

**メール転送設定の変更について：**

- アカウント変更によって影響を受けるユーザーデータの表示が、通知ペイロードの変更イベントと一致していることを確認してください。通常、このデータはアプリのアカウント設定またはユーザープロフィールに表示されます。
- ユーザーがウェブサイトにアクセスしてメールアドレスの変更または確認を完了する必要がある場合は、そのプロセスを完了できるウェブサイトのページへの直接リンクを含めてください。
- ユーザーに情報を提供してください。メール転送設定の変更が他のサービスに影響する場合は、それを伝えてください。アプリがアプリ内購入をサポートしている場合は、新しいメールアドレスでの請求、注文追跡、キャンセルの処理方法をユーザーに理解してもらってください。

**アカウント削除について：**

**注:** ユーザーアカウント情報の保存および保持、およびアカウント変更と削除の処理については、適用される法的要件を必ず遵守してください。これには、アプリが提供されている地域の現地法令への準拠も含まれます。法的義務について不明点がある場合は、法務顧問にご相談ください。

---

## 元スレッド・記事本文

![New requirement for apps using Sign in with Apple for account creation](/rss/downloaded_images/7ea03cb4a58f68f88a1498bc8b09f602.png)

## New requirement for apps using Sign in with Apple for account creation

October 9, 2025

Starting January 1, 2026, developers based in the Republic of Korea must provide a [server‑to‑server notification endpoint](https://developer.apple.com/help/account/capabilities/enabling-server-to-server-notifications) when registering a new Services ID, or updating an existing Services ID, to [associate their website](https://developer.apple.com/help/account/capabilities/configure-sign-in-with-apple-for-the-web) with an app using [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple).

As a reminder, registering a notification endpoint allows Apple to send you important updates about the people who use your app and their account status, including:

- Changes in email forwarding preferences.
- Account deletions in your app.
- Permanent Apple Account deletions.

To learn more about server-to-server notifications, see [WWDC20 session 10173: Get the most out of Sign in with Apple](https://developer.apple.com/videos/play/wwdc2020/10173/).

When you receive these notifications, you should immediately update any data associated with the account change in the app, as well as any necessary server infrastructure, to give people more control of the personal data they’ve shared. For more information, see [Processing changes for Sign in with Apple accounts](https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts).

Before submitting a new app to the App Store, or updating an existing app configuration to register a new Services ID or modify an existing Services ID, please read the guidance below.

### Account change guidance

Account changes are directly related to privacy and control for the user and their personal data, and confirming account changes should be straightforward and transparent.

**For account email forwarding changes:**

- Ensure any displayed user data affected by the account change matches the change event in the notification payload. Typically, this data is displayed in the app’s account settings or user profile.
- If people need to visit a website to finish changing or verifying their email address, include a link directly to the page on your website where they can complete the process.
- Keep users informed. If the email forwarding change affects other services you offer, let them know. If your app supports In-App Purchases, help people understand how billing, order tracking, and cancellations will be handled with the new email address.

**For account deletions:**

**Note:** Always follow applicable legal requirements for storing and retaining user account information and for handling account changes and deletions. This includes complying with local laws where your apps are available. If you have questions regarding your legal obligations, check with your legal counsel.
