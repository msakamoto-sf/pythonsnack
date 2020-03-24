from unittest import TestCase
from functools import singledispatch, singledispatchmethod

# demonstration of python method overloading... NO, "single dispatch" (one kind of "generic function") demo
# refs:
# https://www.python.org/dev/peps/pep-0443/
# https://docs.python.org/ja/3/glossary.html#term-single-dispatch
# https://docs.python.org/ja/3/glossary.html#term-generic-function
# https://docs.python.org/ja/3/library/functools.html#functools.singledispatch
# https://docs.python.org/ja/3/library/functools.html#functools.singledispatchmethod


@singledispatch
def dispatch_func_demo(dispatch_arg) -> str:
    return "unsupported type:" + str(dispatch_arg)


@dispatch_func_demo.register
def dispatch_func_demo_str(dispatch_arg: str) -> str:
    return "string:" + dispatch_arg


@dispatch_func_demo.register
def dispatch_func_demo_int(dispatch_arg: int) -> str:
    return "int:" + str(dispatch_arg)


class TestMethodOverloadDemo(TestCase):
    def test_single_dispatch_func_demo(self):
        self.assertEqual(dispatch_func_demo("hello"), "string:hello")
        self.assertEqual(dispatch_func_demo(100), "int:100")
        self.assertEqual(
            dispatch_func_demo([10, 20, 30]), "unsupported type:[10, 20, 30]"
        )

    def test_single_dispatch_for_instance_method(self):
        # see-also:
        # https://stackoverflow.com/questions/24601722/how-can-i-use-functools-singledispatch-with-instance-methods
        class C1:
            def __init__(self, attr1: str):
                self.attr1 = attr1
                dispatch_demo = (
                    lambda dispatch_arg: "unsupported type:"
                    + str(dispatch_arg)
                    + ":"
                    + self.attr1
                )

                # mypy error: Cannot determine type of 'dispatch_demo'
                # self.dispatch_demo = singledispatch(self.dispatch_demo)
                self.dispatch_demo = singledispatch(dispatch_demo)
                self.dispatch_demo.register(str, self._dispatch_demo_str)
                self.dispatch_demo.register(int, self._dispatch_demo_int)

            # mypy error: Cannot determine type of 'dispatch_demo'
            # def dispatch_demo(self, dispatch_arg) -> str:
            #     return "unsupported type:" + type(dispatch_arg) + ":" + self.attr1

            def _dispatch_demo_str(self, dispatch_arg: str) -> str:
                return "string:" + dispatch_arg + ":" + self.attr1

            def _dispatch_demo_int(self, dispatch_arg: int) -> str:
                return "int:" + str(dispatch_arg) + ":" + self.attr1

        o1 = C1("hello")
        self.assertEqual(o1.dispatch_demo("aaa"), "string:aaa:hello")
        self.assertEqual(o1.dispatch_demo(100), "int:100:hello")
        self.assertEqual(o1.dispatch_demo([1, 2]), "unsupported type:[1, 2]:hello")

    def test_single_dispatch_method_demo(self):
        # see-also:
        # https://docs.python.org/ja/3/library/functools.html#functools.singledispatchmethod
        # https://stackoverflow.com/questions/24601722/how-can-i-use-functools-singledispatch-with-instance-methods
        class C1:
            f1: int = 100

            def __init__(self, attr1: int):
                self.attr1 = attr1

            @singledispatchmethod
            def add(self, arg1) -> str:
                return "unsupported type:" + str(arg1) + ":" + str(self.attr1)

            @add.register
            def _add_str(self, arg1: str) -> str:
                return arg1 + str(self.attr1)

            @add.register
            def _add_int(self, arg1: int) -> str:
                return str(arg1 + self.attr1)

            # do not work, see: https://bugs.python.org/issue39679
            """
            @singledispatchmethod
            @classmethod
            def bigger(cls, arg1) -> str:
                return "unsupported type:" + str(arg1) + ":" + str(cls.f1)

            @bigger.register
            @classmethod
            def _bigger_str(cls, arg1: str) -> str:
                return (arg1 + str(cls.f1)).upper()

            @bigger.register
            @classmethod
            def _bigger_int(cls, arg1: int) -> str:
                return str(arg1 + cls.f1)
            """

        o1 = C1(10)
        self.assertEqual(o1.add("hello"), "hello10")
        self.assertEqual(o1.add(20), "30")
        self.assertEqual(o1.add([1, 2]), "unsupported type:[1, 2]:10")
