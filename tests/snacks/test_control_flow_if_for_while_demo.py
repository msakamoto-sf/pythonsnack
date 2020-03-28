from unittest import TestCase

# demonstration of python major control flow (if, for, while, break, continue, pass)
# ref: https://docs.python.org/ja/3/tutorial/controlflow.html
# ref: https://docs.python.org/ja/3/reference/compound_stmts.html

# see-also:
# https://note.nkmk.me/python-for-usage/


class TestControlFlowIfForDemo(TestCase):
    def test_if_demo(self):
        def ifdemo(a: int) -> str:
            if a < 0:
                return "negative"
            elif a > 0:
                return "positive"
            else:
                return "zero"

        self.assertEqual(ifdemo(1), "positive")
        self.assertEqual(ifdemo(0), "zero")
        self.assertEqual(ifdemo(-1), "negative")

    def test_for_break_continue_demo(self):
        r = []
        for n in [1, 2, 3]:
            r.append(n)

        self.assertEqual(r, [1, 2, 3])

        r = []
        for n in [1, 2, 3, 4, 5, 6]:
            if n > 4:
                break
            r.append(n)

        self.assertEqual(r, [1, 2, 3, 4])

        r = []
        for n in [1, 2, 3, 4, 5, 6]:
            if n % 2 == 0:
                continue
            r.append(n)

        self.assertEqual(r, [1, 3, 5])

    def test_for_with_else_demo(self):
        r = []
        for n in [1, 2, 3]:
            r.append(n)
        else:
            r.append(99)

        self.assertEqual(r, [1, 2, 3, 99])

        r = []
        for n in [1, 2, 3, 4, 5, 6]:
            if n > 4:
                break
            r.append(n)
        else:
            r.append(99)

        # if "break"ed, else-block is ignored.
        self.assertEqual(r, [1, 2, 3, 4])

        r = []
        for n in [1, 2, 3, 4, 5, 6]:
            if n % 2 == 0:
                continue
            r.append(n)
        else:
            r.append(99)

        # if "continue"d, else-block is done.
        self.assertEqual(r, [1, 3, 5, 99])

    def test_nested_for_and_escape_demo(self):
        # see-also: https://note.nkmk.me/python-break-nested-loops/

        # normal nested for-loop demo
        r = []
        for n in [1, 2, 3]:
            r.append(n)
            for m in [4, 5, 6]:
                r.append(m)

        self.assertEqual(r, [1, 4, 5, 6, 2, 4, 5, 6, 3, 4, 5, 6])

        # escaping from nested for-loop demo
        r = []
        for n in [1, 2, 3]:
            r.append(n)
            for m in [4, 5, 6]:
                if m == 5:
                    # (1) jump to (3), escape from nested for-loop
                    break
                r.append(m)
            else:
                # (2) nested for-loop done => continue top level for-loop
                continue
            # (3) : escape from top level for-loop
            break

        self.assertEqual(r, [1, 4])

        # escaping from nested for-loop demo (wrong implemented)
        r = []
        for n in [1, 2, 3]:
            r.append(n)
            for m in [4, 5, 6]:
                if m == 5:
                    # escape from nested for-loop
                    break
                r.append(m)
            # top level for-loop continues...

        self.assertEqual(r, [1, 4, 2, 4, 3, 4])

    def test_for_with_range_demo(self):
        x = range(10)
        self.assertEqual(type(x), range)  # range is NOT list

        r = []
        for n in range(3):
            r.append(n)
        self.assertEqual(r, [0, 1, 2])  # not include 3

        r = []
        for n in range(2, 6):
            r.append(n)
        self.assertEqual(r, [2, 3, 4, 5])  # include start <> NOT include stop

        r = []
        for n in range(0, 10, 3):
            r.append(n)
        self.assertEqual(r, [0, 3, 6, 9])

        r = []
        for n in range(10, 0):
            r.append(n)
        self.assertEqual(r, [])  # if start > stop, return empty range.

        r = []
        for n in range(10, 10):
            r.append(n)
        self.assertEqual(r, [])  # if start == stop, return empty range.

        r = []
        for n in range(10, 0, -3):
            r.append(n)
        self.assertEqual(r, [10, 7, 4, 1])  # start > stop with negative step

    def test_for_with_index_enumerate_demo(self):
        r = []
        for i, s in enumerate(["aa", "bb", "cc"]):
            r.append("[{}]={}".format(i, s))
        self.assertEqual(r, ["[0]=aa", "[1]=bb", "[2]=cc"])

        r = []
        for i, s in enumerate(["aa", "bb", "cc"], 3):
            r.append("[{}]={}".format(i, s))
        self.assertEqual(r, ["[3]=aa", "[4]=bb", "[5]=cc"])

    def test_for_with_zip_demo(self):
        r = []
        for n, m in zip([1, 2, 3], ["aa", "bb", "cc", "dd"]):
            r.append("{}-{}".format(n, m))
        self.assertEqual(r, ["1-aa", "2-bb", "3-cc"])

        r = []
        for i, (n, m) in enumerate(zip([1, 2, 3], ["aa", "bb", "cc", "dd"])):
            r.append("[{}]{}-{}".format(i, n, m))
        self.assertEqual(r, ["[0]1-aa", "[1]2-bb", "[2]3-cc"])

    def test_reversed_for_demo(self):
        r = []
        for n in reversed([1, 2, 3]):
            r.append(n)
        self.assertEqual(r, [3, 2, 1])

        r = []
        for n in reversed(range(3)):
            r.append(n)
        self.assertEqual(r, [2, 1, 0])

        r = []
        for i, s in reversed(list(enumerate(["aa", "bb", "cc"]))):
            r.append("[{}]={}".format(i, s))
        self.assertEqual(r, ["[2]=cc", "[1]=bb", "[0]=aa"])

        r = []
        for i, s in enumerate(reversed(["aa", "bb", "cc"])):
            r.append("[{}]={}".format(i, s))
        self.assertEqual(r, ["[0]=cc", "[1]=bb", "[2]=aa"])

        r = []
        for n, m in reversed(list(zip([1, 2, 3], ["aa", "bb", "cc", "dd"]))):
            r.append("{}-{}".format(n, m))
        self.assertEqual(r, ["3-cc", "2-bb", "1-aa"])

    def test_dict_for_demo(self):
        d = {
            "k1": 100,
            "k2": 200,
            "k3": 300,
        }

        r = []
        for k in d:
            r.append(k)
        self.assertEqual(r, ["k1", "k2", "k3"])

        r = []
        for k in d.values():
            r.append(k)
        self.assertEqual(r, [100, 200, 300])

        r = []
        for k, v in d.items():
            r.append("[{}]={}".format(k, v))
        self.assertEqual(r, ["[k1]=100", "[k2]=200", "[k3]=300"])

    def test_while_break_else_demo(self):
        i = 0
        r = []
        while i < 5:
            r.append(i)
            i += 1
        self.assertEqual(r, [0, 1, 2, 3, 4])

        i = 0
        r = []
        while i < 5:
            r.append(i)
            i += 1
        else:
            r.append(99)
        self.assertEqual(r, [0, 1, 2, 3, 4, 99])

        i = 1
        r = []
        while i < 5:
            if i % 3 == 0:
                break
            r.append(i)
            i += 1
        else:
            r.apend(99)
        self.assertEqual(r, [1, 2])  # while-break ignore else block

    def test_pass_demo(self):
        r = []
        for i in range(10):
            x = i
            if i % 2 == 0:
                pass
            else:
                x *= 10
            r.append(x)
        self.assertEqual(r, [0, 10, 2, 30, 4, 50, 6, 70, 8, 90])
