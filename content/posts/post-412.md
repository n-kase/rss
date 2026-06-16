---
title: "Update on age requirements for apps distributed in Texas"
description: "概要と事実 テキサス州の地方裁判所がSB2420という年齢確認義務を課す州法の執行を差し止める仮処分を出したことが伝えられました。この法律はアプリマーケットプレイスや開発者に対して年齢保証の仕組みを導入することを求めていました。仮処分..."
date: 2026-06-16T10:48:02+09:00
categories: ["テクノロジー"]
tags: ["Apple", "テキサス州", "年齢確認", "アプリストア", "法律"]
image: "/rss/downloaded_images/3c25aace77a0736d1ec069bb112a52d7.png"
---

## AIによる要約

### 概要と事実
テキサス州の地方裁判所がSB2420という年齢確認義務を課す州法の執行を差し止める仮処分を出したことが伝えられました。この法律はアプリマーケットプレイスや開発者に対して年齢保証の仕組みを導入することを求めていました。仮処分の影響を受けて、Appleは以前に発表していた対応実施計画を一時停止し、今後の法廷手続きの推移を見守ると発表しました。なお、開発者が法令遵守に役立つと宣言していたツール群（Declared Age Range API、PermissionKit内のSignificant Change API、StoreKitの新しい年齢評価プロパティ、App Store Server Notificationsなど）はサンドボックスでのテスト用に引き続き提供されます。これらのツールは2026年に施行されるユタ州およびルイジアナ州の同様の法律への対応にも利用可能であり、Declared Age Range APIはiOS 26、iPadOS 26、macOS 26以降のユーザー向けに世界中で利用できると説明されています。

### ネットの反応と意見の変遷
このニュースがネット上で取り上げられると、開発者コミュニティからは法的不確実性の中での対応準備が難しいという懸念と、一時的に実施計画が停止されたことへの安堵が混在して見られました。一方で、未成年者保護を求める声は、年齢確認の仕組みが遅れることでリスクが高まるのではないかと警鐘を鳴らし、立法の早期復活を求める意見も出ました。法廷の動向が注目される中、SNSや技術系フォーラムでは、Appleがツールを引き続き提供する姿勢を評価する声と、実際の運用においてプライバシーやデータ取扱いへの影響を慎重に検討すべきだと指摘する声が交錯し、時間の経過とともに議論の焦点が法的解釈から実装の具体的なガイドラインへと移っていく様子がうかがえました。

### 背景と結論
今回の仮処分は、デジタルサービスにおける年齢確認義務が州レベルで広がりつつある中で、法的な整合性や実装コストへの懸念が裁判所に影響を与えたことを示しています。Appleが対応ツールを引き続き提供する姿勢は、開発者への支援を続けつつ法的リスクを回避しようとするバランスの取れた対応と言えます。今後、他州でも同様の法律が施行される見込みであるため、業界全体として年齢確認の仕組みを標準化し、プライバシー保護と未成年者保護の両立を図る枠組み作りが求められます。この一連の動きは、テクノロジー規制が州ごとに異なる中で、企業が柔軟に対応しながらも社会的責任を果たす重要性を改めて浮き彫りにしています。

[🔗 元記事を読む](https://developer.apple.com/news/?id=8jzbigf4)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Update on age requirements for apps distributed in Texas

December 23, 2025

A recent injunction issued by a district court suspended enforcement of Texas state law SB2420, which introduced age assurance requirements for app marketplaces and developers. In light of this ruling, Apple will pause previously announced implementation plans and monitor the ongoing legal process.

The tools we [previously announced](https://developer.apple.com/news/?id=2ezb6jhj) to help developers meet their compliance obligations will remain available for sandbox testing, including:

- [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)
- [Significant Change API under PermissionKit](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)
- [New age rating property type in StoreKit](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode)
- [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)

These tools can also be used to help developers with their obligations under laws coming into effect in Utah and Louisiana in 2026. The Declared Age Range API remains available worldwide for users on iOS 26, iPadOS 26, and macOS 26, or later.

</details>
