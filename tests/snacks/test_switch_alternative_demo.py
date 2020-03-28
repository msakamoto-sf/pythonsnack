from unittest import TestCase

# demonstration of alt-switch techniques
# see-also:
# https://docs.python.org/3/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python
# https://www.python.org/dev/peps/pep-0275/
# https://qiita.com/Go-zen-chu/items/9bc7011616759dd2fc93
# https://qiita.com/hasegit/items/2cf05de74680717f9010
# https://www.lifewithpython.com/2018/08/python-switch-case-statement.html


class TestSwitchAlternativeDemo(TestCase):
    def test_no_switch_use_if_elif_else(self):
        def f1(s0: str) -> str:
            if s0 in ("aa", "bb"):
                return "aa or bb"
            elif s0 in ("cc", "dd"):
                return "cc or dd"
            elif s0 == "ee":
                return "ee"
            else:
                return "xx"

        self.assertEqual(f1("aa"), "aa or bb")
        self.assertEqual(f1("bb"), "aa or bb")
        self.assertEqual(f1("cc"), "cc or dd")
        self.assertEqual(f1("dd"), "cc or dd")
        self.assertEqual(f1("ee"), "ee")
        self.assertEqual(f1("ff"), "xx")

    def test_no_switch_use_function_dispatch_dict(self):
        func_dispatch_dict = {
            "aa": lambda: "aa or bb",
            "bb": lambda: "aa or bb",
            "cc": lambda: "cc or dd",
            "dd": lambda: "cc or dd",
            "ee": lambda: "ee",
        }

        def f1(s0: str) -> str:
            if s0 in func_dispatch_dict:
                return func_dispatch_dict[s0]()
            return "xx"

        self.assertEqual(f1("aa"), "aa or bb")
        self.assertEqual(f1("bb"), "aa or bb")
        self.assertEqual(f1("cc"), "cc or dd")
        self.assertEqual(f1("dd"), "cc or dd")
        self.assertEqual(f1("ee"), "ee")
        self.assertEqual(f1("ff"), "xx")
