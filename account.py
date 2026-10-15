class Account:
    def __init__(self,balance='20000000',card_password = '3024'):
        self.balance = balance
        self.card_password = card_password

    def account_balance(self):
        return f'Your account balance is equal to :{self.balance}'
    def changing_password(self):
        password1 = input('Please enter your desired password ' /
                          '(make sure the password is 4 digits long):')
        
        password2 = input('Please enter your desired password again ' /
                          '(make sure the password is 4 digits long):')

        
        if len(password1) == 4 and len(password2) == 4 and password1 == password2:
            self.card_password = password1
            return 'password changed'
        else:
            return 'You did not perform the operation correctly. Please try again.'
# obj = Account()

# print(obj.account_balance())
# print(obj.changing_password())