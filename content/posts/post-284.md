---
title: "AIエージェントはCloudflareに賭けろ"
description: "概要と事実 この記事は、AIエージェントを開発する際にCloudflareが適している理由を説明しています。著者はCloudflareの社員であり、まずAIエージェントが必要とする三つの要素――推論モデル、サンドボックス、実行環境――..."
date: 2026-06-16T09:53:58+09:00
categories: ["テクノロジー"]
tags: ["AI", "Cloudflare", "Workers", "サンドボックス", "エージェント"]
image: "/rss/downloaded_images/bf5a668fa997b6a1e1d88636a8560df0.png"
---

## AIによる要約

### 概要と事実
この記事は、AIエージェントを開発する際にCloudflareが適している理由を説明しています。著者はCloudflareの社員であり、まずAIエージェントが必要とする三つの要素――推論モデル、サンドボックス、実行環境――を挙げ、それぞれがCloudflareの提供するサービスでどう実現できるかを示しています。具体的には、Workers AIによるモデルへの簡単なアクセス、SandboxesやBrowser Run、Dynamic Workersといったサンドボックス機能、そしてWorkersやDurable Objects、Workflowsといった実行環境について、コード例を交えて紹介しています。また、従来のコンテナベースのクラウドではAIエージェントの「1対1」の処理に向いていない点を指摘し、Cloudflare Workersの高速起動とメモリ効率の良さを強調しています。

### ネットの反応と意見の変遷
記事自体は技術ブログとして公開され、読者からはCloudflareの新機能への期待や興味を示すコメントが多く見られました。特に、Workers AIの使いやすさや、サンドボックスとしてのDynamic Workersの独自性について称賛の声が上がり、実際に試してみたいという意見が散見されました。一方で、自社の立場からの偏りを指摘する声も一部あり、客観的な評価を求めるコメントもありました。全体としては、技術者コミュニティにおいて話題となり、今後のAIエージェント開発プラットフォームとしてCloudflareへの関心が高まった様子がうかがえます。

### 背景と結論
AIエージェントの普及に伴い、従来のクラウドインフラでは個々のエージェントに専用の実行環境を提供するのが難しくなってきました。Cloudflareは、エッジネットワーク上で高速に起動し、隔離されたサンドボックスを柔軟に提供できる点で、こうしたニーズに合致していると考えられます。本記事は、推論モデルへの簡単なアクセス、多様なサンドボックス選択肢、そして統合された実行環境という三本柱を挙げ、開発者がAIエージェントを効率的に構築できる基盤としてCloudflareを推奨しています。これにより、AIエージェントの開発ハードルが下がり、より多くの革新的なサービスが生まれる可能性が高まると結論づけられます。

<details>
<summary>元スレッド・記事本文</summary>

# AIエージェントはCloudflareに賭けろ

[AI](/topics/ai)



![](/rss/downloaded_images/6f82b8955baa1b36f4b730afc1419538.png)



[Cloudflare](/topics/cloudflare)



![](/rss/downloaded_images/6f6a44854eb9a7537fd52a0dba0a95c9.jpeg)



[Agent](/topics/agent)



![](/rss/downloaded_images/228d6d93dcf2cc6123d11780fe4e4aaa.png)



[tech](/tech-or-idea)

最初に表明しておくと、自分はCloudflareの社員である。

AIエージェント時代にCloudflareは最適なプラットフォームである！今回はCloudflareがなぜAIエージェントに向いているかを紹介する。

#

AIエージェントを構築するためのアーキテクチャについて考えてみる。

##

Cloudflareは今年の4月に出したブログ記事で強く言っていてる。

