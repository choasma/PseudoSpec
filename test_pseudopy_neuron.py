from pseudopy import NonnormalAuto, demo
from matplotlib import pyplot
from scipy.linalg import eigvals
import numpy as np

# get Grcar matrix
A = demo.grcar(32).todense()
A = np.random.rand(3,3)

# compute pseudospectrum for the levels of interest between [1e-5, 1]
pseudo = NonnormalAuto(A, 1e-5, 1)

# plot
pseudo.plot([10**k for k in range(-4, 0)], spectrum=eigvals(A))
pyplot.show()
