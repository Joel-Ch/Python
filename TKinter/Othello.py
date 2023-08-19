from tkinter import * 
from tkinter import messagebox, ttk
import random

# Variables
Player1 = 'X'
stop_game = False

def clicked(r,c):
    global Player1

    if Player1 == "X" and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text = "X")
        states[r][c] = 'X'
        Player1='O'


    if Player1 == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text = 'O')
        states[r][c] = "O"
        Player1 = "X"

    player.config(text=Player1 + "'s Turn")

    check_if_win()

def check_if_win():
    global stop_game


def reset():
    global Player1
    global stop_game
    Player1 = 'X'
    stop_game = False
    player.config(text=Player1+ "'s Turn")
    for i in range(8):
        for j in range(8):
            states[i][j] = 0
            b[i][j].configure(text = " ")

def aiMove():

    # play move
    # clicked(row,col)
    return

# Design window
root = Tk()
# Title of the window            
root.title("Othello") 
root.resizable(0,0)
player = ttk.Label(text=Player1+ "'s Turn", font=("Helvetica", 16))
player.grid(row = 9, column = 0, columnspan=2)
ttk.Button(root, text = "Reset Game", command = lambda:reset()).grid(row = 9, column = 2, columnspan=2)
ttk.Button(root, text="AI Move", command=lambda:aiMove()).grid(row=9, column=4, columnspan=2)

#Button
b = [
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],]

#text for buttons
states = [
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]

# create button grid 
for i in range(8):
    for j in range(8):
                       
        b[i][j] = Button(
                        height = 2, width = 4,
                        font = ("Helvetica","20"),
                        command = lambda r = i, c = j : clicked(r,c))
        b[i][j].grid(row = i, column = j)  


root.mainloop()