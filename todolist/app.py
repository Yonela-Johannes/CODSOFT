
# Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import CRUD

class app():
    def __init__(self):
         # Colors
        self.WHITE = "#fff"
        self.BLACK = "#000"
        self.DARK_BG = "#242323"
        self.PRIMARY = "#252335"
        self.SECONDARY = "#9B1C1C"

        # Variables
        self.width = 500
        self.height = 460
        self.frame_height1 = 50
        self.frame_height2 = 200
        self.frame_height3 = 100
        self.button_width = 7
        self.dimensions = f"{self.width}x{self.height}"

        # Instantiating window/screen/display
        self.window = Tk()
        self.window.title("Phone Book")
        self.window.geometry(self.dimensions)
        self.window.configure(background=self.WHITE)

    def main(self):
        # Init CRUD method
        crud_method = CRUD
        # Frames
        frame_up = Frame(self.window, width=self.width, height=self.frame_height1, bg=self.PRIMARY)
        frame_up.grid(row=0, column=0, padx=0, pady=1)

        frame_down = Frame(self.window, width=self.width, height=self.frame_height2, bg=self.WHITE)
        frame_down.grid(row=1, column=0, padx=0, pady=1)

        # table frame
        frame_table = Frame(self.window, width=self.width, height=self.frame_height3, bg=self.DARK_BG)
        frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=2, sticky=NW)

if __name__ == '__main__':
    app.main().run(debug=True)
