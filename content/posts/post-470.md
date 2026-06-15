---
title: "Next steps for apps distributed in Texas"
description: "Appleは、2026年1月1日からテキサス州で施行されるSB2420法に対応するため、開発者向けに年齢確認や保護者同意を取得するための新しいAPIを公開し、サンドボックス環境でのテストも提供すると発表した。この法律では、未成年がアプ..."
date: 2026-06-15T18:25:30+09:00
categories: ["テクノロジー"]
tags: ["Apple", "Texas SB2420", "年齢確認", "保護者同意", "開発者向けAPI"]
---

## AIによる要約
Appleは、2026年1月1日からテキサス州で施行されるSB2420法に対応するため、開発者向けに年齢確認や保護者同意を取得するための新しいAPIを公開し、サンドボックス環境でのテストも提供すると発表した。この法律では、未成年がアプリをダウンロードしたり重要な機能変更を行う際に保護者の同意が必要となり、年齢情報や同意の取り消しもシステムで通知される仕組みになる。Appleはこうした措置がすべてのユーザーのプライバシーを損なう可能性があると懸念を示しており、開発者は新たな実装負荷とプライバシーへの影響に直面する恐れがある。したがって、開発者は早めに提供されたドキュメントとサンドボックスを活用して実装を確認し、今後ユタ州やルイジアナ州、ブラジルなどでも同様の要件が予定されていることに備えるべきであり、規制とプライバシーのバランスを考える社会的議論も必要だと考えられる。





## 和訳本文
## テキサス州で配布されるアプリの次のステップ
2025年11月4日

今日、近い将来施行される米国の州法（テキサス州のSB2420を含む）への対応を支援するため、開発者に提供するツールの詳細を発表します。これらのツールを提供して開発者が変化する法的環境を乗り切れるように支援する一方で、Appleはテキサス州のSB2420のような法律がもたらす潜在的な影響について懸念を抱いています。具体的には、アプリをダウンロードするだけでも気象予報やスポーツスコアを提供するシンプルなアプリであっても、センシティブな個人情報の収集を義務付けることで、すべてのユーザーのプライバシーが損なわれる可能性があると心配しています。

2026年1月1日から、テキサス州の新しいAppleアカウントには新しい要件が適用されます。これには、18歳未満の未成年に対するダウンロード、購入、アプリに関連する重要な変更についての年齢保証および保護者または保護者による同意が含まれます。保護者または保護者は、以前に承認したあらゆるアプリについて同意を撤回することもできます。

法律の義務を果たすために、開発者は年齢カテゴリ情報を受け取る機能、重要な変更に対する同意をトリガーする機能、そして保護者または保護者が子どもまたはティーンエイジャーが自分のアプリを使用することを承認を撤回したときを知る機能を新たに採用する必要があるかもしれません。開発者は、義務を果たすために役立つ、iOS 26.2およびiPadOS 26.2のベータ版で利用可能な以下のAPIを使用できます。サンドボックステストも利用可能で、これらのAPIを実装してテキサス州法に準拠する際のユーザー体験をテストするのに役立ちます。

### 年齢カテゴリ情報
開発者は、更新された[Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)を使用して、テキサス州法によって定義されるユーザーの年齢カテゴリ（13歳未満、13〜15歳、16〜17歳、18歳以上）を取得できます。2026年1月1日以降にテキサス州で新規に作成されたAppleアカウントのユーザーの年齢カテゴリは、開発者のアプリがリクエストしたときに共有されます。このAPIはまた、ユーザーのデバイスから年齢保証の方法（クレジットカードまたは政府発行のIDなど）についてのシグナル、およびアプリに重要な変更がある場合に同意が必要かどうかも返します。

### 重要な変更に対する同意の取得
アプリへの特定の変更は、年齢保証法に基づいて重要な変更とみなされる場合があります。たとえば、テキサス州のSB2420などです。開発者は、自分のアプリに重要な変更が生じたときを判断する責任があります。

開発者が自分のアプリに重要な変更が生じたことを判断した場合、PermissionKitフレームワークの[Significant Change API](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)を使用して、保護者または保護者に子どもまたはティーンエイジャーがアプリまたはアプリ内の新機能を引き続き使用するための同意を求める必要があります。APIが呼び出されると、子どもまたはティーンエイジャーのユーザーは保護者の同意を求めるシステムダイアログを見ることになり、開発者は同意が得られるまでアクセスを制限できます。

テキサス州法では、アプリの年齢評価の変更も重要な変更とみなされます。開発者はApp Store Connectで年齢評価の選択を最新の状態に保つ必要があります。開発者がアプリの年齢評価を更新すると、バージョンがライブになるとすべてのユーザーのデバイスで評価が更新されます。開発者は、StoreKitの[新しいプロパティ](https://developer.apple.com/documentation/storekit/appstore/ageRatingCode)タイプを使用して、ユーザーのデバイスでアプリの年齢評価が変更されたときを自動的にチェックし、その後Significant Change APIを使用して保護者の同意を求めることができます。

### アプリ同意の撤回
テキサス州の保護者または保護者は、あらゆるアプリに対する同意を撤回できます。これにより、子どもまたはティーンエイジャーのデバイスでのアプリの起動がブロックされます。App Storeは、開発者が設定できるサーバー通知を提供し、[通知を受信](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)することで、保護者または保護者が子どもまたはティーンエイジャーのデバイスでの自分のアプリに対する同意を撤回したことを知ることができます。

### サンドボックステスト
[Sandbox testing](https://developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox)は、iOS 26.2およびiPadOS 26.2のベータ版でDeclared Age Range APIおよびSignificant Change APIの両方に対して利用可能になりました。

### 次のステップ
- ドキュメントを確認し、以下を実装してください：

- [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)
- [PermissionKitにおけるSignificant Change API](https://developer.apple.com/documentation/PermissionKit/SignificantAppUpdateTopic)
-

---

## 元スレッド・記事本文

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
