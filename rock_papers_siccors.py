print("="*19)
print("Rock Paper Scissors")
print("="*19)
print()
print("1) ✊")
print("2) ✋")
print("3) ✌️")

while True:
    player = int(input('\nEnter a number!'))
    if player < 1 or player > 3:
        print('\n --  |E R R O R|  enter only from 1 to 3 inclusive -- ')
    else:
       break

import random
computer = random.randint(1, 3)

choices = {1: '✊', 2: '✋', 3: '✌️'}

print(f'\n you chose      :{choices[player]}')
print(f'\n computer chose :{choices[computer]}')

if player == computer:
    print('='*40)
    print('-- Its a tie! --')
    print('='*40)
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
    print('='*40)
    print('-- Player won!! --')
    print('='*40)
else:
    print('='*40)
    print('-- computer won!! --')
    print('='*40)
