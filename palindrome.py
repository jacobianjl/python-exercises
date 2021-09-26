def palindrome(str):
	'''
		Check if palindrome
	'''
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

def main():
	word = input('Enter a string: ')
	while True:
		if word.isalpha():
			word = str(word)
			break
		word = input('Please enter a valid string: ')
	if palindrome(word):
		print('Yes')
	else:
		print('No')

if __name__ == '__main__':
	main()