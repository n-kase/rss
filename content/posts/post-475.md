---
title: "Walk this way: How Oko leverages AI to make street crossings more accessible"
description: "概要と事実 Okoは、視覚に障害がある人や低視力の人々が横断歩道を安全に渡れるように支援するiPhoneアプリです。2024年のApple Design Award（インクルーシブ部門）およびApp Store Award（カルチャー..."
date: 2026-06-16T11:14:21+09:00
categories: ["テクノロジー"]
tags: ["Oko", "AI", "アクセシビリティ", "アプリ開発", "Apple Design Award"]
image: "/rss/downloaded_images/0bd08ba3be2c34c09b13adc1e15431db.jpeg"
---

## AIによる要約

### 概要と事実
Okoは、視覚に障害がある人や低視力の人々が横断歩道を安全に渡れるように支援するiPhoneアプリです。2024年のApple Design Award（インクルーシブ部門）およびApp Store Award（カルチャーインパクト部門）を受賞しています。アプリはカメラとAIを使って歩行者信号の状態（歩行可、歩行不可など）をリアルタイムで認識し、ハプティック、音声、視覚フィードバックでユーザーに知らせます。開発はベルギーに拠点を置くAYES BVの三人（ヴィンセント・ジャンセン、ミシェル・ジャンセン、ウィレム・ファン・デ・ミエロップ）が中心となり、パンデミック中に趣味のプロジェクトとして始まりました。当初はハードウェアベースのプロトタイプを試しましたが、使い勝手の問題からソフトウェアへ転換し、Swiftをゼロから学んでアプリを完成させました。2021年12月にApp Storeでリリースされ、現在では6人のチームで運営・改善が続いています。

### ネットの反応と意見の変遷
この記事にはネット上の反応やコメントは含まれていませんので、具体的な議論の流れや意見の変遷についてはお伝えできません。

### 背景と結論
Okoの開発チームは、視覚に障害がある友人が外出時に孤立しやすい現状に気づき、AIを活用した簡単なソリューションを模索しました。開発過程では、ハードウェアの制約やiOS開発経験の欠如といった課題に直面しましたが、実際のユーザーからのフィードバックを取り入れながらUIをポートレートモードに最適化し、音声やハプティックフィードバックを既存の信号音に近づける改善を行いました。その結果、シンプルかつ直感的に使えるアプリが完成し、視覚障害者の外出の自信と安全性を高めるツールとして広く評価されています。この事例は、専門的な開発経験がなくてもユーザー中心の設計と迅速なプロトタイピングが社会的インパクトを生む可能性を示しており、アクセシビリティ分野におけるテクノロジーの活用の好例と言えます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=58c4urmu)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Walk this way: How Oko leverages AI to make street crossings more accessible

January 7, 2025



![Screenshots of the app Oko, which show a live camera view of a street crossing with text that says “Countdown signal” and “Don’t walk signal” over the image.](/rss/downloaded_images/0bd08ba3be2c34c09b13adc1e15431db.jpeg)



*Oko* is a testament to the power of simplicity.

The 2024 Apple Design Award winner for Inclusivity and 2024 App Store Award winner for Cultural Impact leverages Artificial Intelligence to help blind or low-vision people navigate pedestrian walkways by alerting them to the state of signals — “Walk,” “Don’t Walk,” and the like — through haptic, audio, and visual feedback. The app instantly affords more confidence to its users. Its bare-bones UI masks a powerful blend of visual and AI tools under the hood. And it’s an especially impressive achievement for a team that had no iOS or Swift development experience before launch.

“The biggest feedback we get is, ‘It’s so simple, there’s nothing complex about it,’ and that’s great to hear,” says Vincent Janssen, one of *Oko*’s three Belgium-based founders. “But we designed it that way because that’s what we knew how to do. It just happened to also be the right thing.”

ADA FACT SHEET



![Oko’s three cofounders, Vincent Janssen, Michiel Janssen, and Willem Van de Mierop, gather around a bank of monitors to review their app.](/rss/downloaded_images/022952c0c72cb0ae2072e72345f0db10.jpeg)



From left: Willem Van de Mierop, Michiel Janssen, and Vincent Janssen are the three cofounders of *Oko*. The app’s name means “eye.”

### Oko

- **Winner:**Inclusivity
- **Team:**AYES BV
- **Available on:**iPhone
- **Team size:**6
- **Previous accolades:**2024 App Store Award winner for Cultural Impact; App Store Editors’ Choice

