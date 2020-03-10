# pythonsnack
Python demonstration, exercise, practice, study, example codes.

require : Python 3.7 >= (using `unittest discover` : 3.2, pip as default : 3.6, `dataclasses` : 3.7)

setup venv and install pip requirements:

```
## create venv
cd (repository root directory)
python -m venv .venv

## activate venv
(linux-bash)
source .venv/bin/activate

(win-cmd)
.venv\Scripts\activate.bat 

(other-shell, platform, see https://docs.python.org/ja/3/library/venv.html )

## update pip in venv
python -m pip install --upgrade pip

## install pip requirements
python -m pip install -r requirements.txt
```

run unittest:

```
$ cd (repository root directory)
$ python -m unittest discover
```

run mypy:

```
mypy tests
mypy snacks
```

## reference

### venv and pip

- `venv --- 仮想環境の作成   Python 3.8.2 ドキュメント`
  - https://docs.python.org/ja/3/library/venv.html
- `12. 仮想環境とパッケージ   Python 3.8.2 ドキュメント`
  - https://docs.python.org/ja/3/tutorial/venv.html
- `Python モジュールのインストール   Python 3.8.2 ドキュメント`
  - https://docs.python.org/ja/3/installing/index.html
- `venv: Python 仮想環境管理 - Qiita`
  - https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

pip コマンドのヘルプ: `python -m pip help`

`pip install` したら `pip freeze` 結果を `requirements.txt` に保存する。そうすれば `pip install -r requirements.txt` で同じパッケージをインストールできる:

- `python -m pip freeze -l > requirements.txt`
- https://pip.pypa.io/en/stable/reference/
- `Python, pip list / freezeでインストール済みパッケージ一覧を確認 | note.nkmk.me`
  - https://note.nkmk.me/python-pip-list-freeze/
- `Python, pipでrequirements.txtを使ってパッケージ一括インストール | note.nkmk.me`
  - https://note.nkmk.me/python-pip-install-requirements/
- `よく使うpipコマンド - Qiita`
  - https://qiita.com/Masaaki_Inaba/items/fe4a246a7e6fcd9c4726

### unittest

- https://docs.python.org/ja/3/library/unittest.html
- https://pymotw.com/3/unittest/
- Python 3 標準の unittest でテストを書く際のディレクトリ構成 - Qiita
  - https://qiita.com/hoto17296/items/fa0166728177e676cd36
- Pythonのunittestでハマったところと、もっと早くに知りたかったこと - Qiita
  - https://qiita.com/jesus_isao/items/f93c11248192645eb25d
- あるディレクトリ以下の unittest を全部実行させる - Qiita
  - https://qiita.com/yoichi22/items/2b488dc0696d9b45fad6

### write test code

- https://coding-exercises.udemy.com/python_3.html
- https://realpython.com/python-testing/#executing-your-first-test
- https://realpython.com/python-mock-library/

### coding rule

- https://pep8-ja.readthedocs.io/ja/latest/
- ［Python入門］Pythonコーディングスタイルガイド：Python入門 - ＠IT
  - https://www.atmarkit.co.jp/ait/articles/1912/10/news045.html

