---
title: "Update for Apps Distributed in Texas"
description: "テキサス州で最近の裁判所の判決により、テキサス州法SB 2420に対する差し止め命令が解除されたため、6月4日から新しく作成されるAppleアカウントは年齢確認の要件が適用されるようになった。これにより、18歳未満の未成年に関するアプ..."
date: 2026-06-15T17:51:34+09:00
categories: ["テクノロジー"]
tags: ["Apple", "Texas SB 2420", "年齢確認", "開発者向けAPI", "プライバシー保護"]
image: "/rss/downloaded_images/cbbc31616b431a9282b1de88227a7793.png"
---

## AIによる要約
テキサス州で最近の裁判所の判決により、テキサス州法SB 2420に対する差し止め命令が解除されたため、6月4日から新しく作成されるAppleアカウントは年齢確認の要件が適用されるようになった。これにより、18歳未満の未成年に関するアプリのダウンロード、アプリ内購入、およびアプリに重大な変更がある場合には、保護者または保護者による同意が必要となり、保護者は以前に与えた同意をいつでも取り消すことができる。この変更に対応するため、開発者はDeclared Age Range APIやSignificant Change API（PermissionKitフレームワーク内）、新しい年齢評価プロパティ、App Storeサーバー通知などを実装し、サンドボックス環境で正常に動作することを確認する必要がある。これらの対応により、未成年者のプライバシー保護と年齢に適した体験の提供が求められ、開発者側のコンプライアンス負荷が増すと同時に、他の州でも同様の規制が広がる可能性がある。したがって、開発者は速やかに関連ドキュメントを確認し、指定されたAPIを組み込んでテストを行うことで、法令遵守とユーザー保護の両立を図るべきである。





## 和訳本文
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

---

## 元スレッド・記事本文

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
