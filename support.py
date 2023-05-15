class CustomerService:
    def __init__(self, email, phone_number):
        self.email = email
        self.phone_number = phone_number
    def contact_support(self, channel):
        # method to contact customer support through selected channel
        if channel == 'email':
            print(f'kindly send an email to {self.email} for support.')
        elif channel == 'phone':
            print(f'kindly call {self.phone_number} for support.')
        else:
            print('Invalid channel selected.')
