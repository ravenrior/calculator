from tkinter import *

class My_Button:
    def __init__(self, sym: str, x: int, y: int, root: type[Tk] | None = None, bg: str | None = "grey", fg: str | None = "black"):
        self.sym: str = sym
        self.x: int = x
        self.y: int = y
        self.root: type[Tk] = root
        self.bg: str = bg
        self.fg: str = fg

    def create_button(self) -> Button:
        Button(self.root, text=self.sym, bg=self.bg, fg=self.fg, width=9, height=4).place(x=self.x, y=self.y)
