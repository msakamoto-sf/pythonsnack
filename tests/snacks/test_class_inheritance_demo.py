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

        class C2a(C1):
            class_attr1 = 200

            def __init__(self, attr1):
                super().__init__(attr1)
                self.attr2 = attr1 + 1

            def get_attr1(self):
                return super().get_attr1()

            def get_attr2(self):
                return self.attr2

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
        o2b = C2b(30)
        self.assertEqual(o2b.attr1, 30)
        self.assertEqual(o2b.attr2, 32)
        self.assertEqual(o2b.get_attr1(), 30)
        self.assertEqual(o2b.get_attr2(), 32)
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

    def test_template_method_demo(self):
        # TODO
        pass

    def test_static_method_inheritance_demo(self):
        # TODO
        pass

    def test_multiple_inheritance_demo(self):
        # TODO
        pass


# TODO abc (abstract base class) demo
# TODO *args, **kwdargs parameter demo
