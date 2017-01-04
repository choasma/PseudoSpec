import sys
sys.path.append('/home/mawand/Documents/PseudoSpec/utils')

from pseudo_spec import *
import numpy as np
import scipy as sp
import scipy.linalg


row = [1,-0.5] + [0]*10
col = [1,-0.5] + [0]*10
a = sp.linalg.toeplitz(col, row)
val = np.linalg.eigvals(a)
a = a.T.dot(a)
p_norm, p_val = norm_inverse_mat_pseudo(a, 1, 1e-3)

print p_norm
print np.real(val), np.imag(val)
print np.real(p_val), np.imag(p_val)


