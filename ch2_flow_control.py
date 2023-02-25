# ending a program early with sys.exit() function
# infinite loop where user must enter exit to activate sys.exit() to stop the program

# import sys

# while True:
#     print('type exit to exit')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('you typed' + response + '.')

# -------------------------------

# a short program: guess the number

# import random
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')

# # ask the player to guess 6 times
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())
    
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high.')
#     else:
#         break # This condition is the correct guess!
    
# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))

# -------------------------------

# a short program: rock, paper, scissors

# import random, sys

# print('ROCK, PAPER, SCISSORS')

# # these variables keep track of the number of wins, losses, and ties
# wins = 0
# losses = 0
# ties = 0

# while True: #the main game loop
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True: #the player input loop
#         print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit() #quit the program
#         if playerMove == 'r' or playerMove == 's':
#             break # break out of the player loop
#         print('Type one of r, p, s, or q.')
    
#     # Display what the player chose:
#     if playerMove == 'r':
#         print('Rock versus...')
#     elif playerMove == 'p':
#         print('Paper versus...')
#     elif playerMove == 's':
#         print('Scissors versus...')
        
#     # Display what the computer chose:
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print('PAPER')
#     elif randomNumber == 3:
#         computerMove = 's'
#         print('SCISSORS')
        
#     # Display and record the win/loss/tie:
#     if playerMove == computerMove:
#         print('It is a tie!')
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print('You lose!')
#         losses = losses + 1