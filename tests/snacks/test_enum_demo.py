from unittest import TestCase
from enum import Enum, unique, auto

# demonstration of enum (from 3.4)
# ref: https://docs.python.org/ja/3/library/enum.html
# see-also:
# - https://qiita.com/macinjoke/items/13aa9ba64cf9b688e74a
# - https://nansystem.com/python-enum-definition-and-convert-from-string-and-get-list/


class Animals(Enum):
    CAT = 1
    DOG = 2
    BIRD = 3
    FISH = 5
    TURTLE = 10
    SNAKE = 4


class TestEnumOfAnimals(TestCase):
    def test_do(self):
        self.assertEqual(str(Animals.CAT), "Animals.CAT")
        self.assertIsInstance(Animals.CAT, Animals)
        self.assertEqual(Animals.CAT.name, "CAT")
        self.assertEqual(Animals.CAT.value, 1)
        self.assertEqual(Animals.TURTLE.value, 10)

        animals1 = []
        for animal in Animals:
            animals1.append(animal)
        self.assertEqual(
            animals1,
            [
                Animals.CAT,
                Animals.DOG,
                Animals.BIRD,
                Animals.FISH,
                Animals.TURTLE,
                Animals.SNAKE,
            ],
        )

        animals2 = set([Animals.CAT, Animals.DOG])
        self.assertEqual(animals2, set([Animals.DOG, Animals.CAT]))

        animal1 = Animals(4)
        self.assertEqual(animal1, Animals.SNAKE)
        self.assertIs(animal1, Animals.SNAKE)

        animal2 = Animals["FISH"]
        self.assertEqual(animal2, Animals.FISH)
        self.assertIs(animal2, Animals.FISH)

        with self.assertRaises(ValueError) as cm1:
            Animals(999)
        self.assertEqual(str(cm1.exception), "999 is not a valid Animals")

        with self.assertRaises(KeyError) as cm2:
            Animals["ABC"]
        self.assertEqual(str(cm2.exception), "'ABC'")


class TestAdvancedUsageDemo(TestCase):
    def test_key_reuse_error(self):
        with self.assertRaises(TypeError) as cm:

            class DuplicateNameEnum(Enum):
                FOO = 1
                FOO = 2

        self.assertEqual(str(cm.exception), "Attempted to reuse key: 'FOO'")

    def test_value_reuse_work(self):
        class DuplicateValueEnum(Enum):
            FOO = 1
            BAR = 2
            BAZ = 2

        self.assertEqual(DuplicateValueEnum.FOO.value, 1)
        self.assertEqual(DuplicateValueEnum.BAR.value, 2)
        self.assertEqual(DuplicateValueEnum.BAZ.value, 2)

        e1 = DuplicateValueEnum(2)
        self.assertEqual(e1, DuplicateValueEnum.BAR)
        self.assertEqual(e1, DuplicateValueEnum.BAZ)
        self.assertEqual(DuplicateValueEnum.BAR, DuplicateValueEnum.BAZ)
        # wow!!
        self.assertIs(DuplicateValueEnum.BAR, DuplicateValueEnum.BAZ)

    def test_unique_value_reuse_error(self):
        with self.assertRaises(ValueError) as cm:

            @unique
            class DuplicateValueEnum2(Enum):
                XX = 1
                YY = 1

        self.assertEqual(
            str(cm.exception),
            "duplicate values found in <enum 'DuplicateValueEnum2'>: YY -> XX",
        )

    def test_auto_value_numbering(self):
        class AutoNumber(Enum):
            ONE = auto()
            TWO = auto()
            THREE = auto()

        self.assertEqual(AutoNumber.ONE.value, 1)
        self.assertEqual(AutoNumber.TWO.value, 2)
        self.assertEqual(AutoNumber.THREE.value, 3)

    def test_named_value(self):
        class NamedValueEnum(Enum):
            def _generate_next_value_(name, start, count, last_values):
                # return name itself as value
                return name

        class News(NamedValueEnum):
            NORTH = auto()
            SOUTH = auto()
            EAST = auto()
            WEST = auto()

        self.assertEqual(News.NORTH.value, "NORTH")
        self.assertEqual(News.SOUTH.value, "SOUTH")
        self.assertEqual(News.EAST.value, "EAST")
        self.assertEqual(News.WEST.value, "WEST")

    def test_enum_iteration(self):
        class Shape(Enum):
            SQUARE = auto()
            CIRCLE = auto()
            TRIANGLE = auto()

        self.assertEqual(list(Shape), [Shape.SQUARE, Shape.CIRCLE, Shape.TRIANGLE,])
        members = {}
        for name, member in Shape.__members__.items():
            members[name] = member.value
        self.assertEqual(members, {"SQUARE": 1, "CIRCLE": 2, "TRIANGLE": 3,})

    def test_custom_init_attr_method(self):
        class StringRepeater(Enum):
            ONE_DOT = (1, ",")
            TWO_COLON = (2, ":")
            THREE_DASH = (3, "-")

            def __init__(self, count: int, joiner: str):
                self.count = count
                self.joiner = joiner

            def repeat(self, target: str) -> str:
                strings = []
                for i in range(self.count):
                    strings.append(target)
                return self.joiner.join(strings)

        self.assertEqual(StringRepeater.ONE_DOT.repeat("hello"), "hello")
        self.assertEqual(StringRepeater.TWO_COLON.repeat("abc"), "abc:abc")
        self.assertEqual(StringRepeater.THREE_DASH.repeat("def"), "def-def-def")

    def test_custom_new_method(self):
        class StringRepeater2(Enum):
            count: int
            joiner: str

            ONE_DOT = (1, ",")
            TWO_COLON = (2, ":")
            THREE_DASH = (3, "-")

            def __new__(cls, count: int, joiner: str):
                obj = object.__new__(cls)
                obj._value_ = count
                obj.count = count
                obj.joiner = joiner
                return obj

            def repeat(self, target: str) -> str:
                strings = []
                for i in range(self.count):
                    strings.append(target)
                return self.joiner.join(strings)

        self.assertEqual(StringRepeater2.ONE_DOT.repeat("hello"), "hello")
        self.assertEqual(StringRepeater2.TWO_COLON.repeat("abc"), "abc:abc")
        self.assertEqual(StringRepeater2.THREE_DASH.repeat("def"), "def-def-def")

        e1 = StringRepeater2(1)
        self.assertEqual(e1.repeat("hello"), "hello")
        self.assertIs(e1, StringRepeater2.ONE_DOT)
        e2 = StringRepeater2["TWO_COLON"]
        self.assertEqual(e2.repeat("abc"), "abc:abc")
        self.assertIs(e2, StringRepeater2.TWO_COLON)
