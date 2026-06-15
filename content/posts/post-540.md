---
title: "Apple Push Notification service server certificate update"
description: "Apple Push Notification service（APNs）の認証局が変更され、サンドボックス向けのサーバー証明書は2025年1月20日、本番環境向けは2025年2月24日に更新されます。これにより、APNsを利用する開..."
date: 2026-06-15T19:26:32+09:00
categories: ["テクノロジー"]
tags: ["Apple", "Push Notification", "証明書更新", "開発者", "セキュリティ"]
image: "/rss/downloaded_images/e51ef68fa667a9c45d748408f4d4a7a8.png"
---

## AIによる要約
Apple Push Notification service（APNs）の認証局が変更され、サンドボックス向けのサーバー証明書は2025年1月20日、本番環境向けは2025年2月24日に更新されます。これにより、APNsを利用する開発者は古い証明書と新しい証明書の両方をアプリケーションのTrust Storeに含める必要があり、そうしないとプッシュ通知の配信に失敗する可能性があります。したがって、開発者は期限前にTrust Storeを確認し、両方の証明書を組み込むことでスムーズな移行を確保すべきです。





## 和訳本文
![Apple Push Notification service server certificate update](/rss/downloaded_images/e51ef68fa667a9c45d748408f4d4a7a8.png)

## Apple Push Notification service サーバー証明書のアップデート

2024年10月17日

Apple Push Notification service (APNs) の認証局（CA）が変更されます。APNs は サンドボックスのサーバー証明書を 2025年1月20日に、本番環境のサーバー証明書を 2025年2月24日に更新します。APNs を使用しているすべての開発者は、新しいサーバー証明書を含むようにアプリケーションの Trust Store を更新する必要があります：[SHA-2 ルート : USERTrust RSA 認証局証明書](https://www.sectigo.com/knowledge-base/detail/Sectigo-Intermediate-Certificates/kA01N000000rfBO)。

スムーズな移行を確保し、プッシュ通知の配信失敗を避けるため、サンドボックスと本番環境に接続する各アプリケーションサーバーのカットオフ日以前に、古いサーバー証明書と新しいサーバー証明書の両方を Trust Store に含めてください。

現在のところ、Apple から発行された APNs SSL プロバイダー証明書を更新する必要はありません。

---

## 元スレッド・記事本文

![Apple Push Notification service server certificate update](/rss/downloaded_images/e51ef68fa667a9c45d748408f4d4a7a8.png)

## Apple Push Notification service server certificate update

October 17, 2024

The Certification Authority (CA) for Apple Push Notification service (APNs) is changing. APNs will update the server certificates in sandbox on January 20, 2025, and in production on February 24, 2025. All developers using APNs will need to update their application’s Trust Store to include the new server certificate: [SHA-2 Root : USERTrust RSA Certification Authority certificate](https://www.sectigo.com/knowledge-base/detail/Sectigo-Intermediate-Certificates/kA01N000000rfBO).

To ensure a smooth transition and avoid push notification delivery failures, please make sure that both old and new server certificates are included in the Trust Store before the cut-off date for each of your application servers that connect to sandbox and production.

At this time, you don’t need to update the APNs SSL provider certificates issued to you by Apple.
