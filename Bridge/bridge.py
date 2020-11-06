"""
Bridge divides a class into separate class hierarchies that can be developed independently.
Bridge allows you to change the implementation and the abstraction. Since all implementations will have a common interface, 
they’d be interchangeable inside the abstraction.
"""

class Abstraction:
    def __init__(self, implementation: 'Implementation') -> None:
        self.implementation = implementation

    def operation(self) -> None:
        self.implementation.operationImp()

class Implementation:
    def operationImp(self) -> None:
        pass

class ConcreteImplementation(Implementation):
    def operationImp(self) -> None:
        print("Concrete Implementation")

class AnotherConcreteImplementation(Implementation):
    def operationImp(self) -> None:
        print("Another Concrete Implementation")




if __name__ == "__main__":
    bridge = Abstraction(ConcreteImplementation())
    bridge.operation()
    bridge = Abstraction(AnotherConcreteImplementation())
    bridge.operation()