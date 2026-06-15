---
title: "なぜAppleは広色域の色空間としてAdobe RGBではなくDCI-P3を採用したのか？"
description: "Appleは2015年のiMacで従来のsRGBより広い色域を持つDCI‑P3系のディスプレイを採用し、広色域ディスプレイではよく知られるAdobe RGBではなくDCI‑P3を選んだ理由を、色域図や実際の写真を使って分析した記事が話..."
date: 2026-06-15T15:25:14+09:00
categories: ["テクノロジー"]
tags: ["Apple", "DCI-P3", "Adobe RGB", "ディスプレイ", "色空間"]
image: "/rss/downloaded_images/5516b7c5a905c4b49ef58dc7d5e13e5d.jpg"
---

## AIによる要約
Appleは2015年のiMacで従来のsRGBより広い色域を持つDCI‑P3系のディスプレイを採用し、広色域ディスプレイではよく知られるAdobe RGBではなくDCI‑P3を選んだ理由を、色域図や実際の写真を使って分析した記事が話題になっている。この分析では、DCI‑P3は青色を除く多くの色でバランスよく広げられ、特に黄緑・黄・オレンジ・赤・マゼンタなどではAdobe RGBよりも広い範囲を再現できる一方、青緑や一部の緑ではAdobe RGBが上回ることが示され、両者は得意とする色域が異なる補完的な関係にあると説明されている。これにより、Appleは専門的な印刷や映像制作だけでなく、一般ユーザーが写真や動画をより鮮やかに楽しめるよう、色のバランスを重視した色空間を採用したと推測され、色再現の目的によって適切な色空間を選ぶ重要性が改めて浮き彫りになった。したがって、色管理を行う際は用途や対象とする色の特性に応じてsRGB、Adobe RGB、DCI‑P3などの色空間を使い分けるべきだという教訓が得られる。

---

## 元スレッド・記事本文

# なぜAppleは広色域の色空間としてAdobe RGBではなくDCI-P3を採用したのか？

![](/rss/downloaded_images/5516b7c5a905c4b49ef58dc7d5e13e5d.jpg)

Appleは2015年10月13日に登場したiMacで従来のsRGBより広い色域を表示できるP3対応ディスプレイを採用しました。広色域ディスプレイではAdobe RGBがよく知られているにもかかわらずなぜAppleがDCI-P3系の色空間を採用したのかを、写真や色管理を扱うサイト「Astramael」が2015年10月19日に公開した記事で実写サンプルや色域図を使って分析しています。

**The Wide Gamut World of Color — iMac Edition**

