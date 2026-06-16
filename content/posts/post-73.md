---
title: "コーディングAIエージェント向けのオープンソースHeroku「InsForge」"
description: "InsForgeというオープンソースのバックエンドサービスが公開され、AIを活用したコーディングエージェントがデータベースや認証、ストレージ、エッジファンクションなどの機能を直接呼び出せるように設計されました。これにより、これまで管理..."
date: 2026-06-16T08:27:45+09:00
categories: ["テクノロジー"]
tags: ["InsForge", "AIエージェント", "オープンソース", "バックエンド", "MCP"]
image: "/rss/downloaded_images/87f25148d7c9aed73503517595359f81.png"
---

## AIによる要約

InsForgeというオープンソースのバックエンドサービスが公開され、AIを活用したコーディングエージェントがデータベースや認証、ストレージ、エッジファンクションなどの機能を直接呼び出せるように設計されました。これにより、これまで管理画面で手動で行っていた設定や操作をエージェント経由で自動化できる仕組みが提供されています。公開当初のネット上の反応では、従来のFirebaseやSupabaseと比較してエージェントネイティブな設計が新鮮だと好意的に受け止める声が多く、特にMCPサーバーやCLI・Skillsといった連携手段が実装されている点に注目が集まりました。一方で、セルフホスト版の構築手順がDockerやGit Bashを使ったやや技術的なハードルがあることや、セキュリティやパフォーマンスの監視機能がクラウド版にのみ実装されていることについて、実際の運用での負担や信頼性に疑問を呈する意見も見られました。時間が経つにつれて、開発者コミュニティではエージェントがバックエンド操作を担うことでプロトタイプ制作のスピードが向上する期待と、同時にエージェントの誤操作や権限管理の必要性について議論が深まっています。この動きは、AIエージェントを日常的な開発フローに組み込む動向を加速させ、インフラストラクチャ側もエージェントフレンドリーな設計が求められるという示唆を与えています。したがって、開発者はエージェントと連携できるバックエンドプラットフォームを検討し、セキュリティ設定や運用監視を十分に確認した上でInsForgeのようなツールを試すことが有益であるという教訓が得られます。

