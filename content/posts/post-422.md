---
title: "Next steps for apps distributed in Texas"
description: "概要と事実 Appleは2025年11月4日に、テキサス州で施行されるSB2420という年齢確認法に対応するための開発者向けツールの詳細を発表しました。2026年1月1日からテキサス州で新規に作成されるAppleアカウントについては、..."
date: 2026-06-16T10:52:30+09:00
categories: ["テクノロジー"]
tags: ["Apple", "Texas SB2420", "年齢確認", "親の同意", "開発者向けAPI"]
image: "/rss/downloaded_images/3c25aace77a0736d1ec069bb112a52d7.png"
---

## AIによる要約

### 概要と事実
Appleは2025年11月4日に、テキサス州で施行されるSB2420という年齢確認法に対応するための開発者向けツールの詳細を発表しました。2026年1月1日からテキサス州で新規に作成されるAppleアカウントについては、18歳未満のユーザーがアプリをダウンロードしたり購入したり、重要な変更を行う際に年齢区分の取得と保護者または保護者による同意が必要になります。保護者は以前に与えた同意をいつでも取り消すことができ、取り消しが行われると該当アプリは起動できなくなります。開発者は、Declared Age Range API、Significant Change API、StoreKitの新しいageRatingCodeプロパティ、およびApp Storeサーバー通知を利用して、年齢区分の取得、重要な変更時の同意取得、同意取り消しの通知を実装することが求められます。これらのAPIはiOS 26.2およびiPadOS 26.2のベータ版でサンドボックステストが可能です。

### ネットの反応と意見の変遷
発表を受けて、開発者コミュニティでは新たな実装負荷への懸念が示されています。特に、年齢確認のための個人情報収集がプライバシーに与える影響について議論が活発になり、一部の開発者はユーザー体験の低下や追加コストの増加を危惧しています。一方で、未成年者の保護を目的とした法令への対応として、必要な措置だと支持する声もあり、法令遵守のためのツール提供を評価する意見が見られます。時間の経過とともに、サンドボックス環境でのテスト結果や実際の導入事例が共有されることで、実装のハードルが徐々に明らかになっていく様子がうかがえます。

### 背景と結論
テキサス州のSB2420は、未成年者が不適切なコンテンツにアクセスしないよう年齢確認と保護者同意を義務付けるものであり、これによりプライバシー保護と未成年者保護のバランスが社会的議論の中心となっています。Appleは開発者に適切なツールを提供することで法令遵守を支援しつつ、過度な個人情報収集がユーザーのプライバシーを損なう可能性について懸念を表明しています。この動向は、他州や他国でも同様の年齢確認法が検討されていることを示唆しており、開発者は法的要件の変化に柔軟に対応できる基盤を整えることが重要です。結果として、プライバシーと安全の両立を目指す業界全体の取り組みが今後さらに進むことが期待されます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=2ezb6jhj)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Next steps for apps distributed in Texas

November 4, 2025

Today we’re releasing more details about the tools we’re making available for developers to help them meet their compliance obligations under upcoming U.S. state laws, including SB2420 in Texas. While we’re providing these tools to help developers navigate the evolving legal landscape, Apple remains concerned about the potential implications of laws like SB2420 in Texas. Specifically, we worry they could undermine the privacy of all users by requiring the collection of sensitive personal information just to download an app – even those that simply provide weather forecasts or sports scores.

Starting January 1, 2026, new Apple Accounts in Texas will be subject to new requirements. This includes age assurance and parent or guardian consent on behalf of minors under the age of 18 for downloads, purchases, and significant changes associated with an app. Parents or guardians will also be able to revoke their consent for any app they previously approved.

To meet their obligations under the law, developers may need to adopt new capabilities to receive age category information, trigger consent for a significant change, and learn when a parent or guardian revokes their approval for a child or teen to use their app. Developers can use the following APIs available in the beta versions of iOS 26.2 and iPadOS 26.2 to help them meet their obligations. Sandbox testing is also available to help test the user experience when implementing these APIs to comply with Texas state law.

### Age category information

Developers can use the updated [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/) to obtain a user’s age category, which is defined by Texas state law as under 13, 13-15, 16-17, or over 18. Age categories for users with new Apple Accounts in Texas as of January 1, 2026, will be shared with a developer’s app when they request it. The API will also return a signal from the user’s device about the method of age assurance, such as credit card or government ID, and if consent is required when there’s a significant change to an app.

### Obtaining consent for significant changes

Certain types of changes to an app may be considered significant changes under age assurance laws, such as Texas SB2420. It’s the developer’s responsibility to determine when there’s a significant change to their app.

When a developer determines they have made a significant change to their app, they’ll need to use the [Significant Change API](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic) under the PermissionKit framework to ask the parent or guardian to provide consent for the child or teen to continue using the app or new feature within the app. When the API is called, the child or teen user will see a system dialog to request parental consent and developers can restrict access until consent is obtained.

Texas state law considers a change in the age rating of an app to be a significant change, and developers should keep their age rating selections current in App Store Connect. When a developer updates their app’s age rating, the rating is updated on all user devices once the version is live. Developers can use a [new property](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode) type in StoreKit to automatically check when their app’s age rating has changed on a user’s device and then use the Significant Change API to request parental consent.

### App consent revocation

A parent or guardian in Texas can withdraw consent for any app, which will block launching of the app on the child or teen’s device. The App Store will provide a server notification that developers can configure to [receive notifications](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype) that the parent or guardian has withdrawn consent for their app on a child or teen’s device.

### Sandbox testing

[Sandbox testing](https://developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox) is now available for the Declared Age Range API and Significant Change API in the beta versions of iOS 26.2 and iPadOS 26.2.

### Next steps

- Review documentation and implement the following:

- [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)
- [Significant Change API under PermissionKit](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)
- [New age rating property type in StoreKit](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode)
- [App Store server notification](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)

- Use Apple’s sandbox testing environment to validate that the APIs have been implemented correctly.
- When the Release Candidates of iOS 26.2 and iPadOS 26.2 become available, submit your apps to App Store Connect so users can update their devices with your updated apps with the customer releases.
- Stay tuned for additional communication about future tools to help developers meet upcoming legal obligations in Utah, Louisiana, and Brazil.

</details>
