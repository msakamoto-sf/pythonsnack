from unittest import TestCase
from dataclasses import dataclass, field
from typing import List, ClassVar

# demonstration of dataclass


class MyNoData1:
    # 型ヒントだけの場合、クラス変数として初期化されない
    str1: str
    int1: int

    def __init__(self, str1: str, int1: int):
        self.str1 = str1
        self.int1 = int1


class TestMyNoData1(TestCase):
    def test_do(self):
        d1: MyNoData1 = MyNoData1("hello", 100)
        d2: MyNoData1 = MyNoData1("world", 200)
        # str1, int1 はインスタンス変数を参照してる。
        self.assertEqual(d1.str1, "hello")
        self.assertEqual(d1.int1, 100)
        self.assertEqual(d2.str1, "world")
        self.assertEqual(d2.int1, 200)

        # 型ヒントだけの場合、クラス変数として初期化されず以下は Attribute Error になる。
        with self.assertRaises(AttributeError) as cm:
            MyNoData1.str1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyNoData1' has no attribute 'str1'"
        )
        with self.assertRaises(AttributeError) as cm:
            MyNoData1.int1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyNoData1' has no attribute 'int1'"
        )


class MyNoData2:
    # 初期値があれば、型ヒントが無い場合のクラス変数と同様に参照可能になる。
    str1: str = "xyz"
    int1: int = -1

    def __init__(self, str1: str, int1: int):
        self.str1 = str1
        self.int1 = int1


class TestMyNoData2(TestCase):
    def test_do(self):
        d1: MyNoData2 = MyNoData2("hello", 100)
        d2: MyNoData2 = MyNoData2("world", 200)
        # str1, int1 はインスタンス変数の方を優先して参照してる。
        self.assertEqual(d1.str1, "hello")
        self.assertEqual(d1.int1, 100)
        self.assertEqual(d2.str1, "world")
        self.assertEqual(d2.int1, 200)

        # 初期値があるのでクラス変数を参照できる。
        self.assertEqual(MyNoData2.str1, "xyz")
        self.assertEqual(MyNoData2.int1, -1)


@dataclass
class MyData1:
    # 型ヒントだけの場合、クラス変数として初期化されない
    str1: str
    int1: int


class TestMyData1(TestCase):
    def test_do(self):
        d1: MyData1 = MyData1("hello", 100)
        d2: MyData1 = MyData1("world", 200)
        # 型ヒントだけで初期値が無いため、デフォルト値を使った __init__ が未定義となる。
        # d3: MyData1 = MyData1()
        # str1, int1 はインスタンス変数を参照してる。
        self.assertEqual(d1.str1, "hello")
        self.assertEqual(d1.int1, 100)
        self.assertEqual(d2.str1, "world")
        self.assertEqual(d2.int1, 200)

        # 型ヒントだけの場合、クラス変数として初期化されず以下は Attribute Error になる。
        with self.assertRaises(AttributeError) as cm:
            MyData1.str1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData1' has no attribute 'str1'"
        )
        with self.assertRaises(AttributeError) as cm:
            MyData1.int1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData1' has no attribute 'int1'"
        )


@dataclass
class MyData2:
    # 初期値があれば、型ヒントが無い場合のクラス変数と同様に参照可能になる。
    str1: str = "xyz"
    int1: int = -1


class TestMyData2(TestCase):
    def test_do(self):
        d1: MyData2 = MyData2("hello", 100)
        d2: MyData2 = MyData2("world", 200)
        # 初期値があるのでデフォルト値を使った __init__ が利用できる。
        d3: MyData3 = MyData2()
        self.assertEqual(d1.str1, "hello")
        self.assertEqual(d1.int1, 100)
        self.assertEqual(d2.str1, "world")
        self.assertEqual(d2.int1, 200)
        self.assertEqual(d3.str1, "xyz")
        self.assertEqual(d3.int1, -1)

        # 初期値があるのでクラス変数を参照できる。
        self.assertEqual(MyData2.str1, "xyz")
        self.assertEqual(MyData2.int1, -1)


