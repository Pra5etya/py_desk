# view.py
import tkinter as tk
import sys
from controller import Controller
from tkinter import messagebox

class View(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.main_view()

        self.refresh_list()

    def main_view(self): 
        self.master.title('Sample Desktop App')
        self.master.geometry('600x600')
        self.master.iconbitmap(sys.executable)

        # init class from controller.py
        self.controller = Controller()

        self.entry_add()

        self.entry_update()

        self.entry_delete()

        self.entry_list()

# =======================
#     Widget Section
# =======================
    def entry_add(self): 
        # name entry
        self.label_name = tk.Label(self.master, text = 'User \t:', font = 8)
        self.label_name.grid(row = 0, column = 0, padx = 5)

        self.name_entry = tk.Entry(self.master, font = 8)
        self.name_entry.grid(row = 0, column = 1, padx = 5)

        # password entry
        self.label_password = tk.Label(self.master, text = 'Pass \t:', font = 8)
        self.label_password.grid(row = 1, column = 0, padx = 5)

        self.pass_entry = tk.Entry(self.master, font = 8)
        self.pass_entry.grid(row = 1, column = 1, padx = 5)

        # ============================
        self.add_button = tk.Button(self.master, text = 'Add', width = 5, font = 8, command = self.add)
        self.add_button.grid(row = 2, column = 1, padx = 5)

    def entry_update(self): 
        # update entry
        self.label_update = tk.Label(self.master, text = 'Update Id :', font = 8)
        self.label_update.grid(row = 3, column = 0, padx = 5)

        self.update_entry = tk.Entry(self.master, font = 8)
        self.update_entry.grid(row = 3, column = 1, padx = 5)

        self.add_button = tk.Button(self.master, text = 'Update', width = 5, font = 8, command = self.update)
        self.add_button.grid(row = 3, column = 2, padx = 5)
    
    def entry_delete(self): 
        # delete entry
        self.delete_id = tk.Label(self.master, text = 'Delete Id \t:', font = 8)
        self.delete_id.grid(row = 4, column = 0, padx = 5)

        self.delete_entry = tk.Entry(self.master, font = 8)
        self.delete_entry.grid(row = 4, column = 1, padx = 5)

        self.delete_button = tk.Button(self.master, text = 'Delete', width = 5, font = 8, command = self.delete)
        self.delete_button.grid(row = 4, column = 2)

    def entry_list(self): 
        # Listbox
        self.list_name = tk.Label(self.master, text = 'Data List', font = 8)
        self.list_name.grid(row = 5, column = 1, padx = 5)

        self.listbox = tk.Listbox(self.master, font = 8, width = 30)
        self.listbox.grid(row = 6, column = 1, padx = 5)

        # Close App
        self.close_button = tk.Button(self.master, text = 'Close', font = 8, command = self.master.destroy)
        self.close_button.grid(row = 7, column = 1, padx = 5)

# =======================
#     Logic Section
# =======================
    def add(self):
        # param for controller
        name = self.name_entry.get()
        pass_ = self.pass_entry.get()

        if name == '' or pass_ == '':
            messagebox.showerror('Error', 'Please fill All Form')

        else:
            print('Insert Data')
            self.controller.insert_controller(name, pass_)

            self.refresh_list()
            messagebox.showinfo('Success', 'Data has been insert')

            # delete from placeholder view
            self.name_entry.delete(0, tk.END)
            self.pass_entry.delete(0, tk.END)

    def refresh_list(self):
        print('View Data')

        self.listbox.delete(0, tk.END)
        
        for row in self.controller.view_controller():
            # insert into column 2 from table database
            self.listbox.insert(tk.END, f'ID: {row[0]}  User: {row[1]}, Pass: {row[2]}')

    def update(self): 

        # param for controller
        up_id = self.update_entry.get()
        up_user = self.name_entry.get()
        up_pass = self.pass_entry.get()

        if up_user == '' or up_pass == '': 
            messagebox.showerror('Error', 'Please fill user or pass form first')

        else: 
            if up_id == '': 
                messagebox.showerror('Error', 'Please fill update form')

            else: 
                print('Update Data')
                self.controller.update_controller(up_user, up_pass, up_id)

                self.refresh_list()
                messagebox.showinfo('Success', 'Data has been updated')

                self.name_entry.delete(0, tk.END)
                self.pass_entry.delete(0, tk.END)
                self.update_entry.delete(0, tk.END)

    def delete(self): 
        
        # param for controller
        del_id = self.delete_entry.get()

        if del_id == '':
            messagebox.showerror('Error', 'Form delete is empty')

        else: 
            print('Delete Data')
            self.controller.delete_controller(del_id)

            self.refresh_list()
            messagebox.showinfo('Success', 'Data has been deleted')

            # delete from placeholder view
            self.delete_entry.delete(0, tk.END)