import random as a

def play_game():
    choices = ['rock', 'paper', 'scissors']
    player1 = a.choice(choices)
    player2 = a.choice(choices)
    
    while True:
        print(f'Player 1 Choice : {player1}')
        print(f'Player 2 Choice : {player2}')
        
        if player1 == player2:
            print("Tie")
            
play_game()