from tkinter import messagebox
from Koonus import Koonus


class Controller:
    def __init__(self, view):
        self.view = view
        self.koonus = Koonus()

    def calculate_cone(self, radius, height):
        try:
            radius = float(radius)
            height = float(height)
            if radius <= 0 or height <= 0:
                messagebox.showerror("Viga", "Raadius ja kõrgus peavad olema positiivsed arvud!")
                return
            self.koonus.set_values(radius, height)
            volume, surface_area, hypotenuse = self.koonus.calculate_values()

            # Ajutise tekstikasti lubamine
            self.view.info_text.config(state="normal")

            # Näitame tulemused kastikeses
            self.view.show_result(volume, surface_area, hypotenuse)

            # Tekstikasti uuesti lukustamine
            self.view.info_text.config(state="disabled")
        except ValueError:
            messagebox.showerror("Viga", "Mõlemad lahtrid peavad olema täidetud numbritega!")
