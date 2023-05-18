#import tkinter
import tkinter as tk

#print function that says 'button clicked'
def button_click():
    print("Button clicked!")

    #Create Root Window
    root = tk.Tk()
    root.title("Button Example")

    #Create button object, its text, and its event (button_click)
    button = tk.Button(root, text="Click Me!", command=button_click())
    button.pack()

    #keeps the root window visible with .mainloop
    root.mainloop()