def four_dimensional_array(arr):
	for a in range(len(arr)):
		for b in range(len(arr[a])):
			for c in range(len(arr[a][b])):
				for d in range(len(arr[a][b][c])):
					print(arr[a][b][c][d])

def matrix_multiply(A, B):
	if len(A[0]) != len(B):
		return
	n = len(B)
	C = [None] * len(A)
	for k in range(len(C)):
		C[k] = [None] * len(B[0])
	for i in range(len(C)):
		for j in range(len(C[i])):
			C[i][j] = 0
			for p in range(n):
				C[i][j] = C[i][j] + A[i][p] * B[p][j]
	return C

if __name__ == '__main__':
	mat_a = [[1,2,3],[4,5,6]]
	mat_b = [[1,2],[3,4],[5,6]]
	print(matrix_multiply(mat_a,mat_b))
