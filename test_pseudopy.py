import matplotlib
matplotlib.use('Agg')

import os
from pseudopy import NonnormalAuto, demo
from scipy.linalg import eigvals
import matplotlib.pyplot as plt

import numpy as np

PATH_RST = "./experiments/basic"



# get Grcar matrix
A = demo.grcar(3).todense()

# compute pseudospectrum for the levels of interest between [1e-5, 1]


for i in range(20):

	pseudo = NonnormalAuto(A, 1e-5, 1e-3)

	noise = np.random.rand(3,3)/1e1
	# plot
	pseudo.plot([10**k for k in range(-4, 0)], spectrum=eigvals(A))
	fName = "pseudo_%03d.png"%i
	plt.xlim(-5,5)	
	plt.ylim(-5,5)	



	plt.savefig(os.path.join(PATH_RST, fName))
	plt.clf()
	print "%s saved"%fName	
	A += noise
