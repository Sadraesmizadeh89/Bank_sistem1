class Utils:
    def __init__(self,balance = 20000000):
         self.balance = balance
    def withdraw_payment(self):
            pt = True
            while pt:
                payment = int(input('How much money do you want? '
                '(Please note that you cannot withdraw more than 300,000\n' \
                ' Tomans and less than 50,000 Tomans)'))

                if 50000 <= payment <= 300000:
                    self.balance -= payment
                    pt = False
                    return 'Transaction accepted. Please receive the payment.'        


                else:
                    print('The entered number is invalid.')

    def deposit_payment(self):
        deposit = int(input('Enter the amount you want to deposit into your account.'))

        self.balance += deposit
        return'The money has been deposited into your account.'
    
# obj = Utils()

# obj.withraw_payment()
# obj.deposit_payment()