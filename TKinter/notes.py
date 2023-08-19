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
        print("Edit Note", self.index)
        

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
    
    
def delete_all_notes():
    global notes
    for note in notes:
        note.label.destroy()
        note.editButton.destroy()
        note.deleteButton.destroy()
    notes = []
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


deleteAllNotes = ttk.Button(
    window,
    text='Delete All Notes',
    command=lambda: delete_all_notes()
).grid(column=2, row=0)


window.mainloop()