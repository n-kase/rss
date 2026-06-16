---
title: "Rooms at the top: How this ADA-winning team built a title that defies description"
description: "概要と事実 Roomsは、Things, Inc.が開発したユーザー生成型の3Dスペースアプリで、2023年にウェブベースのバージョンとしてリリースされました。ユーザーは空の部屋またはテンプレートから始めて、ボクセル風の装飾品やアイテ..."
date: 2026-06-16T11:06:36+09:00
categories: ["テクノロジー"]
tags: ["Rooms", "Apple Design Award", "voxel", "ユーザー生成コンテンツ", "クリエイティブツール"]
image: "/rss/downloaded_images/042b625f600be7cc9f986f4baa4f1042.jpeg"
---

## AIによる要約

### 概要と事実
Roomsは、Things, Inc.が開発したユーザー生成型の3Dスペースアプリで、2023年にウェブベースのバージョンとしてリリースされました。ユーザーは空の部屋またはテンプレートから始めて、ボクセル風の装飾品やアイテム、ペット、アバターを自由に配置し、大学の寮、中世の城、ファンタジー空間、海賊船、さらにはウィーザーのコンサート会場など、さまざまなシーンを作り出すことができます。このアプリはApple Design Award（ADA）の「Visuals and Graphics」部門を受賞しており、開発チームは4人で構成されています。RoomsはiOSとiPadOS向けに提供されており、Luaスクリプト言語をC++とUnityでラップした仕組みにより、各部屋が独立したUnityインスタンスとして動作します。さらに、アイテムをクリックするとその裏側のコードが表示され、ユーザーはコードを編集してカスタマイズを深めることができます。開発陣はレゴやKid Pixなどの幼少期の遊びからインスピレーションを得て、4歳から祖父母まで幅広い年齢層が使えるよう、自由度が高く創造的な体験を目指しました。リリース当初はウェブ版でしたが、モバイル版への移行を優先し、現在はほとんどのユーザーがiPhoneやiPadで部屋の編集に時間を費やしています。コミュニティは活発で、ユーザーが作成したアイテムは現在10,000点以上に達しており、たとえば木の枝に揺れ効果を加えるだけで生きているように見えるという発見が広まるなど、共有と改良のサイクルが生まれています。

### ネットの反応と意見の変遷
記事が公開されると、ネット上ではRoomsが「ゲームなのか、ツールなのか」という議論がすぐに巻き起こりました。多くのユーザーは「ゲームのように楽しめるが、同時に創作のためのツールとしても使える」という柔軟性を称賛し、特に子どもから高齢者まで幅広く受け入れられている点に好感を持っていました。一方で、従来のゲームカテゴリに当てはまらないため、ストアでの検索やレーティングがやや混乱するという指摘も見られました。時間が経つにつれて、コミュニティ内で共有されるクリエイティブなアイテムやスクリプトの例が増え、「自分だけの世界を作れる」という感覚が強調されるようになりました。また、開発チームがオフィス自身をRooms内で再現したエピソードが話題となり、開発者自身が製品を愛用している姿が好印象を与えました。結果として、最初は「何に分類すればいいのか」という疑問があったもの、実際に使ってみたユーザーからは「自由度が高く、飽きが来ない」という肯定的なフィードバックが増えていきました。

### 背景と結論
Roomsの成功は、デジタル空間における「低い入り口と高い天井」という設計哲学に起因しています。ブロックベースのボクセルアプローチにより、直感的に操作できながらも、Luaスクリプトを通じて高度なカスタマイズが可能となり、初心者からプログラマーまで幅広い層が満足できる仕組みになっています。このような柔軟性は、早期インターネットのオープンで実験的な精神を現代のモバイルプラットフォームに呼び戻すものとして評価されています。さらに、ユーザーが生み出すコンテンツがプラットフォーム自体を豊かにするという好循環は、ソーシャルネットワークとしての側面も強めており、単なるアプリやゲームを超えた「創造の場」としての価値を示しています。今後もこのようなユーザー参加型の創造プラットフォームは、教育やエンターテイメント、コミュニティ形成の分野でさらに影響を拡大していくことが期待されます。

