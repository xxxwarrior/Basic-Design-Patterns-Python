from typing import List, Dict



class Model:
    def __init__(self, elements: List[Dict]) -> None:
        self._elements = elements

    def addElement(self, element: Dict) -> None:
        self._elements.append(element)

    def getElement(self, name: str) -> Dict:
        if self._elements[name]:
            return self._elements[name]
        else:
            print("No such element")

    def getElements(self) -> List[Dict]:
        return self._elements



class View:
    def showElementsList(self, elements: List[Dict]) -> None:
        print('Elements Full Form List:')
        for element in elements:
            print(f"* Name: {element['name']}, * Value: {element['value']}")

    def showElementsNames(self, elements: List[Dict]) -> None:
        print('Elements:')
        for element in elements:
            print(element['name'])
        print()



class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def showElements(self, full: bool = False) -> None:
        elements = self.model.getElements()
        if full: 
            self.view.showElementsList(elements)
        else: self.view.showElementsNames(elements)

    def addElement(self, element: Dict) -> None:
        self.model.addElement(element)





if __name__ == "__main__":

    elements = [
        {"name": "Some Element", "value": "Some Element's value"}, 
        {"name": "Another Element", "value": "Another Element's value"},
        {"name": "One More Element", "value": "One More Element's value"}
]

controller = Controller(Model(elements), View())
controller.showElements()
controller.addElement({"name": "Additional Element", "value": "Additional Element's value"})
controller.showElements(full=True)
