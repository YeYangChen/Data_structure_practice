import os

def fibonacci(n):
	if n <= 1:
		return (n,0)
	else:
		(a,b) = fibonacci(n-1)
		return (a+b, a)

def draw_line(tick_length,tick_label=''):
	#draw one line with given tick length followed by optional label
	line = '-'*tick_length
	if tick_label:
		line = line + tick_label
	print(line)

def draw_interval(center_length):
	if center_length > 0:
		draw_interval(center_length-1)
		draw_line(center_length)
		draw_interval(center_length-1)

def draw_ruler(num_inches,major_length):
	#draw ruler with given num_inches and major_length
	draw_line(major_length,'0')
	for j in range(1, 1 + num_inches):
		draw_interval(major_length-1)
		draw_line(major_length,str(j))

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def disk_usage(path):
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			childpath = os.path.join(path,filename)
			total += disk_usage(childpath)
	print('{0:<7}'.format(total),path)
	return total



if __name__ == '__main__':
	print(fibonacci(3))
	print(fibonacci(4))
	print(fibonacci(5))
	draw_ruler(4,4)
	print(factorial(10))