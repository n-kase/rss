---
title: "Coding in the kitchen: How Devin Davies whipped up the tasty recipe app Crouton"
description: "概要と事実 ニュージーランド在住の開発者デビン・デイビスは、自分の料理の手助けになるアプリ「Crouton」をSwiftで開発し、2024年のApple Design Award（インタラクション部門）を受賞しました。Croutonは..."
date: 2026-06-16T11:17:28+09:00
categories: ["テクノロジー"]
tags: ["アプリ開発", "Swift", "Apple Design Award", "クッキングアプリ", "インディーデベロッパー"]
image: "/rss/downloaded_images/f68c91097aa8468a5465305fe6c4cc31.jpeg"
---

## AIによる要約

### 概要と事実
ニュージーランド在住の開発者デビン・デイビスは、自分の料理の手助けになるアプリ「Crouton」をSwiftで開発し、2024年のApple Design Award（インタラクション部門）を受賞しました。Croutonは、ウェブのレシピや古い料理本のメモ、手書きのメモなど、どこからでもレシピを取り込み、機械学習を使って材料を分類・整理する機能を持ちます。調理中は現在の手順・材料・分量（単位変換も含む）だけを表示し、別のアプリに切り替える必要がないように設計されています。デイビスは最初はメモアプリで献立を管理していましたが、使い勝手が悪くなったことをきっかけに、自分のニーズを解決するアプリを作り始めました。Swiftを独学で習得し、約6か月で最初のバージョンをリリースし、その後数年にわたってアップデートを重ね、最終的に受賞に至りました。

### ネットの反応と意見の変遷
この記事にはネット上の反応やコメントは含まれていないため、ネットの反応については記載できません。

### 背景と結論
デイビスはフルタイムの仕事のかたわら、父親も開発者である環境の中でプログラミングに興味を持ち、Swiftが自分に合っていると感じました。彼は「必要なものだけを残し、余計な機能は削る」という設計哲学を貫き、シンプルで直感的な操作感を追求しました。その結果、Croutonは個人開発者でありながら広く使われるツールとなり、料理の準備時間を短縮し、家族や友人への食事作りをサポートしています。今後はApple IntelligenceやApple WatchのLive Activities、翻訳APIなどを活用して機能を拡張したいと考えていますが、基本的なコンセプトは変えない姿勢を強調しています。このように、自分の課題を解決するために作ったアプリが評価される事例は、個人開発者にとっての励みとなり、技術と日常生活の結びつきがイノベーションを生む好例と言えます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=9x75y43e)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Coding in the kitchen: How Devin Davies whipped up the tasty recipe app Crouton

November 4, 2024



![An illustration of a kitchen with teal walls and white cabinets. Two Apple Vision Pro screens float above a stove, on which sits a pot and pan.](/rss/downloaded_images/f68c91097aa8468a5465305fe6c4cc31.jpeg)



Let’s get this out of the way: Yes, Devin Davies is an excellent cook. “I’m not, like, a professional or anything,” he says, in the way that people say they’re not good at something when they are.

But in addition to knowing his way around the kitchen, Davies is also a seasoned developer whose app *Crouton*, a Swift-built cooking aid, won him the 2024 Apple Design Award for Interaction.

*Crouton* is part recipe manager, part exceptionally organized kitchen assistant. For starters, the app collects recipes from wherever people find them — blogs, family cookbooks, scribbled scraps from the ’90s, wherever — and uses tasty ML models to import and organize them. “If you find something online, just hit the Share button to pull it into *Crouton*,” says the New Zealand-based developer. “If you find a recipe in an old book, just snap a picture to save it.”

And when it’s time to start cooking, *Crouton* reduces everything to the basics by displaying only the current step, ingredients, and measurements (including conversions). There’s no swiping around between apps to figure out how many *fl oz* are in a cup; no setting a timer in a different app. It’s all handled right in *Crouton*. “The key for me is: How quickly can I get you back to preparing the meal, rather than reading?” Davies says.

ADA FACT SHEET



![A Crouton screenshot that shows a recipe for butter chicken, with a photo of the dish above a list of ingredients.](/rss/downloaded_images/8b015c4563a9a98c9b7c3a5e15611c5d.jpeg)



### Crouton

- **Winner:**Interaction
- **Available on:**iPhone, iPad, Mac, Apple Vision Pro, Apple Watch
- **Team size:**1

