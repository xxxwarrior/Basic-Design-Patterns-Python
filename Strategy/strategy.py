"""
Strategy lets you define a family of algorithms, put each of them into a separate class, 
and make their objects interchangeable. Instead of implementing a single algorithm directly, 
code receives run-time instructions as to which in a family of algorithms to use.
"""





class BaseStrategy: 
    def execute(self, *args, **kwargs) -> None:
        raise NotImplementedError

class ConcreteStrategy1(BaseStrategy):
    def execute(self, *args, **kwargs) -> None:
        print("'Strategy 1' Method Executed")

class ConcreteStrategy2(BaseStrategy):
    def execute(self, *args, **kwargs) -> None:
        print("'Strategy 2' Method Executed")


class Context:
    def setStrategy(self, strategy: BaseStrategy) -> None:
        self.strategy = strategy

    def executeStrategy(self) -> None:
        self.strategy.execute()



if __name__ == "__main__":    
    context = Context()
    strategy1 = ConcreteStrategy1()
    strategy2 = ConcreteStrategy2()

    context.setStrategy(strategy1)
    context.executeStrategy() 
    context.setStrategy(strategy2)
    context.executeStrategy()