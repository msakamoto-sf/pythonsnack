from unittest import TestCase

# demonstration of underscore convention
# refs:
# https://www.python.org/dev/peps/pep-0008/
# https://docs.python.org/3/tutorial/classes.html#private-variables
# https://docs.python.org/ja/3/tutorial/classes.html#private-variables


class TestUnderscoreConventionDemo(TestCase):
    def test_underscore_ignore_value_acceptance(self):
        x, y, _ = (1, 2, 3)
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def test_single_leading_underscore_indicates_weak_internal(self):
        class C1:
            def __init__(self):
                self.public_str = "hello"
                self._private_str = "world"

        o1 = C1()
        self.assertEqual(o1.public_str, "hello")
        self.assertEqual(o1._private_str, "world")

    def test_single_trailing_underscore_avoids_python_keyword(self):
        def dict_(str_, int_):
            d0 = {}
            d0[str_] = int_
            return d0

        self.assertEqual(dict_("hello", 100), {"hello": 100})

    def test_double_leading_underscore_invoke_name_mangling(self):
        class C1:
            __mangled = "hello"

            def __init__(self, x: int):
                self.xx = self.__make_small(x)

            def make_small(self, x: int) -> int:
                return x - 1

            # hide from subclass
            __make_small = make_small

        class C2(C1):
            __mangled = "world"

            def __init__(self, x: int):
                super().__init__(x)

            def make_small(self, x: int) -> int:
                return x - 2

        # AttributeError: type object 'C1' has no attribute '_TestUnderscoreConventionDemo__mangled'
        # self.assertEqual(C1.__mangled, "hello")
        self.assertEqual(C1._C1__mangled, "hello")
        # AttributeError: type object 'C2' has no attribute '_TestUnderscoreConventionDemo__mangled'
        # self.assertEqual(C2.__mangled, "world")
        self.assertEqual(C2._C2__mangled, "world")

        o2 = C2(10)
        self.assertEqual(o2.xx, 9)
        self.assertEqual(o2.make_small(10), 8)

    def test_double_leading_trailing_underscore_is_special_method(self):
        # see-also: https://docs.python.org/ja/3/library/stdtypes.html#typeiter
        class OneToX:
            def __init__(self, x: int):
                self.cursor = 0
                self.x = x

            def __iter__(self):
                return self

            def __next__(self):
                self.cursor += 1
                if self.cursor > self.x:
                    raise StopIteration()
                return self.cursor

        self.assertEqual([i for i in OneToX(3)], [1, 2, 3])
        self.assertEqual([i for i in OneToX(5)], [1, 2, 3, 4, 5])
