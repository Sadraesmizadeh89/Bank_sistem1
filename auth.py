import time
from datetime import datetime
import json

class AuthManager:

    def __init__(self):

        self.failed_count = 0
        with open('./save_new_account.json', 'r') as file:
            self.users =  json.load(file)


    # ---------------- LOGIN ----------------

    def login(self):
        while self.failed_count < 5:
            username = self.get_username()
            password = self.get_password()
            #print(password)

            # print(repr(username))
            # print(repr(password))
            user = self.athentication(username,password)
            print(user)

            if user:
                print('welcome to your account!')

                self.failed_count = 0

                if self.check_card_expiry(user):
                    print('your expiry card is valid')
                    return user
                else:
                    print('your expiry card is invalid')
                    return False
            else:
                self.failed_count += 1

                print('username or password is incorrect')

                delay = self.failed_count * 5
                print(f'you must be wait {delay} seconds.')
                time.sleep(delay)

        print('you have most 5 faults.try again later ')
        return False
    
    def get_username(self):
        username = input('Enter your username :').strip()

        if (len(username) < 8):
            print('your username is invalid!')
        else:
            return username

    def get_password(self):    
        password = input('Enter your password :').strip()

        if len(password) >= 8:
            return password
        else:
            return False

    def athentication(self, username, password):
        for user in self.users:
            # print(repr(user['user_name']))
            # print(repr(user['password']))
            if (
                username == user['user_name'] 
            and password == user['password']
            ):
                print('your username and password is correct!')
                return user
            
        return None
        
    # ---------------- CARD CHECK ----------------

    def check_card_expiry(self, user):
        # print(user)

        expiry = user["expiry"]

        month_s, year_s = expiry.split("/")   #08/06

        month = int(month_s)
        year = int("20" + year_s)

        today = datetime.now()

        if (year, month) >= (today.year, today.month):

            return True

        return False


# ---------------- USERS ----------------



# ---------------- RUN ----------------

# obj = AuthManager()

# obj.login()