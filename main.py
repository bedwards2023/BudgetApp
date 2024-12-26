import tkinter as tk

#This is the BudgetApp class. This will create the application and change the title to Budget App.
class BudgetApp:  
    def __init__(self,root):

        root.title("Budget App")


root = tk.Tk()
BudgetApp(root)
root.mainloop()
