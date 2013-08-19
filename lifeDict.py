import random
import signal, sys
from termcolor import colored, cprint
colors = ['red','yellow','green','blue','magenta','cyan','white']
liveCell = 35 #for a # symbol
deadCell = 32 # for a space
boardSize = 0



def buildBoard(size):
	board = {}
	global boardSize
	boardSize = size
	for i in range(size):
		for j in range(size):
			board[(i,j)] = 0
	return board

def printBoard(board):
	global boardSize
	res = ' # '*boardSize
	def filterhelper(x):
		if x >= 1:
			return colored(' '+chr(liveCell),'red')
			#return colored(' '+chr(liveCell),colors[(x-1)%7])
#			return colored(' '+str(x),colors[(x-1)%7])
		else:
			return ' '+chr(deadCell)

	for i in range(boardSize-1):
		res = res + '\n'+ '#'
		for j in range(boardSize-1):
			res = res + ' '+ filterhelper(board[(i,j)])
		res += ' #'
	res += '\n' + ' # '*boardSize
	print  res

def birth_cell(board,x,y,rank=1):
	board[(x,y)] = rank

def birth_rand_formation(board,n):
	for i in range(n):
		x = random.randint(5,boardSize-5)
		y = random.randint(5,boardSize-5)
		if board[(x,y)] == 0:
			birth_cell(board,x,y)
	
	
def build_neighbors(board,x,y):
	
	potential_neighbors = [(x-1,y-1),(x-1,y),(x-1,y+1),
				(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
	neighbors = []
	for coord in potential_neighbors:
		if coord  in board.keys():
			neighbors.append(coord)
	return neighbors

def check_neighbors(board,x,y):

	n_live_neighbors = 0
	neighbors = build_neighbors(board,x,y)
	for cell in neighbors:
		if board[cell] >= 1:
			n_live_neighbors += 1
	return n_live_neighbors

def total_live_cells(board):
	total = 0
	for cell in board.keys():
		if board[cell] >= 1:
			total += 1
	return total

def will_live(board,x,y):

	if board[(x,y)] >= 1:
		live = True
	else:
		live = False
	
	n_live_neighbors = check_neighbors(board,x,y)

	if live and n_live_neighbors < 2:
		return False
	elif live and (n_live_neighbors == 2 or n_live_neighbors == 3):
		return True
	elif live and n_live_neighbors > 3:
		return False
	elif not live and n_live_neighbors == 3:
		return True
	else:
		return False

	
def next_board(board):
	next_board = buildBoard(boardSize)	
	for i in range(boardSize):
		for j in range(boardSize):
			if will_live(board,i,j):
				#birth_cell(next_board,i,j,board[(i,j)]+1)
				birth_cell(next_board,i,j,1)
	return next_board






if __name__ == "__main__":
	board = buildBoard(int(sys.argv[1]))
	birth_rand_formation(board,int(sys.argv[2]))
	livecells = total_live_cells(board)
	gen = 0
	lastboard = board
	while(1):
		printBoard(board)
		print gen
		nextboard = next_board(board)
		if (board == nextboard):
			printBoard(nextboard)
			print "your cells settled after %d generations" %(gen)
			break
		if gen%2 == 0:
			lastboard = board
		if (lastboard == nextboard):
			printBoard(nextboard)
			print "your cells are blinking after %d gens" %(gen)
			break

		board = nextboard
		livecells = total_live_cells(board)
		if (livecells == 0):
			print "Your cells died after %d generations :(" %(gen)
			break
		gen += 1


		

