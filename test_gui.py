import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Press the button")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the GUI event loop
root.mainloop()