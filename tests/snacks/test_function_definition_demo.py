from unittest import TestCase
from typing import List

# demonstration of python function definition
# refs: https://docs.python.org/ja/3/tutorial/controlflow.html#defining-functions


class TestClassInheritanceDemo(TestCase):
    def test_func_def_basic_tutorial(self):
        var1: int = 100

        def f1(a: int, b: int) -> int:
            return var1 + a + b

        def f2(a: List[int], b: int) -> None:
            a.append(b)
            a.append(var1)

        def f3(a: int, b: int) -> int:
            var1 = a + b
            return var1 * 2

        self.assertEqual(f1(10, 20), 130)
        list1 = [1, 2]
        f2(list1, 3)
        self.assertEqual(list1, [1, 2, 3, 100])
        self.assertEqual(f3(30, 40), 140)  # var1 in f3 refers new value
        self.assertEqual(var1, 100)  # var1 in outer scope reference is not changed.

        var1 = 200
        self.assertEqual(f1(10, 20), 230)  # var1 in f1 refers new value:200
        list1 = [2, 3]
        f2(list1, 4)
        self.assertEqual(list1, [2, 3, 4, 200])
        self.assertEqual(f3(40, 50), 180)
        self.assertEqual(var1, 200)

    def test_default_arg_demo(self):
        def f1(a: int, b: int = 10, c: int = 20) -> int:
            return a + b + c

        self.assertEqual(f1(1), 31)
        self.assertEqual(f1(1, 2), 23)
        self.assertEqual(f1(1, 2, 3), 6)

        def f2(a: int, dest: List[int] = []) -> List[int]:
            dest.append(a)
            return dest

        # default argument value is evaluated only once at definition time.
        self.assertEqual(f2(1), [1])
        self.assertEqual(f2(2), [1, 2])
        self.assertEqual(f2(3), [1, 2, 3])

        def f2b(a: int, newlist=lambda: []) -> List[int]:
            dest = newlist()
            dest.append(a)
            return dest

        self.assertEqual(f2b(1), [1])
        self.assertEqual(f2b(2), [2])
        self.assertEqual(f2b(3), [3])
        list1: List[int] = []

        def newlist() -> List[int]:
            return list1

        self.assertEqual(f2b(1, newlist), [1])
        self.assertEqual(f2b(2, newlist), [1, 2])
        self.assertEqual(f2b(3, newlist), [1, 2, 3])

    def test_keyword_arg_demo(self):
        def f1(name, age: int = 0, height: int = 50, weight: int = 3) -> str:
            return "name={}, age={} years, height={}cm, weight={}kg".format(
                name, age, height, weight
            )

        self.assertEqual(
            f1("alice"), "name=alice, age=0 years, height=50cm, weight=3kg"
        )
        self.assertEqual(f1("bob", 1), "name=bob, age=1 years, height=50cm, weight=3kg")
        self.assertEqual(
            f1("clark", height=60, weight=4, age=2),
            "name=clark, age=2 years, height=60cm, weight=4kg",
        )
        self.assertEqual(
            f1("daniel", 3, weight=5),
            "name=daniel, age=3 years, height=50cm, weight=5kg",
        )

        def f2(name: str, **kwargs) -> str:
            r = "name=" + name
            for kw in kwargs:
                r = r + ", " + kw + "=" + str(kwargs[kw])
            return r

        self.assertEqual(
            f2("alice", year=3, height=100), "name=alice, year=3, height=100"
        )
        self.assertEqual(
            f2("bob", year=10, hobbies=["game", "swimming"]),
            "name=bob, year=10, hobbies=['game', 'swimming']",
        )
        with self.assertRaises(TypeError) as cm:
            f2("clark", name="daniel")
        self.assertEqual(
            str(cm.exception), "f2() got multiple values for argument 'name'"
        )

    def test_special_params_demo(self):
        # NOTE: "/" special marker parameter does not work (some flake8/mypy/python error)

        # f1, f2, f3 definition leads E225, "missing whitespace around operator",
        # f2 definition leads flake8 E999 / mypy / Python parser error,
        #                   "Syntax Error: named arguments mut follow bare *"
        # def f1(a: int, b: int, /) -> int:
        #     return a + b

        # def f2(a: int, b: int, /, c: int, d: int, *) -> int:
        #     return a + b + c + d

        # def f3(a: int, b: int, /, c: int, d: int, *, e: int, f: int) -> int:
        #     return a + b + c + d + e + f

        def f4(a: int, b: int, *, c: int, d: int) -> int:
            return a + b + c + d

        self.assertEqual(f4(1, 2, c=3, d=4), 10)
        self.assertEqual(f4(a=1, b=2, c=3, d=4), 10)
        # TypeError: f4() takes 2 positional arguments but 4 were given
        # self.assertEqual(f4(1, 2, 3, 4), 10)

        # flake8 E225, "missing whitespace around operator",
        # def f5(name, /, **kwargs) -> str:
        #     pass

    def test_arg_type_mixin_demo(self):
        # TODO *args, **kwdargs parameter demo
        pass

    def test_arbitrary_arg_list_demo(self):
        # TODO
        pass

    def test_unpack_arg_list_demo(self):
        # TODO
        pass
