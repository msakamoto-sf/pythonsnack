def mypkgdemo1_add(n1, n2):
    return n1 + n2


class MyPkgDemo1a:
    def __init__(self, n1):
        self.n1 = n1

    def add(self, n2):
        return self.n1 + n2


class MyPkgDemo1b:
    def __init__(self, n1):
        self.n1 = n1

    def sub(self, n2):
        return self.n1 - n2
