"""
Factory method is used to define the common interface for creating an object,
but the concrete implementation of the instances is delegated to subclasses. 
"""


class Product:
    def someOperation(self) -> str:
        return "Default Product operation"

class ConcreteProduct(Product):
    def someOperation(self) -> str:
        return "ConcreteProduct operation"

class ConcreteProduct1(Product):
    def someOperation(self) -> str:
        return "ConcreteProduct1 operation"


class Creator:
    def factoryMethod(self) -> Product:
        # Default implementation
        return Product()

    def someMethod(self) -> str:
        product = self.factoryMethod()
        return f"Default Creator method and {product.someOperation()}"

class ConcreteCreator(Creator):
    def factoryMethod(self) -> Product:
        return ConcreteProduct()

class ConcreteCreator1(Creator):
    def factoryMethod(self) -> Product:
        return ConcreteProduct1()



def test_func(creator: Creator) -> None:
    print(f"Same interface for any creator: {creator.someMethod()}")


if __name__ == "__main__":
    test_func(ConcreteCreator())
    test_func(ConcreteCreator1())

