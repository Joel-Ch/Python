from tkinter import ttk, Tk

class Note:
    def __init__(self, master, text, index):
        self.master = master
        self.text = text
        self.index = index

        self.label = ttk.Label(master, text=text)
        self.editButton = ttk.Button(master, text="Edit Note", command=self.editNote)
        self.deleteButton = ttk.Button(master, text="Delete Note", command=self.deleteNote)

        self.label.grid(row=index+1, column=0)
        self.editButton.grid(row=index+1, column=1)
        self.deleteButton.grid(row=index+1, column=2)

    
    def editNote(self):
        editWindow = Tk()
        editWindow.title("Edit Note")

        editLabel = ttk.Label(editWindow, text="Edit Note:")
        editLabel.pack()

        editEntry = ttk.Entry(editWindow)
        editEntry.insert(0, self.text)
        editEntry.pack()

        saveButton = ttk.Button(editWindow, text="Save", command=lambda: self.saveEditedText(editEntry.get(), editWindow))
        saveButton.pack()

    def saveEditedText(self, newText, editWindow):
        self.text = newText
        self.label.config(text=newText)
        editWindow.destroy()
        

    def deleteNote(self):
        self.label.destroy()
        self.editButton.destroy()
        self.deleteButton.destroy()
        notes.remove(self)  # Remove the note instance from the list
        rearrangeNotes()

def addNote():
    new_note = Note(window, "New Note "+str(len(notes)), len(notes))

    notes.append(new_note)
    rearrangeNotes()
    
    
def generateTextFile():
    file = open("notes.txt", "w")
    for note in notes:
        file.write(note.text + "\n")
    file.close()

def readFromTextFile():
    file = open("notes.txt", "r")
    for line in file:
        new_note = Note(window, line.strip(), len(notes))
        notes.append(new_note)
    file.close()
    rearrangeNotes()

def rearrangeNotes():
    for index, note in enumerate(notes):
        note.label.grid(row=index+1, column=0)
        note.editButton.grid(row=index+1, column=1)
        note.deleteButton.grid(row=index+1, column=2)
        
notes = []

window = Tk()
# Title of the window            
window.title("Notes")

add_note = ttk.Button(
    window,
    text='Add New Note',
    command=addNote
).grid(column=0, row=0)


GenerateTextFile = ttk.Button(
    window,
    text='Generate Text File',
    command=lambda: generateTextFile()
).grid(column=1, row=0)

ReadFromTextFile = ttk.Button(
    window,
    text='Read From Text File',
    command=lambda: readFromTextFile()
).grid(column=2, row=0)


window.mainloop()