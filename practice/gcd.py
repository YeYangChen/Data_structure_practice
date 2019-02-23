def gcd(r1, r2):
	if r1 <= r2:
		if r1 == 0:
			return r2
		else:
			return gcd(r2 % r1, r1)
	else:
		return gcd(r2, r1)

if __name__ == '__main__':
	r1 = int(input('en'))
	r2 = int(input('sd'))
	print(gcd(r1,r2))