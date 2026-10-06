import json
import string


class Save:
    def __init__(self, save_line,save_file,user):
        self.user = user 
        self.save_file = save_file
        self.save_line = save_line

        self.dic_information = {
            'card_number':None,
            'user_name': None,
            'password': None,
            'expiry': None,
            'cvv2':None,
            'id':None
        }

        with open('./save_new_account.json', 'r') as safi:  # safi --> save_file
            content = safi.read()

            if not content:
                self.save_line = []
            else:
                safi.seek(0)
                self.save_line = json.load(safi)

            safi.seek(0)
            self.user = json.load(safi)

    def add_new_account(self):

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
        # print(self.save_line)

        for i in self.user:
            # print(self.save_line)
            result +=1
        # print(result)
        # print(result)

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


# obj = Save('','')
# obj.add_new_account()