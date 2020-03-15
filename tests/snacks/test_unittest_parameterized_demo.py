from unittest import TestCase
from parameterized import parameterized, parameterized_class, param


# demonstration of wolever/parameterized
# ref: https://github.com/wolever/parameterized
# see-also:
# - http://h-miyako.hatenablog.com/entry/2017/08/16/173000
# - https://qiita.com/nittyan/items/0152a3b93e17c177f5f5


class TestParameterizedExpandDemo(TestCase):
    @parameterized.expand(
        [(1, 2, 3, 6), (10, 20, 30, 60), (4, 5, 6, 15),]
    )
    def test_add_xyz(self, x, y, z, expected):
        self.assertEqual(x + y + z, expected)

    @parameterized.expand(
        [
            param(1, 2, 3, 6),
            param(10, 20, expected=130),
            param(10, 20, 70),
            param(20, 30, z=50),
            param(0, 0),
        ]
    )
    def test_add_xyz_with_param(self, x, y, z=100, expected=100):
        self.assertEqual(x + y + z, expected)


@parameterized_class(
    [
        {"x": 1, "y": 2, "z": 3, "expected": 6},
        {"x": 10, "y": 20, "expected": 330},
        {"expected": 600},
    ]
)
class TestParameterizedClassDemo(TestCase):
    x: int = 100
    y: int = 200
    z: int = 300

    def test_add_xyz(self):
        self.assertEqual(self.x + self.y + self.z, self.expected)
