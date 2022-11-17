## 紹介
Pydo(アクティブ状態にしないかつ、sudo権限を持った状態で扱えるツール)
の作成に取り掛かりました。

###### 現状は
###### 「ホームディレクトリで作成(clone)しないと動かない」
クソクソ状態ですが、勉強しながら使いやすくしようと思っております。
よかったら使ってみてください。

## 最初に
ある日、Raspberry Pi上でPythonを使いNeoPixelを制御していました。
普段通り、Pythonのvenv(virtualenv)を使って仮想環境を用意、アクティブにしてコードを書いて実行しようしたんですよ。

そしたら...
sudoがない、rootじゃないと、権限のないユーザーは実行できないんだよと怒られました。

raspi-configでSPI interfaceをenableにするのもありなんだが、 
##### めんどい

ていうか、shell上でvenvのactiveをつけたり外したりするのも
##### めんどい

アクティブ状態にしないかつ、sudo権限を持った状態でvenvを使えたらいいじゃん!
というのがきっかけで投稿しました。
よーし、やるぞぉぉうぅ...💤

## venv
##### venvとは？
以下の記事をどうぞ
[venv: Python 仮想環境管理](https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)


## 環境
・Raspberry Pi 3b +
・Raspberry Pi OS (Debianベースなら、動くと思う)
・apt(deb形式パッケージ管理ツール)
・Bashシェルスクリプト
・Python 3.8.9 (Python 3.7~)
・venv 
・pip 

## インストール

Raspiの場合、初期状態で入ってると思うが Python3をインストール
```
sudo apt-get update
sudo apt-get install python3
```
venvとpipをインストール
```command
sudo apt install python3-pip python3-venv
```

## 仮想環境を作る
適当な場所に仮想環境を作ります。
今回は、ユーザー名をpiと仮定して

/home/pi(ユーザー名)/test/myenv

ホームディレクトリにテストフォルダを作成し、myenvという仮想環境を作成します。

```commond
mkdir ~/test     #Homeディレクトリにtestフォルダを作成

python3 -m venv ~/test/myenv  #testフォルダの中にmyenvを作成
```

## 仮想環境のPythonを使いたいんだ
まず、ざっくりとvenvの仕組みを知ることが大事。
##### venvの仕組みを知る
venvで作成された仮想環境のPythonは、
/usr/bin/pythonにシンボリックリンクを越して繋がっている。
根っこは一緒だが、実行時にPythonインタプリンタ、ライブラリの参照場所を変えることで環境下を変えているのだ。
そんな実行環境を作ってるのが、venv。
ならvenvのPythonを、直で実行するだけでvenvの仮想環境でPythonを扱えるのだ。

------

#### venvのpythonを実行させるシェルスクリプトを作成する
```command
touch ~/test/main.sh  #main.shを作成
chmod 755 ~/test/main.sh  #main.shに権限を付与
```
そして、main.shに以下を書き込む
```bash:main.sh 
#!/bin/bash

sudo ~/test/myenv/bin/python $@  #このコマンドだと直打ちで実行もできる。
```


#### 環境変数の追加
main.shをコマンドとして実行できるように環境変数用意する
```bash
export PATH=$HOME/test/myenv/bin:$PATH 
export PATH=$HOME/test/:$PATH
sudo ln -si ~/test/main.sh /usr/local/bin #シンボリックリンク

#terminalを再度開き
#Hello Worldを試したり
main.sh helloworld.py
#これでpipバージョンが見れたらOK
main.sh -m pip --version

```

#### 最後に
めんどいめんどいと言ってましたが、ただ単にあったらいいかもって感じで取り組みました。

condaやvenvなどの仮想環境を使いこなすと、とても管理しやすいです。

最初の紹介にもあったのですが、この記事で書いた内容を改良していつでもactiveせず、sudo状態でvenvを使えるようなツールの作成を始めました。

最後まで見ていただいてありがとうございます。


## 参考
・[venv: Python 仮想環境管理](https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)

・[えんでぃの技術ブログ](https://endy-tech.hatenablog.jp/entry/how_venv_works_in_python)
