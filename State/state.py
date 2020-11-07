"""
State lets you handle the objects behavior when its state changes.
"""


class Context:
    def __init__(self) -> None:
        self.state = State()

    def setState(self, state) -> None:
        self.state = state

    def request(self) -> None:
        self.state.handle()

class State:
    def handle(self) -> None:
        pass

class ConcreteStateA(State):
    def handle(self) -> None:
        print("Handled by State A")

class ConcreteStateB(State):
    def handle(self) -> None:
        print("Handled by State B")




if __name__ == "__main__":
    context = Context()
    context.setState(ConcreteStateA())
    context.request()
    context.setState(ConcreteStateB())
    context.request()

    