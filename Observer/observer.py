"""
Observer is used to define "one-to-many" relations betweeen the objects,
so when the state of one (observable) object changes, all its dependents (observers) are notified, 
usually by calling one of their methods.
"""


from typing import Any


class Observer:
    def update(self, observable: 'Observable') -> None:
        print(f"The subject {observable.name} is {observable.state}")

class ConcreteObserver(Observer):
    pass


class Observable:

    def __init__(self, *args, **kwargs) -> None:
        self.observers = []

    def registerObserver(self, observer: Observer) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer: Observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self) -> None:
        for observer in self.observers:
            observer.update(self)


class ConcreteSubject(Observable):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def changeState(self, state: Any) -> None:
        self.state = state
        self.notifyObservers()




if __name__ == "__main__":
    subject = ConcreteSubject("Test")
    observer = ConcreteObserver()
    subject.registerObserver(observer)
    subject.changeState("Testing")

