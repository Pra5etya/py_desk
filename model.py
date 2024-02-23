import sqlite3
import bcrypt
from tkinter import messagebox

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        self.tb_sample_data = 'sample_data'
        self.tb_sample_personal = 'sample_personal'

        self.tb_users = 'users'
        self.tb_personals = 'users_personals'

        self.create_table()

    def create_table(self): 
        # Table Sample Data
        # ===========================
        self.cur.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.tb_sample_data} (
            id INTEGER PRIMARY KEY, 
            username VARCHAR UNIQUE NOT NULL, 
            password VARCHAR NOT NULL
            )'''
        )


        # # Table Sample Personal
        # # ===========================
        # self.cur.execute(
        #     f'''CREATE TABLE IF NOT EXISTS {self.tb_sample_personal} (
        #     id Integer PRIMARY KEY, 
        #     {self.tb_sample_data}_id VARCHAR NOT NULL, 
        #     file_location VARCHAR NOT NULL, 
        #     FOREIGN KEY ({self.tb_sample_data}_id) REFERENCES {self.tb_sample_data}(id)
        #     )'''
        # )


        # Table Users
        # ===========================
        self.cur.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.tb_users} (
            email VARCHAR PRIMARY KEY NOT NULL, 
            username VARCHAR UNIQUE NOT NULL, 
            password VARCHAR NOT NULL, 
            contact INTEGER UNIQUE NOT NULL
            )'''
        )

        self.conn.commit()

        # Table Users - personal data
        # ===========================
        self.cur.execute(
            f'''CREATE TABLE IF NOT EXISTS {self.tb_sample_personal} (
            id Integer PRIMARY KEY, 
            {self.tb_sample_data}_id VARCHAR NOT NULL, 
            file_location VARCHAR NOT NULL, 
            FOREIGN KEY ({self.tb_sample_data}_id) REFERENCES {self.tb_sample_data}(id)
            )'''
        )

#       CHIPPER ONE-WAY
# =================================        
    def create_chipper(self, text): 
        print('create chipper')
        
        salt_ = bcrypt.gensalt()
        bytes = text.encode()

        hashed = bcrypt.hashpw(password = bytes, salt = salt_)
        
        return hashed
    
    def check_chipper(self, text, chipper): 
        bytes = text.encode()
        return bcrypt.checkpw(password = bytes, hashed_password = chipper)

#       ENCRYPT & DECRYPT
# =================================
    def encrypt_data(): 
        print('enkripsi')

    def decrypt_data(): 
        print('dekripsi')

#       INSERT SECTIONS
# =================================
    def insert_tb_sample(self, username, password):
        # Table Users
        # ===========================
        self.cur.execute(
            f'''INSERT INTO {self.tb_sample_data} (
            id, username, password
            ) 
            VALUES (NULL, ?, ?)''', 
            (username, password)
        )

        self.conn.commit()

    def insert_tb_users(self, email, username, password, contact):
        # chipper
        email_chipper = self.create_chipper(email)
        password_chipper = self.create_chipper(password)
        contact_chipper = self.create_chipper(contact)

        self.cur.execute(
            f'''SELECT * FROM {self.tb_users} (
            WHERE email = ?
            )''', 
            (email_chipper)
        )
        if self.cur.fetchone(): 
            messagebox.showerror("Error", "Email already exists")

        self.cur.execute(
            f'''SELECT * FROM {self.tb_users} (
            WHERE username = ?
            )''', 
            (username)
        )

        if self.cur.fetchone(): 
            messagebox.showerror("Error", "Username already exists")

        self.cur.execute(
            f'''SELECT * FROM {self.tb_users} (
            WHERE contact = ?
            )''', 
            (contact_chipper)
        )

        if self.cur.fetchone(): 
            messagebox.showerror("Error", "Contact already exists")

        self.cur.execute(
            f'''INSERT INTO {self.tb_users} (
            email, username, password, contact
            )
            VALUES (?, ?, ?, ?)''', 
            (email_chipper, username, password_chipper, contact_chipper)
        )



        self.conn.commit()


#       VIEW SECTIONS
# =================================
    def view_data(self):
        self.cur.execute(
            f'''SELECT * FROM {self.tb_sample_data}'''
        )

        rows = self.cur.fetchall()
        return rows

    def view_file(self): 
        self.cur.execute(
            f'''SELECT * FROM {self.tb_sample_personal}'''
        )

        rows = self.cur.fetchall()
        return rows
    

#       UPDATE SECTIONS
# =================================
    def update_data(self, username, password, id): 
        self.cur.execute(
            f'''UPDATE {self.tb_sample_data} 
            SET username = ?, password = ? 
            WHERE id = ?''', 
            (username, password, id)
        )
    

#       DELETE SECTIONS
# =================================
    def delete_data(self, id): 
        self.cur.execute(
            f'''DELETE FROM {self.tb_sample_data} 
            WHERE id = ?''', 
            (id)
        )

        self.conn.commit()


#   UPLOAD & DOWNLOAD SECTIONS
# =================================
    def update_file(self, file_update, uuid, username): 
        self.cur.execute(
            f'''UPDATE  {self.tb_sample_data} 
                         SET file_location = ? 
                         WHERE uuid = ? & name = ?''', 
                         (file_update, uuid, username)
        )

        self.conn.commit()

    def download_data(self, id_data): 
        self.cur.execute(f'''SELECT name FROM {self.tb_sample_data} 
                        WHERE id=?''', (id_data))
        
        self.conn.commit()    


#       CLOSED CONNECTIONS
# =================================
    def __del__(self):
        self.conn.close()
