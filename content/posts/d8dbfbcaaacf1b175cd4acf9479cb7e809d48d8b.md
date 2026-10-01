---
title: "FreshRSS 1.26.2"
description: "FreshRSS / FreshRSS Public Uh oh! There was an error while loading. Please reload this page . Notifications You must be signed in to change notification setting…"
date: 2025-05-04T05:27:27+09:00
categories: ["未分類"]
---

## 本文

FreshRSS

/

FreshRSS

Public

Uh oh!

There was an error while loading. Please reload this page .

Notifications

You must be signed in to change notification settings

Fork

1.3k

Star

16.2k

FreshRSS 1.26.2

Compare

Choose a tag to compare

Sorry, something went wrong.

Filter

Loading

Sorry, something went wrong.

Uh oh!

There was an error while loading. Please reload this page .

No results found

View all tags

Alkarex

released this

03 May 20:23

·

950 commits

to edge

since this release

1.26.2

4c5e8e7

This commit was signed with the committer’s verified signature .

Alkarex

Alexandre Alapetite

GPG key ID: A24378C38E812B23

Verified

Learn about vigilant mode .

Milestone

This is a security-focussed release for FreshRSS 1.26.x , addressing several CVEs (thanks @Inverle ) 🛡

A few highlights ✨:

Implement JSON string concatenation with & operator

Support multiple JSON fragments in HTML+XPath+JSON mode (e.g. JSON-LD)

Multiple security fixes with CVEs

Bug fixes

Notes ℹ:

Favicons will be reconstructed automatically when feeds gets refreshed. After that, you may need to refresh your Web browser as well.

This release has been made by @Alkarex , @Frenzie , @hkcomori , @loviuz , @math-GH

and newcomers @dezponia , @glyn , @Inverle , @Machou , @mikropsoft

Full changelog :

Features

Implement JSON string concatenation with & operator #7414

Support multiple JSON fragments in HTML+XPath+JSON mode #7369

Bug fixing

Fix escaping of tag search #7468

Fix CLI parsing of Boolean flags #7430

Fix API for labels with slash #7437

SimplePie

Fix support for feeds with XML preamble + DTD #7515 , simplepie#914

Merged upstream #7434

Upstream fix simplepie#912

Security

Disallow <iframe srcdoc=""> #7494 , CVE-2025-32015

Disallow <button formaction=""> #7506

Improve favicons hash to avoid favicon pollution #7505 , CVE-2025-46339

Add Content-Security-Policy HTTP headers to favicons #7471 , CVE-2025-31136

Web scraping forbid security HTTP headers in cURL #7496 , CVE-2025-46341

Add some HTTP headers Referrer-Policy: same-…

!["FreshRSS 1.26.2"](/rss/rss_digest_images/797e05ab57940601b66627e6b2c02449a79f2c26.jpg)

[🔗 元記事を読む](https://github.com/FreshRSS/FreshRSS/releases/tag/1.26.2)

出典: FreshRSS releases

<details>
<summary>RSSメタ情報</summary>

- カテゴリ: 未分類
- フィード: FreshRSS releases
- 公開日: 2025-05-04T05:27:27+09:00
- 取得: RSS ダイジェスト 09:44 分 スナップショット

</details>
