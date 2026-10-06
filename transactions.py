import random
from checking_card import Check_Card
import json

class Found_transfer: 
    def __init__(self,balance,audience_balance,distination_card_number= '0'):
        self.balance = balance
        self.a_balance = audience_balance
        self.save_information = []
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
                try:
                    # print(repr(self.central_data))
                    self.distination_card_number = input("Enter the distination_card_number number: ").strip()   # ,

                    found = False

                    for central in self.central_data:
                        if self.distination_card_number == central['card_number']:
                            found = True

                            if central['is_active'] == 'True':
                                print(f'This card belongs to: {central["user_name"]}')
                            else:
                                print('This card is not active')

                            break

                    if not found:
                        raise ValueError('Enter a valid destination card number')

                    if self.distination_card_number.isdigit():
                        flag = False
                    else:
                        raise ValueError('Enter a valid value')
                except:
                    print('Enter a valid value')
                        
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
            if (self.balance['balance'] - 20000) >= transfer:
                self.balance['balance'] -= transfer
                self.a_balance['balance'] += transfer
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
    def sheba(self):
        print('Transaction is above 10,000,000 Toman. Using Sheba instead.')

        transfer = int(input('Enter the amount to be transferred: '))

        self.balance['balance'] -= transfer
        self.a_balance['balance'] += transfer

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