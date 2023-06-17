from tkinter import ttk, Tk

Calculation = ""
Output = ""

def clicked(r,c):
    global Calculation
    global Output
    if (b[r][c] == "="):
        Output = eval(Calculation)
        OutputBox.config(text = Output)
    elif (b[r][c] == "C"):
        Calculation = ""
        Output = ""
        Calculator.config(text = Calculation)
        OutputBox.config(text = Output)
    else:
        Calculation = Calculation + str(b[r][c])
        Calculator.config(text = Calculation)

# Design window
root = Tk()
# Title of the window            
root.title("Calculator") 
root.resizable(0,0)

Calculator = ttk.Label(text=Calculation)
Calculator.grid(row = 0, columnspan = 3)
OutputBox = ttk.Label(text=Output)
OutputBox.grid(row = 0, column = 3)

#Buttons
b = [
     ["1","2","3","+"],
     ["4","5","6","-"],
     ["7","8","9","*"],
     ["C", "0", "=", "/"]]

# create button grid 
for i in range(4):
    for j in range(4):   
        ttk.Button(text = (b[i][j]), command = lambda r = i, c = j : clicked(r,c)).grid(row = i+1, column = j)  



root.mainloop()