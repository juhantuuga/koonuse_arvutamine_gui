from tkinter import *


class View:
    def __init__(self, controller):
        self.info_text = None
        self.info_label = None
        self.bottom_frame = None
        self.btn_calculate = None
        self.frame2 = None
        self.entry_height = None
        self.label_height = None
        self.entry_radius = None
        self.label_radius = None
        self.frame1 = None
        self.top_frame = None
        self.root = Tk()
        self.controller = controller
        self.root.title("Koonuse arvutamine")
        self.center_window(450, 300)
        self.root.minsize(450, 300)
        self.root.maxsize(450, 300)
        self.initialize()

    def initialize(self):
        # Ülemine raam
        self.top_frame = Frame(self.root, padx=20, pady=20)
        self.top_frame.pack(expand=True, fill=BOTH)

        self.frame1 = Frame(self.top_frame)
        self.frame1.pack(side=LEFT, expand=True, fill=BOTH)

        self.label_radius = Label(self.frame1, text="Raadius:")
        self.label_radius.pack(anchor=W)
        self.entry_radius = Entry(self.frame1)
        self.entry_radius.pack(expand=True, fill="x")

        self.label_height = Label(self.frame1, text="Kõrgus:")
        self.label_height.pack(anchor=W)
        self.entry_height = Entry(self.frame1)
        self.entry_height.pack(expand=True, fill="x")

        self.frame2 = Frame(self.top_frame, padx=5)
        self.frame2.pack(side=RIGHT, expand=True, fill=BOTH)

        self.btn_calculate = Button(self.frame2, text="Arvuta", command=self.calculate, border=1, bg="#e8faed")
        self.btn_calculate.pack(expand=True, fill=BOTH)

        # Alumine raam
        self.bottom_frame = Frame(self.root, padx=20, pady=20)
        self.bottom_frame.pack(expand=True, fill=BOTH)

        self.info_label = Label(self.bottom_frame, text="Sisestatud väärtused ja tulemused:")
        self.info_label.pack()

        self.info_text = Text(self.bottom_frame, border=0)
        self.info_text.pack()

        # Lukusta alumine raam
        for widget in self.bottom_frame.winfo_children():
            widget.configure(state="disabled")

    def center_window(self, width, height):
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def calculate(self):
        self.controller.calculate_cone(self.entry_radius.get(), self.entry_height.get())

    def show_result(self, volume, surface_area, hypotenuse):
        result_str = (f"Raadius: {self.entry_radius.get()}, Kõrgus: {self.entry_height.get()}"
                      f"\nKoonuse ruumala: {volume}\nRingi pindala: {surface_area}\nKolmnurga hüpotenuus: {hypotenuse}")
        self.info_text.delete(1.0, END)
        self.info_text.insert(END, result_str)

    def run(self):
        self.root.mainloop()
