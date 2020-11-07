"""
Memento is used to save an object's states and restore its previous state if necessary.
"""

from typing import Any


class Memento:
    def __init__(self, state: Any) -> None:
        self.state = state

    def setState(self, state: Any) -> None:
        self.state = state

    def getState(self) -> Any:
        return self.state


class Originator:
    def __init__(self, state: Any) -> None:
        self.state = state

    def setState(self, state: Any) -> None:
        self.state = state
        print(f'Originator: the state is {self.state}')

    def getState(self) -> Any:
        print(f'Originator: the state is {self.state} ')
        return self.state

    def saveState(self) -> Memento:
        return Memento(self.state)

    def restoreState(self, memento: Memento) -> None:
        self.state = memento.getState()
        print(f'Originator: the state is restored to {self.state} ')


class CareTaker:
    def __init__(self, originator: Originator) -> None:
        self.originator = originator
        self.history = [self.originator.saveState()]
        print("CareTaker: the original state is saved")

    def save(self) -> None:
        print("CareTaker: Originator's state is saved")
        self.history.append(self.originator.saveState())

    def undo(self) -> None:
        print("CareTaker: Originator's state is restoring")
        memento = self.history.pop()
        self.originator.restoreState(memento)





if __name__ == "__main__":
    originator = Originator(1)
    careTaker = CareTaker(originator)
    originator.setState(2)
    careTaker.save()
    originator.setState(3)
    careTaker.undo()

