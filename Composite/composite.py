"""
Composite is used to unite the objects into a tree-like structure and treat it like a single object.
"""


class Component:
    def operation(self) -> None:
        pass

    def add(self, component: 'Component') -> None:
        pass

    def remove(self, component: 'Component') -> None:
        pass

    def getChild(self, index: int) -> None:
        pass


class Composite(Component):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []

    def operation(self) -> None:
        print(self.name)
        for child in self.children:
            child.operation()

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def getChild(self, index: int) -> None:
        return self.children[index]


class Leaf(Component):
    def __init__(self, name: str) -> None:
        self.name = name

    def operation(self) -> None:
        print(f"Child {self.name}")





if __name__ == "__main__":

    bob = Leaf('Bob')
    kate = Leaf('Kate')
    amy = Leaf('Amy')
    rob = Leaf('Rob')
    kim = Leaf('Kim')
    composite = Composite('Composite')
    composite.add(bob)
    composite.add(kate)
    composite.add(amy)
    composite1 = Composite('Composite 1')
    composite1.add(rob)
    composite1.add(kim)
    composite.add(composite1)

    composite.operation()

# Output: 

# Composite
# Child Bob
# Child Kate
# Child Amy
# Composite 1
# Child Rob
# Child Kim