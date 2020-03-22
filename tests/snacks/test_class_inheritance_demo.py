from unittest import TestCase

# demonstration of python class inheritance
# refs: https://docs.python.org/ja/3/tutorial/classes.html#inheritance


class TestClassInheritanceDemo(TestCase):
    def test_basic_inheritance(self):
        class C1:
            class_attr1 = 100

            def __init__(self, attr1):
                self.attr1 = attr1

            def get_attr1(self):
                return self.attr1

            def get_attrx(self):
                # get_attrz() is not defined in C1
                return self.get_attry() + self.get_attrz() + self.attr1

            def get_attry(self):
                # default implementation
                return 0

        class C2a(C1):
            class_attr1 = 200

            def __init__(self, attr1):
                super().__init__(attr1)
                self.attr2 = attr1 + 1

            def get_attr1(self):
                return super().get_attr1()

            def get_attr2(self):
                return self.attr2

            def get_attry(self):
                # override
                return self.attr2 * 2

            def get_attrz(self):
                return self.attr2 - 2

        class C2b(C1):
            class_attr1 = 300

            def __init__(self, attr1):
                super().__init__(attr1)
                self.attr2 = attr1 + 2

            def get_attr1(self):
                # another way to call base class' instance method
                return C1.get_attr1(self)

            def get_attr2(self):
                return self.attr2

            def get_attry(self):
                # override
                return self.attr2 * 3

            def get_attrz(self):
                return self.attr2 - 3

        self.assertEqual(C1.class_attr1, 100)
        self.assertEqual(C2a.class_attr1, 200)
        self.assertEqual(C2b.class_attr1, 300)
        o1 = C1(10)
        self.assertEqual(o1.attr1, 10)
        self.assertEqual(o1.get_attr1(), 10)
        o2a = C2a(20)
        self.assertEqual(o2a.attr1, 20)
        self.assertEqual(o2a.attr2, 21)
        self.assertEqual(o2a.get_attr1(), 20)
        self.assertEqual(o2a.get_attr2(), 21)
        # 21(=attr2) * 2 + 21(=attr2) - 2 + 20(=attr1) : C1#get_attrx() calls C2a#get_attrz()
        self.assertEqual(o2a.get_attrx(), 81)
        o2b = C2b(30)
        self.assertEqual(o2b.attr1, 30)
        self.assertEqual(o2b.attr2, 32)
        self.assertEqual(o2b.get_attr1(), 30)
        self.assertEqual(o2b.get_attr2(), 32)
        # 32(=attr2) * 3 + 32(=attr2) - 3 + 30(=attr1) : C1#get_attrx() calls C2b#get_attrz()
        self.assertEqual(o2b.get_attrx(), 155)
        self.assertTrue(isinstance(o1, C1))
        self.assertTrue(isinstance(o2a, C1))
        self.assertTrue(isinstance(o2a, C2a))
        self.assertFalse(isinstance(o2a, C2b))
        self.assertTrue(isinstance(o2b, C1))
        self.assertTrue(isinstance(o2b, C2b))
        self.assertFalse(isinstance(o2b, C2a))
        self.assertFalse(isinstance(o1, (C2a, C2b)))
        self.assertTrue(isinstance(o2a, (C2a, C2b)))
        self.assertTrue(isinstance(o2b, (C2a, C2b)))
        self.assertTrue(issubclass(C2a, C1))
        self.assertTrue(issubclass(C2b, C1))
        self.assertFalse(issubclass(C2a, C2b))

    def test_static_method_inheritance_demo(self):
        # see-also:
        # https://docs.python.org/ja/3/library/functions.html#super
        # https://stackoverflow.com/questions/26788214/super-and-staticmethod-interaction/26807879
        # https://stackoverflow.com/questions/805066/call-a-parent-classs-method-from-child-class
        class C1:
            m1 = 100

            @classmethod
            def add_c(cls, a):
                return cls.m1 + a

            @staticmethod
            def add_s(a, b):
                return a + b

            @classmethod
            def sub_c(cls, a):
                return cls.m1 - a

            @staticmethod
            def sub_s(a, b):
                return a - b

        class C2a(C1):
            @classmethod
            def add_c2(cls, a):
                return C1.add_c(a) + 1

            @staticmethod
            def add_s2(a, b):
                return C1.add_s(a, b) + 2

            @classmethod
            def sub_c(cls, a):
                # override
                return C1.sub_c(a) - 1

            @staticmethod
            def sub_s(a, b):
                # override
                return C1.sub_s(a, b) - 2

        class C2b(C1):
            @classmethod
            def add_c2(cls, a):
                return super(C2b, cls).add_c(a) + 3

            @staticmethod
            def add_s2(a, b):
                return super(C2b, C2b).add_s(a, b) + 4

            @classmethod
            def sub_c(cls, a):
                # override
                return super(C2b, cls).sub_c(a) - 3

            @staticmethod
            def sub_s(a, b):
                # override
                return super(C2b, C2b).sub_s(a, b) - 4

        self.assertEqual(C2a.add_c(10), 110)  # C1.m1 + 10
        self.assertEqual(C2a.add_c2(10), 111)  # C1.m1 + 10 + 1
        self.assertEqual(C2a.add_s2(10, 20), 32)  # 10 + 20 + 2
        self.assertEqual(C2a.sub_c(10), 89)  # C1.m1 - 10 - 1
        self.assertEqual(C2a.sub_s(10, 20), -12)  # 10 - 20 - 2
        self.assertEqual(C2b.add_c(20), 120)  # C1.m1 + 20
        self.assertEqual(C2b.add_c2(20), 123)  # C1.m1 + 20 + 3
        self.assertEqual(C2b.add_s2(20, 30), 54)  # 20 + 30 + 4
        self.assertEqual(C2b.sub_c(20), 77)  # C1.m1 - 20 - 3
        self.assertEqual(C2b.sub_s(20, 30), -14)  # 20 - 30 - 4

    def test_multiple_inheritance_demo(self):
        # see-also
        # https://docs.python.org/ja/3/tutorial/classes.html#multiple-inheritance
        # https://docs.python.org/ja/3/library/functions.html#super
        # https://qiita.com/Kodaira_/items/42dfe18c81af98bf0db3
        # https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
        class C1:
            def __init__(self, f1):
                self.f1 = f1

            def add(self, a):
                # print("C1", self.f1)
                return self.f1 + a

            def sub(self, a):
                return self.f1 - a

        class C2a(C1):
            def __init__(self, f1):
                super().__init__(f1 + 1)
                self.f2 = f1 + 2

            def add(self, a):
                x = super().add(a)
                # print("C2a", x)
                return x + self.f2 + 3

            def mul(self, a):
                return self.f1 * self.f2 * a

        class C2b(C1):
            def __init__(self, f1):
                super().__init__(f1 + 4)
                self.f2 = f1 + 5

            def add(self, a):
                x = super().add(a)
                # print("C2b", x)
                return x + self.f2 + 6

            def div(self, a):
                return self.f1 / a + self.f2

        class C3(C2a, C2b):
            def __init__(self, f1):
                super().__init__(f1)

        o3 = C3(10)
        self.assertEqual(o3.f1, 15)  # C2a#__init__() and C2b#__init__()
        self.assertEqual(o3.f2, 12)  # C2a#__init__()
        self.assertEqual(o3.add(30), 78)  # = C2a#add(C2b#add(C1#add()))
        # C1#add() = 15 + 30 => 45
        # C2b#add() = 45 + 12 + 6 => 63
        # C2a#add() = 63 + 12 + 3 => 78
        self.assertEqual(o3.sub(10), 5)  # 15 - 10
        self.assertEqual(o3.mul(2), 360)  # 15 * 12 * 2
        self.assertEqual(o3.div(3), 17)  # 15/3 + 12

    def test_method_overload_demo(self):
        # see-also:
        # https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
        # https://docs.python.org/ja/3/library/functools.html#functools.singledispatch
        # TODO
        pass


# TODO abc (abstract base class) demo
# TODO *args, **kwdargs parameter demo
