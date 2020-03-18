import snacks.mypkgdemo1.module1 as module1
from .module1 import module1_add as add1


def module2_add(n1, n2, n3):
    return module1.module1_add(n1, n2, n3) + 1


class ClassInModule2:
    @staticmethod
    def add(n1, n2, n3):
        return add1(n1, n2, n3) + 2
