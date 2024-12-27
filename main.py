import tkinter as tk
from tkinter import ttk

#This is the BudgetApp class. This will create the application and change the title to Budget App.
class BudgetApp:  
    def __init__(self,root):

        #Name the window
        root.title("Budget App")
        #Set size for window
        root.geometry("1000x800")
        
        #This allows the user to change the size of the window
        sizegrip= ttk.Sizegrip(root)
        sizegrip.place(x=0, y=0, relx=1, rely=1, anchor="se")

root = tk.Tk()
BudgetApp(root)
root.mainloop()
