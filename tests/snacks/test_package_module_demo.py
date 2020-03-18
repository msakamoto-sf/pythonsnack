from unittest import TestCase
from snacks.mypkgdemo1 import MyPkgDemo1a, MyPkgDemo1b, mypkgdemo1_add

# relative import
from .mypkgdemo1 import MyPkgDemo1c, MyPkgDemo1d, mypkgdemo1_sub

import snacks.mypkgdemo1.module1 as module1
from snacks.mypkgdemo1 import module2


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
