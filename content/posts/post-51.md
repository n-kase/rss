---
title: "コーディングAIエージェント向けのオープンソースHeroku「InsForge」"
date: 2026-06-15T13:55:30+09:00
categories: ["GIGAZINE"]
tags: ["AI", "Summary"]
image: "/rss/downloaded_images/a7ce8d21dd8faf4ae7849da6b508ffe7.png"
---

## 注目の画像

![画像](/rss/downloaded_images/a7ce8d21dd8faf4ae7849da6b508ffe7.png)

![画像](/rss/downloaded_images/e0021274fe83ef55359bf92bd040b9ed.png)

![画像](/rss/downloaded_images/518e212479a03490803d141ee8178ee4.png)

## 概要（何が起きているのか）
- InsForgeというオープンソースのバックエンドプラットフォームが公開され、AIコーディングエージェントが直接データベースや認証などを操作できるようになった。  
- 主な機能は認証、PostgreSQL DB、S3互換ストレージ、Edge Functions（Deno）、コンピュート、サイトデプロイ、リアルタイム、ベクトル検索、アナリティクス、決済、メッセージング、Cronジョブなど。  
- AIエージェント向けにModel Gateway（LLMプロバイダー統合）とMCP Server、CLI/Skillsが提供され、ターミナルからバックエンド操作が可能。  

## 示唆（それによって何が引き起こされそうなのか）
- AIエージェントがバックエンド構築を自動化できるため、開発スピードが上がり、プロトタイプやMVPの作成が容易になる。  
- クラウド版には自動スキャンと改善提案機能があり、セキュリティやパフォーマンスの維持がエージェントに任せやすくなる。  
- ネット上では「Herokuライク」かつオープンソースという点で、ベンダーロックインを避けたい開発者から注目が集まっている。  
- セルフホスト手順がDockerとGit Bashで示されており、ローカル環境でも簡単に試せるため、教育や個人プロジェクトでの採用が促進される可能性がある。  

## まとめ（だからどうなのか）
- AIエージェントを使ってフルスタックアプリを開発する場合は、InsForgeをバックエンドとして導入すると、管理画面操作をコードで自動化できるので試してみるべき。  
- セキュリティやパフォーマンスを常に監視したい場合は、クラウド版の自動スキャン機能を活用し、エージェントに改善プロンプトを渡す仕組みを組み込むと良い。

---

## 元スレッド・記事本文

# コーディングAIエージェント向けのオープンソースHeroku「InsForge」

![](/rss/downloaded_images/a7ce8d21dd8faf4ae7849da6b508ffe7.png)


AIを利用してWebアプリを作成する場合、** Firebase**や

**などのバックエンドサービスを利用することが多いですが、これまで管理画面でユーザーの操作が必須だったほとんどの作業をコーディングAIエージェントが直接行える様に拡張したオープンソースのバックエンドサービス「**

[Supabase](https://supabase.com/)**InsForge**」が公開されています。

**InsForge - The agent-native cloud infrastructure platform**


[https://insforge.dev/](https://insforge.dev/)![](/rss/downloaded_images/e0021274fe83ef55359bf92bd040b9ed.png)


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

**・関連記事**

[FirebaseのようにGUIでバックエンドを構築できる無料でオープンソースのシステム「PocketBase」、わずか1ファイルのみ - GIGAZINE](https://gigazine.net/news/20251206-pocketbase)


[独自のデータベースやWordPressなどのアプリを簡単にセルフホストできて管理できるオープンソースPaaS「Coolify」 - GIGAZINE](https://gigazine.net/news/20251213-coolify)


[オープンソースでセルフホスト可能なBaaSプラットフォーム「Appwrite」を使ってみた - GIGAZINE](https://gigazine.net/news/20220328-appwrite)


[Office 365・Bitwarden・GitHub・Google・Cloudflare・DockerHubなどアメリカのクラウドサービスから実際に脱却してみた記録 - GIGAZINE](https://gigazine.net/news/20250321-moving-away-from-us-cloud-services)

**・関連コンテンツ**

 in  [AI](https://gigazine.net/news/C48/),   [ソフトウェア](https://gigazine.net/news/C4/),   [レビュー](https://gigazine.net/news/C12/),  Posted by darkhorse_logmk

You can read the machine translated English article ** InsForge: An open-source Heroku-like pla…**.
