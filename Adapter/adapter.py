"""
Adapter establishes the collaboration of objects with incompatible interfaces.
"""


class Target:
    def request(self) -> str:
        return "Default target behavior"

class Adaptee:
    def specificRequest(self) -> str:
        return "Specific behavior of an adaptee"

class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return self.adaptee.specificRequest()



def test_func(obj: Target) -> None:
    print(obj.request())


if __name__ == "__main__":
    target = Target()
    adapted = Adapter(Adaptee())

    test_func(target)
    test_func(adapted)