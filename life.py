import random
from termcolor import colored, cprint

liveCell = 35
deadCell = 32
class Cell(object):
	

	def __init__(self,live=False):
		self.live = live
	
	def __str__(self):
		if self.live:
			return colored(chr(liveCell),'red')
		else:
			return chr(deadCell)




			
class Board(object):
	def __init__(self, size):
		self.board = {}
		self.size = size
		for i in range(self.size):
			for j in range(self.size):
				self.board[(i,j)] = Cell(False)

		
	
	def __str__(self):
		res = ''
		for i in range(self.size -1):
			res = res + '\n'
			for j in range(self.size-1):
				res = res + ' ' + str(self.board[(i,j)])

		return res


	def __eq__(self,other):
		if not self.size == other.size:
			return False
		for i in range(self.size-1):
			for j in range(self.size-1):
				if not self.board[(i,j)].live == other.board[(i,j)].live:
					return False
		return True
	
	def birth_cell(self,x,y):
		self.board[(x,y)]= Cell(True)
	
	def birth_formation_random(self,n):
		for i in range(n):
			x = random.randint(5,self.size-5)
			y = random.randint(5,self.size-5)
			if not self.board[(x,y)].live:
				self.birth_cell(x,y)
	
	def build_neighbors(self,x,y):
		potential_neighbors = [(x-1,y-1),(x-1,y),(x-1,y+1),
				(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
	
	 	neighbors = []
		for coord in potential_neighbors:
			if coord in self.board.keys():
				neighbors.append(coord)
		return neighbors

	def check_neighbors(self,x,y):
		n_live_neighbors = 0
		neighbors = self.build_neighbors(x,y)
		for cell in neighbors:
			if self.board[cell].live:
				n_live_neighbors +=1
		return n_live_neighbors

	def total_live_cells(self):
		total = 0
		for cell in self.board.keys():
			if self.board[cell].live:
				total += 1
		return total

	def will_live(self,x,y):
		n_live_neighbors = self.check_neighbors(x,y)
		alive = self.board[(x,y)].live

		if alive and n_live_neighbors > 2:
			return False

		elif alive and (n_live_neighbors == 2 or n_live_neighbors ==3):
			return True
		elif alive and n_live_neighbors > 3:
			return False
		elif not alive and n_live_neighbors == 3:
			return True
		else:
			return False
	

			

class LifeGame(object):

	def __init__(self,boardsize,startingNumber):
		self.game = []
		self.boardsize = boardsize
		gen0 = Board(self.boardsize)
		gen0.birth_formation_random(startingNumber)
		self.game.append(gen0)
	
	def next_board(self):
		self.game.append(Board(self.boardsize))
		currentboard = self.game[-2]
		for i in range(self.boardsize):
			for j in range(self.boardsize):
				if currentboard.will_live(i,j):
					self.game[-1].birth_cell(i,j)

	
	def play(self):
		gen = 0
		while(1):
			print self.game[-1]
			self.next_board()
			livecells = self.game[-1].total_live_cells()
			print str(gen) + ' ' + str(livecells)
			if livecells < 1:
				print "cells died" 
				print "%d gens" %gen
				break
			
			gen +=1

			if self.game[-1] == self.game[-2]:
				print "cells stabilized" 
				print "%d gens" %gen 
				break

			breaker = 0
			for item in self.game[:-2]:
				if item == self.game[-1]:
					print "cells blinking, infinite loop"
					print "%d gens" %gen
					breaker = 1

			if breaker == 1: break
					







if __name__ == "__main__":
	lifegame = LifeGame(35,250)
	lifegame.play()
