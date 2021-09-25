def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

def main():
	number = input('Find fibonnaci sequence for this many terms: ')
	while True:
		if number.isdigit():
			number = int(number)
			break
        number = input('Please enter an integer: ') 
    for i in range(number):
         print(fibonacci(number))
         
if __name__ == '__main__':
	main()