# selenium サンプルアプリケーション

aizulabのページからお知らせ一覧を表示する。

```
.
├── README.md
├── doc
│   └── selenium.md
├── docker-compose.yml
├── poetry.lock
├── pyproject.toml
├── selenium_example
│   └── main.py
└── tests
```

## 参考リンク

selenium公式ドキュメント及び、pythonライブラリドキュメント

- [Selenium](https://www.selenium.dev/ja/)
- [Selenium with Python — Selenium Python Bindings 2 documentation](https://selenium-python.readthedocs.io/)

## 動かし方

このプロジェクトを試す方法について。
下記はMacによる説明になる。

### 必要アプリケーション

- Docker
- vscode
- DevContainer(vscode拡張機能)

#### seleniumドライバーを起動する

**x86_64の場合**

`./selenium-exa`ディレクトリにて`docker compose up -d`を実行する。

http://localhost:4444 に接続し、起動したかを確認する。

**ARMの場合**

`./docker-compose.yml`の書き換えが必要になる。
下記のように書き換える。

```yaml
    # x86_64
    # image: selenium/standalone-chrome:latest
    # arm
    image: seleniarm/standalone-chromium:latest
```

`./selenium-exa`ディレクトリにて`docker compose up -d`を実行する。

http://localhost:4444 に接続し、起動したかを確認する。

#### DevContainerの起動

vacodeにてコマンドパレットを表示し、　`cmd(ctrl) + shift + p`　下記のコマンドを実行する。

`Dev Containers: Reopen in Container`

開発コンテナの実行が完了したら、`python ./selenium_example/main.py`からpythonスクリプトを実行する。


#### 画面にてデバックを行う

画面を見ながらデバックする方法について。


`Finder`のメニューバーから**移動 > サーバーへ接続**を選択する

`vnc://localhost:5900`を入力し接続を選択する。

パスワードには`secret`を入力する。

しばらくすると画面共有アプリが起動し、画面が表示される。

下記のスクリプトがコメントアウトされていることを確認すること。

```python
# options.add_argument("--headless")
```

pythonデバック機能を使用して、１行ごとに実行していく。
