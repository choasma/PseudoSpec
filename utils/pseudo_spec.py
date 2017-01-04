import numpy as np


def norm_inverse_mat(mat):
	I = np.identity(mat.shape[0])
	mat  = np.linalg.inv(mat)
	norm = np.linalg.norm(mat, ord='fro')
	return norm


def norm_inverse_mat_pseudo(mat, val_idx, e):
	size = mat.shape[0]
	I = np.identity(size)
	val, vec = np.linalg.eig(mat)

	noise = np.random.rand(size,size)*e
	mat = mat - noise	

	mat  = np.linalg.inv(mat - val[val_idx]*I)
	norm = np.linalg.norm(mat, ord='fro')

	return norm, np.linalg.eigvals(mat)




if __name__ == '__main__':
	a = np.random.rand(3,3)
	val, vec = np.linalg.eigh(a)
	norm_inverse_mat(a)

