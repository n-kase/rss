---
title: "Fable 5停止をきっかけにUbuntuでGemma 4 E2Bを動かした記録"
description: "概要と事実 Claude Fable 5という生成AIサービスが突然利用できなくなったことをきっかけに、著者はクラウドサービスに依存しないローカル環境を整えることを考えました。Ubuntu 22.04.5 LTS上にOllamaをイン..."
date: 2026-06-16T12:18:34+09:00
categories: ["テクノロジー"]
tags: ["Ubuntu", "Ollama", "Gemma", "LLM", "ローカルLLM"]
image: "/rss/downloaded_images/20376c6ffd85b8168b74fd312038cd61.png"
---

## AIによる要約

### 概要と事実
Claude Fable 5という生成AIサービスが突然利用できなくなったことをきっかけに、著者はクラウドサービスに依存しないローカル環境を整えることを考えました。Ubuntu 22.04.5 LTS上にOllamaをインストールし、軽量なGemma 4 E2Bモデルを動作させる手順を記録しています。具体的には、curlでOllamaのインストールスクリプトを実行し、バージョンを確認した後、systemdサービスとして起動していることを確認しました。その後、`ollama run gemma4:e2b`コマンドでモデルを取得・実行し、日本語でディスク容量やメモリ使用量の確認方法を質問したところ、適切な回答が返ってきたことを報告しています。また、必要に応じてより大きなサイズのモデルへ切り替える方法や、API経由での呼び出し、不要になったモデルの削除方法も併せて説明しています。

### 背景と結論
クラウドベースの生成AIサービスが予期せず利用停止になるリスクに備え、手元のハードウェアでも最低限の作業が続けられる環境を作ることが目的でした。GTX 1650の4GB VRAMという制約がある中で、軽量かつ実行しやすいGemma 4 E2Bを選んだのは、導入のハードルを下げつつ基本的な質問応答やコマンド確認に十分な性能を見込めたからです。Ollamaを使うことでモデルの取得から実行、API呼び出しまでが比較的簡単に行えることを確認し、ローカルLLMを「避難先」として活用できる可能性を示しました。今後はこの環境をベースに、必要に応じてより大きなモデルや自作ツールへの組み込みを検討することが考えられます。

