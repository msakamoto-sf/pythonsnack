"""
TODO
 * `Pythonで作成した自作モジュールを様々な階層からimport - かざん`
   *  http://okuya-kazan.hatenablog.com/entry/2017/06/24/013541
 * `Python3 自作モジュールのインポートにハマる - かもメモ`
   *  https://chaika.hatenablog.com/entry/2018/08/24/090000
 * `Python __init__.pyの書き方 - Qiita`
   *  https://qiita.com/PYTHONISTA/items/2dcabc93365a62397afe
 * `Python の __init__.py とは何なのか - Qiita`
   *  https://qiita.com/msi/items/d91ea3900373ff8b09d7
 * `Python パッケージ作成: __init__.py の __all__ を手作業でメンテナンスしたくない - Qiita`
   *  https://qiita.com/suzuki-kei/items/8fea67655abf216a5013
 * `6. モジュール — Python 3.8.2 ドキュメント`
   *  https://docs.python.org/ja/3/tutorial/modules.html
"""


def mypkgdemo1_add(n1, n2):
    return n1 + n2


class MyPkgDemo1a:
    def __init__(self, n1):
        self.n1 = n1

    def add(self, n2):
        return self.n1 + n2


class MyPkgDemo1b:
    def __init__(self, n1):
        self.n1 = n1

    def sub(self, n2):
        return self.n1 - n2
