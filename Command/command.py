"""
Command encapsulates the request as an object. 
It adds a level of abstraction between an object that invokes a command and the object that perfoms it.
"""


class Invoker:
    def __init__(self) -> None:
        self._commands = []

    def addCommand(self, command: 'Command') -> None:
        self._commands.append(command)

    def execute(self) -> None:
        for command in self._commands:
            command.execute()


class Command:
    def __init__(self, reciever: 'Reciever') -> None:
        self._reciever = reciever

    def execute(self) -> None:
        pass

class ConcreteCommand(Command):
    def execute(self) -> None:
        print("The execution of Concrete Command")
        self._reciever.action()

class AnotherConcreteCommand(Command):
    def execute(self) -> None:
        print("The execution of Another Concrete Command")
        self._reciever.action()


class Reciever:
    def action(self) -> None:
        print("Reciever's in action")


if __name__ == "__main__":
    reciever = Reciever()
    command1 = ConcreteCommand(reciever)
    command2 = AnotherConcreteCommand(reciever)
    invoker = Invoker()
    invoker.addCommand(command1)
    invoker.addCommand(command2)
    invoker.execute()