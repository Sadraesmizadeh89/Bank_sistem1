import json
import string

class Staf:
    def __init__(self,user,tracking_code,save_line):
        self.user = user 
        self.tracking_code = tracking_code
        self.save_line = save_line

        self.dic_information = {
            'card_number':None,
            'user_name': None,
            'password': None,
            'expiry': None,
            'cvv2':None,
            'id':None
        }
        with open('./save_new_account.json','r') as use:       # use --> user
            self.user = json.load(use)
        with open('./bank.json','r') as bank:
            self.tracking_code = json.load(bank)
        

    def read_user_account(self):
        get_user_information = int(input('Enter the user id :'))

        for user in self.user:
            if get_user_information == user['id']:
                print(user)

    def reviewing_transactions(self):
        get_tracking_code = input('Enter the traking code for display transaction details:')
        print(type(get_tracking_code))

        for tk in self.tracking_code:
            if get_tracking_code == tk['tracking code']:
                print(tk)
                break
        else:
            print('no such code exists')

    def create_a_new_account_for_the_user(self):
        with open('./save_new_account.json', 'r') as file:
            content = file.read()

            if not content:
                self.save_line = []
            else:
                file.seek(0)
                self.save_line = json.load(file)

        user_name = input('Enter a user name for your account:')
        expiry = input('Enter a expiry for your account:')
        cvv2 = input('Enter your cvv2 card:')

        result1 = self.get_card_number()

        if not result1:
            print(result1)
            return False
        
        result2 = self.check_password_complate()

        if not result2:
            print(result2)
            return False

        result = 0

        for i in self.user:
            result += 1

        self.dic_information['user_name'] = user_name
        self.dic_information['expiry'] = expiry
        self.dic_information['cvv2'] = cvv2
        self.dic_information['id'] = result + 1

        self.save_line.append(self.dic_information)

        with open('./save_new_account.json', 'w') as f:
            json.dump(self.save_line, f, indent=5)

    def check_password_complate(self):
        try_password = True
        while try_password:
            password = input('Enter a password for your account:')

            if any(i in string.punctuation for i in password):
                if any(i in string.ascii_letters for i in password):
                    if any(i in string.ascii_lowercase for i in password):
                        if any(i in string.ascii_uppercase for i in password):
                            if any(i in string.digits for i in password):
                                if len(password) >= 8:
                                    print('sgin up successful')
                                    self.dic_information['password'] = password
                                    return password

                                else:
                                    print('your password is not more than 8')
                                    continue
                            else:
                                print('your password do not have digit')
                                continue
                        else:
                            print('your password do not have ascii_uppercase')
                            continue
                    else:
                        print('your password do not have ascii_lowercase')
                        continue
                else:
                    print('your password do not have ascii_letters')
                    continue
            else:
                print('your password do not have punctuation')
                continue

    def get_card_number(self):
        card_number = input('Enter your card number:')

        if card_number:
            rev_a = [int(x) for x in reversed(card_number)]
            total = 0
            for index, num in enumerate(rev_a):
                if index % 2 == 1:
                    num *= 2
                    if num > 9:
                        num -= 9
                total += num

            if total % 10 == 0:
                print("The card number is valid.")
                self.dic_information['card_number'] = card_number
                return card_number
                
            else:
                print("The card number is invalid.")
                return False

    def delete_user(self):
        delete_id = int(input("Enter user ID: "))

        for user in self.user:
            if user["id"] == delete_id:
                self.user.remove(user)
                # print(self.user)
                with open('./save_new_account.json', 'w') as pir_mard_mehraboon:
                    json.dump(self.user, pir_mard_mehraboon, indent=5)
                    print('account deleted')
                break
        else:
            print('this id not found!')
            self.delete_user()

# obj = Staf('','','')
# # obj.read_user_account()
# # obj.reviewing_transactions()
# # obj.create_a_new_account_for_the_user()
# obj.delete_user()