"""
Decorator is used to dynamically add some new behavior to a component. 
The pattern is a flexible alternative to inheritance when you need to extend functionality of a class
cause it doesn't affect the class' implementation or any other classes or subclasses.
"""


class Component: 
    def method1(self) -> str:
        return "Default implementation of method1"
    
    def method2(self) -> str:
        return "Default implementation of method2"

class ConcreteComponent(Component):
    def method1(self) -> str:
        return "Overwritten implementation of method1"


class Decorator(Component):
    def __init__(self, wrappedObj: Component) -> None:
        self.wrappedObj = wrappedObj

class ConcreteDecorator(Decorator):
    def method1(self) -> str:
        return f"{self.wrappedObj.method1()} + ConcreteDecorator"

    def method2(self) -> str:
        return f"{self.wrappedObj.method2()} + ConcreteDecorator"

class AnotherConcreteDecorator(Decorator):
    def method1(self) -> str:
        return f"{self.wrappedObj.method1()} + AnotherConcreteDecorator"

    def method2(self) -> str:
        return f"{self.wrappedObj.method2()} + AnotherConcreteDecorator"


if __name__ == "__main__":
    component = ConcreteComponent()
    print(component.method1())
    decorator1 = ConcreteDecorator(component)
    print(decorator1.method1())
    print(decorator1.method2())
    decorator2 = AnotherConcreteDecorator(decorator1)
    print(decorator2.method1()) 