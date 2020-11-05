"""
Description:
Adapter is a structural design pattern which establishes the collaboration of objects with incompatible interfaces.
"""


class Target:
    def request(self):
        return "Default target behavior"

class Adaptee:
    def specificRequest(self):
        return "Specific behavior of an adaptee"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specificRequest()



def test_func(obj):
    print(obj.request())


if __name__ == "__main__":
    target = Target()
    adapted = Adapter(Adaptee())

    test_func(target)
    test_func(adapted)