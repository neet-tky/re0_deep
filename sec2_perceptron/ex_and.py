import numpy as np
import itertools

def AND(x1, x2):
	w1, w2, theta = .5, .5, .7

	tmp = w1 * x1 + w2 * x2

	if tmp > theta:
		return 1

	else:
		return 0


for x1, x2 in itertools.product([0, 1], [0, 1]):
	print(x1, x2, AND(x1, x2))