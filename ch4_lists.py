# working with lists

# catNames = []

# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] #list concatenation

# print('The cat names are:')
# for name in catNames:
#     print('' + name)
        
# -------------------------------

# using for loops with lists

# for i in range(4):
#     print(i)

# -------------------------------

# using for loops with lists another example

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# -------------------------------

# example program: magic 8 ball with a list

# import random

# messages = [
#     'It is certain',
#     'Yes decidedly so',
#     'Reply hazy try again', 
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful'
# ]

# print(messages[random.randint(0, len(messages) - 1)])

# -------------------------------

# a short program: Conway's Game of Life
# Conway’s Game of Life is an example of cellular automata: a set of rules governing the behavior of a field made up of discrete cells.
# more Python studio games - https://github.com/asweigart/pythonstdiogames

# import random, time, copy

# WIDTH = 60
# HEIGHT = 20

# # Create a list of list for the cells:
# nextCells = []

# for x in range(WIDTH):
#     column = [] # create a new column
#     for y in range(HEIGHT):
#         if random.randint(0, 1) == 0:
#             column.append('#') # add a living cell
#         else:
#             column.append('') # add a dead cell
#     nextCells.append(column) # nextCells is a list of column lists
    
# while True: # main program loop
#     print('\n\n\n\n\n') # separate each step with newlines
#     currentCells = copy.deepcopy(nextCells)
    
#     # Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end='') # print the # or space
#         print() # print a new line at the end of the row
    
#     # Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             # get neighboring coordinates
#             # '% WIDTH' ensures leftCoord is always between 0 and WIDTH -1
#             leftCoord = (x - 1) % WIDTH
#             rightCoord = (x + 1) % WIDTH
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT
            
#             # Count number of living neighbors:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1 # Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1 # Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1 # Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1 # Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1 # Bottom-right neighbor is alive.
            
#             # Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
#                 # Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == ' ' and numNeighbors == 3:
#                 # Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                 # Everything else dies or stays dead:
#                 nextCells[x][y] = ' ' 
#                 time.sleep(1) # Add a 1-second pause to reduce flickering.