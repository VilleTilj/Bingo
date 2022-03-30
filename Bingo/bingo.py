'''
This software is made as a visualization tool for Bingo host to show what numbers have allready came during the game.
'''

import tkinter as tk

from tkinter import Menu
from tkinter import font as tkFont

GRID_X_START = 480
GRID_Y_START = 20
GRID_Y_DELTA = 66
GRID_X_DELTA = 75

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
        self.is_fullscreen = False

        self.mainwindow.bind("<Escape>", lambda x: root.destroy())

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
                new_button.place(x= GRID_X_START + x_delta, y= GRID_Y_START + y_delta)
                self.buttons.append(new_button)
                
                # Change row and adjust parameters for next button placement.
                if bingo_index % 10 == 0:
                    x_delta = 0
                    y_delta += GRID_Y_DELTA
                else:
                    x_delta += GRID_X_DELTA
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
        Menu_toolbar.add_command(label='Full screen on/off', command=self.toggle_fullscreen)
        menu_bar.add_cascade(label="Options", menu=Menu_toolbar)


    def __change_button_color(self, index) -> None:
        '''
        Private method:
        Changes the bingo sheet's buttons color when pressed.
        @ index : Index to find out wanted button
        '''
        self.buttons[index].configure(bg='#10f520') if self.buttons[index]['bg'] == 'white' else self.buttons[index].configure(bg='white')


    def toggle_fullscreen(self):
        '''
        Private method:
        Change between fullscreen and non fullscreen.
        '''
        if self.is_fullscreen:
            root.attributes("-fullscreen", False)
            self.is_fullscreen = False
        else:
            root.attributes("-fullscreen", True)  
            self.is_fullscreen = True


    def __destroy_window(self):
        self.mainwindow.destroy()
            


if __name__ == '__main__':
    # Init mainwindow
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()   
    root.geometry(f'{screen_width}x{screen_height}')
    root.attributes("-fullscreen", False)  

    root.title("Bingo Screen")

    app = Bingo_board(root)

    # Start game loop
    root.mainloop()