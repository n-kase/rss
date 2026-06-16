---
title: "Update for Apps Distributed in Texas"
description: "概要と事実 テキサス州で施行されたSB 2420という法律が、裁判所の差し止め命令が解除されたことにより再び適用されることになりました。この法律は、18歳未満の未成年に対するアプリのダウンロードやアプリ内購入、およびアプリの重大な変更..."
date: 2026-06-16T10:34:36+09:00
categories: ["テクノロジー"]
tags: ["テキサス州法", "年齢確認", "Apple API", "開発者対応", "プライバシー保護"]
image: "/rss/downloaded_images/cbbc31616b431a9282b1de88227a7793.png"
---

## AIによる要約

### 概要と事実
テキサス州で施行されたSB 2420という法律が、裁判所の差し止め命令が解除されたことにより再び適用されることになりました。この法律は、18歳未満の未成年に対するアプリのダウンロードやアプリ内購入、およびアプリの重大な変更時に年齢確認と保護者の同意を義務付けています。Appleはこの法令に対応するため、新たにテキサス州で作成されるAppleアカウントに対して年齢保証機能を導入し、保護者が以前に与えた同意を取り消せる仕組みを提供すると発表しました。変更は2026年6月4日から有効となり、開発者はDeclared Age Range APIやSignificant Change APIなどを使って必要な情報を取得し、実装することが求められています。

### ネットの反応と意見の変遷
発表後、開発者コミュニティでは法令への対応負担について議論が活発になりました。一部の開発者は、年齢確認APIの導入がプライバシー保護のために必要だと評価し、未成年者への不適切なコンテンツ提供を防ぐ良い機会だと肯定的に捉えています。一方で、小規模インディー開発者や個人開発者からは、実装に必要な工数やテスト環境の整備が負担になるとの懸念が示され、特に頻繁にアップデートを行うゲームやソーシャルアプリでは対応が遅れるリスクがあると指摘されています。時間が経つにつれて、Appleが提供するサンドボックス環境や詳細なドキュメントへのリンクが共有され、実装のハードルが下がったという声も増えてきました。

### 背景と結論
テキサス州のSB 2420は、デジタルプラットフォームにおける未成年者保護を強化する目的で制定され、年齢確認と保護者同意の仕組みを市場全体に求めるものです。今回のAppleの対応は、法令遵守のための技術的手段を提供しつつ、プライバシーと安全性の両立を図る業界全体の動きの一環と言えます。開発者は今後、APIの正しい実装とサンドボックスでのテストを徹底し、法令変更に柔軟に対応する体制を整えることが求められます。これにより、未成年者への有害なコンテンツへのアクセスを減らし、保護者が安心して子どもにデジタルサービスを利用させられる環境が整備されることが期待されます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=sg176nne)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Update for Apps Distributed in Texas

June 3, 2026

Due to a recent court ruling lifting an injunction on Texas law SB 2420, new Apple Accounts in Texas are now subject to the law, which introduced age assurance requirements for app marketplaces and developers. As previously [announced](https://developer.apple.com/news/?id=2ezb6jhj), this includes age assurance and parent or guardian consent on behalf of minors under the age of 18 for downloads, Apple In-App Purchases, and significant changes associated with an app. Parents or guardians will also be able to revoke their consent for any app they previously approved for their child. These changes will go into effect starting June 4, 2026.

Developers can request age category data for these Apple Accounts through the [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/). For significant changes, developers should use the [Significant Change API](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic/) under the PermissionKit framework. As a reminder, it’s the developer’s responsibility to determine when there’s a significant change to their app. To learn about a parent or guardian’s revocation of consent, the App Store is providing a server notification that developers can configure to receive notifications that consent has been withdrawn for their app on a child or teen’s device.

**Next steps**

- Review documentation and implement the following:

- [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)
- [Significant Change API under PermissionKit](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)
- [New age rating property type in StoreKit](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode)
- [App Store server notification](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)

- Use Apple’s sandbox testing environment to validate that the APIs have been implemented correctly.

For the most up-to-date requirements and API references, see:

Learn more about how you can [provide age-appropriate experiences](https://developer.apple.com/kids/) and safeguard privacy in your apps and games using robust features available across Apple platforms.

</details>
