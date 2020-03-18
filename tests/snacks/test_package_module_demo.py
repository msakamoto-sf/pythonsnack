from unittest import TestCase
from snacks.mypkgdemo1 import MyPkgDemo1a, MyPkgDemo1b, mypkgdemo1_add

# relative import
from .mypkgdemo1 import MyPkgDemo1c, MyPkgDemo1d, mypkgdemo1_sub

import snacks.mypkgdemo1.module1 as module1
from snacks.mypkgdemo1 import module2

# demonstration of package/module imports
# ref: https://docs.python.org/ja/3/tutorial/modules.html
# ref: https://docs.python.org/ja/3/reference/import.html
# see-also:
# - Pythonで作成した自作モジュールを様々な階層からimport - かざん
#   - http://okuya-kazan.hatenablog.com/entry/2017/06/24/013541
# - Python3 自作モジュールのインポートにハマる - かもメモ
#   - https://chaika.hatenablog.com/entry/2018/08/24/090000
# - Python __init__.pyの書き方 - Qiita
#   - https://qiita.com/PYTHONISTA/items/2dcabc93365a62397afe
# - Python の __init__.py とは何なのか - Qiita
#   - https://qiita.com/msi/items/d91ea3900373ff8b09d7


# from .mypkgdemo2 import *
# -> flake8 で以下のルール違反で指摘される。
# "Name may be undefined, or defined from star imports: module (F405)"
# https://www.flake8rules.com/rules/F405.html
# -> 断念して、__init__.py 側で手動でエイリアスを設定して import の軽量化を試みた。
from .mypkgdemo2 import (
    module3_sub,
    module4_sub,
    module5_sub,
    ClassInModule3,
    ClassInModule4,
    ClassInModule5,
)


class TestPackageModuleDemo(TestCase):
    def test_package_demo(self):
        self.assertEqual(mypkgdemo1_add(1, 2), 3)
        o1 = MyPkgDemo1a(10)
        self.assertEqual(o1.add(20), 30)
        o2 = MyPkgDemo1b(20)
        self.assertEqual(o2.sub(5), 15)

        self.assertEqual(mypkgdemo1_sub(5, 4), 1)
        o3 = MyPkgDemo1c(30)
        self.assertEqual(o3.mul(3), 90)
        o4 = MyPkgDemo1d(40)
        self.assertEqual(o4.div(4), 10)

    def test_module_demo(self):
        self.assertEqual(module1.module1_add(1, 2, 3), 6)
        self.assertEqual(module1.ClassInModule1.add(4, 5, 6), 16)
        self.assertEqual(module2.module2_add(2, 3, 4), 10)
        self.assertEqual(module2.ClassInModule2.add(3, 4, 5), 14)

    def test_import_wildcard(self):
        self.assertEqual(module3_sub(3, 2), 1)
        self.assertEqual(module4_sub(3, 2, 1), 0)
        self.assertEqual(module5_sub(4, 3, 2, 1), -2)
        self.assertEqual(ClassInModule3.sub(6, 5), 0)
        self.assertEqual(ClassInModule4.sub(10, 2, 1), 5)
        self.assertEqual(ClassInModule5.sub(10, 1, 2, 3), 1)
