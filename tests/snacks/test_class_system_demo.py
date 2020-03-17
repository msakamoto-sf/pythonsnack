from unittest import TestCase

# demonstration of python class system
# ref: https://docs.python.org/ja/3/tutorial/classes.html
# ref: https://docs.python.org/ja/3/reference/datamodel.html
# ref: https://docs.python.org/ja/3/library/functions.html


class TestClassSystemDemo(TestCase):
    def test_class_var_sharing(self):
        class C1:
            attr1 = 100

            def get_attr1(self):
                return self.attr1

        self.assertTrue(hasattr(C1, "attr1"))
        self.assertEqual(getattr(C1, "attr1"), 100)
        with self.assertRaises(AttributeError) as cm:
            getattr(C1, "attrX")
        self.assertEqual(str(cm.exception), "type object 'C1' has no attribute 'attrX'")

        self.assertEqual(C1.attr1, 100)
        o1 = C1()
        self.assertEqual(o1.attr1, 100)
        self.assertEqual(o1.get_attr1(), 100)  # self.attr1 refers C1.attr1
        o1.attr1 = 200  # affect to o1.attr1, not C1.attr1
        self.assertEqual(C1.attr1, 100)
        self.assertEqual(o1.attr1, 200)
        self.assertEqual(
            o1.get_attr1(), 200
        )  # self.attr1 refers o1.attr1 (instance var)

        self.assertTrue(hasattr(o1, "attr1"))
        self.assertEqual(getattr(o1, "attr1"), 200)
        with self.assertRaises(AttributeError) as cm:
            getattr(o1, "attrX")
        self.assertEqual(str(cm.exception), "'C1' object has no attribute 'attrX'")

        o2 = C1()
        self.assertEqual(o2.attr1, 100)
        C1.attr1 = 300
        self.assertEqual(getattr(C1, "attr1"), 300)
        self.assertEqual(C1.attr1, 300)
        o3 = C1()
        self.assertEqual(o2.attr1, 300)  # o2.attr1 => C1.attr1
        self.assertEqual(o3.attr1, 300)

        # class var can be added at runtime.
        C1.attr2 = "hello"
        self.assertTrue(hasattr(C1, "attr2"))
        self.assertEqual(getattr(C1, "attr2"), "hello")
        # added class var can be accessed through already created instance.
        self.assertEqual(o1.attr2, "hello")
        self.assertTrue(hasattr(o1, "attr2"))
        self.assertEqual(getattr(o1, "attr2"), "hello")

    def test_instance_var(self):
        class C1:
            def __init__(self, f1):
                self.f1 = f1

        self.assertFalse(hasattr(C1, "f1"))
        with self.assertRaises(AttributeError) as cm:
            getattr(C1, "f1")
        self.assertEqual(str(cm.exception), "type object 'C1' has no attribute 'f1'")

        o1 = C1(100)
        self.assertEqual(o1.f1, 100)
        self.assertFalse(hasattr(C1, "f1"))
        self.assertTrue(hasattr(o1, "f1"))
        self.assertEqual(getattr(o1, "f1"), 100)
        with self.assertRaises(AttributeError) as cm:
            getattr(o1, "attrX")
        self.assertEqual(str(cm.exception), "'C1' object has no attribute 'attrX'")

        o2 = C1(200)
        self.assertEqual(o1.f1, 100)
        self.assertEqual(o2.f1, 200)

        o3 = C1(100)
        self.assertEqual(o3.f1, 100)
        self.assertEqual(o3.f1, o1.f1)
        self.assertNotEqual(o3, o1)
        self.assertIsNot(o3, o1)

        # instance var can be added after instance creation
        o3.f2 = "hello"
        self.assertTrue(hasattr(o3, "f2"))
        self.assertEqual(getattr(o3, "f2"), "hello")
        self.assertFalse(hasattr(o1, "f2"))  # not affect to already created instance

    def test_class_var_instance_var_mix(self):
        class C1:
            f1 = 100

            def __init__(self, f1):
                self.f1 = f1

        self.assertEqual(C1.f1, 100)
        o1 = C1(200)
        self.assertEqual(C1.f1, 100)
        # prefer instance var rather than class var
        self.assertEqual(o1.f1, 200)

        C1.f1 = 300
        o2 = C1(400)
        self.assertEqual(C1.f1, 300)  # overwritten class var
        self.assertEqual(o1.f1, 200)  # not affect to already created instance var
        self.assertEqual(o2.f1, 400)

    def test_classmethod_staticmethod(self):
        class C1:
            m1 = 100

            @classmethod
            def add_c(cls, a):
                return cls.m1 + a

            @staticmethod
            def add_s(a, b):
                return a + b

        self.assertEqual(C1.add_c(10), 110)
        self.assertEqual(C1.add_s(10, 20), 30)
        o1 = C1()
        self.assertEqual(o1.add_c(20), 120)
        self.assertEqual(o1.add_s(30, 40), 70)
        o1.m1 = 200  # not affect to C1.m1
        self.assertEqual(C1.add_c(10), 110)
        self.assertEqual(C1.add_s(10, 20), 30)
        self.assertEqual(o1.add_c(20), 120)
        self.assertEqual(o1.add_s(30, 40), 70)
        C1.m1 = 300
        self.assertEqual(C1.add_c(10), 310)
        self.assertEqual(C1.add_s(10, 20), 30)
        self.assertEqual(o1.add_c(20), 320)
        self.assertEqual(o1.add_s(30, 40), 70)

    def test_init_and_new(self):
        # see-also:
        # https://qiita.com/FGtatsuro/items/49f907a809e53b874b18
        # https://babaye.hatenablog.com/entry/2019/07/13/180916

        class C1:
            def __new__(cls, n1, n2):
                tmp = super().__new__(cls)
                tmp.n1 = n1 + 1
                tmp.n2 = n2 + 2
                return tmp

            def __init__(self, n1, n2):
                self.n1 = self.n1 * 2 + n1
                self.n2 = self.n2 * 3 + n2

        o1 = C1(10, 20)
        # n1 => __init__: (__new__: 10 + 1) * 2 + 10
        self.assertEqual(o1.n1, 32)
        # n2 => __init__: (__new__: 20 + 2) * 3 + 20
        self.assertEqual(o1.n2, 86)

    def test_constructor_overload(self):
        # see-also:
        # https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
        # https://stackoverflow.com/questions/141545/how-to-overload-init-method-based-on-argument-type
        # https://qiita.com/miyashiiii/items/9dcb2114ac0843a73fce
        # https://qiita.com/_ha1f/items/532e67c3590ebc0988e8

        class C1:
            def __init__(self, a, b, c):
                self.sum = a + b + c

            @classmethod
            def from1(cls, a):
                return cls(a, a + 1, a + 2)

            @classmethod
            def from2(cls, a, b):
                return cls(a, b, b + 1)

        o1 = C1(1, 2, 3)
        self.assertEqual(o1.sum, 6)
        o2 = C1.from1(4)
        self.assertEqual(o2.sum, 15)
        o3 = C1.from2(5, 6)
        self.assertEqual(o3.sum, 18)
