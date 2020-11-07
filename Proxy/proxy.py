"""
Proxy provides you a substitute object which controls the access to a real service object.
"""



class Subject:
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print('Real subject handled the request')


class Proxy(Subject):
    def __init__(self, subject: Subject) -> None:
        self.subject = subject

    def request(self) -> None:
        self.subject.request()




if __name__ == "__main__":
    proxy = Proxy(RealSubject())
    proxy.request()






