
#TIC TAC TOE

BOARD = [[0, 0, 0],
	 [0, 0, 0],
 	[0, 0, 0]]

def game(BOARD):
	i = 0
	for row in BOARD:
		print(row)
	for row in BOARD:
		while i < 9:
			row_, column_ = input("enter row number and column number of the "
					     "cell you wish to draw on").split()

			if int(row_)> 3 or int(column_)> 3:
				print("Error: the board only has 3 rows and 3 columns. Please"
				      " try inputting again")
				i = i -2
			else:
				row_position = (int(row_) -1)
				column_position = (int(column_) -1)
				if BOARD[row_position][column_position] != 0:
					print("sorry, that square is already taken, please"
					      " pick another square")
					continue
				if i % 2 == 1:
					BOARD[row_position][column_position] = "X"
					i += 1
				elif i % 2 == 0:
					BOARD[row_position][column_position] = "*"
					i += 1

				print(BOARD[0])
				print(BOARD[1])
				print(BOARD[2])

			#horizontal rows win conditions
			for row in BOARD:
				if row == ["X", "X", "X"]:
					print("Player X has Won!")
					i = 9
				elif row == ["*", "*", "*"]:
					print("Player * has Won!")
					i = 9

			#vertical rows win conditions
			for j in range(0, 3):
				if BOARD[0][j] == BOARD[1][j] == BOARD[2][j] == "X":
					print("Player X has Won!")
					i = 9

				elif BOARD[0][j] == BOARD[1][j] == BOARD[2][j] == "*":
					print("Player * has Won!")
					i = 9

			#diagonal win conditions
			if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == "X":
					i = 9
					print("Player X has Won!")
			elif BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == "*":
					i = 9
					print("Player * has Won!")
			elif BOARD[2][0] == BOARD[1][1] == BOARD[0][2] == "*":
					i = 9
					print("Player * has Won!")
			elif BOARD[2][0] == BOARD[1][1] == BOARD[0][2] == "X":
					i = 9
					print("Player X has Won!")
			elif i == 8:
				print("It's a Tie!")
				i += 1
issing-function-docstring)
TIC-TAC-TOE.py:8:9: W0621: Redefining name 'board' from outer scope (line 4) (redefined-outer-name)

game(BOARD)
