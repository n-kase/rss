---
title: "Q&amp;A: How Plane Finder set itself up for the long haul"
description: "概要と事実 Plane Finderは2009年にリリースされたフライトトラッキングアプリで、創業者であるジョディーとリー・アームストロング夫妻が率いるわずか8人のチームによって運営されています。当初は単純に「地図上の飛行機」を表示す..."
date: 2026-06-16T10:40:17+09:00
categories: ["テクノロジー"]
tags: ["Plane Finder", "Apple ecosystem", "flight tracking", "small team", "Liquid Glass"]
image: "/rss/downloaded_images/5b3fd25c726e0634211c5f2bda3f0e5f.jpeg"
---

## AIによる要約

### 概要と事実
Plane Finderは2009年にリリースされたフライトトラッキングアプリで、創業者であるジョディーとリー・アームストロング夫妻が率いるわずか8人のチームによって運営されています。当初は単純に「地図上の飛行機」を表示するだけのアプリでしたが、Appleのプラットフォームにネイティブで対応し続けることで、独自の受信機ネットワークを構築し、世界中の航空機から位置情報を直接取得するエンド・ツー・エンドのフライトトラッキングビジネスへと進化しました。MapKitやMetal、StoreKit 2などのApple純正ツールを活用し、サードパーティ製フレームワークやクロスプラットフォームツールに頼らない開発方針を貫いています。さらに、最新のUIデザインであるLiquid Glassへの早期導入や、機械学習やファウンデーションモデルへの取り組みも進めています。

### ネットの反応と意見の変遷
記事内では開発者コミュニティからのフィードバックが重要な位置を占めており、ジョディーはApple内部のスタッフから熱意ある意見を頻繁に受け取っていると述べています。これにより、ツールの正しい使い方や実装の妥当性を確認し、改善点を見つけることができたと語っています。また、ユーザー側からも「自分の地域では飛行機が見えない」といった声が寄せられ、それをきっかけに受信機を配布してネットワークを拡大してきた経緯が紹介されています。こうした双方向のやり取りは、時間とともに技術選択や製品方針の微調整に反映され、コミュニティの声を製品改善に活かすサイクルが形成されていることが伺えます。

### 背景と結論
Plane Finderの成功は、プラットフォームの変化に早期に適応し、ネイティブ開発に特化することで得られる安定性と拡張性によるものです。小規模チームでも、プラットフォームが提供する統合ツール（決済、ローカライズ、クラウドサービスなど）を活用すれば、グローバル規模のサービスを構築できるという示唆を与えています。さらに、自社でハードウェアを設計・製造し、ユーザー参加型でネットワークを拡大するアプローチは、デジタルサービスと物理インフラを結びつける新たなビジネスモデルとして注目されます。今後はLiquid Glassの完全導入や機械学習の活用により、さらに高度なユーザー体験とデータ分析が期待され、小さなチームでもプラットフォームの力を借りて長期的に成長できるという教訓が得られます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=cmd9p4g7)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Q&A: How Plane Finder set itself up for the long haul

April 3, 2026



![Two iPhone screenshots of the app Plane Finder. The screenshot on the left shows a map of the San Francisco area and information about a flight from JFK to SFO. The screenshot on the right show a map of all plane traffic activity over Europe.](/rss/downloaded_images/5b3fd25c726e0634211c5f2bda3f0e5f.jpeg)



*Plane Finder* is a sparkling example of what happens when a small team grows with a platform.

Launched in 2009, *Plane Finder* didn’t scale over the years by adding headcount, vendors, or complexity. Instead, founders Jodie and Lee Armstrong made a long-term bet on Apple’s ecosystem — staying native, sticking close to first-party tools, and reading platform signals early. And over time, an app that began as “planes on a map” evolved into a full end-to-end flight-tracking business — one that includes a global network of physical hardware — built and operated by a team of just eight people.

We talked to the married founders about their early days, the new design and Liquid Glass, and the challenges of running a global flight tracking network.

### Plane Finder

- **Available on:**iPhone, iPad, Apple Watch
- **Team size:**8
- **Based in:**UK

