import json

class Found_transaction:
     def find_transaction(self):
            found = True
            while found:
                find_transation = input('Enter your tracking code: ')
            
                try:
                    with open('./bank.json', 'r') as file_read:
                        lines = json.load(file_read)
                except FileNotFoundError:
                    print("No transaction record found (bank.txt missing).")

                # print(lines)
                for l in lines:
                    if find_transation in l['tracking code']:
                        print('Transaction found:', l)
                        found = False
                        break

                if found:
                 print('Tracking code not found. Please try again.')

# obj = Found_transaction()

# obj.find_transaction()