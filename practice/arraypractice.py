def insert(arr,index,value):
	if index < 0 or index >= len(arr):
		return
	for k in range(len(arr)-1,index,-1):
		arr[k] = arr[k-1]
	arr[index] = value

def new_array(arr):
	result_array = [None]*len(arr)
	for k in range(len(arr)):
		if (arr[(k+len(arr)+1)%len(arr)] * arr[(k+len(arr)-1)%len(arr)]) % 2 == 0:
			result_array[k] = 0
		else:
			result_array[k] = 1
	return result_array

arr1 = [-4,15,3,7,None,0,None]; arr2 = [7,4,3,6,1,6,8]
insert(arr1,3,-82)
print(arr1)
print(new_array(arr2))