import numpy as np
from matplotlib import pyplot

from life import LifeGame

i = 0
numgames = 10
size = 15
numcells = 15
fullResults = []

for j in range(10,150,5):

	results = {'initial cells': 0, 'death': 0, 'loop': 0, 'stable': 0}
	initcells = 0
	while(i < numgames):
		
		game = LifeGame(size,j)
		initcells +=game.game[-1].total_live_cells()
		game.play(False)
		if game.endcode == 1:
			results['death'] += 1
		elif game.endcode == 2:
			results['stable'] += 1
		elif game.endcode == 3:
			results['loop'] += 1
		i += 1
	results['initial cells'] = initcells/numgames
	fullResults.append(results)
	i = 0

print "size of board: %d square" %size
for item in fullResults:
	print "average initial cells: %d " %item['initial cells'],
	print "deaths: %d, loops: %d, stable: %d" %(item['death'],item['loop'],
			item['stable'])