[Download Oko from the App Store](https://apps.apple.com/us/app/oko-cross-streets-and-maps/id1583614988)

For Janssen and his cofounders, brother Michiel and longtime friend Willem Van de Mierop, Oko — the name translates to “eye” — was a passion project that came about during the pandemic. All three studied computer science with a concentration in AI, and had spent years working in their hometown of Antwerp. But by the beginning of 2021, the trio felt restless. “We all had full-time jobs,” says Janssen, “but the weekends were pretty boring.” Yet they knew their experience couldn’t compare to that of a longtime friend with low vision, who Janssen noticed was feeling more affected as the autumn and winter months went on.

“We really started to notice that he was feeling isolated more than others,” says Janssen. “Here in Belgium, we were allowed to go for walks, but you had to be alone or with your household. That meant he couldn’t go with a volunteer or guide. As AI engineers, that got us thinking, ‘Well, there are all these stories about autonomous vehicles. Could we come up with a similar system of images or videos that would help people find their way around public spaces?’”

I had maybe opened Xcode three times a few years before, but otherwise none of us had any iOS or Swift experience.

Vincent Janssen,

Okofounder

The trio began building a prototype that consisted of a microcomputer, 3D-printed materials, and a small portable speaker borrowed from the Janssen brothers’ father. Today, Janssen calls it “hacky hardware,” something akin to a small computer with a camera. But it allowed the team and their friend — now their primary tester — to walk the idea around and poke at the technology’s potential. Could AI recognize the state of a pedestrian signal? How far away could it detect a Don’t Walk sign? How would it perform in rain or wind or snow? There was just one way to know. “We went out for long walks,” says Janssen.

And while the AI and hardware performed well in their road tests, issues arose around the hardware’s size and usability, and the team begin to realize that software offered a better solution. The fact that none of the three had the slightest experience building iOS apps was simply a hurdle to clear. “I had maybe opened Xcode three times a few years before,” says Janssen, “but otherwise none of us had any iOS or Swift experience.”



![Two screenshots of the app Oko. The screenshot on the left shows a suggested walking path through a map view. The screenshot on the right shows a live image of a street crossing with the words “Walk signal” highlighted in a green bubble at the top of the screen.](/rss/downloaded_images/24b60bf14692fe0ca68ecfa60492f7f3.jpeg)



*Oko* helps people navigate pedestrian walkways through interactive maps and audio, visual, and haptic feedback.

So that summer, the team pivoted to software, quitting their full-time jobs and throwing themselves into learning Swift through tutorials, videos, and trusty web searches. The core idea crystallized quickly: Build a simple app that relied on Camera, the Maps SDK, and a powerful AI algorithm that could help people get around town. “Today, it’s a little more complex, but in the beginning the app basically opened up a camera feed and a Core ML model to process the images,” says Janssen, noting that the original model was brought over from Python. “Luckily, the tools made the conversion really smooth.” (*Oko*’s AI models run locally on device.)

With the software taking shape, more field testing was needed. The team reached out to accessibility-oriented organizations throughout Belgium, drafting a team of 100 or so testers to “codevelop the app,” says Janssen. Among the initial feedback: Though *Oko* was originally designed to be used in landscape mode, pretty much everyone preferred holding their phones in portrait mode. “I had the same experience, to be honest,” said Janssen, “but that meant we needed to redesign the whole thing.”



![A group of men stand in a room with green walls looking at a large monitor that contains notes and sketches for the app *Oko*.](/rss/downloaded_images/6222af067a16f01b65b80123bffb8da6.jpeg)



The *Oko* team navigates through prototypes at a review session in their hometown of Antwerp, Belgium.

Other changes included amending the audio feedback to more closely mimic existing real-world sounds, and addressing requests to add more visual feedback. The experience amounted to getting a real-world education about accessibility on the fly. “We found ourselves learning about VoiceOver and haptic feedback very quickly,” says Janssen.

Still, the project went remarkably fast — *Oko* launched on the App Store in December 2021, not even a year after the trio conceived of it. “It took a little while to do things, like make sure the UI wasn’t blocked, especially since we didn’t fully understand the code we wrote in Swift,” laughs Janssen, “but in the end, the app was doing what it needed to do.”

We found ourselves learning about VoiceOver and haptic feedback.

Vincent Janssen,

Okofounder

The accessibility community took notice. And in the following months, the *Oko* team continued expanding its reach — Michiel Janssen and Van de Mierop traveled to the U.S. to meet with accessibility organizations and get firsthand experience with American street traffic and pedestrian patterns. But even as the app expanded, the team retained its focus on simplicity. In fact, Janssen says, they explored and eventually jettisoned some expansion ideas — including one designed to help people find and board public transportation — that made the app feel a little too complex.

Today, the *Oko* team numbers 6, including a fleet of developers who handle more advanced Swift matters. “About a year after we launched, we got feedback about extra features and speed improvements, and needed to find people who were better at Swift than we are,” laughs Janssen. At the same time, the original trio is now learning about business,

...（長文のため省略されました）

</details>
