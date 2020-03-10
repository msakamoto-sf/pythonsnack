import unittest
from dataclasses import dataclass, field
from typing import List, Dict

# demonstration of typing module.


# https://docs.python.org/ja/3/library/dataclasses.html
@dataclass
class MyTypeDemos:
    str1: str = 'hello typing module'
    int1: int = 100

    # see: https://stackoverflow.com/questions/53632152/why-cant-dataclasses-have-mutable-defaults-in-their-class-attributes-declaratio
    # see: https://stackoverflow.com/questions/52063759/passing-default-list-argument-to-dataclasses
    strings: List[str] = field(default_factory=lambda: ['aaa', 'bbb', 'ccc'])
    ints: List[int] = field(default_factory=lambda: [10, 20, 30])
    str2int: Dict[str, int] = field(default_factory=lambda: {
        'aaa': 10,
        'bbb': 20,
        'ccc': 30,
    })
    str2strings: Dict[str, List[str]] = field(default_factory=lambda: {
        'aaa': ['AA', 'BB', 'CC', ],
        'bbb': ['DD', 'EE', ],
        'ccc': [],
    })

# TODO more and more typing combination demo


class TestTypingDemo(unittest.TestCase):

    def test_my_type_demo(self):
        a = MyTypeDemos()
        self.assertEqual(a.str1, 'hello typing module')
        self.assertEqual(a.int1, 100)
        self.assertListEqual(a.strings, ['aaa', 'bbb', 'ccc'])
        self.assertListEqual(a.ints, [10, 20, 30])
        self.assertDictEqual(a.str2int, {
            'aaa': 10,
            'bbb': 20,
            'ccc': 30,
        })
        # dict.keys() はsetではなく(py3)、listそのものでもないため、厳密にlistで扱うにはlist()でラップする。
        # see: https://stackoverflow.com/questions/13886129/why-does-pythons-dict-keys-return-a-list-and-not-a-set
        # see: https://stackoverflow.com/questions/28310338/using-set-on-dictionary-keys
        # see: https://www.javadrive.jp/python/dictionary/index8.html
        self.assertListEqual(list(a.str2strings.keys()), ['aaa', 'bbb', 'ccc'])
        self.assertListEqual(a.str2strings['aaa'], ['AA', 'BB', 'CC', ])
        self.assertListEqual(a.str2strings['bbb'], ['DD', 'EE', ])
        self.assertListEqual(a.str2strings['ccc'], [])