[🔗 元記事を読む](https://zenn.dev/yamadatt/articles/20260614-ubuntu-gemma4-ollama)

<details>
<summary>AI要約用RAWデータ（抽出された元記事テキスト）</summary>

# Fable 5停止をきっかけにUbuntuでGemma 4 E2Bを動かした記録

[Ubuntu](/topics/ubuntu)



![](/rss/downloaded_images/903f14aec7e11c26adbdb3b6261037e3.png)



[Ollama](/topics/ollama)



![](/rss/downloaded_images/691cdf6bb64a2eaa7b70fff2ac68ad85.png)



[Gemma](/topics/gemma)



![](/rss/downloaded_images/4bbe8f03eeddc1c11c5bc40ef887cfe8.png)



[tech](/tech-or-idea)

##

先日、Claude Fable 5が突然使えなくなりました。

使い始めたばかりのモデルが、こちらの設定ミスではなく外部要因で急に使えなくなる。これはなかなか衝撃でした。

普段の作業ではクラウドの生成AIサービスにかなり頼っています。ただ、今回の件で「いつ生成AIのサービスが使えなくなるかわからない」という前提も持っておいた方がよさそうだと感じました。

そこで、最低限ローカルでもなんとかできる環境を用意しておくため、Ubuntu上でGemma 4を動かしてみることにしました。

今回は、モデル実行環境としてOllamaを使います。Ollamaのモデルライブラリに `gemma4:e2b` が用意されているため、Ubuntu側ではOllamaを入れて `ollama run gemma4:e2b` するだけで動かせます。

この記事は、Fable 5の利用停止をきっかけに、UbuntuへGemma 4 E2Bを導入して簡単に動作確認するまでの作業ログです。

##

今回の目的は、「最高性能のローカルLLM環境を作ること」ではありません。

クラウドの生成AIサービスが突然使えなくなったときに、最低限ローカルでも作業を続けられる状態を作ることです。記事の下書き、コマンド確認、短い相談ぐらいができれば、完全な代替ではなくても退避先としては意味があります。

その前提で、Gemma 4 E2Bを選びました。

理由は次のとおりです。

- Ollamaで `gemma4:e2b`としてすぐ実行できる
- E2BはGemma 4の中でも軽量で、まず試す用途に向いている
- 手元のGPUがGTX 1650の4GB VRAMなので、大きいモデルより小さいモデルから始めたかった
- Gemma 4は比較的新しい世代のモデルで、ローカル実行向けの選択肢として試す価値がある

要するに、今回は「強いモデルを限界まで動かす」よりも、「手元のUbuntuで確実に動くローカルLLMの避難先を作る」ことを優先しました。

##

- OS: Ubuntu 22.04.5 LTS (jammy)
- 実行環境: Ollama
- モデル: Gemma 4 E2B (`gemma4:e2b`)
- GPU: NVIDIA GeForce GTX 1650 (VRAM 4GB)

Ubuntuのバージョンは、以下のコマンドで確認しました。

```
lsb_release -a
```
結果は次のとおりです。

```
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.5 LTS
Release:        22.04
Codename:       jammy
```
GPUは `nvidia-smi` で確認しました。

```
nvidia-smi
```
実行結果です。

```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce GTX 1650        On  |   00000000:01:00.0 Off |                  N/A |
| 48%   49C    P8              5W /   75W |    1515MiB /   4096MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            1003      G   /usr/lib/xorg/Xorg                       24MiB |
|    0   N/A  N/A            1311      G   /usr/bin/gnome-shell                      7MiB |
|    0   N/A  N/A            1762      G   /usr/libexec/gnome-initial-setup          2MiB |
|    0   N/A  N/A          214663      C   ...local/lib/ollama/llama-server       1476MiB |
+-----------------------------------------------------------------------------------------+
```
`llama-server` が約1.5GBのGPUメモリを使っており、Gemma 4 E2BはGTX 1650の4GB VRAMでも動作しました。

Gemma 4には複数のサイズがあります。Ollamaでは、軽めに試すなら `gemma4:e2b`、少し余裕がある環境なら `gemma4:e4b`、より大きいモデルを試すなら `gemma4:12b` / `gemma4:26b` / `gemma4:31b` という選び方ができます。

今回は軽めに試したかったので、`gemma4:e2b` を使いました。

##

Ollama公式のLinux向けインストールコマンドを実行します。

```
curl -fsSL https://ollama.com/install.sh | sh
```
インストール後、バージョンを確認します。

```
ollama --version
```
以下が出力です。

```
ollama version is 0.30.8
```
systemdのサービスとして起動しているかも確認しておきます。

```
systemctl status ollama --no-pager
```
出力は次のとおりです。

```
● ollama.service - Ollama Service
Loaded: loaded (/etc/systemd/system/ollama.service; enabled; vendor preset: enabled)
Active: active (running) since Sat 2026-06-13 21:59:28 JST; 6min ago
Main PID: 209276 (ollama)
Tasks: 10 (limit: 18819)
Memory: 147.7M
CPU: 2.123s
CGroup: /system.slice/ollama.service
└─209276 /usr/local/bin/ollama serve
Hint: Some lines were ellipsized, use -l to show in full.
```
`active (running)` になっていればOKです。

もし起動していなければ、以下で起動します。

```
sudo systemctl enable --now ollama
```
##

OllamaでGemma 4 E2Bを実行します。

```
ollama run gemma4:e2b
```
初回実行時はモデルのダウンロードが走るため、しばらく待ちます。ダウンロードが終わると、そのまま対話できるようになります。

試しに日本語で質問してみました。

```
>>> Ubuntuでディスク容量を確認するコマンドを教えて
```
`df -h` や `du -sh` を使う、という内容の回答が返ってきました。日本語で聞いて日本語で返ってくるので、ちょっとした作業メモやコマンド確認には普通に使えそうです。

##

今回使った `gemma4:e2b` より少し大きいモデルを試すなら、`e4b` も候補です。

```
ollama run gemma4:e4b
```
さらに大きいモデルでは、`12b` や `26b`、`31b` も用意されています。

```
ollama run gemma4:12b
```
Ollama公式ライブラリ（[gemma4](https://ollama.com/library/gemma4)）で確認できる主なサイズは以下のとおりです。

| タグ | サイズ | コンテキスト長 | 備考 |
|---|---|---|---|
| `gemma4:e2b` | 7.2GB | 128K | edge向け（Effective 2B） |
| `gemma4:e4b` | 9.6GB | 128K | edge向け（Effective 4B） |
| `gemma4:12b` | 7.6GB | 256K | |
| `gemma4:26b` | 18GB | 256K | Mixture-of-Experts（active 4B） |
| `gemma4:31b` | 20GB | 256K | Dense |

手元のVRAMに合わせて選ぶとよいです。今回のGTX 1650（4GB）では `e2b` が無難でした。

##

OllamaはローカルでAPIサーバーも起動します。デフォルトでは `localhost:11434` です。

```
curl http://localhost:11434/api/chat \
-d '{
"model": "gemma4:e2b",
"messages": [
{
"role": "user",
"content": "Ubuntuで現在のメモリ使用量を確認するコマンドを教えて"
}
]
}'
```
CLIだけでなく、スクリプトや自作ツールから呼び出せるのは便利です。ローカルで閉じた簡単な補助ツールを作るときに使えそうです。

##

試したあとにディスク容量を空けたい場合は、モデルを削除します。

```
ollama rm gemma4:e2b
```
ローカルLLMはモデルファイルが大きいので、試し終わったモデルを消せることも覚えておくと安心です。

##

Fable 5の突然の利用停止をきっかけに、ローカルLLM環境としてUbuntu上でGemma 4 E2Bを試しました。

UbuntuにGemma 4を導入するだけなら、Ollama経由がかなり簡単でした。

やったことは以下です。

-
`curl -fsSL https://ollama.com/install.sh | sh`でOllamaをインストール
-
`ollama run gemma4:e2b`でGemma 4 E2Bを取得・実行
- 必要に応じて `gemma4:e4b`や`gemma4:12b`など別サイズを指定
-
`localhost:11434`のAPIからも呼び出し可能

まずはCLIで試し、使いどころが見えてきたらAPI経由で既存のツールに組み込む、という流れが良さそうです。

[GitHubで編集を提案](https://github.com/yamadatt/zenn/blob/main/articles/20260614-ubuntu-gemma4-ollama.md)

## Discussion

</details>
