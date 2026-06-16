---
title: "Sign in with Apple と iCloud+ Hide My Email の新ドメイン"
description: "概要と事実 Appleは今夏後半に、Sign in with AppleとiCloud+ Hide My Emailで使用されているメールアドレスのドメインを統合すると発表しました。新しい共通ドメインはprivate.icloud.c..."
date: 2026-06-16T12:33:10+09:00
categories: ["テクノロジー"]
tags: ["Apple", "iCloud", "プライバシー", "ドメイン変更", "開発者向け"]
image: "/rss/downloaded_images/026cb4d830960aa475b5ca57d426c216.jpg"
---

## AIによる要約

### 概要と事実
Appleは今夏後半に、Sign in with AppleとiCloud+ Hide My Emailで使用されているメールアドレスのドメインを統合すると発表しました。新しい共通ドメインは**private.icloud.com**となり、今後発行されるすべてのアドレスはこのドメイン下で提供されます。たとえば、これまでprivaterelay.appleid.comで発行されていたSign in with Appleのアドレスや、icloud.comで発行されていたiCloud+ Hide My Emailのアドレスは、今後はprivate.icloud.comになります。既存のアドレスは引き続き機能し、メールの転送も中断なく行われます。

開発者やサービス提供者側には、アカウントシステムやメール検証ロジック、許可リストに新しいドメインを追加することが求められます。また、ドメインベースのフィルタリングや抑制リスト、ルーティングルールを明示的に列挙している場合は、そこにprivate.icloud.comも含める必要があります。

### 背景と結論
この変更は、Appleがプライバシー保護サービスの管理をシンプルにし、ユーザーにとって一貫した体験を提供する狙いがあります。複数のドメインを抱えることで生じていた設定ミスや互換性の問題を減らし、開発者側の対応負荷を軽減することが期待されます。一方で、既存のシステムに依存しているサービスでは、アップデート作業が発生するため、早めの対応が重要です。全体として、プライバシー重視のサービスをより統一的に運用するための一歩であり、今後同様のドメイン統合が他の機能にも広がる可能性があります。

[🔗 元記事を読む](https://developer.apple.com/news/?id=sus6t6ab)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

## New domain for Sign in with Apple and iCloud+ Hide My Email

June 15, 2026

Later this summer, Apple will unify the email domains used by Sign in with Apple and iCloud+ Hide My Email under a single, shared domain: **private.icloud.com**.

New addresses generated for both features will be issued on the new domain. For example:

- Sign in with Apple addresses, previously issued on `privaterelay.appleid.com`, will be issued on`private.icloud.com`.

- iCloud+ Hide My Email addresses, previously issued on `icloud.com`, will be issued on`private.icloud.com`.

Existing addresses on the legacy domains will continue to work and forward mail to users without interruption.

### What you need to do

- Developers with apps or websites that use Sign in with Apple should ensure that their account systems, email validation logic, and allowlists accept addresses on the new `private.icloud.com`domain in addition to existing domains:`privaterelay.appleid.com`and`icloud.com`.

- Email service providers should update any domain-based filtering, suppression lists, or routing rules that explicitly enumerate relay domains so that the new `private.icloud.com`domain is included.

</details>