[Download Crouton from the App Store](https://apps.apple.com/us/app/crouton-recipe-manager/id1461650987)

*Crouton* is the classic case of a developer whipping up something he needed. As the de facto chef in the house, Davies had previously done his meal planning in the Notes app, which worked until, as he laughs, “it got a little out of hand.”

At the time, Davies was in his salad days as an iOS developer, so he figured he could build something that would save him a little time. (It’s in his blood: Davies’s father is a developer too.) "Programming was never my strong suit,” he says, “but once I started building something that solved a problem, I started thinking of programming as a means to an end, and that helped.”

Davies’s full-time job was his meal ticket, but he started teaching himself Swift on the side. Swift, he says, clicked a lot faster than the other languages he’d tried, especially as someone who was still developing a taste for programming. “It still took me a while to get my head into it,” he says, “but I found pretty early on that Swift worked the way I wanted a language to work. You can point *Crouton* at some text, import that text, and do something with it. The amount of steps you don’t have to think about is astounding.”

I found pretty early on that Swift worked the way I wanted a language to work.

Devin Davies,

Crouton

Coding with Swift offered plenty of baked-in benefits. Davies leaned on platform conventions to make navigating *Crouton* familiar and easy. Lists and collection views took advantage of Camera APIs. VisionKit powered text recognition; a separate model organized imported ingredients by category.

“I could separate out a roughly chopped onion from a regular onion and then add the quantity using a Core ML model,” he says. “It’s amazing how someone like me can build a model to detect ingredients when I really have zero understanding of how it works.”



![An Apple Vision Pro screenshot of Crouton, showing a window containing a chocolate chip cookie recipe floating over a gray marble kitchen counter.](/rss/downloaded_images/22534b4d14cc1e3a04eb6e5d282ee4d4.jpeg)



Davies designed *Crouton* with simplicity in mind at all times. “I spent a lot of time figuring out what to leave out rather than bring in,” he says.

The app came together quickly: The first version was done in about six months, but *Crouton* simmered for a while before finding its audience. “My mom and I were the main active users for maybe a year,” Davies laughs. “But it’s really important to build something that you use yourself — especially when you’re an indie — so there’s motivation to carry on.”

Davies served up *Crouton* updates for a few years, and eventually the app gained more traction, culminating with its Apple Design Award for Interaction at WWDC24. That’s an appropriate category, Davies says, because he believes his approach to interaction is his app’s special sauce. “My skillset is figuring out how the pieces of an app fit together, and how you move through them from point A to B to C,” he says. “I spent a lot of time figuring out what to leave out rather than bring in.”



![A *Crouton* screenshot that shows a grid of recipes, including burritos, butter chicken, and chocolate chip cookies. Each module includes a photo of the dish.](/rss/downloaded_images/6a82ed0b272b21a32d20c59ac8fd4e9f.jpeg)



*Crouton* recipes can be imported from blogs, cookbook, scraps of paper, or anywhere else they might be found.

Davies hopes to use the coming months to explore spicing up *Crouton* with Apple Intelligence, Live Activities on Apple Watch, and translation APIs. (Though *Crouton* is his primary app, he’s also built an Apple Vision Pro app called *Plate Smash*, which is presumably very useful for cooking stress relief.)

But it’s important to him that any new features or upgrades pair nicely with the current *Crouton*. “I’m a big believer in starting out with core intentions and holding true to them,” he says. “I don’t think that the interface, over time, has to be completely different.”

My skillset is figuring out how the pieces of an app fit together, and how you move through them from point A to B to C.

Devin Davies,

Crouton

Because it’s a kitchen assistant, *Crouton* is a very personal app. It’s in someone’s kitchen at mealtime, it’s helping people prepare means for their loved ones, it’s enabling them to expand their culinary reach. It makes a direct impact on a person’s day. That’s a lot of influence to have as an app developer — even when a recipe doesn’t quite pan out.

“Sometimes I’ll hear from people who discover a bug, or even a kind of misunderstanding, but they’re always very kind about it,” laughs Davies. “They’ll tell me, ‘Oh, I was baking a cake for my daughter’s birthday, and I put in way too much cream cheese and I ruined it. But, great app!’”

[Meet the 2024 Apple Design Award winners](https://developer.apple.com/design/awards/)

*Behind the Design is a series that explores design practices and philosophies from finalists and winners of the Apple Design Awards. In each story, we go behind the screens with the developers and designers of these award-winning apps and games to discover how they brought their remarkable creations to life.*

</details>
