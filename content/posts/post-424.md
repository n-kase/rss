---
title: "Introducing Time Allowances"
description: "Appleは、iOS 27、iPadOS 27、macOS 27以降に新たに導入される「Time Allowances」機能を発表しました。この機能は、エンターテインメント、ゲーム、ソーシャルメディアなどのカテゴリ別に子どものアプリ利..."
date: 2026-06-15T17:49:27+09:00
categories: ["テクノロジー"]
tags: ["Apple", "iOS", "Time Allowances", "親向け管理", "アプリカテゴリ"]
image: "/rss/downloaded_images/3c25aace77a0736d1ec069bb112a52d7.png"
---

## AIによる要約
Appleは、iOS 27、iPadOS 27、macOS 27以降に新たに導入される「Time Allowances」機能を発表しました。この機能は、エンターテインメント、ゲーム、ソーシャルメディアなどのカテゴリ別に子どものアプリ利用時間を柔軟に管理できるように設計されており、専門家の研究に基づき年齢に合わせた初期設定を提供し、保護者が子どもに最適だと判断した設定に調整できるようになります。これにより、保護者は子どものスクリーンタイムをより細かくコントロールでき、過度な利用を抑えることが期待されます。また、アプリ開発者にはソーシャルメディア機能の有無を明示することが求められ、年齢制限の質問票が更新されることで、アプリのカテゴリ分けや年齢評価に影響を与える可能性があります。したがって、開発者はアプリの機能を正確に申告し、年齢に適した設計を心がけるべきであり、保護者はこのツールを活用して子どもにより健全なメディア利用習慣を身につけさせることが推奨されます。





## 和訳本文
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

---

## 元スレッド・記事本文

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
