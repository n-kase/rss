---
title: "Update on age requirements for apps distributed in Texas"
description: "テキサス州で施行が予定されていたアプリマーケットプレイス向けの年齢確認義務を定めた州法SB2420について、地方裁判所が差し止め命令を出し、その施行が一時停止されたことを受けて、Appleはこれまで発表していた対応策の実装計画を保留し..."
date: 2026-06-15T18:18:24+09:00
categories: ["テクノロジー"]
tags: ["Apple", "テキサス州法", "年齢確認", "アプリ開発", "法律動向"]
---

## AIによる要約
テキサス州で施行が予定されていたアプリマーケットプレイス向けの年齢確認義務を定めた州法SB2420について、地方裁判所が差し止め命令を出し、その施行が一時停止されたことを受けて、Appleはこれまで発表していた対応策の実装計画を保留し、今後の訴訟の推移を見守っている。これにより、開発者向けに提供していたDeclared Age Range APIやPermissionKitのSignificant Change API、StoreKitの新しい年齢評価プロパティ、App Store Server Notificationsなどのテスト用ツールは引き続きサンドボックス環境で利用可能であり、2026年に施行が予定されるユタ州やルイジアナ州の同様の法律への対応にも活用できる。このように法的な不確実性が続く中、開発者は柔軟に対応できるツールを活用しつつ、各州の規制動向を注視すべきだという教訓が得られる。





## 和訳本文
## テキサス州で配布されるアプリの年齢要件に関するアップデート

2025年12月23日

地方裁判所が出した最近の差し止め命令により、アプリマーケットプレイスと開発者に年齢保証要件を導入したテキサス州法SB2420の施行が停止された。この判断を受けて、Appleは以前に発表していた実装計画を一時停止し、進行中の法的手続きを監視する。

開発者がコンプライアンス義務を満たすために私たちが[以前発表した](https://developer.apple.com/news/?id=2ezb6jhj)ツールは、サンドボックステストのために引き続き利用可能であり、以下を含む：

- [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)
- [PermissionKitにおけるSignificant Change API](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)
- [StoreKitの新しい年齢評価プロパティタイプ](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode)
- [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)

これらのツールは、2026年に施行が予定されるユタ州とルイジアナ州の法律に関する開発者の義務を果たすのにも役立つ。Declared Age Range APIは、iOS 26、iPadOS 26、macOS 26以降のユーザーに対して世界中で引き続き利用可能である。

---

## 元スレッド・記事本文

## Update on age requirements for apps distributed in Texas

December 23, 2025

A recent injunction issued by a district court suspended enforcement of Texas state law SB2420, which introduced age assurance requirements for app marketplaces and developers. In light of this ruling, Apple will pause previously announced implementation plans and monitor the ongoing legal process.

The tools we [previously announced](https://developer.apple.com/news/?id=2ezb6jhj) to help developers meet their compliance obligations will remain available for sandbox testing, including:

- [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)
- [Significant Change API under PermissionKit](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)
- [New age rating property type in StoreKit](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode)
- [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)

These tools can also be used to help developers with their obligations under laws coming into effect in Utah and Louisiana in 2026. The Declared Age Range API remains available worldwide for users on iOS 26, iPadOS 26, and macOS 26, or later.
