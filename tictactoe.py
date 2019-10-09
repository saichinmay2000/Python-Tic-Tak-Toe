from __future__ import print_function			//which allows to print the program in which ever the python a user uses without changing the code s we used __future__

choices = []						//This allows to initialize an array of name choice.				

for x in range (0, 9) :
    choices.append(str(x + 1))				//Using the for loop to take the input of the numbers the user inputs..

playerOneTurn = True					//Making the dirst user to start the game so we made that true
winner = False						//to calculate winner at the end of the game first we made it to false

def printBoard() :					//we created a definition of the board which prints the structure of the board
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')

while not winner :					//If the user is not winner then obviously the loop should be continued so we are printing the board again..
    printBoard()

    if playerOneTurn :
        print( "Player 1:")				//Using the if-else coz to know the turn of the player and printing in the output.
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))			//Then taking the input from the respective player.. 
    except:
        print("please enter a valid field")		//Checking the suitable input
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':		//The input must satisfy the following conditions as per the requirements
        print("illegal move, plase try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'			//Player one is handelling X
    else :
        choices[choice - 1] = 'O'			//Player two is handelling O

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")		//At last we are printing the total board and the winner..
