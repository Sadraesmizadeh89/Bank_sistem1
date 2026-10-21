import random
from checking_card import Check_Card
import json

class Found_transfer: 
    def __init__(self,balance,audience_balance,distination_card_number= '0',user_id='',dist_id=''):
        self.balance = balance
        self.a_balance = audience_balance
        self.save_information = []
        self.user_id = user_id
        self.dist_id = dist_id
        self.record_tracking_code = {
            "distination_card_number":None,
            "transfer":None,
            "tracking code":None
                }
        self.distination_card_number = distination_card_number

        with open('./centeral_bank.json','r') as cb:
                self.central_data = json.load(cb)

        with open('./save_new_account.json', 'r') as bal:
            self.balance = json.load(bal)

        with open('./centeral_bank.json', 'r') as bal_audience:
            self.a_balance = json.load(bal_audience)

    def found_transfer(self):
        with open('./bank.json', 'r') as file:
            content = file.read()
            
            # print(bool(content))
            if not content:
                self.save_information = []
            else:
                file.seek(0)
                self.save_information = json.load(file)

        flag = True

        while flag:
            self.distination_card_number = input("Enter the destination card number: ").strip()

            if not self.distination_card_number.isdigit():
                print('Enter a valid card number')
                continue

            found = False

            for index, central in enumerate(self.central_data):
                if self.distination_card_number == central['card_number']:
                    found = True

                    if central.get('is_active') == 'True':
                        print(f'This card belongs to: {central["user_name"]}')

                        self.dist_id = index
                        flag = False
                    else:
                        print('This card is not active')

                    break

            if not found:
                print('Enter a valid destination card number')
                        
        obj =  Check_Card(self.distination_card_number)
        print('sadra')
        if obj.check_luhn() == False:
            self.found_transfer()
        else:
            print(obj.check_luhn())
        while True:
            transfer = int(input('Enter the amount to be transferred: '))
            if transfer > 5000:
                break
            else:
                print('Enter a valid amount')
        if transfer <= 10000000:
            # print(type(self.balance))
            # print(self.balance)
            if (self.balance[self.user_id]['balance'] - 20000) >= transfer:

                self.balance[self.user_id]['balance'] -= transfer
                self.a_balance[self.dist_id]['balance'] += transfer
                # self.w_central_data['balance'] += transfer

                randoms_number = [str(i) for i in range(1, 11)]
                k_r = random.sample(randoms_number, 5)
                k_r_str = ''.join(k_r)
                self.tracking_code = k_r_str
                # print(k_r_str)
                print(f'Your tracking code is: {k_r_str}')

                self.record_tracking_code['distination_card_number'] = self.distination_card_number
                self.record_tracking_code['transfer'] = transfer
                self.record_tracking_code['tracking code'] = k_r_str

                self.save_information.append(self.record_tracking_code)

                with open('./bank.json', 'w', encoding='utf-8') as bank:
                    json.dump(self.save_information, bank, indent=5)

                return 'The amount has been transferred.'
            
        elif transfer > 10000000:
            self.sheba()
        
        else:
            return 'Sheba transaction completed.'

        with open('./centeral_bank.json', 'w') as wbicb: #  wbicb-->write balance in centeral bank
            json.dump(self.a_balance, wbicb)

    def sheba(self):
        print('Transaction is above 10,000,000 Toman. Using Sheba instead.')

        transfer = int(input('Enter the amount to be transferred: '))

        self.balance[self.user_id]['balance'] -= transfer
        self.a_balance[self.dist_id]['balance'] += transfer

        randoms_number = [str(i) for i in range(1, 11)]
        k_r = random.sample(randoms_number, 5)
        k_r_str = ''.join(k_r)
        self.tracking_code = k_r_str
        # print(k_r_str)
        print(f'Your tracking code is: {k_r_str}')

        self.record_tracking_code['distination_card_number'] = self.distination_card_number
        self.record_tracking_code['transfer'] = transfer
        self.record_tracking_code['tracking code'] = k_r_str

        self.save_information.append(self.record_tracking_code)

        with open('./bank.json', 'w', encoding='utf-8') as bank:
            json.dump(self.save_information, bank, indent=5)

        return 'The amount has been transferred.'

# obj = Found_transfer(2000000)

# obj.found_transfer()