import unittest
from dataclasses import dataclass, field
from typing import List, Dict, TypeVar, Generic

# demonstration of typing module.


@dataclass
class MyTypeDemo1:
    str1: str = "hello typing module"
    int1: int = 100

    strings: List[str] = field(default_factory=lambda: ["aaa", "bbb", "ccc"])
    ints: List[int] = field(default_factory=lambda: [10, 20, 30])
    str2int: Dict[str, int] = field(
        default_factory=lambda: {"aaa": 10, "bbb": 20, "ccc": 30,}
    )
    str2strings: Dict[str, List[str]] = field(
        default_factory=lambda: {
            "aaa": ["AA", "BB", "CC",],
            "bbb": ["DD", "EE",],
            "ccc": [],
        }
    )


class TestMyTypeDemo1(unittest.TestCase):
    def test_do(self):
        a: MyTypeDemo1 = MyTypeDemo1()
        self.assertEqual(a.str1, "hello typing module")
        self.assertEqual(a.int1, 100)
        self.assertListEqual(a.strings, ["aaa", "bbb", "ccc"])
        self.assertListEqual(a.ints, [10, 20, 30])
        self.assertDictEqual(a.str2int, {"aaa": 10, "bbb": 20, "ccc": 30,})
        # dict.keys() はsetではなく(py3)、listそのものでもないため、厳密にlistで扱うにはlist()でラップする。
        # see: https://stackoverflow.com/questions/13886129/why-does-pythons-dict-keys-return-a-list-and-not-a-set # noqa: E501
        # see: https://stackoverflow.com/questions/28310338/using-set-on-dictionary-keys # noqa: E501
        # see: https://www.javadrive.jp/python/dictionary/index8.html
        self.assertListEqual(list(a.str2strings.keys()), ["aaa", "bbb", "ccc"])
        self.assertListEqual(a.str2strings["aaa"], ["AA", "BB", "CC",])
        self.assertListEqual(a.str2strings["bbb"], ["DD", "EE",])
        self.assertListEqual(a.str2strings["ccc"], [])


T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")


class MyTypeDemoPair1(Generic[T1, T2]):
    left: T1
    right: T2

    def __init__(self, left: T1, right: T2):
        self.left = left
        self.right = right


class TestMyTypeDemoPair1(unittest.TestCase):
    def test_do(self):
        p1: MyTypeDemoPair1[int, str] = MyTypeDemoPair1(100, "hello")
        self.assertEqual(p1.left, 100)
        self.assertEqual(p1.right, "hello")
        p2: MyTypeDemoPair1[str, int] = MyTypeDemoPair1("world", 200)
        self.assertEqual(p2.left, "world")
        self.assertEqual(p2.right, 200)


class MyTypeDemoPair2(Generic[T1, T2, T3], MyTypeDemoPair1[T1, T2]):
    middle: T3

    def __init__(self, left: T1, middle: T3, right: T2):
        super().__init__(left, right)
        self.middle = middle


class TestMyTypeDemoPair2(unittest.TestCase):
    def test_do(self):
        p1: MyTypeDemoPair2[int, str, int] = MyTypeDemoPair2(100, "hello", 200)
        self.assertEqual(p1.left, 100)
        self.assertEqual(p1.middle, "hello")
        self.assertEqual(p1.right, 200)


class MyTypeDemoPair3(Generic[T4], MyTypeDemoPair1[str, str]):
    middle: T4

    def __init__(self, left: str, middle: T4, right: str):
        super().__init__(left, right)
        self.middle = middle


class TestMyTypeDemoPair3(unittest.TestCase):
    def test_do(self):
        p1: MyTypeDemoPair3[int] = MyTypeDemoPair3("hello", 100, "world")
        self.assertEqual(p1.left, "hello")
        self.assertEqual(p1.middle, 100)
        self.assertEqual(p1.right, "world")


# TODO more and more typing combination demo
