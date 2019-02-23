def new_array(arr):
	result = [0,1]
	for k in range(len(arr)):
		result[0] = result[0] + arr[k]
		result[1] = result[1] * arr[k]
	return result

def average(arr):
	sum = 0
	count = 0
	for k in range(len(arr)):
		sum = sum + arr[k]
		count = count + 1
	average = sum / count
	print(average)

def noneShallPass(fellowship):
	if len(fellowship) < 9:
		return False
	elif len(fellowship) < 10:
		for i in fellowship:
			if i is None:
				continue
		if i is not None:
			i = None
		else:
			return i
	else:
		 return False
	return True

array = [None,None,None,3,None,1,None,None,None]
print(noneShallPass(array))
