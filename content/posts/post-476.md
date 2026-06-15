---
title: "New requirements for apps available in Texas"
description: "テキサス州では2026年1月1日からSB2420という新法が施行され、アプリマーケットプレイスと開発者に年齢確認の義務が課されることになり、特に未成年者のアプリダウンロードには保護者の同意が必要になる。これにより、ユーザーのプライバシ..."
date: 2026-06-15T18:31:11+09:00
categories: ["テクノロジー"]
tags: ["テキサス州法", "年齢確認", "アプリプライバシー", "Apple", "子どものオンライン安全"]
---

## AIによる要約
テキサス州では2026年1月1日からSB2420という新法が施行され、アプリマーケットプレイスと開発者に年齢確認の義務が課されることになり、特に未成年者のアプリダウンロードには保護者の同意が必要になる。これにより、ユーザーのプライバシーへの懸念が高まると同時に、開発者は新たなAPIを導入して年齢層取得や同意の再取得を実装しなければならず、アプリ利用のハードルが上がる可能性がある。したがって、法令遵守とプライバシー保護の両立が求められ、開発者はユーザーの信頼を損なわないよう最小限の情報収集にとどめるべきだという教訓が得られる。





## 和訳本文
## テキサス州で利用可能なアプリに関する新しい要件

2025年10月8日

2026年1月1日から、テキサス州の新しい州法であるSB2420が施行され、アプリマーケットプレイスと開発者に年齢保証の要件が導入されます。私たちは子どものオンライン安全を強化する目標を共有していますが、SB2420は、天気やスポーツスコアを確認したいだけのユーザーであっても、あらゆるアプリをダウンロードする際に機密性の高い個人を特定できる情報の収集を要求することにより、ユーザーのプライバシーに影響を与える懸念があります。Appleは、法律の制約の中でプライバシーを守りながら子どもの安全を強化する業界をリードするツールを、親と開発者に引き続き提供します。

この法律が発効すると、テキサス州に居住して新しいApple Accountを作成するユーザーは、18歳以上であるかどうかを確認する必要があります。18歳未満のユーザーのためのすべての新しいApple Accountは、[ファミリー共有グループ](https://support.apple.com/en-us/108380)に参加することが義務付けられ、親または保護者は、未成年者によるすべてのApp Storeダウンロード、アプリ購入、およびAppleのIn-App Purchaseシステムを使用した取引に対して同意を提供する必要があります。これは開発者にも影響を与え、法律に基づく義務を果たすために新しい機能を採用し、アプリ内の動作を変更する必要があります。同様の要件は、来年後半にユタ州とルイジアナ州でも施行される予定です。

今日は、これらの新しい要件に対応するために行っているアップデートの詳細と、開発者を支援するために提供するツールについて共有します。

プライバシーを守りながら開発者が義務を果たせるよう支援するため、ユーザーの年齢カテゴリを取得し、テキサス州法で求められる重大な変更を管理する機能を導入します。[Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/)は今すぐ実装可能で、今後数か月の間にテキサス州の新しいアカウントユーザーに必要な年齢カテゴリを提供するようにアップデートされます。また、今年後半にリリースされる新しいAPIにより、開発者はアプリに重大な変更があったと判断した際に、システム体験を呼び出してユーザーが親の同意を再取得できるようにすることができます。さらに、親は未成年者が引き続きアプリを使用している場合でも同意を取り消すことができます。追加の技術文書など、さらなる詳細は今年秋に公開されます。

私たちは、オンライン上の脅威から子どもを守るには継続的な警戒と努力が必要だと理解しています。そのため、[業界をリードする機能](https://developer.apple.com/kids/)を引き続き創出し、開発者が年齢に適した体験を提供し、アプリやゲームでのプライバシーを守れるよう支援するとともに、[包括的なツールセット](https://www.apple.com/newsroom/2025/06/apple-expands-tools-to-help-parents-protect-kids-and-teens-online/)を親に提供し、オンラインでの子どもの安全を守るお手伝いを続けていきます。

---

## 元スレッド・記事本文

## New requirements for apps available in Texas

October 8, 2025

Beginning January 1, 2026, a new state law in Texas — SB2420 — introduces age assurance requirements for app marketplaces and developers. While we share the goal of strengthening kids’ online safety, we are concerned that SB2420 impacts the privacy of users by requiring the collection of sensitive, personally identifiable information to download any app, even if a user simply wants to check the weather or sports scores. Apple will continue to provide parents and developers with industry-leading tools that help enhance child safety while safeguarding privacy within the constraints of the law.

Once this law goes into effect, users located in Texas who create a new Apple Account will be required to confirm whether they are 18 years or older. All new Apple Accounts for users under the age of 18 will be required to join a [Family Sharing group](https://support.apple.com/en-us/108380), and parents or guardians will need to provide consent for all App Store downloads, app purchases, and transactions using Apple's In-App Purchase system by the minor. This will also impact developers, who will need to adopt new capabilities and modify behavior within their apps to meet their obligations under the law. Similar requirements will come into effect later next year in Utah and Louisiana.

Today we’re sharing details about updates that we’re making and the tools we’ll provide to help developers meet these new requirements.

To assist developers in meeting their obligations in a privacy-preserving way, we’ll introduce capabilities to help them obtain users’ age categories and manage significant changes as required by Texas state law. The [Declared Age Range API](https://developer.apple.com/documentation/declaredagerange/) is available to implement now, and will be updated in the coming months to provide the required age categories for new account users in Texas. And new APIs launching later this year will enable developers, when they determine a significant change is made to their app, to invoke a system experience to allow the user to request that parental consent be re-obtained. Additionally, parents will be able to revoke consent for a minor continuing to use an app. More details, including additional technical documentation, will be released later this fall.

We know protecting kids from online threats requires constant vigilance and effort. That’s why we will continue to create [industry-leading features](https://developer.apple.com/kids/) to help developers provide age-appropriate experiences and safeguard privacy in their apps and games, and empower parents with a [comprehensive set of tools](https://www.apple.com/newsroom/2025/06/apple-expands-tools-to-help-parents-protect-kids-and-teens-online/) to help keep their kids safe online.