[🔗 元記事を読む](https://gigazine.net/news/20260614-insforge/)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

# コーディングAIエージェント向けのオープンソースHeroku「InsForge」



![](/rss/downloaded_images/a7ce8d21dd8faf4ae7849da6b508ffe7.png)




AIを利用してWebアプリを作成する場合、** Firebase**や

**などのバックエンドサービスを利用することが多いですが、これまで管理画面でユーザーの操作が必須だったほとんどの作業をコーディングAIエージェントが直接行える様に拡張したオープンソースのバックエンドサービス「**

[Supabase](https://supabase.com/)**InsForge**」が公開されています。

**InsForge - The agent-native cloud infrastructure platform**


[https://insforge.dev/](https://insforge.dev/)

![](/rss/downloaded_images/e0021274fe83ef55359bf92bd040b9ed.png)




**InsForge/InsForge: The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, storage, compute, hosting, and AI gateway to ship full-stack apps end-to-end.**

[https://github.com/InsForge/InsForge](https://github.com/InsForge/InsForge)


**◆InsForgeの基本機能一覧**


| 機能名 | 説明 |
|---|---|
| Authentication | ユーザー管理・認証・セッション |
| Database | [PostgreSQL](https://www.postgresql.org/) |
| Storage | 互換ファイルストレージ[Amazon S3](https://aws.amazon.com/jp/s3/) |
| Edge Functions | ベースのエッジで動作するサーバーレスコード[Deno](https://deno.com/) |
| Compute | 長時間稼働コンテナサービス |
| Site Deployment | サイトのビルドとデプロイ |
| Realtime | データ変更のリアルタイムサブスクリプション |
| Vector | によるベクトル検索・埋め込み[pgvector](https://github.com/pgvector/pgvector) |
| Analytics | イベント追跡・使用状況分析 |
| Payment | 統合による決済・サブスクリプション管理[Stripe](https://stripe.com/jp) |
| Messaging | メール・通知・トランザクションメッセージ送信 |
| Cron Jobs | スケジュールされた定期ジョブ |


**◆InsForgeが独自に実装している機能**

**・Model Gateway**

複数のLLMプロバイダーを** OpenAI**互換APIとしてまとめて扱えるため、アプリからAIモデルへの接続をシンプルにできます。

**・MCP Server**

AIエージェントの拡張機能である

**に対応したサーバーが用意されており、InsForgeのバックエンド機能を外部ツールとして呼び出せるため、データベース・認証・ストレージなどの状態を確認しながら開発を進められます。**

[MCP](https://modelcontextprotocol.io/docs/getting-started/intro)**・CLIとSkills**

AIエージェントがターミナルから直接呼び出せるCLIとその操作を補助するSkillsが用意されており、クラウド版ではSkillsによってバックエンド操作の手順を把握しながら作業できます。READMEではCLIとSkillsはクラウド版のみと説明されており、セルフホスト版でAIエージェントにInsForgeを操作させる場合はMCP Serverの利用が基本とのこと。

**◆InsForgeのセルフホスト構築方法**

今回はWindowsに

**と**

[Docker Desktop](https://www.docker.com/ja-jp/products/docker-desktop/)**のGit Bashを用意した環境で構築します。作業フォルダを用意し、**

[Git for Windows](https://gitforwindows.org/)**と**

[docker-compose.yml](https://raw.githubusercontent.com/insforge/insforge/main/deploy/docker-compose/docker-compose.yml)**をダウンロードして保存。**

[.env.example](https://raw.githubusercontent.com/insforge/insforge/main/deploy/docker-compose/.env.example)mkdir -p insforge cd insforge curl -L -o docker-compose.yml "https://raw.githubusercontent.com/insforge/insforge/main/deploy/docker-compose/docker-compose.yml" curl -L -o .env.example "https://raw.githubusercontent.com/insforge/insforge/main/deploy/docker-compose/.env.example"



.env.exampleを.envとしてコピー。


cp .env.example .env


.envを環境に合わせて書き換えます。


# .env API_BASE_URL=http://localhost:7130 VITE_API_BASE_URL=http://localhost:7130 # Authentication # openssl rand -hex 16などでランダムな値を生成 JWT_SECRET=【ランダムな値32文字以上推奨】 ROOT_ADMIN_USERNAME=【任意のメールアドレス】 ROOT_ADMIN_PASSWORD=【任意のパスワード】


コンテナを立ち上げます。


docker compose up -d


コンテナが起動したらブラウザで.envに設定したURLにアクセスするとログインフォームが表示されるので「Email」に.envで設定したメールアドレス、「Password」に.envで設定したパスワードを入力して「Sign in」をクリック。




![](/rss/downloaded_images/518e212479a03490803d141ee8178ee4.png)




ログインすると連携するAIエージェントの設定画面が表示されるので「AIエージェント選択」フォームから連携するAIエージェントを選択。




![](/rss/downloaded_images/3b0de2f052c45674439f08dcb8aee529.png)




設定の手順が表示されるので、Step1の「Terminal Command」をコピー。




![](/rss/downloaded_images/24cd740783d84b8bc16b70137ac7b85a.png)




Git Bashでコピーしたコマンドを実行するとMCPサーバーが立ち上がります。




![](/rss/downloaded_images/311f1a2b850beef14f4a4de48046e98e.png)




次にStep2の「prompt」をコピーしAIエージェントのチャット欄にペーストして実行するとInsForge用のMCPが設定されます。




![](/rss/downloaded_images/35f0c497cc8282ff8e9479db7cfc6a08.png)




** Claude Code**の場合は、MCPサーバー起動後Claude Codeを立ち上げた時点でInsForge用のMCPを導入するかどうか聞かれるのでユーザーレベルでの利用かプロジェクトのみの利用か選択します。



![](/rss/downloaded_images/7c894089ade00e91c52c307a1d53fe07.png)




MCPの設定が完了したら「閉じる」をクリック。




![](/rss/downloaded_images/578061e72885bc28836836c76a50d661.png)




管理画面が表示されれば構築完了です。




![](/rss/downloaded_images/6cc6ca80ccb94cd9a3ff6d6f261fb3c3.png)




AIエージェントとInsForgeの接続確認として「I'm using InsForge as my backend platform, call InsForge MCP's fetch-docs tool to learn about InsForge instructions.」と指示するとMCPサーバーを通してInsForgeから以下のような返答がありました。




![](/rss/downloaded_images/fefdfb632472ae827219edf4447f0ff9.png)




日本語の指示による実装テストとして「title、content、authorカラムを持つpostsテーブルを作成してください」と入力すると指示通りのテーブルが作成されました。




![](/rss/downloaded_images/346bff40823237b4ac68104c52129197.png)




管理画面からテーブルが作成されていることが確認できます。




![](/rss/downloaded_images/648bb6ecaa344621ce464e27affb6d86.png)




「ユーザープロフィール用の画像アップロード機能を追加してください」と指示するとバックエンドで必要なストレージやテーブルを作成し、フロントエンドでの実装用スクリプトが表示されました。




![](/rss/downloaded_images/4e0f08571a01d3a140b8c6cd23ecbb86.png)




これまで管理画面で行っていた操作をコーディングAIエージェントからMCP経由で実装できます。


なお、クラウド版にはバックエンドを毎日スキャンしてセキュリティ・パフォーマンス・動作状態の問題を検出し、問題があれば修正内容をAIコーディングエージェントに渡すためのプロンプトを表示する** 機能**があります。

</details>
