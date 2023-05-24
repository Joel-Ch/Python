import tkinter as tk
from tkinter import ttk

# dictionary of prefixes
prefixes = {'p': 1e-12, 'n': 1e-9, 'u': 1e-6, 'm': 1e-3, '-': 1, 'k': 1e3, 'M': 1e6, 'G': 1e9, 'T': 1e12}

def convert(value, prefix1, prefix2):
    try:
        value = float(value.get())
        prefix1 = prefixes[prefix1.get()]
        prefix2 = prefixes[prefix2.get()]
        output.config(text=str(value*prefix1/prefix2))
    except:
        output.config(text="Invalid Input")

# create window
window=tk.Tk()
window.title("Prefix Converter")
window.resizable(False, False)

# value
ttk.Label(text="Enter a number: ").pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
value = ttk.Entry()
value.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

# prefix1
ttk.Label(text="Enter a prefix: ").pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
prefixBox1 = ttk.Combobox(values=' '.join(prefixes), state='readonly')
prefixBox1.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

# prefix2
ttk.Label(text="Enter a second prefix: ").pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
prefixBox2 = ttk.Combobox(values=' '.join(prefixes), state='readonly')
prefixBox2.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

# confirm button
ttk.Button(text="Convert", command=lambda: convert(value, prefixBox1, prefixBox2)).pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

# output
output = ttk.Label(text="Output")
output.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

# keep window open until closed manually
window.mainloop()