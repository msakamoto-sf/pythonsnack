import unittest

from snacks.mypkgdemo1 import num_op


class TestNumOp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(num_op.add(10, 20), 30)
        self.assertEqual(num_op.add(10, -10), 0)

    def test_sub(self):
        self.assertEqual(num_op.sub(30, 10), 20)
        self.assertEqual(num_op.sub(10, 20), -10)


