
import matplotlib
matplotlib.use('Agg')
from pseudopy import NonnormalAuto, demo
import matplotlib.pyplot as plt
from scipy.linalg import eigvals



from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.models import load_model



import numpy as np


import glob




PATH_MODEL = '/vol/graphics-solar/mawand/Project/keras/examples'
EXT = ".hdf5"
pattern = ("%s/*%s")%(PATH_MODEL,EXT)
FLIST = glob.glob(pattern)

#models = []
#
#i=0
#
#for item in FLIST:
#	i += 1
#	print 'loading model [%s]'%item
#	models.append(load_model(item))

wIdx = 5
lIdx = 6 




for i in range(len(models)):
	print models[i]
	A = models[i].get_weights()[lIdx][:,:,0,wIdx]
	#A = models[i].get_weights()[lIdx]
	A = A.T.dot(A)
	print A
	# compute pseudospectrum for the levels of interest between [1e-5, 1]

	try:
		pseudo = NonnormalAuto(A, 1e-7, 1e-5)
		pseudo.plot([10**k for k in range(-10, 0)], spectrum=eigvals(A))

		fName = "pseudo_%03d.png"%i

		plt.savefig(fName)
		plt.clf()
		print "save fig [%s]"%fName

	except:
		continue
