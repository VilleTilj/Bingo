import tkinter as tk
import numpy as np
from tkinter import Menu
from tkinter import font as tkFont


class ChangeButton:

    def __init__(self, master, grid=np.zeros((9,10))):
        self.init_state = True
        self.mainwindow = master
        self.frame = tk.Frame(self.mainwindow)
        self.frame.pack(expand = False)
        self.__create_menu()
        self.grid = grid
        self.buttons = []
        bingo_index = 1
        font = tkFont.Font(family='Tunga', size=16, weight=tkFont.BOLD)

        x_delta, y_delta = 0,0
        for i in range(9):
            for j in range(10):
                new_button = tk.Button(self.mainwindow, text=str(bingo_index), bg='white', height = 2, 
                                         width = 5, font=font, command=lambda index=bingo_index - 1: self.toggle_text(index))
                new_button.place(x=0 + x_delta, y=115 + y_delta)
                self.buttons.append(new_button)
                bingo_index += 1
                x_delta += 40
                y_delta += 40
        self.init_state = False


    def __create_menu(self):
        menu_bar = Menu(self.mainwindow)
        self.mainwindow.config(menu=menu_bar)
        Menu_toolbar = Menu(menu_bar)
        Menu_toolbar.add_command(label="Exit software", command=self.__destroy_window)
        menu_bar.add_cascade(label="Options", menu=Menu_toolbar)

    def __destroy_window(self):
        self.mainwindow.destroy()

    def toggle_text(self, index):
        self.buttons[index].configure(bg='red')
            

    



root = tk.Tk()
root.attributes("-fullscreen", True)  # substitute `Tk` for whatever your `Tk()` object is called

root.title("Bingo Screen")

app = ChangeButton(root)

root.mainloop()