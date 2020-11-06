"""
Description:
Builder is used to encapsulate the step by step creation of the object.
"""


class Product:
    def __init__(self):
        self.part1 = ""
        self.part2 = ""
        self.part3 = ""

    def makePart1(self, part):
        self.part1 = part

    def makePart2(self, part):
        self.part2 = part

    def makePart3(self, part):
        self.part3 = part

    def getParts(self):
        print(f"Product's parts: {self.part1}, {self.part2}, {self.part3}")


class Builder:
    def __init__(self):
        self.product = Product()

    def getProduct(self):
        return self.product.getParts()


class ConcreteBuilder(Builder):
    def buildPart1(self):
        self.product.makePart1("Part 1A")

    def buildPart2(self):
        self.product.makePart2("Part 2A")

    def buildPart3(self):
        self.product.makePart3("Part 3A")

class AnotherConcreteBuilder(Builder):
    def buildPart1(self):
        self.product.makePart1("Part 1B")

    def buildPart2(self):
        self.product.makePart2("Part 2B")

    def buildPart3(self):
        self.product.makePart3("Part 3B")



class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.buildPart1()
        self.builder.buildPart2()
        self.builder.buildPart3()

    def getResult(self):
        self.builder.getProduct()





if __name__ == "__main__":
    director = Director(ConcreteBuilder())
    director1 = Director(AnotherConcreteBuilder())

    director.construct()
    director1.construct()

    director.getResult()
    director1.getResult()


