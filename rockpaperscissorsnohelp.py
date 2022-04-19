from random import randint


t = ['Rock', 'Paper', 'Scissors']

computer = t[randint(0,2)]

player = False

while player == False:
    player = input('Rock, Paper, Scissors? ')
    if player == computer:
        print('Tie! ')
    elif player == 'Rock':
        if computer == 'Scissors':
            print('You win! Rock smashes Scissors. ')
        else:
            print('You lose! Paper covers Rock. ')
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose! Rock smashes Scissors. ')
        else:
            print('You win! Scissors cuts paper. ')
    elif player == 'Paper':
        if computer == 'Rock':
            print('You win! Paper covers Rock. ')
        else:
            print('You lose! Scissors cuts Paper. ')
    else:
        print('Please enter valid selection from Rock, Paper, or Scissors. ')
    break


