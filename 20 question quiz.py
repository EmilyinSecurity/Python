# First python quiz out of 20 points by Emily Mankge

print('Welcome to the "what do you know?" quiz!')
print('Use strings for your first 10 answers. \n>>')

name = input('What is your name? \n>>')
print(f"It's good to have you here, {name}!")
print(" === === === === === === === === === === ")

score = 0

print('1. What is the longest river in Africa? \n')
answer = input('>>').lower()

if answer == 'the nile' or answer == 'nile':
    score += 1
    print(f'Correct! you have {score} point!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('2. What colour is the sky on a clear day?\n')
answer = input('>>').lower()

if answer == 'blue':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('3. How many days are in a week? \n')
answer = input('>>').lower()

if answer == 'seven':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('4. How many sides does a triangle have? \n')
answer = input('>>').lower()

if answer == 'three':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('5. What air do humans breathe in to stay alive? \n')
answer = input('>>').lower()

if answer == 'oxygen':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('6. What continent is Botswana in? \n')
answer = input('>>').lower()

if answer == 'africa':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('7. How many continents are there in the world? \n')
answer = input('>>').lower()

if answer == 'seven':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('8. What is the opposite of day? \n')
answer = input('>>').lower()

if answer == 'night':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('9. What is the 4th month of the year? \n')
answer = input('>>').lower()

if answer == 'april':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === === ")

print('10. Who wrote the play "Romeo and Julliet"?\n')
answer = input('>>').lower()

if answer == 'william Shakespeare' or answer == 'shakespeare':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === ===\n ")

print('Now, moving to mathematical questions!\n Answer with numbers only')
print('+++ +++ +++ +++ +++ +++ +++ +++ +++ +++')

print('11. What is 100/4? \n')
answer = input('>>')

if answer == '25':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('12. What is the square root of 49? \n')
answer = input('>>')

if answer == '7':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('13. What is 15% of 200? \n')
answer = input('>>')

if answer == '30':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('14. If a car travels 60km in 2hrs, what is the average speed in(km/h)? \n')
answer = input('>>')

if answer == '30':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === ===")

print('15. How many degrees are there in a full circle? \n')
answer = input('>>')

if answer == '360':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('16. What is the smallest prime number? \n')
answer = input('>>')

if answer == '2':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('17. How many zeros are in one million? \n')
answer = input('>>')

if answer == '6':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === == ")

print('18. What is the largest two-digit even number? \n')
answer = input('>>')

if answer == '98':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print(" === === === === === === === === === === ")

print('19. What is the missing number in the sequence: 2, 4, _, 8?\n')
answer = input('>>')

if answer == '6':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print("=== === === === === === === === === === ")

print('20. What is the next prime number after 7?\n')
answer = input('>>')

if answer == '11':
    score += 1
    print(f'Correct! you have {score} points!')

else:
    print('Incorrect!')
print("=== === === === === === === === === === ")

#Final score
print('\nYou scored' , score, 'out of 20!')

if score in range(18,21):
    print('FINAL GRADE: A1')
    
if score in range(16,18):
    print('FINAL GRADE: B2')
    
if score in range(14,16):
    print('FINAL GRADE: B3')

if score in range(12,14):
    print('FINAL GRADE: C4')

if score in range(10,12):
    print('FINAL GRADE: C5')

if score in range(8,10):
    print('FINAL GRADE: C6')

if score in range(6,8):
    print('FINAL GRADE: D7')

if score in range(4,6):
    print('FINAL GRADE: E8')

if score in range(0,4):
    print('FINAL GRADE: F9')
    
#QUIZ GAME CREATED by EMILY MANKGE
