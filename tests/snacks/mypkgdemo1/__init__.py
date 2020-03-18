def mypkgdemo1_sub(n1, n2):
    return n1 - n2


class MyPkgDemo1c:
    def __init__(self, n1):
        self.n1 = n1

    def mul(self, n2):
        return self.n1 * n2


class MyPkgDemo1d:
    def __init__(self, n1):
        self.n1 = n1

    def div(self, n2):
        return self.n1 / n2
