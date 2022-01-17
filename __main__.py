from tkinter import *
from package import *

root = Tk()
root.geometry("500x200")


payment_method_button = Button(root, text='Payment_methods', command = p_m).pack()
monthly_sales = Button(root, text='Monthly sales', command = m_s).pack()

root.mainloop()