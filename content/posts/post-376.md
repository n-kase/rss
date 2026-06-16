---
title: "Introducing Time Allowances"
description: "概要と事実 Appleは2026年6月8日に、iOS 27、iPadOS 27、macOS 27以降で新しく導入される「Time Allowances」機能を発表しました。この機能は、エンターテインメント、ゲーム、ソーシャルメディアな..."
date: 2026-06-16T10:33:46+09:00
categories: ["テクノロジー"]
tags: ["iOS", "Time Allowances", "親向け管理", "アプリカテゴリ", "ソーシャルメディア"]
image: "/rss/downloaded_images/3c25aace77a0736d1ec069bb112a52d7.png"
---

## AIによる要約

### 概要と事実
Appleは2026年6月8日に、iOS 27、iPadOS 27、macOS 27以降で新しく導入される「Time Allowances」機能を発表しました。この機能は、エンターテインメント、ゲーム、ソーシャルメディアなどのカテゴリ別に子どもがアプリに費やす時間を保護者が柔軟に管理できるようにするものです。専門家の研究に基づいて作成され、子どもの年齢に合わせた初期設定が提供され、保護者は必要に応じて調整できます。アプリがどのTime Allowanceカテゴリに属するかは、App Store Connectで設定した主要または副次的なカテゴリ（エンターテインメントまたはゲーム）によって決まります。ソーシャルメディアについては、アプリがソーシャル機能を提供しているかどうかを問うアンケートに回答することでカテゴリが決定され、その結果に応じて年齢制限が設定されます。

### ネットの反応と意見の変遷
発表以降、開発者コミュニティではこの新しいカテゴリ分けがアプリの提出プロセスにどのように影響するかが話題になっています。一部の開発者は、ソーシャル機能があるかどうかを明示する義務が増えることで、アップデートの手続きが煩雑になるのではないかと懸念しています。一方で、保護者向けの機能として子どものアプリ利用を適切に管理できる点は評価され、特に年齢に応じた制限をかけやすくなるという声が多いです。時間が経つにつれて、ソーシャル機能をオフにしている未成年向けのアプリについては、Time Allowancesのソーシャルメディアカテゴリに含まれないという仕組みが理解され、混乱が減少してきました。

### 背景と結論
この機能は、デジタル機器の利用が増加する中で、保護者が子どものアプリ使用状況を把握しやすくすることを目的としています。年齢に応じた設定を提供することで、過剰な利用を防ぎつつ、子どもが楽しめるコンテンツへのアクセスを保つバランスを取ろうとしています。今後、2026年9月からは新しいバージョンやアップデートを提出する際に、ソーシャル機能の有無を必ず申告する必要が出てくるため、開発者はアンケートへの対応を早めに行うことが求められます。全体として、子どもへの配慮と開発者の実務負担の両方を考慮した施策であり、今後のアプリエコシステムにおいて重要な役割を果たすと考えられます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=0d2gpmml)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Introducing Time Allowances

June 8, 2026



![](/rss/downloaded_images/14b811a2197feea71d9eec67ccd50138.jpeg)



New Time Allowances in iOS 27, iPadOS 27, and macOS 27, or later, give parents more flexible ways to manage the time their kids spend in apps across categories, including Entertainment, Games, and Social Media. Time Allowances are developed based on expert research and tailored to a child’s age to give parents a helpful starting point. Parents can adjust these settings based on what they determine is best for their child. Time Allowance categories are different from categories for user discovery on the App Store.

### Entertainment and Games

Your app or game will appear in a Time Allowance category based on the information you provide in App Store Connect. Apps and games with Entertainment or Games selected as a primary or secondary category in App Store Connect will be sorted into the corresponding Time Allowance categories.

### Social Media

The Time Allowance category for Social Media will be based on whether your app or game offers social media capabilities, regardless of the category selected in App Store Connect. This includes the ability to redistribute, amplify, or interact with user-generated content through a social feed or similar discovery method that visibly spreads content to many users. Starting July 2026, the age rating questionnaire will be updated to let you indicate whether your app or game includes social media capabilities.

- If you indicate that your app or game includes social media capabilities, it will be placed in the Time Allowance category for Social Media and receive a minimum age rating of 13+.
- If you indicate that your app or game includes social media capabilities but they are disabled for anyone under 13, it won’t be included in the Time Allowance category for Social Media for users under 13. You'll also need to use the Declared Age Range API (at a minimum) to check users’ age ranges. If you select this option, your overall responses in the age rating questionnaire determine your age rating and may result in a rating lower than 13+. Your app or game may still be grouped in the Time Allowance category for Games or Entertainment based on the primary or secondary category selected in App Store Connect, and will remain in the Social Media category for users 13 and above.

Starting September 2026, you’ll be required to indicate whether your app or game includes social media capabilities in order to submit new versions or updates to the App Store, or for notarization for distribution on alternative app marketplaces.

[Design safe and age‑appropriate experiences for your apps and games](https://developer.apple.com/kids/)

</details>