[http://www.astramael.com/1](http://www.astramael.com/1)

![](/rss/downloaded_images/67e719c4f664f483e90f24b299c7569d.png)

色域とはディスプレイや画像データが表現できる色の範囲のことです。一般的なウェブ画像や多くの写真では標準的な色空間である** sRGB**が使われていますが、より広い色域を扱う色空間として

**や**

[Adobe RGB](https://en.wikipedia.org/wiki/Adobe_RGB_color_space)**があります。**

[DCI-P3](https://ja.wikipedia.org/wiki/DCI-P3)通常の白色LEDバックライトは青い光が強い一方、赤色や緑色の光はそれほど強くありません。2015年後半のiMacでは緑色と青色のLEDに赤色の蛍光体を組み合わせたGB-r LEDバックライトを使うことで赤色と緑色の成分を強め、緑色・赤色・シアン・黄色・マゼンタなどをより鮮やかに表示できるようになったとのこと。

Adobe RGBはプロ向けのディスプレイでよく使われる広色域の色空間ですが、AppleはiMacの広色域ディスプレイでAdobe RGBではなくDCI-P3系のApple P3を採用しました。AstramaelではAppleが採用したDCI-P3系の色空間のことを「Apple P3」と表記しています。

2D色度図でAdobe RGBとApple P3を比べると、青緑色や緑色の一部ではAdobe RGBよりもApple P3のカバー範囲が狭くなっていることが分かります。しかし黄緑色・黄色・オレンジ色・赤色・マゼンタでは、Adobe RGBよりもApple P3の方が広い範囲をカバーできています。

![](/rss/downloaded_images/118d8dc9cca3525e419cd3d271e4f287.jpg)

また、標準的なsRGBと比べるとApple P3の方がかなり広い色域をカバーしていることも示されています。

![](/rss/downloaded_images/f1b153b030323fbdb5d2eb95d8fca355.jpg)

これらの比較をもとに、Astramaelは「Apple P3はAdobe RGBを全面的に上回る色空間ではなく、得意な色が異なる色空間」と説明しています。以下はカナダ・ジャスパー国立公園のバレー・オブ・ファイブ・レイクスにあるファースト・レイクの写真です。

![](/rss/downloaded_images/f86976852c7c723cc06732629b5dea29.jpg)

青緑色はAdobe RGBがApple P3を上回る例とされており、Adobe RGBとApple P3のどちらもsRGBよりかなり広い範囲を再現できるとのこと。以下の画像では各色空間で再現できない部分に色を重ねて示されており、赤色はsRGBで再現できない部分、青色はsRGBとApple P3で再現できない部分、緑色はsRGB・Apple P3・Adobe RGBのいずれでも再現できない部分を表しています。画像から、sRGB→Apple P3→Adobe RGBの順に色のカバー範囲が広くなっていることが読み取れます。

![](/rss/downloaded_images/15d52ce4f764ea98f9c1b5e82d2f8c75.jpg)

続いて、以下はオレンジ色に塗装された自動車「E92 BMW M3」の写真。オレンジ色は「Apple P3がAdobe RGBとsRGBの両方を上回る領域のひとつ」と説明されています。

![](/rss/downloaded_images/c8626d06436bfa0912c212dd272db803.jpg)

以下の画像ではそれぞれの色空間で再現できない部分に色が重ねられており、緑色がsRGBで再現できない部分、青色がApple P3で再現できない部分、ピンク色がAdobe RGBで再現できない部分です。オレンジ色の塗装ではsRGBやAdobe RGBで再現できない部分が広く示されている一方、Apple P3で再現できない部分は少なく、Apple P3がこのオレンジ色を得意としていることが分かります。

![](/rss/downloaded_images/776fbd654717044593186ec23e79bd02.jpg)

また、緑色のオオハナインコの写真を使った比較では、Apple P3とAdobe RGBが同じ写真の中の異なる緑色を得意としていることが取り上げられています。

![](/rss/downloaded_images/61412c19428e7192b4baf5b1c73cbc3d.jpg)

以下の画像のピンク色はsRGBで再現できない部分、黄色はApple P3で再現できない部分、青色はAdobe RGBで再現できない部分を表しており、Apple P3は背景の植物にある黄緑色をうまく再現できる一方、インコの体にある純度がより高く暗い緑色は再現しきれないことが分かります。逆に、Adobe RGBはインコの緑色をよく再現できる一方、背景の植物ではやや足りない部分があります。なお、sRGBは「Apple P3とAdobe RGBのどちらにも及ばない」と説明されています。

![](/rss/downloaded_images/d7745b8407b0534d687a75a0045a143a.jpg)

ただし、例として挙げた写真はいずれも差が分かりやすく出る画像を慎重に選んだものであり、「多くの写真において広色域のメリットはないか、あっても小さい」とのことです。

AppleがAdobe RGBではなくP3を選んだ理由について、Astramaelは「推測しかできない」と断った上で、Apple P3はsRGBを特定の方向だけに大きく広げるのではなく、「青色を除く多くの色でバランスよく広げたような色空間」だと説明しています。そのため、Appleは印刷や映像制作などの専門用途だけでなく、多くの人が写真や映像をより鮮やかに楽しめることを重視してP3を選んだのではないか、というのがAstramaelの見方です。