[🔗 元記事を読む](https://developer.apple.com/news/?id=sqd5xv4n)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## Rooms at the top: How this ADA-winning team built a title that defies description

April 8, 2025



![A series of iPhones, all showing different screens from Rooms, in a diagonal floating layout against a deep purple background.](/rss/downloaded_images/042b625f600be7cc9f986f4baa4f1042.jpeg)



Ask Jason Toff whether his Apple Design Award winner is a game or an app, and his answer is yes.

“There’s no one-sentence description for *Rooms*, and that can be a blessing,” laughs Toff, CEO and head designer of Things, Inc. “It’s not entirely a game, and it’s not entirely a tool. It’s more like a toy.”

It’s also a blank canvas, cozy game, coding teacher, and social network — but we’re getting ahead of ourselves. At its heart, *Rooms* is a collection of user-generated 3-D spaces that feels like the open-ended world of the early internet. Start with an empty room or existing template, then fill it with an array of voxel decorations, items, pets, and avatars to create whatever space you like: a college apartment, medieval castle chamber, floating fantasy realm, pirate ship, or a Weezer concert (really), to name just a few. The only limits are the room’s boundaries — and *Rooms* fans have even gotten around those. “Our 404 page is a room with no walls,” Toff says, “so people just started copying it to work around the constraint.”

ADA FACT SHEET



![A screenshot from Rooms, showing a cluttered dorm room in voxel-art style. A loft bed, bookshelf, and assorted books and decorations can be seen in the room.](/rss/downloaded_images/2912bbd9fa76859a05484fbd12752d9c.jpeg)



### Rooms

- **Winner:**Visuals and Graphics
- **Team:**Things, Inc.
- **Available on:**iOS, iPadOS
- **Team size:**4

[Download Rooms from the App Store](https://apps.apple.com/us/app/rooms/id6443548715)

In fact, that community element is a strong point: This creative tapestry of quirky games, tranquil havens, and clever ideas has been conjured by real people, which makes *Rooms* a social network as well. What’s more, users can click on each item to reveal its underlying code, offering them more options for customization.

To create *Rooms* — which, incidentally, won the ADA for Visuals and Graphics in games — Toff and cofounders Nick Kruge and Bruno Oliveira threw themselves back into their childhoods. “I was obsessed with Legos as a kid,” says Toff, not unexpectedly. “I found myself wondering, ‘What’s the digital equivalent of that?’”



![A screenshot from Rooms, showing a bowl of ramen on a table in a restaurant. Around it are other bowls and a tray of toppings.](/rss/downloaded_images/938e29e2df3a5dd51d5b0e3603ebf01c.jpeg)



*Rooms* isn’t just about rooms; creators have plenty of ways to noodle on their ideas.

Drawing on that inspiration — as well as Toff’s experiences with *Kid Pix* on his dad’s 1989-era Mac — the *Rooms* team began envisioning something that, as Oliveira says, kept the floor low but the ceiling high. “We wanted anyone from 4-year-olds to their grandparents to be able to use *Rooms*,” he says, “and that meant making something free-form and creative.”

It also meant building something that gave a sense of approachability and creativity, which led them right to voxels. “Blocks have a charm, but they can also be kind of ugly,” Toff laughs. “Luckily, Bruno’s were cute and soft, so they felt approachable and familiar.” And from Oliveira’s side, blocks offered a practical value. “It’s much easier to do 3-D modeling with blocks,” says Oliveira. “You can just add or remove voxels whenever you want, which lowers the bar for everyone.”

We wanted anyone from 4-year-olds to their grandparents to be able to use

Rooms, and that meant making something free-form and creative.Jason Toff, CEO and head designer of Things, Inc.


*Rooms* launched in 2023 as a web-based app that included 1,000 voxel objects and allowed users to write their own code. It gained traction through both word of mouth and, more directly, a video that went viral in the cozy-gaming community. “All of a sudden, we had all these people coming,” says Oliveira, “and we realized we needed to prioritize the mobile app. Nick was like, ‘I think we can get feature parity with desktop on the iPhone screen,’ and we basically pulled a rabbit out of a hat.” Today, the vast majority of *Rooms* users are on mobile, where they spend the bulk of their time editing. “We were just shocked by how much time people were spending making rooms,” he says. “These weren’t quick five-minute projects. We did not anticipate that.”



![A rendering of the Things, Inc., offices in Rooms style. In the illustration, three voxel-art people sit at computers in a corner offices with windows overlooking a city.](/rss/downloaded_images/05a539696ee0d7860f9033421151234d.jpeg)



Of course the Things, Inc. team rebuilt their own offices in *Rooms*.

All that building fed into a social aspect as well. Toff says most of the items in *Rooms* are now created, edited, and amplified by lots of different users. “Here’s a good example: We have a sway effect that makes things wave back and forth a little,” he says. “Someone realized that if they put some branches on a tree and added that effect, the tree immediately looked alive. Now everyone’s doing that. There’s a real additive effect to building in Rooms.” Today, the Rooms library contains more than 10,000 items.

There’s a lot of power under the hood, too. “Rooms uses a Lua scripting language that runs in a C++ context,” says Oliveira, “so it’s kind of Lua, encased in C++, encased in Unity, encased in iOS.” Every room, he says, is a new Unity instance. And adding native iOS elements — like sliders on the Explore page and a bottom navigation — gives what he calls the “design chef’s kiss.”



![An early prototype of Rooms that shows a corner living room with blue walls and a blue floor. An orange ball sits on the floor, and a purple couch and lamp with yellow shade can be seen.](/rss/downloaded_images/83014191e01de419192152a2c0a8c2d8.jpeg)



An early sketch of *Rooms* shows how the room design came together early in the process.

Like its community, the *Rooms* team is used to moving fast. “One day I said, ‘It would be cool if this had a D-pad and A/B buttons,” says Toff, “and about 10 hours later Bruno was like, ‘Here you go.’” On another lark, Toff mentioned that it would be fun to let users fly around their rooms, and Kruge and Oliveira promptly created a “camera mode” that’s come to be known internally as the “Jason-Cam.”

That’s satisfying to a team that simply set out to build a cutting-edge plaything. “We always had this metaphor that Rooms was a swimming pool with a shallow side and a deep side,” says Oliveira. “It should be fun for people dabbling in the shallow side. But it should also be amazing for people swimming in the deep end. If you just want to look at rooms, you can. But you can also dive all the way down and write complicated code. There’s something for everyone.”

[Meet the 2024 Apple Design Award winners](https://developer.apple.com/design/awards/)

*Behind the Design is a series that explores design practices and philosophies from finalists and winners of the Apple Design Awards. In each story, we go behind the screens with the developers and designers of these award-winning apps and games to discover how they brought their remarkable creations to life.*

</details>
