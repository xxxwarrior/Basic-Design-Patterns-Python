"""
Iterator is used to iterate over a collection of elements without exposing its implementation.
Iterator and Aggregator can be abstract classes and ConcreteIterator and ConcreteAggregator can be added.
"""


from typing import List, Any


class Iterator:
    def __init__(self, collection: List[Any]) -> None:
        self.collection = collection
        self.index = 0

    def hasNext(self) -> bool:
        return False if self.index >= len(self.collection) else True

    def next(self) -> Any:
        element = self.collection[self.index]
        self.index += 1
        return element

    def remove(self) -> int:
        self.collection.pop()


class Aggregate:
    def __init__(self, collection: List[Any]) -> int:
        self.collection = collection

    def createIterator(self) -> Iterator:
        return Iterator(self.collection)




if __name__ == "__main__":
    aggregate = Aggregate([1, 5, 3, 1, 6, 8, 2])
    iterator = aggregate.createIterator()

    while iterator.hasNext():
        element = iterator.next()
        print(element)


