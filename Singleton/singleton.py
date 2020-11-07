"""
Singleton ensures that there's only one instance of the class and provides only one global point of access to it.
"""


class Singleton:
    uniqueInstance = None

    def __init__(self) -> None:
        if Singleton.uniqueInstance != None:
            raise Exception("Can't create another instance!")
        else: Singleton.uniqueInstance = self

    @staticmethod
    def getInstance() -> 'Singleton':
        if Singleton.uniqueInstance == None:
            Singleton()
        return Singleton.uniqueInstance

        

        
if __name__ == "__main__":
    singleton1 = Singleton()
    print(Singleton.getInstance())

    try: 
        Singleton()
    except: 
        print("It doesn't work exactly as expected!")