# field(init=False) と __post_init__ の組み合わせデモ
@dataclass
class MyData3:
    first_name: str
    last_name: str
    full_name: str = field(init=False)

    def __post_init__(self):
        self.full_name = self.first_name + " " + self.last_name


class TestMyData3(TestCase):
    def test_do(self):
        d0: MyData3 = MyData3("aaa", "bbb")
        self.assertEqual(d0.first_name, "aaa")
        self.assertEqual(d0.last_name, "bbb")
        self.assertEqual(d0.full_name, "aaa bbb")


@dataclass
class MyData4:
    # 初期値が無いためクラス変数としては参照できない。
    str1: str

    # 初期値があるのでクラス変数として参照できる。
    str2: str = "xyz"
    str3: str = field(default="abc")

    # mypy error: Attributes without a default cannot follow attributes with one
    # str4: str = field(init=True)

    # 初期値が無いためクラス変数としては参照できない。
    str5: ClassVar[str]

    # 初期値があるのでクラス変数として参照できる。
    str6: ClassVar[str] = "XYZ"


class TestMyData4(TestCase):
    def test_do(self):
        # str1 は型ヒントしか無いため、クラス変数としては扱われない。
        with self.assertRaises(AttributeError) as cm:
            MyData4.str1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData4' has no attribute 'str1'"
        )
        # str2 は初期値があるため、クラス変数として扱われる。
        self.assertEqual(MyData4.str2, "xyz")
        # str3 は直接初期値は設定されていないが、field()のデフォルト値指定によりクラス変数としてデフォルト値が設定される。
        self.assertEqual(MyData4.str3, "abc")
        # str5 は型ヒントしか無いため、ClassVar を使っていても、クラス変数としては扱われない。
        with self.assertRaises(AttributeError) as cm:
            MyData4.str5
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData4' has no attribute 'str5'"
        )
        # str6 は初期値があるため、クラス変数として扱われる。
        self.assertEqual(MyData4.str6, "XYZ")

        d1: MyData4 = MyData4(str1="hello", str2="world")
        self.assertEqual(d1.str1, "hello")
        self.assertEqual(d1.str2, "world")
        self.assertEqual(d1.str3, "abc")
        # AttributeError: 'MyData4' object has no attribute 'str5'
        # self.assertEqual(d1.str5, "")
        self.assertEqual(d1.str6, "XYZ")

        d2: MyData4 = MyData4(str1="HELLO", str2="WORLD", str3="ABC")
        self.assertEqual(d2.str1, "HELLO")
        self.assertEqual(d2.str2, "WORLD")
        self.assertEqual(d2.str3, "ABC")
        # AttributeError: 'MyData4' object has no attribute 'str5'
        # self.assertEqual(d2.str5, "")
        self.assertEqual(d2.str6, "XYZ")

        d3: MyData4 = MyData4("foo")
        self.assertEqual(d3.str1, "foo")
        self.assertEqual(d3.str2, "xyz")
        self.assertEqual(d3.str3, "abc")
        # AttributeError: 'MyData4' object has no attribute 'str5'
        # self.assertEqual(d2.str5, "")
        self.assertEqual(d3.str6, "XYZ")

        self.assertEqual(MyData4.str2, "xyz")
        self.assertEqual(MyData4.str3, "abc")
        self.assertEqual(MyData4.str6, "XYZ")

        MyData4.str2 = "Z"
        MyData4.str3 = "ZZ"
        MyData4.str6 = "ZZZ"
        # クラス変数を更新しても、str2/3 についてはインスタンス変数を優先して参照してる。
        self.assertEqual(d1.str1, "hello")
        self.assertEqual(d1.str2, "world")
        self.assertEqual(d1.str3, "abc")
        self.assertEqual(d1.str6, "ZZZ")
        self.assertEqual(d2.str1, "HELLO")
        self.assertEqual(d2.str2, "WORLD")
        self.assertEqual(d2.str3, "ABC")
        self.assertEqual(d2.str6, "ZZZ")
        self.assertEqual(d3.str1, "foo")
        self.assertEqual(d3.str2, "xyz")
        self.assertEqual(d3.str3, "abc")
        self.assertEqual(d3.str6, "ZZZ")


# TODO final
# TODO @dataclass(freeze=True)
# TODO list, map default factory
