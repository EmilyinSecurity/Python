'''Logic
1. Welcome screen
2. Ask for account number or ID
3. Ask for pin (authentication)
4. Display transction options
5. Withdraw/deposit/balance/exit
'''

#User details
full_name = 'Roronoa Zoro'
account_no = 12345678910
pin = 2025
current_balance = 5000

#ATM screen
print('Welcome to Blue Sea Bank!')
print('=== === === === === === === ===')

account = input('Enter you account number:\n>>')

if int(account) == account_no:
      passcode = input('Enter your 4 digit pin: \n>>')

      if int(passcode) == pin:
         print(f'Welcome {full_name}!')

         #Successful authentication
         print('What would you like to do? \n 1. Deposit \n 2. Withdrawal \n 3. Check Balance \n 4. Exit')
         transaction = input ('>>').strip().lower()

         if transaction == '1' or transaction == 'deposit':
             deposit_amount = int(input('Enter deposit amount:'))

             new_balance = deposit_amount + current_balance
             print(f'Your new balance is {new_balance}')
             print('Thank You for banking with us, {full_name}. Enjoy your day!')

         elif transaction == '2' or transaction == 'withdrawal':
              withdrawal_amount = int(input('Enter amount:'))

              if withdrawal_amount > current_balance:
                  print('Insufficient funds, try again later!')

              else:

                new_balance = current_balance - withdrawal_amount
                print('Please take your cash!')
                print(f'your new balance is {new_balance}. Thank you for banking with us, {full_name}')

         elif transaction == '3' or transaction == 'check balance':
             print(f'Your current balance is {current_balance}')

         elif transaction == '4' or transaction == 'exit':
             print(f'Thank you, {full_name}. Enjoy your day!')

         else:
            print('Invalid option. Try again later!')
        
    
      else:
          print('Incorrect pin, Try again later!')

else:
    print('Invalid user')
          

