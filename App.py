from Model import Model
from View import View
from Controller import Controller
from Koonus import Koonus


class App:
    def __init__(self):
        self.view = View(Controller(self))
        self.koonus = Koonus()
        self.model = Model()
        self.controller = Controller(self.view)
        self.view.controller = self.controller  # Seon kontrolleri vaatega
        self.view.run()


if __name__ == "__main__":
    app = App()
