"""
Facade provides a unified interface to a group of interfaces. It simplifies the iteraction with a complex system of classes.
"""


class Facade:
    def __init__(self) -> None:
        # The instances can be passed to a constructor 
        self.someClass = SomeClass()
        self.anotherClass = AnotherClass()
        self.oneMoreClass = OneMoreClass()

    def execute(self) -> None:
        self.someClass.someOperation()
        self.anotherClass.anotherOperation()
        self.oneMoreClass.oneMoreOperation()

class SomeClass:
    def someOperation(self) -> None:
        print("Operation of Some Class")

class AnotherClass:
    def anotherOperation(self) -> None:
        print("Operation of Another Class")

class OneMoreClass:
    def oneMoreOperation(self) -> None:
        print("OneMoreClass operation")

if __name__ == "__main__":
    facade = Facade()
    facade.execute()