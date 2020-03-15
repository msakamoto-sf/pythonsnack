## reference

- unittest
  - https://docs.python.org/ja/3/library/unittest.html

### mypy check

```
cd (git-cloned-root)/
python -m venv .venv
python -m pip install -r requirements.txt

(linux)
source .venv/bin/activate

(win-cmd)
.venv\Scripts\activate.bat 

mypy tests
mypy snacks
```

refs:
- `mypyやっていくぞ - Qiita`
  - https://qiita.com/k-saka/items/8f05c89f675af219e081

### type hitn & typing module.

- https://docs.python.org/ja/3/library/typing.html
- https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
- `Pythonと型チェッカー`
  - https://www.slideshare.net/t2y/python-typechecker-20180519
- `Python の型ヒントと typing と mypy | 民主主義に乾杯`
  - https://python.ms/type/
- `Pythonとmypyで型ヒントを利用する（基礎編）`
  - https://doitu.info/blog/5aaa8deaab60b20097abdb83
- `Python と型アノテーション`
  - https://www.slideshare.net/quintia/python-76118249

