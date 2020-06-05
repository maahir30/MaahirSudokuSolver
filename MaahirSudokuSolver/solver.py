'''
APPROACH:
1 Find an empty square to use
2 Start putting numbers on it
3 check if that number works
	- check row (left/right)
	- check column (up/down)
	- check grid (3x3 square)
4 Continue proccess for every empty square
5 Move back if number doesn't work (backtracking)
 - check if board is solved 
 - loop through 1-9
 - check if they work
 - set empty square to it
 - if it doesn't work, go back change the old square
 - continue with entire board until there are no more empty
   squares, meaning the board is solved. 
6 Show the start and end through a board visualizer
7 Possibly add a GUI using pygame to show the board being solved. 

'''

#zeroes indicate a blank space
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


#prints the sudoku board
def printSudoku(board):
	for x in range(len(board)):
		if x % 3 == 0 and x != 8 and x != 0:
			print("-------------------------------")

		
		for y in range(len(board[1])):
			
			if y % 3 == 0 and y != 8 and y != 0:
				print(" | ", end = "")

			if y != 8:
				print(str(board[x][y]), " ", end="")
			else:
				print(str(board[x][y]))
	

#find an empty square on the board, along with its index location and returns it as a tuple. 
def findSquare(board):
	for row in range(9):
		for column in range(9):
			if board[row][column] == 0:
				return (row,column) # y,x 
	return False
	

#goes throught numbers 1-9 and checks which ones are valid in the position 

def checkNumberValid(board, number, position):
	#CHECK COLUMN:
	for row in board:
		if row[position[1]] == number and row != board[position[0]]:
			return False

	#CHECK GRID: 
	#set up x variable
	
	if 0 <= (position[1]) /3 < 1:
		x_coor = 0


	elif 1 <= position[1]/3 < 2:
		x_coor = 1

	elif 2 <= position[1]/3 < 3:	
		x_coor = 2

	#set up y variable
	if 0 <= position[0]/3 < 1:
		y_coor = 0


	elif 1 <= position[0]/3 < 2:
		y_coor = 1

	elif 2 <= position[0]/3 < 3:	
		y_coor = 2
	

	#Go through each grid and check for repeated numbers
	for y in range(y_coor*3, y_coor*3+3):
		for x in range(x_coor*3, x_coor*3+3):
			if board[y][x] == number and board[position[0]][position[1]] != board[y][x]:
				return False

	#CHECK ROW:
	for column in range(9):
		if board[position[0]][column] == number and column != position[1]:
			return False

	return True





def solvedBoard(board):
	#printSudoku(board)
	#print('------------------------ \n ------------------------ \n ------------------------')
	empty_square = findSquare(board)
	if not empty_square:
		return True
	else:
		row, column = empty_square
	
	for ans in range(1,10):
		if checkNumberValid(board, ans, (row, column)):
			board[row][column] = ans
			
			if solvedBoard(board): 
				return True
		
			board[row][column] = 0


	return False









#Final script	
print('\n\n\nHere is the starting board: ')
printSudoku(board)
solvedBoard(board)
print('\n\n\nHere is the solved board!')
printSudoku(board)
print("\n\nNOTE: If you are seeing an unsolved board, it means that your sudoku board was invalid. Please change it to a valid puzzle and try again.\n")



