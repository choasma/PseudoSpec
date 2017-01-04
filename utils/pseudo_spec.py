import numpy as np


def norm_inverse_mat(mat):
	I = np.identity(mat.shape[0])
	mat  = np.linalg.inv(mat)
	norm = np.linalg.norm(mat, ord='fro')
	return norm



def inverse_mat_pseudo_1st(mat, val_idx, e):
	'''
		first definition of pseudospectra
		
		sig_e(A) is the set of z \in C such that
		|| (zI-A)^{-1}|| > e^{-1}		
	
	'''



def inverse_mat_pseudo_2nd(mat, val_idx, e):
	'''
		second definition of pseudospectra

		sig_e(A) is the set of z \in C such that
		z \in sig(A+E)
		for some E \in C^NxN with ||E|| < e	

	'''
	size = mat.shape[0]
	I = np.identity(size)
	val, vec = np.linalg.eig(mat)

	noise = np.random.rand(size,size)*e
	mat = mat - noise	

	mat  = np.linalg.inv(mat - val[val_idx]*I)
	norm = np.linalg.norm(mat, ord='fro')

	return norm, np.linalg.eigvals(mat)


def inverse_mat_pseudo_3rd(mat, val_idx, e):
	'''
		third definition of pseudospectra

		sig_e(A) is the set of z \in C such that
		||(zI-A)v|| < e
		for some v \in C^/n with ||v||=1

	'''

if __name__ == '__main__':
	a = np.random.rand(3,3)
	val, vec = np.linalg.eigh(a)
	norm_inverse_mat(a)

