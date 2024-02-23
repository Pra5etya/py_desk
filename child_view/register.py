import tkinter as tk
import sys, re, os
from controller import Controller
from tkinter import messagebox, filedialog

class regView(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.main_view()


    def main_view(self): 
        self.title('Register Data')
        self.geometry('600x600')
        self.iconbitmap(sys.executable)

        # init class from controller.py
        self.controller = Controller()

        self.register_data()


# =======================
#     Widget Section
# =======================
    def register_data(self): 
        # email entry
        self.label_email = tk.Label(self, text = 'Email \t\t:', font = 8)
        self.label_email.grid(row = 0, column = 0, padx = 5)

        self.email_entry = tk.Entry(self, font = 8, justify = 'left')
        self.email_entry.grid(row = 0, column = 1, padx = 5)

        # name entry
        self.label_username = tk.Label(self, text = 'Username \t:', font = 8)
        self.label_username.grid(row = 1, column = 0, padx = 5)

        self.username_entry = tk.Entry(self, font = 8, justify = 'left')
        self.username_entry.grid(row = 1, column = 1, padx = 5)

        # password entry
        self.label_password = tk.Label(self, text = 'Password \t:', font = 8)
        self.label_password.grid(row = 2, column = 0, padx = 5)

        self.pass_entry = tk.Entry(self, font = 8, show = '*', justify = 'left')
        self.pass_entry.grid(row = 2, column = 1, padx = 5)

        # contact entry
        self.contact_label = tk.Label(self, text = 'Whats App \t:', font = 8)
        self.contact_label.grid(row = 3, column = 0, padx = 5)

        self.contact_entry = tk.Entry(self, font = 8,  justify = 'left')
        self.contact_entry.grid(row = 3, column = 1, padx = 5)

        # ============================
        self.add_button = tk.Button(self, text = 'Register', width = 10, font = 8, bd = 5, command = self.add)
        self.add_button.grid(row = 4, column = 1, padx = 5, pady = 10)


# =======================
#     Logic Section
# =======================    
    def add(self):
        # param for controller
        email_ = self.email_entry.get()
        username_ = self.username_entry.get()
        pass_ = self.pass_entry.get()
        contact_ = self.contact_entry.get()

        if email_ == '':
            messagebox.showerror('Error', 'Please fill email Form')

        elif username_ == '':
            messagebox.showerror('Error', 'Please fill name Form')

        elif pass_ == '':
            messagebox.showerror('Error', 'Please fill password Form')

        elif contact_ == '': 
            messagebox.showerror('Error', 'Please fill contact Form')

        else:
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(email_pattern, email_): 
                messagebox.showerror("Error", "Email not valid!")
             
            else:
                print('Insert Data')
                self.controller.reg_data(email_, username_, pass_, contact_)

                # self.refresh_list()
                messagebox.showinfo('Success', 'Data has been insert')

                # delete from placeholder view
                self.email_entry.delete(0, tk.END)
                self.username_entry.delete(0, tk.END)
                self.pass_entry.delete(0, tk.END)
                self.contact_entry.delete(0, tk.END)