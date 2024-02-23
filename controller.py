from model import Database

class Controller:
    def __init__(self):
        # init database name
        self.db = Database("sample.db")

    def insert_controller_sample(self, user, _pass): 
        # add data into table - model.py
        self.db.insert_tb_sample(
            username = user, 
            password = _pass
        )

    def view_controller(self): 
        # view data from table - model.py
        return self.db.view_data()
    
    def update_controller(self, username, password, id_data): 
        # update data from table - model.py
        return self.db.update_data(
            username = username, 
            password = password, 
            id = id_data
        )

    def delete_controller(self, id_data): 
        # delete data from table model.py
        self.db.delete_data(id = id_data)

    def upload_file(self): 
        print('save file')

    def update_file(self): 
        print('update file')

    def download_data(self): 
        print('download data')

    def download_file(self): 
        print('download file')

    def reg_data(self, email_, username_, password_, contact_): 
        self.db.insert_tb_users(
            email = email_, 
            username = username_, 
            password = password_, 
            contact = contact_
        )