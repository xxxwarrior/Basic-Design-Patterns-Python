"""
Mediator is used to create a special mediator object that controls indirect coupling between other objects.
"""



class Mediator:
    def __init__(self, collegue: 'Collegue', anotherCollegue: 'Collegue') -> None:
        self.collegue = collegue
        self.collegue.mediator = self
        self.anotherCollegue = anotherCollegue
        self.anotherCollegue.mediator = self

class ConcreteMediator(Mediator):
    def notify(self, event: str) -> None:
        if event == 'EventA':
            self.collegue.actionB()
        elif event == 'AnotherEventA':
            self.collegue.actionB()
            self.anotherCollegue.actionB()



class Collegue:
    def __init__(self, mediator: Mediator = None) -> None:
        self.mediator = mediator


class ConcreteCollegue(Collegue):
    def actionA(self) -> None:
        print('A action by Concrete Mediator')
        self.mediator.notify('EventA')

    def actionB(self) -> None:
        print('B action by Concrete Mediator')
        self.mediator.notify('EventB')

class AnotherConcreteCollegue(Collegue):
    def actionA(self) -> None:
        print('A action by Another Concrete Mediator')
        self.mediator.notify('AnotherEventA')

    def actionB(self) -> None:
        print('B action by Another Concrete Mediator')
        self.mediator.notify('AnotherEventB')





if __name__ == "__main__":
    collegue1 = ConcreteCollegue()
    collegue2 = AnotherConcreteCollegue()
    mediator = ConcreteMediator(collegue1, collegue2)

    collegue1.actionA()
    collegue2.actionA()
    collegue2.actionB()





