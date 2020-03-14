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

run from command line:
```
cd (repository root directory)
(activate venv)

## run unittest:
python -m unittest discover

## run flake8:
flake8 snacks tests

## run mypy:
mypy snacks tests

## run black (dry-run)
black --diff snacks tests

## run black (write-back to files)
black snacks tests
```

## vscode integration

**before opening vscode, you MUST have done creating venv and pip install -r requirements**

after opening vscode (first-time only):
1. select "Python: Select Interpreter" command from the Command Palette (`Ctrl+Shift+P`)
2. choose "Python 3.x.y ... .venv" (.venv python)
   - NOTE: vscode automatically generate `.vscode/settings.json` at this time.
3. add below settings to `.vscode/settings.json`

```
{
    "python.venvPath": ".venv",
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.lintOnSave": true,

    "python.pythonPath": "(path inserted by vscode)"
}
```

- Why are you put `.vscode/settings.json` to git repository ?
  - Because venv's `python.pythonPath` is different between some platoforms. for Win, `Scripts\\python.exe` <> but linux/macos, `bin/python`.
  - I gave up putting these cross-platform behabiours to one-single-common `settings.json` X(

refs:

- `Using Python Environments in Visual Studio Code`
  - https://code.visualstudio.com/docs/python/environments
- `VS CodeでWorkspace毎に使用するPython実行環境を切り替える | LogixSquare`
  - https://logixsquare.com/techblog/visual-studio-code-python-version-settings/

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

### linter, checker, formatter

- flake8
  - https://pypi.org/project/flake8/
- mypy
  - http://mypy-lang.org/
  - https://github.com/python/mypy
- black (formatter)
  - https://github.com/psf/black

- `Python開発を円滑に進めるためのツール設定 Part.1 - ログミーTech`
  - https://logmi.jp/tech/articles/322611
- `Python開発を円滑に進めるためのツール設定 Part.2 - ログミーTech`
  - https://logmi.jp/tech/articles/322612
- `Pythonでの開発を効率的に進めるためのツール設定`
  - https://www.slideshare.net/aodag/python-172432039
- `Python 3.7とVisual Studio Codeで型チェックが捗る内作Pythonアプリケーション開発環境の構築 - Qiita`
  - https://qiita.com/shibukawa/items/1650724daf117fad6ccd
- `超簡単VSCodeでPythonソースコード自動チェック・整形（venv・flake8・mypy・black利用）｜10mohi6｜note`
  - https://note.com/10mohi6/n/n87e7867bfb79
- `Visual Studio Code を使ったPython環境の構築 - Qiita`
  - https://qiita.com/shinno21/items/c33802da7145b36106e2
- `もうPythonの細かい書き方で議論しない。blackで自動フォーマットしよう - Make組ブログ`
  - https://blog.hirokiky.org/entry/2019/06/03/202745

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

