import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from tkinter import *

class Book():


    def __init__(self):
        self.df = pd.read_csv('testtxt.csv')
    

    def add_new(self,name,athor,year,gener,amount):
        
        int(amount)
        int(year)
        dic = {"name":name,"athor":athor,"year":year,"gener":gener,"amount":amount}
        new_df = pd.concat([self.df,pd.DataFrame([dic])],ignore_index=True)
        self.df = new_df
        self.df.to_csv('dz.csv',index=False)

    def window_for_add(self):
        new_window = Toplevel()
        new_window.title("додати нову книгу")
        Label(new_window,text='назва книги').pack(pady=5)
        name = Entry(new_window)
        name.pack()
        Label(new_window,text="автор").pack(pady=5)
        athor = Entry(new_window)
        athor.pack()
        Label(new_window,text='рік випуску').pack(pady=5)
        year = Entry(new_window)
        year.pack()
        Label(new_window,text='жанр').pack(pady=5)
        gener = Entry(new_window)
        gener.pack()
        Label(new_window,text='кількість').pack(pady=5)
        amount = Entry(new_window)
        amount.pack()
        
        def click():
            self.add_new(name.get(),athor.get(),year.get(),gener.get(),amount.get())
            new_window.destroy()

        bt = Button(new_window,text='додати',command=click)
        bt.pack(pady=20)

    def change_name(self,in_which_book:str,new_name:str,):
       
            self.df.loc[self.df['name'].str.upper() == in_which_book,'name'] = new_name
            self.df.to_csv("testtxt.csv",index=False)


    def window_to_chage_name(self):

        new_window = Toplevel()
        Label(new_window,text='введіть назву книги яку хочете змінити').pack(pady=5)
        name_to_change = Entry(new_window)
        name_to_change.pack()
        Label(new_window,text="нова назва").pack(pady = 5)
        new_name = Entry(new_window)
        new_name.pack()


        def click():
            b = name_to_change.get().strip().upper()
            self.change_name(b,new_name.get())
        
        bt = Button(new_window,text="змінити",command=click)
        bt.pack(pady=20)

    def remove_book(self,what_to_remove):

        new_df = self.df[self.df['name'].str.upper()!=what_to_remove]
        self.df = new_df
        self.df.to_csv('testtxt.csv',index=False)

    def window_to_remove(self):
        new_window = Toplevel()
        
        Label(new_window,text='що видалити? введіть назву').pack(pady=5)

        name = Entry(new_window)
        name.pack()
        def click():
            b = name.get().strip().upper()
            self.remove_book(b)
        bt = Button(new_window,text='видалити',command=click)
        bt.pack(pady=20)

    def gistograma(self):
        y = self.df.groupby('years').size
        x = self.df['year'].values
        plt.bar(x,y,color='lime')
        plt.xlabel("кількість")
        plt.ylabel("роки")
        plt.show()
a = Book()
root = Tk()
root.title("книги")


def add_book():
    a.window_for_add()
def change_name_for_book():
    a.window_to_chage_name()
def remove_book_from_df():
    a.window_to_remove()
bt_for_add = Button(root,text="додати книгу",command=add_book)
bt_for_change_name = Button(root,text='змінити назву книги',command=change_name_for_book)
bt_for_remove = Button(root,text="видалити книгу",command=remove_book_from_df)

bt_for_add.pack()
bt_for_change_name.pack()
bt_for_remove.pack()
a.gistograma()
root.mainloop()

