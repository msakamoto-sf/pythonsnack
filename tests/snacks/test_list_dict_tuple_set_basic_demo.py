from unittest import TestCase

# demonstration of python major data structure (list, dict, tuple, set) basic operations
# ref: https://docs.python.org/ja/3/tutorial/datastructures.html


class TestListDictTupleSetBasicDemo(TestCase):
    def test_list_demo(self):
        # see-also: https://docs.python.org/ja/3/tutorial/introduction.html#lists
        persons = ["alice", "bob", "clark", "daniel", "eva"]
        self.assertEqual(len(persons), 5)
        # normal index access demo
        self.assertEqual(persons[0], "alice")
        self.assertEqual(persons[1], "bob")
        self.assertEqual(persons[-1], "eva")
        self.assertEqual(persons[-2], "daniel")
        # slicing demo
        self.assertEqual(persons[:], ["alice", "bob", "clark", "daniel", "eva"])
        self.assertEqual(persons[2:], ["clark", "daniel", "eva"])
        self.assertEqual(persons[:3], ["alice", "bob", "clark"])
        self.assertEqual(persons[1:3], ["bob", "clark"])
        self.assertEqual(persons[-1:], ["eva"])
        self.assertEqual(persons[-1:-3], [])
        self.assertEqual(persons[:-1], ["alice", "bob", "clark", "daniel"])
        self.assertEqual(persons[-3:-1], ["clark", "daniel"])
        # value assign demo
        persons[3] = "danny"
        self.assertEqual(persons[3], "danny")
        persons[0:3] = ["anny", "bobson", "charly"]
        self.assertEqual(persons, ["anny", "bobson", "charly", "danny", "eva"])
        persons[1:4] = ["bob", "clark", "charly"]
        self.assertEqual(persons, ["anny", "bob", "clark", "charly", "eva"])
        # sclicing clear demo
        persons[:] = []
        self.assertEqual(len(persons), 0)

        # append demo
        persons.append("alice")
        persons.append("bob")
        persons += ["clark", "daniel"]
        persons += ("eve", "fred")
        persons.extend(["geroge", "helen"])
        persons.extend(("iris", "jon"))
        self.assertEqual(
            persons,
            [
                "alice",
                "bob",
                "clark",
                "daniel",
                "eve",
                "fred",
                "geroge",
                "helen",
                "iris",
                "jon",
            ],
        )

        # clear/insert/pop/del demo
        self.assertIsNone(persons.clear())
        self.assertEqual(len(persons), 0)
        self.assertIsNone(persons.insert(0, "eve"))
        self.assertIsNone(persons.insert(0, "bob"))
        self.assertIsNone(persons.insert(1, "clark"))
        self.assertIsNone(persons.insert(2, "daniel"))
        self.assertIsNone(persons.insert(0, "alice"))
        self.assertEqual(persons, ["alice", "bob", "clark", "daniel", "eve"])
        self.assertEqual(persons.pop(), "eve")
        self.assertEqual(persons.pop(), "daniel")
        self.assertEqual(persons.pop(1), "bob")
        del persons[1]
        self.assertEqual(persons, ["alice"])

        # count/index demo
        prices = [100, 200, 300, 150, 300, 150, 150, 90]
        self.assertEqual(prices.count(0), 0)
        self.assertEqual(prices.count(100), 1)
        self.assertEqual(prices.count(300), 2)
        self.assertEqual(prices.count(150), 3)
        self.assertEqual(prices.index(100), 0)
        self.assertEqual(prices.index(200), 1)
        self.assertEqual(prices.index(300), 2)
        self.assertEqual(prices.index(300, prices.index(300) + 1), 4)
        with self.assertRaises(ValueError) as cm:
            prices.index(0)
        self.assertEqual(str(cm.exception), "0 is not in list")
        with self.assertRaises(ValueError) as cm:
            prices.index(100, 999)
        self.assertEqual(str(cm.exception), "100 is not in list")

        # reverse/sort demo
        self.assertIsNone(prices.sort())
        self.assertEqual(prices, [90, 100, 150, 150, 150, 200, 300, 300])
        self.assertIsNone(prices.reverse())
        self.assertEqual(prices, [300, 300, 200, 150, 150, 150, 100, 90])

    def test_dict_demo(self):
        # see-also: https://docs.python.org/ja/3/library/stdtypes.html#mapping-types-dict
        d0 = {"k1": 10, "k2": 20, "k3": 30}
        self.assertEqual(len(d0), 3)
        self.assertEqual(d0["k1"], 10)
        self.assertEqual(d0["k2"], 20)
        self.assertEqual(d0["k3"], 30)
        d1 = dict([("k1", 10), ("k2", 20), ("k3", 30)])
        self.assertEqual(d0, d1)
        d2 = dict(k1=10, k2=20, k3=30)
        self.assertEqual(d0, d2)

        # udpate demo
        # see-also: https://note.nkmk.me/python-dict-add-update/
        d0 = {"k1": 10, "k2": 20}
        d0.update({"k2": 25, "k3": 30})
        self.assertEqual(d0, {"k1": 10, "k2": 25, "k3": 30})
        d0.update(k3=35, k4=40)
        self.assertEqual(d0, {"k1": 10, "k2": 25, "k3": 35, "k4": 40})
        d0.update(**{"k2": 20, "k3": 30}, **{"k4": 45, "k5": 50})
        self.assertEqual(d0, {"k1": 10, "k2": 20, "k3": 30, "k4": 45, "k5": 50})
        d0 = {"k1": 10, "k2": 20}
        d0.update([("k2", 25), ("k3", 30)])
        self.assertEqual(d0, {"k1": 10, "k2": 25, "k3": 30})
        d0 = {}
        d0.update(zip(["k1", "k2", "k3"], [10, 20, 30]))
        self.assertEqual(d0, {"k1": 10, "k2": 20, "k3": 30})

        # del/in/not in demo
        d0 = {"k1": 10, "k2": 20, "k3": 30}
        del d0["k1"]
        self.assertEqual(d0, dict(k2=20, k3=30))
        self.assertFalse("k1" in d0)
        self.assertTrue("k1" not in d0)
        self.assertTrue("k2" in d0)
        self.assertTrue("k3" in d0)
        del d0["k2"], d0["k3"]
        self.assertEqual(len(d0), 0)

        d0 = {"k2": 20, "k3": 30}
        # list/keys/values  demo
        self.assertEqual(list(d0), ["k2", "k3"])
        self.assertNotEqual(type(d0.keys()), list)
        self.assertEqual(list(d0.keys()), ["k2", "k3"])
        self.assertNotEqual(type(d0.values()), list)
        self.assertEqual(list(d0.values()), [20, 30])
        r = []
        for k, v in d0.items():
            r.append("[{}]={}".format(k, v))
        self.assertEqual(r, ["[k2]=20", "[k3]=30"])

        # clear/get/setdefautl  demo
        self.assertIsNone(d0.clear())
        self.assertEqual(len(d0), 0)
        d0 = dict(k1=10, k2=20, k3=30)
        self.assertEqual(d0.get("k1"), 10)
        self.assertIsNone(d0.get("xx"))
        self.assertEqual(d0.get("xx", -1), -1)
        with self.assertRaises(KeyError) as cm:
            d0["xx"]
        self.assertEqual(str(cm.exception), "'xx'")
        d0["k1"] = 90
        d0["k4"] = 40
        self.assertEqual(d0["k1"], 90)
        self.assertEqual(d0["k4"], 40)
        self.assertEqual(d0.setdefault("k1"), 90)
        self.assertEqual(d0["k1"], 90)  # not changed
        self.assertIsNone(d0.setdefault("k5"))
        self.assertTrue("k5" in d0)  # changed
        self.assertIsNone(d0["k5"])  # changed
        self.assertEqual(d0.setdefault("k1", 100), 90)
        self.assertEqual(d0["k1"], 90)  # not changed
        self.assertEqual(d0.setdefault("k6", 110), 110)
        self.assertEqual(d0["k6"], 110)  # changed

        # pop/popitem demo
        d0 = dict(k1=10, k2=20, k3=30)
        self.assertEqual(d0.pop("k1"), 10)
        with self.assertRaises(KeyError) as cm:
            d0.pop("xx")
        self.assertEqual(str(cm.exception), "'xx'")
        self.assertEqual(d0.pop("xx", -1), -1)
        self.assertEqual(d0.popitem(), ("k3", 30))
        self.assertEqual(d0.popitem(), ("k2", 20))
        with self.assertRaises(KeyError) as cm:
            d0.popitem()
        self.assertEqual(str(cm.exception), "'popitem(): dictionary is empty'")

    def test_tuple_demo(self):
        t = 10, 20, 30
        self.assertEqual(t, (10, 20, 30))
        self.assertEqual(len(t), 3)
        self.assertEqual(t[0], 10)
        self.assertEqual(t[1], 20)
        self.assertEqual(t[2], 30)
        x, y, z = t
        self.assertEqual((x, y, z), (10, 20, 30))
        t = (10,)
        self.assertEqual(type(t), tuple)
        self.assertEqual(len(t), 1)
        self.assertEqual(t[0], 10)
        t = (1, 2), (3, 4), (5, 6)
        self.assertEqual(len(t), 3)
        self.assertEqual(t[0], (1, 2))
        self.assertEqual(t[1], (3, 4))
        self.assertEqual(t[2], (5, 6))

        # list to tuple
        # see-also: https://note.nkmk.me/python-list-tuple-convert/
        l0 = [10, 20, 30]
        t = tuple(l0)
        self.assertEqual(type(t), tuple)
        x, y, z = t
        self.assertEqual(len(t), 3)
        self.assertEqual(t[0], 10)
        self.assertEqual(t[1], 20)
        self.assertEqual(t[2], 30)
        l1 = list(t)
        self.assertEqual(type(l1), list)
        self.assertEqual(len(l1), 3)
        self.assertEqual(l1[0], 10)
        self.assertEqual(l1[1], 20)
        self.assertEqual(l1[2], 30)

    def test_set_demo(self):
        # see-also:
        # https://docs.python.org/ja/3/library/stdtypes.html#set

        s0 = set()
        self.assertEqual(type(s0), set)
        self.assertEqual(len(s0), 0)
        self.assertFalse(1 in s0)

        s0 = {}
        self.assertEqual(type(s0), dict)  # oops!!

        s0 = {10, 20, 30}
        self.assertEqual(type(s0), set)
        self.assertEqual(len(s0), 3)
        self.assertFalse(1 in s0)
        self.assertTrue(1 not in s0)
        self.assertTrue(10 in s0)
        self.assertTrue(20 in s0)
        self.assertTrue(30 in s0)

        self.assertIsNone(s0.clear())
        self.assertEqual(len(s0), 0)
        s0 = set("aabbbcccc")
        self.assertEqual(len(s0), 3)
        self.assertEqual(s0, {"a", "b", "c"})

        self.assertIsNone(s0.add("e"))
        self.assertIsNone(s0.add("f"))
        self.assertEqual(s0, {"e", "f", "a", "b", "c"})  # un-ordered

        self.assertIsNone(s0.remove("a"))
        self.assertIsNone(s0.remove("b"))
        self.assertEqual(s0, {"c", "e", "f"})
        with self.assertRaises(KeyError) as cm:
            s0.remove(999)
        self.assertEqual(str(cm.exception), "999")

        self.assertIsNone(s0.discard("c"))
        self.assertIsNone(s0.discard("d"))
        self.assertEqual(s0, {"e", "f"})

        # basic operation (without update)
        s1 = {1, 2, 3}
        s2 = {2, 3, 4}
        self.assertEqual(s1 | s2, {1, 2, 3, 4})  # union
        self.assertEqual(s1 & s2, {2, 3})  # intersection
        self.assertEqual(s1 - s2, {1})  # difference
        self.assertEqual(s1 ^ s2, {1, 4})  # symmetric_difference

        # basic operation (with update)
        s1 |= s2  # union
        self.assertEqual(s1, {1, 2, 3, 4})
        s1 &= {2, 3}  # intersection
        self.assertEqual(s1, {2, 3})
        s1 = {1, 2, 3}
        s1 -= s2  # difference
        self.assertEqual(s1, {1})
        s1 = {1, 2, 3}
        s1 ^= {2, 3, 4}  # symmetric_difference
        self.assertEqual(s1, {1, 4})

        # set to list
        l0 = list(s1)
        self.assertEqual(l0, [1, 4])
        # list to set
        s0 = set([1, 2, 3, 2, 1])
        self.assertEqual(s0, {1, 2, 3})
