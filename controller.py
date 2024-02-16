from model import Database

class Controller:
    def __init__(self):
        # init database name
        self.db = Database("sample.db")

    def insert_controller(self, user, _pass): 
        # add data into table - model.py
        self.db.insert_data(user, _pass)

    def view_controller(self): 
        # view data from table - model.py
        return self.db.view_data()
    
    def update_controller(self, username, password, id_data): 
        # update data from table - model.py
        return self.db.update_data(username, password, id_data)

    def delete_controller(self, id): 
        # delete data from table model.py
        self.db.delete_data(id)
