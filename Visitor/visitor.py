"""
Visitor is used when you need to add some new behavior to a class hierarchy 
without changing existing code.
"""


from typing import List



class Element:
    def accept(self, visitor: 'Visitor') -> None:
        pass

class ConcreteElement(Element):
    def accept(self, visitor: 'Visitor') -> None:
        visitor.visitConcreteElement()

class AnotherConcreteElement(Element):
    def accept(self, visitor: 'Visitor') -> None:
        visitor.visitAnotherConcreteElement()



class Visitor:
    def visitConcreteElement(self) -> None:
        pass

    def visitAnotherConcreteElement(self) -> None:
        pass

class ConcreteVisitor(Visitor):
    def visitConcreteElement(self) -> None:
        print('Concrete Visitor visited Concrete Element')

    def visitAnotherConcreteElement(self) -> None:
        print('Concrete Visitor visited Another Concrete Element')

class AnotherConcreteVisitor(Visitor):
    def visitConcreteElement(self) -> None:
        print('Another Concrete Visitor visited Concrete Element')

    def visitAnotherConcreteElement(self) -> None:
        print('Another Concrete Visitor visited Another Concrete Element')



def test_func(visitor: Visitor, elements: List[Element]) -> None:
    for element in elements:
        element.accept(visitor)



if __name__ == "__main__":
    elements = [ConcreteElement(), AnotherConcreteElement()]

    visitor1 = ConcreteVisitor()
    visitor2 = AnotherConcreteVisitor()

    test_func(visitor1, elements)
    test_func(visitor2, elements)