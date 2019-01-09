
# NFCを用いて学籍番号を抽出する

### 概要
就職活動説明会での出席確認用に、
Python module for near field communication である [nfcpy module](https://github.com/nfcpy/nfcpy) を使って学生証をピッ！として学籍番号を抜きましょう！のためのリポジトリです。


### 使用した python のバージョン

python2系でしか nfcpy が動作しないため、今回用いる python の version は以下の通りです。

```bash
$ python2.7 -V
Python 2.7.12

$ pip2.7 -V
pip 18.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)
```

### 事前準備

以下の2つは必要になりますので、インストールしておいてくださいね。

```
$ brew install libusb
$ pip2.7 install nfcpy
```

### 実行方法

コマンドラインから実行したかったので、 `#!/usr/bin/env python2.7` を先頭につけてから `chmod +x` を実行した後、以下のコマンドで実行できるようにしています。基本的には引数はありませんが、ファイル名や保存する形式を指定するために設定しても良いかもしれないですね。

```bssh
$ ./main.py 
SONY RC-S380/P on usb:020:007
学生証をかざしてください： 　　　　　　　　　　　# 学生証をかざす
学籍番号 : 1733340447 の出席を確認しました。
学生証をかざしてください：　　　　　　　　　　　 # 3秒後に表示
```

出力したファイルの内容は以下の通りです。

* json 形式

```json
{ "time" : "Wed Jan  9 19:01:17 2019", "uId" : "1733340447" }
```

* csv 形式

```csv
Wed Jan  9 19:04:19 2019,1733340447
```

### エラー内容

以下のエラーが出たら、`pip` のインストールが上手く行っていない可能性がありますね。

```bash
$ ./main.py 
Traceback (most recent call last):
  File "./main.py", line 11, in <module>
    import nfc
ImportError: No module named nfc
```

7、8行目の以下のコードは自分の環境では `pip2.7` でインストールをしていたとしても、上手くいかなかったのでそれの回避用です。必要ないのでコメントアウトしています。

```python
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
```

以下のエラーが出たら、そもそも PaSoRi が接続されていない可能性がありますね。
数回このエラーと挨拶を交わしました。

```bash
$ ./main.py 
Traceback (most recent call last):
  File "./main.py", line 93, in <module>
    main()
  File "./main.py", line 83, in main
    clf = nfc.ContactlessFrontend('usb')
  File "/usr/local/lib/python2.7/site-packages/nfc/clf/__init__.py", line 75, in __init__
    raise IOError(errno.ENODEV, os.strerror(errno.ENODEV))
IOError: [Errno 19] Operation not supported by device
```