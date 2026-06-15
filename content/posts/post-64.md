---
title: "なぜAppleは広色域の色空間としてAdobe RGBではなくDCI-P3を採用したのか？"
description: "Appleは2015年に発売されたiMacで、従来のsRGBよりも広い色域を持つディスプレイを採用した。広色域の代表格として知られるAdobe RGBではなく、映画業界で使われるDCI‑P3系の色空間（記事では「Apple P3」と呼..."
date: 2026-06-15T14:45:38+09:00
categories: ["テクノロジー"]
tags: ["AI", "Summary"]
image: "/rss/downloaded_images/5516b7c5a905c4b49ef58dc7d5e13e5d.jpg"
---

## 何が起きているのか
Appleは2015年に発売されたiMacで、従来のsRGBよりも広い色域を持つディスプレイを採用した。広色域の代表格として知られるAdobe RGBではなく、映画業界で使われるDCI‑P3系の色空間（記事では「Apple P3」と呼ばれる）を選んだ理由を、色管理サイトAstramaelが実際の写真や色域図を使って分析した。

## それによって何が引き起こされそうなのか
この選択により、一般ユーザーが日常的に見る写真や動画がより鮮やかに、特に赤・黄・オレンジ系の色が強調される表示になる。プロ向けの印刷作業ではAdobe RGBがまだ有利だが、Appleの方針は「多くの人が楽しめる vivid な色」を重視したため、今後は消費者向けメディアやコンテンツ制作でもP3を基準とする動きが広がり、色管理の標準が少しずつシフトする可能性がある。また、他メーカーも同様のバランス型広色域を採用しやすくなるため、ディスプレイ市場全体の色表現の基準が変わっていく兆しが見える。

## だからどうなのか
Appleはプロフェッショナルな印刷や映像制作のニーズだけでなく、一般ユーザーが日常の写真や動画をもっと楽しめるように、色のバランスを取ったDCI‑P3を採用した。つまり、「広色域は特殊な用途のためだけではなく、みんながもっと鮮やかに見えることを重視すべき」という教訓が得られる。

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

**・関連記事**

[Appleが策定したスマホやPCの画面をもっと豊かな色合いで表現できる色空間「Display P3」とは？ - GIGAZINE](https://gigazine.net/news/20200303-display-p3)


[4K対応の新型21.5インチiMacの性能を旧iMacや最新MacBook Proなどと徹底比較 - GIGAZINE](https://gigazine.net/news/20151014-4k-21-imac-review)


[ブラウザによって色が異なる「色空間」の不思議な世界 - GIGAZINE](https://gigazine.net/news/20210528-browser-different-colors)


[PNGファイルの仕様が20年以上ぶりにバージョンアップ、HDR・アニメーションPNG・Exifをサポート - GIGAZINE](https://gigazine.net/news/20250626-png-update)

**・関連コンテンツ**

in  [メモ](https://gigazine.net/news/C7/),  Posted by log1b_ok

You can read the machine translated English article ** Why did Apple choose DCI-P3 instead of A…**.