[https://blog.cloudflare.com/ja-jp/welcome-to-agents-week/](https://blog.cloudflare.com/ja-jp/welcome-to-agents-week/)

インターネットは元々、AI時代を想定してつくられていません。クラウドも同様です。


スマートフォンの登場で端末が大量に増えた。一つのアプリケーションをたくさんのクライアントに配信しなくてはいけない。そこでコンテナの技術を使ってアプリケーションをスケールさせた。1対多だ。これがいわゆる「クラウド」である。

AI時代では1対1になる。それぞれのエージェントが一人のユーザーを担当する。LLMが処理の流れを決め、整理し、ツールを実行して動き続けるための独立した環境が必要となる。

コンテナをベースとした旧来のクラウドはAIには向いていない。一方でCloudflareにはCloudflare Workersがある。

##

Cloudflare WorkersはV8 Isolateで動いている。V8はGoogle Chromeで使われてるJavaScriptエンジンである。イメージしてほしい。WebブラウザがWebページを開くとV8がページ内のJavaScriptを実行する。元々ブラウザで使われいてた技術をサーバーサイドに持ってきたのが、Workersの発明だ。

コンテナと比べて、パフォーマンスがよい。とびきり速く立ち上がって、メモリ効率がよくて、無限にスケールする。そして、環境は隔離されている。



![V8](/rss/downloaded_images/5194e55a371acd3239f06598095d5150.png)




このWorkersがAIエージェント構築にぴったりだ。ユーザーのタスクごとに全く別のアプリケーションを大量に素早く立ち上げることができる。



![クラウドとV8](/rss/downloaded_images/a7ea302a23cff133e8690d1019c9bf63.png)




#

自分はAIエージェントを作るためには3つの要素が必要だと思っている。

- 推論モデル - エージェントが考える
- サンドボックス - エージェントが（コードetc.を）実行する
- 実行環境 - エージェントを置く環境



![3つの要素](/rss/downloaded_images/47ae4372c920150994b0068d43ad5810.png)




CloudflareだとWorkersとはじめとした技術が揃っている。

- 推論モデル - Workers AI / AIモデル
- サンドボックス - Sandboxes / Dynamic Workers / Browser Run
- 実行環境 - Workers / Durable Objects / Workflows

一つずつ解説ししょう。

##

推論モデルはAIエージェントが考えるために必要である。CloudflareはWorkers AIを提供している。これは推論モデルがCloudflareネットワーク上で動くという代物。オープンなモデルを使うことができて、LLMから画像生成、スピーチtoテキストまで80個ほどある。

また、最近では、外部のAIプロバイダーのモデルもAI Gatewayをプロキシして共通のインターフェースで使うことができるようになった。つまり、Cloudflareで使えるモデルは180個以上になる。



![SS](/rss/downloaded_images/23f51088771038505e1d31eb28c72483.png)




モデルにアクセスするだけなら、OpenAIやAnthropicのAPIを叩けばいいんじゃないの？それはそうだが、Workers AIの使い心地は非常に強力だ。

BindingというAIモデルに方法でアクセスできる。JavaScriptのメソッド呼び出しをするだけでLLMの推論結果を得ることができる。外部APIを叩くとなると、SDKをインポートして、IDとパスワード相当を入力して⋯云々としなくてはいけないのが、これだけだ。

```
const result = env.AI.run('@cf/meta/llama-3.3-70b-instruct-fp8-fast', {
messages: [
{
role: 'user',
content: 'What is the origin of the phrase Hello World'
}
]
})
```
この書き心地の良さは人間だけのものではない。キーを直接書く必要がないので、AIに書かせる時も安心である。

他にもCloudflareには、Workers AIや外部モデルへのゲートウェイになってログをとったり、キャッシュができたり、制限ができたるするAI Gatewayがあったり、ベクターデーターベースのVectorizeや、ドキュメントと入れると自動でRAGを作ってくれるAI Searchなどがある。

##

AIエージェントはコードやコマンドを実行する。その際にサンドボックスが必要だ！それがないと人間のパソコンの重要なデータを消してしまうかもしれないし、サーバーをクラッシュさせてしまうかもしれない。

Cloudflareでは3つのサンドボックスを提案している。

- Sandboxes
- Browser Run
- Dynamic Workers

紹介しよう。

###

CloudflareではWorkersだけではなくコンテナが動くContainersというプロダクトがある。Dockerイメージが動く。SandboxesはContainersを利用した隠蔽されたサンドボックス環境である。

これはPythonを実行するコード例。Workersから呼び出し、結果をレスポンスで返している。

```
import { getSandbox } from '@cloudflare/sandbox'
export { Sandbox } from '@cloudflare/sandbox'
export default {
async fetch(request: Request, env: Env): Promise<Response> {
const sandbox = getSandbox(env.Sandbox, 'user-123')
const result = await sandbox.exec('python --version')
return Response.json({
output: result.stdout,
exitCode: result.exitCode,
success: result.success
})
}
```
Gitのレポジトリを取ってきて、テストを実行するなんてことも簡単に書ける。

```
import { getSandbox } from '@cloudflare/sandbox'
export { Sandbox } from '@cloudflare/sandbox'
export default {
async fetch(request: Request, env: Env) {
const sandbox = getSandbox(env.Sandbox, 'agent-session-47')
await sandbox.gitCheckout('https://github.com/org/repo', {
targetDir: '/workspace',
depth: 1
})
return sandbox.exec('npm', ['test'], { stream: true })
}
```
面白いのはプレビュー機能で、サンドボックス内で立ち上げたHTTPサーバーのポートを外部から参照可能なURLにアタッチして他の人間やAIがアクセスできるようにできる。

```
import { getSandbox } from '@cloudflare/sandbox'
export { Sandbox } from '@cloudflare/sandbox'
export default {
async fetch(request: Request, env: Env) {
const { hostname } = new URL(request.url)
const sandbox = getSandbox(env.Sandbox, 'agent-session-47')
await sandbox.startProcess('python -m http.server 8000')
const exposed = await sandbox.exposePort(8000, { hostname })
console.log(exposed.url)
// ...
}
```
Sandboxesはコンテナなので、AIがやりたいことが全部できる。

###

Browser Renderingと呼ばれていたものがAIエージェント向けにパワーアップしてBroser Runになった。これはCloudflareのネットワーク上でヘッドレスブラウザが動くというもの。Browser SessionsとQuick Actionsという2つの使い方がある。

####

Browser SessionsではPuppeteerもしくはPlaywrightをWorkers（もしくはCDP=Chrome DevTools Protocol）から操作する。例えば、APIの用意されていないWebサイトを操作することができる。AIエージェントが空港券の予約をしたり、競合サイトの情報収集をするかもしれない。

####

Quick Actionsは簡単なインターフェースでステートレスなブラウザタスクを実行することができる。スクリーンショット、PDF生成、スクレイピング等々。

エンドポイントを叩くだけでコードが必要ない。

```
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/screenshot' \
-H 'Authorization: Bearer <apiToken>' \
-H 'Content-Type: application/json' \
-d '{
"url": "https://example.com"
}' \
--output "screenshot.png"
```
また、WorkersからBindingでアクセスもできる。

```
const response = await env.BROWSER.quickAction('screenshot', {
url: 'https://example.com'
})
```
AIエージェントとは違う文脈だが、Browser RunとHonoのJSXを使うとWokrersで簡単にスタイル付き画像を作れる。

[https://x.com/yusukebe/status/2065941599251747034?s=20](https://x.com/yusukebe/status/2065941599251747034?s=20)

####

AIエージェントがBrowser Runを使えばいい。悪意のある、もしくは危険なサイトから隔離させられるし、クッキーやキャッシュ、セッション情報が残らなず使い捨てができる。

###

サンドボックスの最後に紹介するのがDynamic Workersだ。

簡単に言うとWorkersからWorkersを立ち上げることができて、立ち上げられたWorkersをDynamic Workersと呼ぶ、という感じ。これができるようになった。

Workersと同じV8 Isolateなので、立ち上がりが速く、メモリが効率がよい。Cloudflareではブログで「コンテナより100倍速い」と言ってるが決して煽りだけではないと思う。

[https://blog.cloudflare.com/dynamic-workers/](https://blog.cloudflare.com/dynamic-workers/)

使い方が面白い。文字列でWorkersのコードをWorkers内に書く。

```
export default {
async fetch(request: Request, env: Env): Promise<Response> {
const worker = env.LOADER.load({
compatibilityDate: '2026-05-23',
mainModule: 'src/index.js',
modules: {
'src/index.js': `
export default {
fetch(request) {
return new Response("Hello from a dynamic Worker");
},
};
`,
},
globalOutbound: null
})
const entrypoint = worker.getEntrypoint()
return entrypoint.fetch(request)
}
```
だいぶ気持ち悪いコードだが、変数を渡すことができるのでユーザーが送ってきたコードをそのまま実行すると、POSTのボディにコードを書いて実行結果をそのまま出すというマジックみたいなことができる。

[https://x.com/yusukebe/status/2061635761389396156?s=20](https://x.com/yusukebe/status/2061635761389396156?s=20)

Dynamic Workersのより具体的な話は以下にまとめている。

[https://speakerdeck.com/yusukebe/dynamic-workersnituite](https://speakerdeck.com/yusukebe/dynamic-workersnituite)

で、このDynamic Workersをサンドボックスに使うのである。WorkersはJavaScriptの実行環境なので、JavaScriptでできる範囲の計算リソースとして使えるし、D1やR2といったプロダクトと連携させることができる。

###

Dynamic Workersの面白い使い方をやった。先日6月6日の[フロントエンド・PHPカンファレンス北海道2026](https://frontend-php-con.hokkaido.jp/)で「AI時代のUIはどこに行く？その2！」という発表内で紹介した。

[https://speakerdeck.com/yusukebe/aishi-dai-nouihadokohexing-ku-sono2](https://speakerdeck.com/yusukebe/aishi-dai-nouihadokohexing-ku-sono2)

Generative UIには一般的には3つのアプローチがあるのだが、その新しい4番目として「Dynamic」を提案して、それで使っている。

肝はAIがReactのJSXを書いて、Dynamic Workers上で実行、SSRして、その結果をiframeで読み込むというものだ。ユーザーのチャット画面に表示することを想定しているのだが、ReactのSSRなので、Suspenseなんかが使えて面白い。



![Dynamic](/rss/downloaded_images/dcdf510f53faf1e641e42b64690356a6.png)




デモでは本当にLLMがReactのコンポーネントを書いてレンダリングした結果を我々は見ることが出来た。



![Demo](/rss/downloaded_images/580766774b86c569590c940ee5bcff47.png)




AIがコードを書いて、Dynamic Workers上で実行する良い例である。

###

以上、3つのサンドボックスを紹介した。コンテナだけじゃないのがミソだ。そしてこの3つのAIに段階的に使わせることができる。



![実行ラダー](/rss/downloaded_images/3a58358f8875cd4d0ab8440b97a57f93.png)




つまり、JavaScriptの実行など簡単なことは立ち上がりの速いDynamic Workersにやらせる。ブラウザの操作ならBrowser Run。コンテナを立ち上げるまでもない。特殊なコマンドの実行やコンパイルが必要になった場

...（長文のため省略されました）

</details>
