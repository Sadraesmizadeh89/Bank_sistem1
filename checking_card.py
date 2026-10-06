class Check_Card:
    def __init__(self,distination_card_number):
        self.distination_card_number = distination_card_number

    def check_luhn(self):
        if self.distination_card_number:
            print('sadra2')
        
        rev_a = [int(x) for x in reversed(self.distination_card_number)]
        total = 0
        for index, num in enumerate(rev_a):
            if index % 2 == 1:
                num *= 2
                if num > 9:
                    num -= 9
            total += num

        if total % 10 == 0:
            print("The card number is valid.")
            
        else:
            print("The card number is invalid.")
            return False

    def get_card_number(self):
            self.check_luhn()
            
            # چک بانک
            banks = {
                '603799': 'Bank Melli Iran',
                '603770': 'Bank Saderat Iran',
                '603769': 'Bank Keshavarzi Iran',
                '589210': 'Bank Sepah',
                '610433': 'Bank Mellat',
                '628023': 'Bank Maskan',
                '627648': 'Export Development Bank of Iran',
                '627961': 'Bank of Industry and Mine',
                '627353': 'Bank Tejarat',
                '589463': 'Refah Bank',
                '639347': 'Bank Pasargad',
                '627412': 'Eghtesad Novin Bank',
                '622106': 'Parsian Bank',
                '627488': 'Karafarin Bank',
                '621986': 'Saman Bank',
                '639346': 'Sina Bank',
                '639607': 'Sarmayeh Bank',
                '502806': 'City Bank',
                '502938': 'Day Bank',
                '627381': 'Ansar Bank',
                '639599': 'Ghavamin Bank'
            }

            if self.distination_card_number.isdigit() and len(self.distination_card_number) == 16:
                prefix = self.distination_card_number[:6]
                bank_name = banks.get(prefix)
                if bank_name:
                    print(f"This card belongs to: {bank_name}")
            
            else:
                print("Invalid card format. Try again.")

