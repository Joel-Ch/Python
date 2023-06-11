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

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] !=0: # check rows
            stop_game = True

            winner = messagebox.showinfo("Winner", states[i][0] + " Won")
            break

        elif states [0][i] == states[1][i] == states[2][i] != 0: # check columns
            stop_game = True

            winner = messagebox.showinfo("Winner", states[0][i]+ " Won!")
            break

        elif states[0][0] == states[1][1] == states[2][2] !=0: # check \ diagonal
            stop_game = True

            winner = messagebox.showinfo("Winner", states[0][0]+ " Won!")
            break

        elif states[0][2] == states[1][1] == states[2][0] !=0: # check / diagonal
            stop_game = True

            winner = messagebox.showinfo("Winner" , states[0][2]+ " Won!")
            break

        elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
            stop_game = True

            winner = messagebox.showinfo("tie", "Tie")

            break

def reset():
    global Player1
    global stop_game
    Player1 = 'X'
    stop_game = False
    player.config(text=Player1+ "'s Turn")
    for i in range(3):
        for j in range(3):
            states[i][j] = 0
            b[i][j].configure(text = " ")

def aiMove():
    index = [0]*9
    k = 0

    #create list of available moves
    for i in range (3):
        for j in range (3):
            if states[i][j] == 0:
                index[k] = index[k] + j + 3*i + 1#index from 1 to 9
                k += 1

    # remove excess 0s in list
    indexNoZeros = [x for x in index if x != 0]
    selectedIndex = random.choice(indexNoZeros)-1 # return to 0 to 8

    # get row and col from index
    row = selectedIndex // 3
    col = selectedIndex % 3

    # play move
    clicked(row,col)

# Design window
root = Tk()
# Title of the window            
root.title("Noughts & Crosses") 
root.resizable(0,0)
player = ttk.Label(text=Player1+ "'s Turn", font=("Helvetica", 16))
player.grid(row = 3, column = 0, columnspan=1)
ttk.Button(root, text = "Reset Game", command = lambda:reset()).grid(row = 3, column = 1)
ttk.Button(root, text="AI Move", command=lambda:aiMove()).grid(row=3, column=2)

#Button
b = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]

#text for buttons
states = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]

# create button grid 
for i in range(3):
    for j in range(3):
                       
        b[i][j] = Button(
                        height = 4, width = 8,
                        font = ("Helvetica","20"),
                        command = lambda r = i, c = j : clicked(r,c))
        b[i][j].grid(row = i, column = j)  


root.mainloop()