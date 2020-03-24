from unittest import TestCase
from abc import ABC, abstractmethod

# demonstration of Abstract Base Class (abc) @abstractmethod
# refs:
# https://docs.python.org/ja/3/library/abc.html
# see-also:
# https://qiita.com/kaneshin/items/269bc5f156d86f8a91c4


class TestAbstractBaseClassDemo(TestCase):
    def test_abc_method_templating_demo(self):
        class C1(ABC):
            def __init__(self, attr1: str):
                self.attr1 = attr1

            def call_abstract_method(self, s1: str) -> str:
                return "hello," + self.my_abstract_method(s1) + ":" + self.attr1

            @abstractmethod
            def my_abstract_method(self, s1: str) -> str:
                pass

        class C2a(C1):
            def __init__(self, attr1: str):
                super().__init__(attr1)

            def my_abstract_method(self, s1: str) -> str:
                return "alice/" + s1

        class C2b(C1):
            def __init__(self, attr1: str):
                super().__init__(attr1)

            def my_abstract_method(self, s1: str) -> str:
                return "bob/" + s1

        o2a = C2a("abc")
        self.assertEqual(o2a.call_abstract_method("foo"), "hello,alice/foo:abc")
        o2b = C2b("def")
        self.assertEqual(o2b.call_abstract_method("bar"), "hello,bob/bar:def")

    def test_abc_classmethod_demo(self):
        class C1(ABC):
            attr1: str = "ABC"

            @classmethod
            def call_abstract_classmethod(cls, s1: str) -> str:
                return "hello," + cls.my_abstract_classmethod(s1) + ":" + cls.attr1

            @classmethod
            @abstractmethod
            def my_abstract_classmethod(cls, s1: str) -> str:
                pass

        class C2a(C1):
            @classmethod
            def my_abstract_classmethod(cls, s1: str) -> str:
                return "alice/" + s1

        class C2b(C1):
            @classmethod
            def my_abstract_classmethod(cls, s1: str) -> str:
                return "bob/" + s1

        self.assertEqual(C2a.call_abstract_classmethod("foo"), "hello,alice/foo:ABC")
        self.assertEqual(C2b.call_abstract_classmethod("bar"), "hello,bob/bar:ABC")
