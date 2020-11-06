"""
Chain of Responsibility allows you to give request handling to a chain of objects until one of them handles it.
"""

class Handler:
    def __init__(self, nextHandler: 'Handler' = None) -> None:
        self.nextHandler = nextHandler
        self.requestToHandle = ""

    def handleRequest(self, request: str) -> None:
        if request != self.requestToHandle and self.nextHandler:
            self.nextHandler.handleRequest(request)
        elif request != self.requestToHandle and not self.nextHandler:
            print(f'Unsupported requeset')
        else: print(f'Request is handled by {self.__class__.__name__}')
         

class ConcreteHandler(Handler):
    def __init__(self, nextHandler: Handler = None) -> None:
        self.nextHandler = nextHandler
        self.requestToHandle = "Concrete Request"

        
class AnotherConcreteHandler(Handler):
    def __init__(self, nextHandler: Handler = None) -> None:
        self.nextHandler = nextHandler
        self.requestToHandle = "Another Request"


class OneMoreHandler(Handler):
    def __init__(self, nextHandler: Handler = None) -> None:
        self.nextHandler = nextHandler
        self.requestToHandle = "One More Request"




if __name__ == "__main__":
    handler = ConcreteHandler()
    handler1 = AnotherConcreteHandler()
    handler2 = OneMoreHandler()
    handler.nextHandler = handler1
    handler1.nextHandler = handler2

    handler.handleRequest("One More Request")
