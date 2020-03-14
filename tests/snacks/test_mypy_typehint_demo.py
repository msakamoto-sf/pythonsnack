import unittest

# demonstration of type hinting


def int_to_str_demo(x: int) -> str:
    return "int to string {}".format(x)


def int_to_str_demo_none(x: int) -> None:
    # mypy error: No return value expected
    # return "int to string {}".format(x)
    pass


class TestMyPyTypehintDemo(unittest.TestCase):
    def test_int_to_str_demo(self):
        result: str = int_to_str_demo(123)
        self.assertEqual(result, "int to string 123")
