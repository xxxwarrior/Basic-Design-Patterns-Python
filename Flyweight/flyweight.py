"""
Flyweight is used to create an object shared by multiple contexts.
The usage of this pattern reduces memory consumption by caching the the same data used by multiple objects.
"""

class Flyweight:
    def __init__(self, state: int) -> None:
        self.state = state
        
    def operation(self) -> None:
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self) -> None:
        print(f"Flyweight with state {self.state}")



class FlyweightFactory:
    flyweights = {}

    def getFlyweight(self, key: int) -> Flyweight:
        if not self.flyweights.get(key):
            self.flyweights[key] = ConcreteFlyweight(key)
        
        return self.flyweights[key]


if __name__ == "__main__":
    factory = FlyweightFactory()
    factory.getFlyweight(1)
    factory.getFlyweight(2)
    factory.getFlyweight(1).operation()

    
