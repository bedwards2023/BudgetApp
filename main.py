import tkinter as tk
from tkinter import ttk


#This is the BudgetApp class. This will create the application and change the title to Budget App.
class BudgetApp(tk.Tk):  
    def __init__(self,title):

        #main setup
        super().__init__()
        self.title("Budget App")
        #Set size for window
        self.geometry("1000x800")
        
        #This allows the user to change the size of the window
        sizegrip= ttk.Sizegrip(self)
        sizegrip.pack(side=tk.BOTTOM, anchor=tk.SE)

        #Theme
        self.tk.call('source','elegance/elegance.tcl')
        self.set_theme('light')

if __name__ == '__main__':
    BudgetApp('Budget App').mainloop()

