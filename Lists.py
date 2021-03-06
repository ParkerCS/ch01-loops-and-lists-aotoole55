# Everything works.  Well done.  

#LISTS (35PTS TOTAL)
#In these exercises you write functions. Of course, you should not only write the functions,
#you should also write code to test them. For practice, you should also comment your
#functions as explained above.



#PROBLEM 1 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

import random

for i in range(1):
    j = random.randrange(20)
    print(answer_list[j])



# PROBLEM 2 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
suit_list = ['Heart', 'Diamond', 'Club', 'Spade']
value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

playing_cards = []
shuffled_deck = []

for i in range(1):
    for j in range(len(value_list)):
        for k in range(4):
            playing_cards.append([suit_list[k], value_list[j]])
    print(playing_cards)

def shuffle_deck():
    for l in range(len(playing_cards)):
        m = random.randrange(len(playing_cards))
        shuffled_deck.append(playing_cards[m])
        playing_cards.remove(playing_cards[m])

shuffle_deck()
print(shuffled_deck)



# PROBLEM 3 (The sieve of Eratosthenes - 10pts)
# The sieve of Eratosthenes is a method to find all prime numbers between
# 1 and a given number using a list. This works as follows: Fill the list with the sequence of
# numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime.
# Now loop over the list. Find the next number on the list that is not zero,
# which, at the start, is the number 2. Now set all multiples of this number to zero.
# Then find the next number on the list that is not zero, which is 3.
# Set all multiples of this number to zero. Then the next number, which is 5
# (because 4 has already been set to zero), and do the same thing again.
# Process all the numbers of the list in this way. When you have finished,
# the only numbers left on the list are primes.
# Use this method to determine all the primes between 1 and 1000.

number_list = []

for i in range(1001):
    number_list.append(i)
    if number_list[i] == 1:
        number_list[i] = 0

for val in number_list:
    if val != 0:
        for i in range(len(number_list)):
            if number_list[i] % val == 0 and number_list[i] != val:
                number_list[i] = 0
print(number_list)


# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

# The main program will be something along the lines of (in pseudo-code):
# display board

row = ([1,2,3])
column = ([1,2,3])
move = []

def draw_board(board):
    print("   |   |")
    print(" "+ board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("-------------")
    print(" "+ board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("-------------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("   |   |")


board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
total = 0

def winner():
    done = True

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                print("X wins!")
                done = False
            elif board[i][0] == "O":
                print("O wins!")
                done = False

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                print("X wins!")
                done = False
            elif board[0][i] == "O":
                print("O wins!")
                done = False

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            print("X wins!")
            done = False
        elif board[0][0] == "O":
            print("O wins!")
            done = False


    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            print("X wins!")
            done = False
        elif board[0][2] == "O":
            print("O wins!")
            done = False

    return done


done = True
player = 1

while done:
    user_input_row = int(input("Enter a row (0-2): "))

    if user_input_row > 2 or user_input_row < 0:
        print("Not in interval.")
        user_input_row = int(input("Enter a row (0-2): "))

    user_input_column = int(input("Enter a column (0-2): "))

    if user_input_column > 2 or user_input_column < 0:
        print("Not in interval.")
        user_input_column = int(input("Enter a column (0-2): "))

    if board[user_input_row][user_input_column] != " ":
        print("Error. That space is taken")
        continue

    elif player == 1:
        board[user_input_row][user_input_column] = "X"
        total +=1
        player = 2

    elif player == 2:
        board[user_input_row][user_input_column] = "O"
        total +=1
        player = 1

    if total >= 9 and winner():
        print("It's a tie!")
        done = False

    if not winner():
        draw_board(board)
        break

    draw_board(board)




# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player

# CHALLENGE PROBLEM 5 (Battleship NO CREDIT, JUST IF YOU WANT TO TRY IT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
