def get_exponents(f):
	count = {}
	for i in f:
		if not i in count:
			count[i] = 1
		else:
			count[i] += 1
	return count

def is_prime(x):
	if x == 2 or x == 3:
		return True
	if x % 2 == 0:
		return False
	for i in range(3, int(x ** 0.5) + 1, 2):
		if x % i == 0:
			return False
	return True

def prime_factorise(n):
	factors = []
	while True:
		if n == 0 or n == 1:
			break
		for i in range(2, n+1):
			if n % i == 0:
				if is_prime(i):
					factors.append(i)
					n = n/i 
					break
	if len(factors) != 0:
		factor_exponents = get_exponents(factors)
		for factor, exponent in factor_exponents:
			print(str(factor) + '^' + str(exponent) + '\n')

def main():
	number = input('Enter a number to find the prime factors for: ')
	while True:
		if isinstance(number, int):
			break
		number = input('Please enter an integer: ')
	prime_factorise(number)

if __name__ == '__main__':
	main()