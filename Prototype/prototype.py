"""
Prototype is used when creating new instances at a run-time is expensive,
so you create copies of existing objects and return them when necessary.
"""



from copy import deepcopy 
from typing import List


class Prototype:
    def clone(self) -> None:
        pass

class ConcretePrototype(Prototype):
    def __init__(self) -> None:
        self.name = 'Concrete Prototype'

    def clone(self) -> Prototype:
        return deepcopy(self)

class AnotherConcretePrototype(Prototype):
    def __init__(self) -> None:
        self.name = 'Another Concerete Prototype'

    def clone(self) -> Prototype:
        return deepcopy(self)


class Registry:
    def __init__(self, prototypes: List[Prototype] = None) -> None:
        if prototypes:
            self.prototypes = [prototype.clone() for prototype in prototypes]
        else: self.prototypes = []

    def getPrototype(self, className) -> Prototype:
        for prototype in self.prototypes:
            if type(prototype).__name__ == str(className):
                return prototype
            else: 
                newPrototype = className().clone()
                self.prototypes.append(newPrototype)
                return newPrototype
            


if __name__ == "__main__":
    prototype1 = ConcretePrototype()
    registry = Registry([prototype1,])
    print(registry.getPrototype(ConcretePrototype))
    print(registry.getPrototype(AnotherConcretePrototype))


