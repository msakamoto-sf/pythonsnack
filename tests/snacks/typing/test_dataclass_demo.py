from unittest import TestCase
from dataclasses import dataclass, field, FrozenInstanceError
from typing import List, Dict, Tuple, ClassVar

# demonstration of dataclass
# ref : https://docs.python.org/ja/3/library/dataclasses.html
# ref : https://docs.python.org/ja/3/library/typing.html

# 全体通して、Pythonのクラス変数とインスタンス変数の扱いの違いに注意
# ref: https://docs.python.org/ja/3/tutorial/classes.html
# see: https://uxmilk.jp/41600
# see: https://qiita.com/kxphotographer/items/60588b7c747094eba9f1


class MyNoData1:
    # 型ヒントだけの場合、クラス変数として初期化されない
    # see: https://www.python.org/dev/peps/pep-0526/#class-and-instance-variable-annotations
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
    # see: https://www.python.org/dev/peps/pep-0526/#class-and-instance-variable-annotations
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
    # see: https://www.python.org/dev/peps/pep-0526/#class-and-instance-variable-annotations
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
    # see: https://www.python.org/dev/peps/pep-0526/#class-and-instance-variable-annotations
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


@dataclass(frozen=True)
class MyData5:
    str1: str
    int1: int


class TestMyData5(TestCase):
    def test_do(self):
        d1: MyData5 = MyData5("hello", 100)
        self.assertEqual(d1.str1, "hello")
        self.assertEqual(d1.int1, 100)
        with self.assertRaises(FrozenInstanceError) as cm:
            d1.str1 = "aaa"
        self.assertEqual(cm.exception.args[0], "cannot assign to field 'str1'")
        with self.assertRaises(FrozenInstanceError) as cm:
            d1.int1 = 200
        self.assertEqual(cm.exception.args[0], "cannot assign to field 'int1'")


@dataclass
class MyData6:
    strings1: List[str]
    dict1: Dict[str, str]
    tuple1: Tuple[str, int]


class TestMyData6(TestCase):
    def test_do(self):
        d1: MyData6 = MyData6(["abc", "def"], {"k1": "v1"}, ("xx", 100))
        self.assertListEqual(d1.strings1, ["abc", "def"])
        self.assertEqual(len(d1.dict1), 1)
        self.assertEqual(d1.dict1["k1"], "v1")
        self.assertEqual(d1.tuple1, ("xx", 100))

        d2: MyData6 = MyData6(
            strings1=["ABC", "DEF"], dict1={"k2": "v2"}, tuple1=("zz", 200)
        )
        self.assertListEqual(d2.strings1, ["ABC", "DEF"])
        self.assertEqual(len(d2.dict1), 1)
        self.assertEqual(d2.dict1["k2"], "v2")
        self.assertEqual(d2.tuple1, ("zz", 200))

        # 型ヒントしか無いためクラス変数としては参照できない。
        with self.assertRaises(AttributeError) as cm:
            MyData6.strings1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData6' has no attribute 'strings1'"
        )
        with self.assertRaises(AttributeError) as cm:
            MyData6.dict1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData6' has no attribute 'dict1'"
        )
        with self.assertRaises(AttributeError) as cm:
            MyData6.tuple1
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData6' has no attribute 'tuple1'"
        )

        # 参照できなくても、任意のクラス変数として後から設定することはできる。
        MyData6.strings1 = ["aa", "bb"]
        MyData6.dict1 = {"kx": "vx"}
        MyData6.tuple1 = ("XX", 300)
        # ただし @dataclass が生成した __init__ には反映されない。
        with self.assertRaises(TypeError) as cm:
            MyData6()
        self.assertEqual(
            cm.exception.args[0],
            "__init__() missing 3 required positional arguments: 'strings1', 'dict1', and 'tuple1'",
        )


@dataclass
class MyData7:
    # see: https://stackoverflow.com/questions/53632152/why-cant-dataclasses-have-mutable-defaults-in-their-class-attributes-declaratio # noqa: E501
    # see: https://stackoverflow.com/questions/52063759/passing-default-list-argument-to-dataclasses # noqa: E501
    # ValueError: mutable default <class 'list'> for field strings1 is not allowed: use default_factory
    # strings1: List[str] = field(default=["aa", "bb"])
    strings2: List[str] = field(default_factory=lambda: ["aa", "bb"])
    # ValueError: mutable default <class 'dict'> for field dict1 is not allowed: use default_factory
    # dict1: Dict[str, str] = field(default={"k1": "v1", "k2": "v2"})
    dict2: Dict[str, str] = field(default_factory=lambda: {"k1": "v1", "k2": "v2"})
    tuple1: Tuple[str, int] = field(default=("xx", 100))
    tuple2: Tuple[str, int] = field(default_factory=lambda: ("zz", 200))


class TestMyData7(TestCase):
    def test_do(self):
        d1: MyData7 = MyData7()
        self.assertListEqual(d1.strings2, ["aa", "bb"])
        self.assertEqual(len(d1.dict2), 2)
        self.assertEqual(d1.dict2["k1"], "v1")
        self.assertEqual(d1.dict2["k2"], "v2")
        self.assertEqual(d1.tuple1, ("xx", 100))
        self.assertEqual(d1.tuple2, ("zz", 200))

        d2: MyData7 = MyData7(
            strings2=["AA", "BB"],
            dict2={"k3": "v3"},
            tuple1=("xx", 100),
            tuple2=("zz", 200),
        )
        self.assertListEqual(d2.strings2, ["AA", "BB"])
        self.assertEqual(len(d2.dict2), 1)
        self.assertEqual(d2.dict2["k3"], "v3")
        self.assertEqual(d2.tuple1, ("xx", 100))
        self.assertEqual(d2.tuple2, ("zz", 200))

        # default_factory で生成したdictについては、別インスタンスとなる。
        self.assertIsNot(d1.strings2, d2.strings2)
        self.assertIsNot(d1.dict2, d2.dict2)
        # tuple については tuple の性質上、default でも default_factory でも同じインスタンスと判定される。
        self.assertIs(d1.tuple1, d2.tuple1)
        self.assertIs(d1.tuple2, d2.tuple2)

        # default_factory を指定した場合、クラス変数としては初期値が無いため、クラス変数としては参照できない。
        with self.assertRaises(AttributeError) as cm:
            MyData7.strings2
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData7' has no attribute 'strings2'"
        )
        with self.assertRaises(AttributeError) as cm:
            MyData7.dict2
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData7' has no attribute 'dict2'"
        )
        with self.assertRaises(AttributeError) as cm:
            MyData7.tuple2
        self.assertEqual(
            cm.exception.args[0], "type object 'MyData7' has no attribute 'tuple2'"
        )

        # tuple1 については default 指定があるため、クラス変数として参照できる。
        self.assertEqual(MyData7.tuple1, ("xx", 100))

        # 参照できなくても、任意のクラス変数として後から設定することはできる。
        MyData7.strings = ["ab", "cd"]
        MyData7.dict2 = {"k4": "v4"}
        MyData7.tuple1 = ("AA", 12)
        MyData7.tuple2 = ("BB", 34)
        # ただし @dataclass が生成した __init__ でのデフォルト値には反映されない。
        d3: MyData7 = MyData7()
        self.assertListEqual(d3.strings2, ["aa", "bb"])
        self.assertEqual(len(d3.dict2), 2)
        self.assertEqual(d3.dict2["k1"], "v1")
        self.assertEqual(d3.dict2["k2"], "v2")
        self.assertEqual(d3.tuple1, ("xx", 100))
        self.assertEqual(d3.tuple2, ("zz", 200))
