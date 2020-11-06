"""
Abstract Factory is used to create the families of related or dependent objects without specifying their concrete classes.
""" 



class AbstractProductA:
    def someOperation(self) -> None:
        pass

class ProductA1(AbstractProductA):
    def someOperation(self) -> str:
        return "Product A1 operates"

class ProductA2(AbstractProductA):
    def someOperation(self) -> str:
        return "Product A2 operates"


class AbstractProductB:
    def someOperation(self) -> None:
        pass

class ProductB1(AbstractProductB):
    def someOperation(self) -> str:
        return "Product B1 operates"

class ProductB2(AbstractProductB):
    def someOperation(self) -> str:
        return "Product B2 operates"



class AbstractFactory:
    def createProductA(self) -> None:
        pass

    def createProductB(self) -> None:
        pass


class ConcreteFactory(AbstractFactory):
    def createProductA(self) -> AbstractProductA:
        return ProductA1()

    def createProductB(self) -> AbstractProductB:
        return ProductB1()

class AnotherConcreteFactory(AbstractFactory):
    def createProductA(self) -> AbstractProductA:
        return ProductA2()

    def createProductB(self) -> AbstractProductB:
        return ProductB2()




def test_func(factory):
    A = factory.createProductA()
    B = factory.createProductB()

    print(A.someOperation(), B.someOperation())



if __name__ == "__main__":
    test_func(ConcreteFactory())
    test_func(AnotherConcreteFactory())







