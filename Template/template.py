"""
Template Method is a behavioral design pattern where you define a "skeleton" of an algorithm in a parent class
and let the subclasses override some of its steps without changing the structure.
"""



class AbstractClass:
    def templateMethod(self) -> None:
        print("The template method is in action")
        print(self.someOperation())
        print("The subclasses will change some steps")
        print(self.operation())
        print(self.anotherOperation())

    def operation(self) -> None:
        return "Some default operation"

    def someOperation(self) -> None:
        pass

    def anotherOperation(self) -> None:
        pass

class ConcreteClass(AbstractClass):
    def someOperation(self) -> str:
        return "An operation of a Concrete Class"

    def anotherOperation(self) -> str:
        return "Another operation of a Concrete Class"

class AnotherConcreteClass(AbstractClass):
    def someOperation(self) -> str:
        return "An operation of Another Concrete Class"

    def anotherOperation(self) -> str:
        return "Another operation of Another Concrete Class"


if __name__ == "__main__":
    concreteClass = ConcreteClass()
    anotherConcreteClass = AnotherConcreteClass()

    concreteClass.templateMethod()
    anotherConcreteClass.templateMethod()

