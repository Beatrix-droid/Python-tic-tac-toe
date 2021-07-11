


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
							print(board[0])
							print(board[1])
							print(board[2])
					elif i % 2 == 0:
							board[row_position][column_position] = "*"
							i += 1

							print(board[0])
							print(board[1])
							print(board[2])
				continue
		for row in board:
					if row == ["X", "X", "X"]:
						for row in board:
							print(row)
						break
						return "Player X has Won!"

					elif row == ["*", "*", "*"]:
						for row in board:
							print(row)
						break
						return "Player * has Won!"


		for j in range(0, 3):
					if board[0][j] == board[1][j] == board[2][j] == "X":
						for row in board:
							print(row)

						return "Player X has Won!"

		for j in range(0, 3):
					if board[0][j] == board[1][j] == board[2][j] == "*":
						for row in board:
							print(row)
						break
					return "Player * has Won!"

		if board[0][0] == board[1][1] == board[2][2] == "*":
					for row in board:
						print(row)
					return "Player * has Won!"

		if board[0][0] == board[1][1] == board[2][2] == "X":
					for row in board:
						print(row)
					return "Player X has Won!"


		if board[2][0] == board[1][1] == board[0][2] == "*":
					for row in board:
						print(row)
					break
					return "Player * has Won!"

		if board[2][0] == board[1][1] == board[0][2] =="X":
					for row in board:
						print(row)
					break
					return "Player X has Won!"

		#else:
		#	if "0" not in board:
		#		print("it's a Tie!")

game(board)