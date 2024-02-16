import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

        self.table_name = 'users'
        self.create_table()

    def create_table(self): 
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.table_name} 
                         (id INTEGER PRIMARY KEY, 
                         name TEXT, 
                         password TEXT)''')
        self.conn.commit()
        
    def insert_data(self, username, password):
        self.cur.execute(f'''INSERT INTO {self.table_name} 
                         VALUES (NULL, ?, ?)''', 
                         (username, password))
        self.conn.commit()

    def view_data(self):
        self.cur.execute(f'''SELECT * FROM {self.table_name}''')
        rows = self.cur.fetchall()
        return rows
    
    def update_data(self, username, password, id_data): 
        self.cur.execute(f'''UPDATE {self.table_name} 
                         SET name=?, password=? 
                         WHERE id=?''', 
                         (username, password, id_data))
        self.conn.commit()
    
    def delete_data(self, id_data): 
        self.cur.execute(f'''DELETE FROM {self.table_name} 
                         WHERE id=?''', 
                         (id_data))
        self.conn.commit()

    def upload_file(self, username, password, file_up): 
        self.cur.execute(f'''INSERT INTO {self.table_name} 
                         VALUES (NULL, ?, ?, ?)''', 
                         (username, password, file_up))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
