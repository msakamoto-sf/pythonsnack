from unittest import TestCase, skip


# TODO setUp() and tearDown()


@skip("skip demo for test class")
class TestUnittestSkipDemo1(TestCase):
    def test_fail1(self):
        self.fail("fail() demo1")

    def test_fail2(self):
        self.fail("fail() demo2")


class TestUnittestSkipDemo2(TestCase):
    @skip("skip demo for test method")
    def test_fail3(self):
        self.fail("fail() demo3")


class TestUnittestAssertDemo(TestCase):
    def test_assert_basic_equal(self):
        str1 = "abc"
        self.assertEqual(str1, "abc")
        self.assertNotEqual(str1, "hello")
        int1 = 100
        self.assertEqual(int1, 100)
        self.assertNotEqual(int1, 200)
        bool1 = True
        self.assertTrue(bool1)
        self.assertFalse(not bool1)

        # compare list values and order
        list1 = [100, "hello", True]
        self.assertEqual(list1, [100, "hello", True])
        self.assertNotEqual(list1, [100, "Hello", True])
        self.assertNotEqual(list1, ["hello", 100, True])

        # compare tuple values and order
        tuple1 = (100, "hello", True)
        self.assertEqual(tuple1, (100, "hello", True))
        self.assertNotEqual(tuple1, (100, "Hello", True))
        self.assertNotEqual(tuple1, (200, "HELLO", False))

        # compare set values
        set1 = set([100, "hello", True])
        self.assertEqual(set1, set([100, "hello", True]))
        self.assertEqual(set1, set([True, 100, "hello"]))
        self.assertNotEqual(set1, set([100, "Hello", True]))

        # compare dict keys and values
        dict1 = {"k1": 100, "k2": "hello", "k3": True}
        self.assertEqual(dict1, {"k1": 100, "k2": "hello", "k3": True})
        self.assertEqual(dict1, {"k2": "hello", "k1": 100, "k3": True})
        self.assertNotEqual(dict1, {"K1": 100, "k2": "hello", "k3": True})
        self.assertNotEqual(dict1, {"k1": 200, "k2": "hello", "k3": True})

    def test_assert_is(self):
        list1 = [100, 200]
        list2 = [100, 200]
        self.assertEqual(list1, list2)
        list3 = list1
        self.assertEqual(list1, list3)
        # from 3.1
        self.assertIsNot(list1, list2)
        self.assertIs(list1, list3)

    def test_assert_is_none(self):
        x = None
        y = not x
        # from 3.1
        self.assertIsNone(x)
        self.assertIsNotNone(y)

    def test_assert_in(self):
        # from 3.1

        list1 = [100, "hello", True]
        self.assertIn(100, list1)
        self.assertIn("hello", list1)
        self.assertIn(True, list1)
        self.assertNotIn(200, list1)
        self.assertNotIn("world", list1)
        self.assertNotIn(False, list1)

        tuple1 = (100, "hello", True)
        self.assertIn(100, tuple1)
        self.assertIn("hello", tuple1)
        self.assertIn(True, tuple1)
        self.assertNotIn(200, tuple1)
        self.assertNotIn("world", tuple1)
        self.assertNotIn(False, tuple1)

        set1 = set([100, "hello", True])
        self.assertIn(100, set1)
        self.assertIn("hello", set1)
        self.assertIn(True, set1)
        self.assertNotIn(200, set1)
        self.assertNotIn("world", set1)
        self.assertNotIn(False, set1)

        # for dict, assertIn() check key existing, not value.
        dict1 = {"k1": 100, "k2": "hello", "k3": True}
        self.assertIn("k1", dict1)
        self.assertNotIn("kx", dict1)
        self.assertNotIn(100, dict1)

    def test_assert_isinstance(self):
        class C1:
            pass

        class C2(C1):
            pass

        class C3(C1):
            pass

        class C4(C3):
            pass

        class C5:
            pass

        class C6(C5):
            pass

        o1 = C1()
        o2 = C2()
        o3 = C3()
        o4 = C4()
        o5 = C5()
        o6 = C6()
        # from 3.2
        self.assertIsInstance(o1, C1)
        self.assertIsInstance(o2, C2)
        self.assertIsInstance(o3, C3)
        self.assertIsInstance(o4, C4)
        self.assertIsInstance(o5, C5)
        self.assertIsInstance(o6, C6)
        # accept base class
        self.assertIsInstance(o2, C1)
        self.assertIsInstance(o3, C1)
        self.assertIsInstance(o4, C1)
        self.assertIsInstance(o4, C3)
        self.assertIsInstance(o5, C5)
        self.assertIsInstance(o6, C5)
        # accept class tuple for multiple base class
        self.assertIsInstance(o4, (C1, C5))
        self.assertIsInstance(o6, (C1, C5))
        self.assertNotIsInstance("hello", (C1, C5))
        # for strict type assertion:
        self.assertIs(type(o2), C2)
        self.assertIs(type(o3), C3)
        self.assertIs(type(o4), C4)
        self.assertIs(type(o5), C5)
        self.assertIs(type(o6), C6)
        self.assertIsNot(type(o6), C5)

    def test_assert_raise_exception(self):
        def div(x, y):
            return x / y

        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

        # with self.assertRaises(ZeroDivisionError):
        #     div(1, 1)
        # -> AssertionError: ZeroDivisionError not raised

        class DemoError(Exception):
            def __init__(self, errcode, message):
                self.errcode = errcode
                self.message = message

        with self.assertRaises(DemoError) as cm:
            raise DemoError(100, "hello")
        self.assertEqual(cm.exception.errcode, 100)
        self.assertEqual(cm.exception.message, "hello")

        # with self.assertRaises(DemoError, "hello") as cm:
        #     raise DemoError(100, "hello")
        # -> TypeError: 'str' object is not callable

    def test_assert_raise_regex(self):
        # from 3.1
        with self.assertRaisesRegex(ValueError, "literal"):
            int("XYZ")

        with self.assertRaisesRegex(
            ValueError, r"invalid literal for int\(\) with base \d+"
        ):
            int("XYZ")

    def test_assert_almost_equal_for_float(self):
        f1 = 0.1 * 3
        self.assertAlmostEqual(f1, 0.3)
        self.assertNotAlmostEqual(f1, 0.3, 20)

    def test_assert_great_or_less(self):
        # from 3.1
        self.assertGreater(2, 1)
        self.assertGreaterEqual(2, 1)
        self.assertGreaterEqual(2, 2)
        self.assertLess(1, 2)
        self.assertLessEqual(1, 2)
        self.assertLessEqual(2, 2)

    def test_assert_regex(self):
        # from 3.1
        self.assertRegex("abc", r"a(b|c){2}")
        # from 3.2
        self.assertNotRegex("def", r"a(b|c){2}")
