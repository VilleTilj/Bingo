'''
This software is made as a visualization tool for Bingo host to show what numbers have allready came during the game.
'''

import tkinter as tk
import numpy as np
from tkinter import Menu
from tkinter import font as tkFont

'''
Class Bingo_board is responsible for drawing the buttons with numbers on the tkinter mainwindow. 
The buttons change color when pressed to visualise numbers called. 
'''
class Bingo_board:

    def __init__(self, mainwindow_root):
        self.mainwindow = mainwindow_root
        self.__create_menu()
        self.buttons: list = []
        self.__create_buttons()
        

    def __create_buttons(self):
        '''
        
        '''
        # Change default font for numbers
        font = tkFont.Font(family='Tunga', size=16, weight=tkFont.BOLD)
        
        # Init parameters for adjusting buttons to right places
        bingo_index: int = 1
        x_delta, y_delta = 0, 0
        
        # Loop though x and y axis for the button grid and create buttons
        for _ in range(9):
            for _ in range(10):
                new_button = tk.Button(self.mainwindow, text=str(bingo_index), bg='white', height = 2, 
                                         width = 5, font=font, command=lambda index=bingo_index - 1: self.__change_button_color(index))
                new_button.place(x= 150 + x_delta, y= 40 + y_delta)
                self.buttons.append(new_button)
                
                # Change row and adjust parameters for next button placement.
                if bingo_index % 10 == 0:
                    x_delta = 0
                    y_delta += 65
                else:
                    x_delta += 75
                bingo_index += 1


    def __create_menu(self):
        '''
        Private method:
        Create dropdown menu for possible options, like exiting the software.
        '''
        menu_bar = Menu(self.mainwindow)
        self.mainwindow.config(menu=menu_bar)
        Menu_toolbar = Menu(menu_bar)
        Menu_toolbar.add_command(label="Exit software", command=self.__destroy_window)
        menu_bar.add_cascade(label="Options", menu=Menu_toolbar)


    def __change_button_color(self, index) -> None:
        '''
        Private method:
        Changes the bingo sheet's buttons color when pressed.
        @ index : Index to find out wanted button
        '''
        self.buttons[index].configure(bg='red') if self.buttons[index]['bg'] == 'white' else self.buttons[index].configure(bg='white')


    def __destroy_window(self):
        self.mainwindow.destroy()
            


if __name__ == '__main__':
    # Init mainwindow
    root = tk.Tk()
    root.attributes("-fullscreen", True)  

    root.title("Bingo Screen")

    app = Bingo_board(root)

    root.mainloop()