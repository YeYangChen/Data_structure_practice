import random

def quicksort(arr):
	quicksortHelper(arr,0,len(arr)-1)

def quicksortHelper(arr, low, high):
	if low < high:

		splitpoint = partition(arr,low,high)

		quicksortHelper(arr,low,splitpoint-1)
		quicksortHelper(arr,splitpoint+1,high)

def partition(arr, low, high):
	pivotvalue = arr[low]

	leftmark = low+1; rightmark = high

	done = False

	while not done:

		while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
			leftmark = leftmark + 1
		while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
			rightmark = rightmark - 1

		if leftmark > rightmark:
			done = True
		else:
			temp = arr[leftmark]
			arr[leftmark] = arr[rightmark]
			arr[rightmark] = temp

	arr[low] = arr[rightmark]
	arr[rightmark] = pivotvalue
	
	return rightmark

if __name__ == '__main__':
	testarray = []
	for k in range(100):
		testarray.append(random.randint(0,1000))
	quicksort(testarray)
	print(testarray)