[Download Plane Finder from the App Store >](https://apps.apple.com/us/app/plane-finder-flight-tracker/id361273585)

**Take us back to 2009. What sparked the idea for  Plane Finder, and what were those early days like?**

**Lee:** We’ve been on the App Store since about a year after it opened. It feels like a lifetime. But the real spark was seeing the unveiling of the iPhone itself in 2007. We were actually in the United States when it came out, so we picked one up, not really knowing what we’d do with it. There was no App Store yet, and I couldn’t even use it as a phone in the UK. It was literally just to hold and swipe back and forth. But that moment became such a huge part of our journey. We still have that iPhone on display.

**In those early days, did you have aspirations of becoming an end-to-end flight tracking platform?**

**Jodie:** Not at all. We started with just the app. Today, we collect our own positional information directly from aircraft, put it inside apps, and sell our data commercially.

**You’re a small team of eight people. What’s that like?**

**Lee:** I don’t think we could have done it without Apple technologies. We’re a small team, and we wouldn’t have the platform or methods to market on a global scale without the App Store — credit cards, StoreKit, localization. We really value the App Store as a platform.



![](/rss/downloaded_images/68beb02574f96c0a17cbc64e29432ccb.jpeg)



*Plane Finder* is known for adopting Apple technologies and features — like ARKit, MapKit, and Liquid Glass — early. Which tools have made the biggest difference?

**Lee:** It all goes back to MapKit. We flippantly say the app is “planes on a map,” and MapKit is core to that. We’re also big users of Metal for our 3D globe view. And we just wouldn’t be able to handle subscriptions and monetization with promotional offers without StoreKit 2. We don’t use any third parties or cross-platform frameworks. We’re all in on Apple technologies because they provide everything we need.

**What made you willing to be such early adopters?**

**Jodie:** I steer the company from the mindset of a quote I heard years ago: “When new technologies come along, you can either be part of the steamroller or part of the road.” We always want to be part of the steamroller. We’re quick to evaluate new technology, and if we can lean into it in a way that makes sense for our products, we go for it.

**Can you talk about the process of adopting Liquid Glass?**

**Jodie:** We were on board with the concept straight away. From a leadership perspective, we said, “This is the future. We’ve got to make it make sense for what we do.” The design and engineering teams worked incredibly hard bringing those two things together — staying current and leaning into the tech while making it make sense for our world.

**What does the developer community mean to you?**

**Lee:** It’s the reinforcement piece. When you’re working in silos, the community gives you confidence that you’re applying technologies correctly. It’s all well and good seeing WWDC sessions with slides and sample code, but that’s very specific. Seeing how it works in the real world is invaluable.

**Jodie:** Everyone I speak to within Apple has passion and opinions about our app. They’re very engaged, and every piece of feedback is valuable. We’ve been asked questions over the years like “Why do you do this with your toolbar?” All that conversation is helpful.



![A photo of six members of the Plane Finder team, all standing outside in a courtyard next to an office building.](/rss/downloaded_images/af549337ee0e663a95fc4a82d3d44091.jpeg)



*Plane Finder* isn’t just an app. You’ve deployed thousands of flight tracking devices worldwide. How has Apple’s ecosystem enabled that?

**Jodie:** There’s a symbiotic relationship between people enjoying the app and wanting to get involved by hosting receivers where we need coverage.

**Lee:** When we first started, we had one receiver covering the south of the UK. People downloaded the app and said, “This is great, but I live in Scotland and can’t see any planes.” So we’d send them a receiver. Before long, we heard that from Sweden, the United States, Africa, and Asia.

**Jodie:** Today, we use the app to find people in locations where we want to improve coverage. We’re leveraging the power of the audience to grow the network even further.

**What’s next?**

**Jodie:** We haven’t finished our Liquid Glass journey. We’re working on an internal project code-named “Plane Finder Double Glazed” — the next iteration with wider UI changes that we held back initially. We’re also looking at how we can leverage machine learning and foundation models.

**What’s one thing people don’t realize about running a global flight tracking network?**

**Lee:** We own and operate the network of receivers that power it. A lot of people think we buy that data like other companies do.

**Jodie:** We’ve designed and manufactured receivers and antennas. There’s more to us than just being an app!

### Keep reading

Developer stories explore best practices and philosophies from some of the most inventive developers in the Apple community. In each story, we go behind the screens with developers, designers, and engineers to find out how they brought their remarkable creations to life.

</details>
