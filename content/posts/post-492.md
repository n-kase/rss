---
title: "Apple Push Notification service server certificate update"
description: "概要と事実 Apple Push Notification service（APNs）の認証局が変更になることが発表されました。サンドボックス環境では2025年1月20日に、本番環境では2025年2月24日にサーバー証明書が更新されま..."
date: 2026-06-16T11:20:53+09:00
categories: ["テクノロジー"]
tags: ["APNs", "証明書更新", "開発者向け", "プッシュ通知", "セキュリティ"]
image: "/rss/downloaded_images/e7afb1909a75f1cbc37c50f962879780.jpg"
---

## AIによる要約

### 概要と事実
Apple Push Notification service（APNs）の認証局が変更になることが発表されました。サンドボックス環境では2025年1月20日に、本番環境では2025年2月24日にサーバー証明書が更新されます。開発者はアプリのTrust Storeに新しいサーバー証明書を含める必要があり、古い証明書と新しい証明書の両方を切り替え日までに入れておくことが求められます。現在のところ、Appleから発行されたAPNs SSLプロバイダー証明書の更新は不要です。

### 背景と結論
証明書の更新は、セキュリティ基準の向上や認証局の変更に伴う定期的なメンテナンスです。開発者がTrust Storeを適切に更新しないと、プッシュ通知の配信が失敗する可能性があります。そのため、早めに証明書の追加作業を行い、移行期間中に両方の証明書を保持することが推奨されます。この対応により、サービスの中断を防ぎ、ユーザーへの通知が安定して届けられる見込みです。

[🔗 元記事を読む](https://developer.apple.com/news/?id=09za8wzy)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>



![Apple Push Notification service server certificate update](/rss/downloaded_images/e51ef68fa667a9c45d748408f4d4a7a8.png)



## Apple Push Notification service server certificate update

October 17, 2024

The Certification Authority (CA) for Apple Push Notification service (APNs) is changing. APNs will update the server certificates in sandbox on January 20, 2025, and in production on February 24, 2025. All developers using APNs will need to update their application’s Trust Store to include the new server certificate: [SHA-2 Root : USERTrust RSA Certification Authority certificate](https://www.sectigo.com/knowledge-base/detail/Sectigo-Intermediate-Certificates/kA01N000000rfBO).

To ensure a smooth transition and avoid push notification delivery failures, please make sure that both old and new server certificates are included in the Trust Store before the cut-off date for each of your application servers that connect to sandbox and production.

At this time, you don’t need to update the APNs SSL provider certificates issued to you by Apple.

</details>
