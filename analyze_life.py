import numpy as np
from matplotlib import pyplot

from life import LifeGame

results = {'death': 0, 'loop': 0, 'stable': 0}
i = 0
numgames = 100
size = 10
numcells = 200

while(i < numgames):

	game = LifeGame(size,numcells)
	game.play(False)
	if game.endcode == 1:
		results['death'] += 1
	elif game.endcode == 2:
		results['stable'] += 1
	elif game.endcode == 3:
		results['loop'] += 1
	i += 1

print "on a size %d board with %d initial cells:" %(size,numcells)
print results

