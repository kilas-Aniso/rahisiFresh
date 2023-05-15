class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    def register(self):
        new_user = User()
        return new_user
    def login(self, email, password):
        # method to authenticate user's login credentials
        if self.email == email and self.password == password:
            self.is_logged_in = True
            print("Login successful!")
        else:
            print("Invalid login credentials")
    def logout(self):
        # method to log out the user
        self.is_logged_in = False
        print("Logged out successfully!")

class Admin:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    def register(self):
        new_user = Admin()
        return new_user
    def login(self, email, password):
        # method to authenticate user's login credentials
        if self.email == email and self.password == password:
            self.is_logged_in = True
            print("Login successful!")
        else:
            print("Invalid login credentials")
    def logout(self):
        # method to log out the user
        self.is_logged_in = False
        print("Logged out successfully!")