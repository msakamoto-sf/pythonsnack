# -*- coding: utf_8 -*-
# ^^^^^^^^^^^^^^^^^^^^^^ see: https://qiita.com/KEINOS/items/6efc1147b917d7811b5b
# see-also: https://pep8-ja.readthedocs.io/ja/latest/#id12
from unittest import TestCase
import decimal

# demonstration of python string usage
# refs:
# https://docs.python.org/ja/3/library/stdtypes.html#textseq
# https://docs.python.org/ja/3/library/string.html
# https://docs.python.org/ja/3/reference/lexical_analysis.html#strings


class TestStringDemo(TestCase):
    def test_string_lietral_byte_array_conversion_unicode_demo(self):
        # ref: https://docs.python.org/ja/3/reference/lexical_analysis.html#string-and-bytes-literals
        # ref: https://docs.python.org/ja/3/howto/unicode.html
        # ref: https://docs.python.org/ja/3/library/codecs.html#standard-encodings
        self.assertEqual("\x61\x62\x63", "abc")
        # unicode codepoint
        self.assertEqual(chr(26085) + chr(26412) + chr(35486), "日本語")
        # unicode escape
        self.assertEqual("\u65E5\u672C\u8a9e", "日本語")
        # raw escape
        self.assertEqual(r"abc\ndef\ghi", "abc\\ndef\\ghi")

        self.assertEqual("abc".encode("latin_1"), b"\x61\x62\x63")
        self.assertEqual("abcd".encode("latin_1"), b"\x61\x62" + b"\x63\x64")
        self.assertEqual("abc\r\ndef".encode("latin_1"), b"\x61\x62\x63\r\ndef")
        self.assertEqual(
            "\u65E5本語".encode("utf_8"), b"\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e"
        )
        self.assertEqual(b"\x61\x62\x63".decode("utf_8"), "abc")
        self.assertEqual(b"\x61\x62\x63\r\ndef".decode("latin_1"), "abc\r\ndef")
        self.assertEqual(
            b"\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e".decode("utf_8"), "\u65E5本語"
        )

        # int <> byte array conversion demo
        self.assertEqual((0).to_bytes(1, "big"), b"\x00")
        self.assertEqual((0xFF).to_bytes(1, "big"), b"\xff")
        self.assertEqual(int.from_bytes(b"\x00", "big"), 0)
        self.assertEqual(int.from_bytes(b"\xFF", "big"), 255)

        # 0x00 - 0xFF latin-1 conversion demo
        b00_to_ff = (
            b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
            + b"\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
            + b"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f"
            + b"\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f"
            + b"\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f"
            + b"\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
            + b"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f"
            + b"\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
            + b"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f"
            + b"\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
            + b"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf"
            + b"\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
            + b"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf"
            + b"\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
            + b"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef"
            + b"\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
        )
        i00_to_ff = list(b00_to_ff)
        for i in range(256):
            self.assertEqual(b00_to_ff[i], i)  # byte_array[i] return integer
            self.assertEqual(i00_to_ff[i], i)
        s1 = b00_to_ff.decode("latin_1")
        # "latin_1" codec save 0x00 - 0xFF
        self.assertEqual(s1.encode("latin_1"), b00_to_ff)

    def test_concat_demo(self):
        s1 = "aaa" "bbb"
        self.assertEqual(s1, "aaabbb")

    def test_here_doc(self):
        s1 = """
aaa
"bbb"
'ccc'
"""
        self.assertEqual(s1, "\naaa\n\"bbb\"\n'ccc'\n")
        s1 = """\
aaa
"bbb"
'ccc'"""
        self.assertEqual(s1, "aaa\n\"bbb\"\n'ccc'")
        s1 = """\
aaa
"bbb"
'ccc'\
"""
        self.assertEqual(s1, "aaa\n\"bbb\"\n'ccc'")
        s1 = """
aaa
"bbb"
'ccc'
""".strip()
        self.assertEqual(s1, "aaa\n\"bbb\"\n'ccc'")

    def test_split_join(self):
        self.assertEqual(",".join(["aa", "bb", "cc"]), "aa,bb,cc")
        self.assertEqual("a b  c".split(), ["a", "b", "c"])
        self.assertEqual("a b  c".split(" "), ["a", "b", "", "c"])
        self.assertEqual("a,b,,c,".split(","), ["a", "b", "", "c", ""])
        self.assertEqual("a,b,,c,".split(",", 2), ["a", "b", ",c,"])
        self.assertEqual(
            "aa\nbb\rcc\r\ndd\vee\x0bff\fgg\x0chh".splitlines(),
            ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh"],
        )

    def test_format(self):
        # refs: https://docs.python.org/ja/3/library/string.html#format-string-syntax
        # see-also:
        # https://gammasoft.jp/blog/python-string-format/
        # https://qiita.com/Morio/items/b79ead5f881e6551d9e1
        self.assertEqual("{},{},{}".format(1, 2, 3), "1,2,3")
        self.assertEqual("{2},{0},{1}".format(1, 2, 3), "3,1,2")
        self.assertEqual("{n1},{n2},{n3}".format(n1=1, n3=3, n2=2), "1,2,3")
        self.assertEqual(
            "{0},{1[0]},{1[1]},{l1[0]},{l1[1]}".format(1, [2, 3], l1=[4, 5]),
            "1,2,3,4,5",
        )
        self.assertEqual("{0:<5},{0:>5},{0:^5}".format("aaa"), "aaa  ,  aaa, aaa ")
        self.assertEqual("{0:@<5},{0:@>5},{0:@^5}".format("aaa"), "aaa@@,@@aaa,@aaa@")

        self.assertEqual(
            "{0:b},{0:d},{0:o},{0:x},{0:X},{0:#x},{0:#X}".format(45),
            "101101,45,55,2d,2D,0x2d,0X2D",
        )
        self.assertEqual(
            "{0:>8b},{0:0>8b},{0:0>5d}".format(45), "  101101,00101101,00045"
        )
        self.assertEqual(
            "{0:>8b},{0:0>8b},{0:0>5d}".format(45), "  101101,00101101,00045"
        )
        self.assertEqual(
            "{:+,.2f},{:+,.2f}".format(1234.567, -1234.567), "+1,234.57,-1,234.57"
        )

    def test_f_string(self):
        # refs: https://docs.python.org/ja/3/reference/lexical_analysis.html#f-strings
        # see-also: https://qiita.com/shirakiya/items/2767b30fd4f9c05d930b
        name = "Alice"
        self.assertEqual(f"name={name}", "name=Alice")
        width = 10
        precision = 4
        v = decimal.Decimal("12.34567")
        self.assertEqual(f"result: {v:{width}.{precision}}", "result:      12.35")
        n = 1024
        self.assertEqual(f"{n:#0x}", "0x400")
        # self.assertEqual(f"newline: {ord('\n')}", "newline: 10")
        newline = ord("\n")
        self.assertEqual(f"newline: {newline}", "newline: 10")
