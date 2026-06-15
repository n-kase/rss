---
title: "New features for APNs token authentication are now available"
description: "Appleは、APNsのトークン認証キーにチームスコープとトピック固有のオプションを追加し、開発環境と本番環境での使用を制限したり、特定のアプリのバンドルIDに紐付けて管理を細かくできるようにしたことを発表しました。これにより、セキュ..."
date: 2026-06-15T19:03:11+09:00
categories: ["テクノロジー"]
tags: ["APNs", "トークン認証", "セキュリティ", "Apple", "開発者"]
image: "/rss/downloaded_images/e51ef68fa667a9c45d748408f4d4a7a8.png"
---

## AIによる要約
Appleは、APNsのトークン認証キーにチームスコープとトピック固有のオプションを追加し、開発環境と本番環境での使用を制限したり、特定のアプリのバンドルIDに紐付けて管理を細かくできるようにしたことを発表しました。これにより、セキュリティが強化され、特に多数のアプリを扱う大規模な組織ではキーの整理と運用が楽になると期待されます。既存のキーは引き続き利用できるため、新しい機能を活用したい場合のみキーの更新を検討すればよいという教訓が得られます。





## 和訳本文
![APNs トークン認証の新機能が今利用可能](/rss/downloaded_images/e51ef68fa667a9c45d748408f4d4a7a8.png)

## APNs トークン認証の新機能が今利用可能

2025年2月17日

Apple Push Notification サービス (APNs) の新しいトークン認証キーを作成する際に、アップグレードされたセキュリティ オプションを利用できるようになりました。

**チームスコープ キー** は、トークン認証キーを開発環境または本番環境に限定できるため、セキュリティの追加レイヤーが提供され、意図した環境でのみキーが使用されることを保証します。

**トピック固有キー** は、各キーを特定のバンドル ID に関連付けることで、より細かい制御が可能になり、キー管理がより合理的かつ整理しやすくなります。これは、異なるチームで複数のアプリを管理する大規模な組織にとって特に有益です。

既存のキーは、すべてのプッシュ トピックと環境で引き続き機能します。現時点では、新しい機能を活用したい場合を除いて、キーを更新する必要はありません。

APNs との通信をトークンベースで保護する方法の詳細な手順については、「[トークンベースの接続を APNs に確立する](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns)」を参照してください。

---

## 元スレッド・記事本文

![New features for APNs token authentication are now available](/rss/downloaded_images/e51ef68fa667a9c45d748408f4d4a7a8.png)

## New features for APNs token authentication are now available

February 17, 2025

You can now take advantage of upgraded security options when creating new token authentication keys for the Apple Push Notification service (APNs).

**Team-scoped keys** enable you to restrict your token authentication keys to either development or production environments, providing an additional layer of security and ensuring that keys are used only in their intended environments.

**Topic-specific keys** provide more granular control by enabling you to associate each key with a specific bundle ID, allowing for more streamlined and organized key management. This is particularly beneficial for large organizations that manage multiple apps across different teams.

Your existing keys will continue to work for all push topics and environments. At this time, you don’t have to update your keys unless you want to take advantage of the new capabilities.

For detailed instructions on how to secure your communications with APNs, read [Establishing a token-based connection to APNs](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns).
