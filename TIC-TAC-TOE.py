#TIC TAC TOE

board = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

def game(board):
	i = 1
	for row in board:
		print(row)

	for row in board:
		while i < 9:
			row_, column_ = input("enter row number and column number of the " 
					"cell you wish to draw on").split()

			if int(row_) > 3 or int(column_) >3:
				print("Error: the board only has 3 rows and 3 columns. Please"
				" try inputting again")
				i = i -2
			else:
				row_position = (int(row_) -1)
				column_position = (int(column_) -1)
				if board[row_position][column_position] != 0:
					print("sorry, that square is already taken, please"
					" pick another square")
					continue
				if i % 2 == 1:
					board[row_position][column_position] = "X"
					i += 1
				elif i % 2 == 0:
					board[row_position][column_position] = "*"
					i += 1

				print(board[0])
				print(board[1])
				print(board[2])

			for row in board:
				if row == ["X", "X", "X"]:
					print("Player X has Won!")
					i = 9
				elif row == ["*", "*", "*"]:
					print("Player * has Won!")
					i = 9

				else:
<<<<<<< HEAD
					for j in range(0, 3):
						if board[0][j] == board[1][j] == board[2][j] == "X":
							i = 9
							print("Player X has Won!")
							break

					for j in range(0, 3):
						if board[0][j] == board[1][j] == board[2][j] == "*":
							i = 9
							print("Player * has Won!")
							break
						break


					if board[0][0] == board[1][1] == board[2][2] == "X":
						i = 9
						print("Player X has Won!")
						break
					if board[0][0] == board[1][1] == board[2][2] == "*":
						i = 9
						print("Player * has Won!")
						break
					if board[2][0] == board[1][1] == board[0][2] == "*":
						i = 9
						print("Player * has Won!")
						break

					if board[2][0] == board[1][1] == board[0][2] =="X":
						i = 9
						print("Player X has Won!")
						break

=======
					row_position = (int(row_) -1)
					column_position = (int(column_) -1)
					if board[row_position][column_position] != 0:
						print("sorry, that square is already taken, please"
							  " pick another square")
						continue
					if i % 2 == 1:
							board[row_position][column_position] = "X"
							i += 1
					elif i % 2 == 0:
							board[row_position][column_position] = "*"
							i += 1

					print(board[0])
					print(board[1])
					print(board[2])

				for row in board:
					if row == ["X", "X", "X"]:
						print("Player X has Won!")
						i = 9
					elif row == ["*", "*", "*"]:
						print("Player * has Won!")
						i = 9

					else:
						for j in range(0, 3):
							if board[0][j] == board[1][j] == board[2][j] == "X":
								print("Player X has Won!")
								i = 9
							elif board[0][j] == board[1][j] == board[2][j] == "*":
								print("Player * has Won!")
								i = 9
						if board[0][0] == board[1][1] == board[2][2] == "X":
							print("Player X has Won!")
							i = 9
						if board[0][0] == board[1][1] == board[2][2] == "*":
							print("Player * has Won!")
							i = 9
						if board[2][0] == board[1][1] == board[0][2] == "*":
							print("Player * has Won!")
							i = 9
						if board[2][0] == board[1][1] == board[0][2] =="X":
							print("Player X has Won!")
							i = 9
						else:
							continue
>>>>>>> 3f3ca3a8234285cfcfa5b4df6b2d55b1ea7813b2

		#else:
		#	if "0" not in board:
		#		print("it's a Tie!")

game(board)
<<<<<<< HEAD
#print(game(board))
=======
#print(game(board))
>>>>>>> 3f3ca3a8234285cfcfa5b4df6b2d55b1ea7813b2
