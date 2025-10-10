import random
choices = {1: '✊', 2: '✋', 3: '✌️'}

#=====================================

def banner():
   print("="*35)
   print("--- Rock Paper Scissors---")
   print("="*35)
   print("---> Pick a move;")
   print("\n1) ✊")
   print("2) ✋")
   print("3) ✌️")
   print()
   print("="*35)

def show_inputs(player, computer):
    print(f'\n=== ---> You chose : {choices[player]}')
    print(f'=== ---> Computer chose : {choices[computer]}')
 
def victory_message():
   if player_move == computer_move:
      print('\n === 💨Its a Tie!😒 === ')
   elif player_move == 1 and computer_move == 3 or player_move == 2 and computer_move == 1 or player_move == 3 and computer_move == 1:
      print('\n === 👏You Won!🎉 === ')
   else:
      print('\n === 😔Computer Won!😥 ===')


banner()

while True:
    player_move = (int(input('\n --> Enter your move! : ')))
    if player_move < 0 or player_move > 3:                   # --> Take player's move
       print('\n === ---> 🤦Enter a Valid move bhai! === ')
    else:
       break

computer_move = random.randint(1, 3)                # --> Take computer's move
show_inputs(player_move, computer_move)             # --> Show both moves
victory_message()                                   # --> Show who won
