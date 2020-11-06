"""
Description:
Bridge is a structural design pattern that divides a class into separate class hierarchies that can be developed independently.
Bridge allows you to change the implementation and the abstraction. Since all implementations will have a common interface, they’d be interchangeable inside the abstraction.
"""

class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        self.implementation.operationImp()

class Implementation:
    def operationImp(self):
        pass

class ConcreteImplementation(Implementation):
    def operationImp(self):
        print("Concrete Implementation")

class AnotherConcreteImplementation(Implementation):
    def operationImp(self):
        print("Another Concrete Implementation")




if __name__ == "__main__":
    bridge = Abstraction(ConcreteImplementation())
    bridge.operation()
    bridge = Abstraction(AnotherConcreteImplementation())
    bridge.operation()