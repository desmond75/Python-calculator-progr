"""A simple calculator program which can perform  basic 
   math opeartions between two numbers , calculate simple interest
   and also calculate the highest common factor between two numbers 

   By: Fon Desmond Ade
   Email: adedesmond6@gmail.com
   """

   

def calculate_simple_interest(principal, interest_rate, time):
	"""Calculates the simple interest of a principal amount 
	   invested for a particular period of time """

	result = (principal * interest_rate * time) / 100
	return result




def list_factors_of(number):
	'''This function takes takes a number and 
	   return a list containing factors of that number '''

	factors_of_number = []
	for num in range(1, number + 1):
		if number % num == 0:
			factors_of_number.append(num)
	return factors_of_number



def calculate_highest_common_factor(number1, number2):
	'''takes two numbers and return a list of their
	   factors using our [highest_common_factor()] function '''

	 #this list will hold numbers that are factors of number1 and number2
	factors_of_number1_and_number2 = [] 

	factors_of_number1 = list_factors_of(number1)#get factors of first argument

	factors_of_number2 = list_factors_of(number2)#get factors of second argument


	for number in factors_of_number1:
		#Looks for numbers that are both 
		#factors to number1 and number2 and
		# appends it to factors_of_number1_and_number2 list 
		if number in factors_of_number2:
			factors_of_number1_and_number2.append(number)

	highest_number = max(factors_of_number1_and_number2)#gets the highest number in this list 
	return highest_number




def menu():
	"""display instructions to the screen"""
	print('''

		  Caculator
		  =========
		  Enter     Function 

		  2   ------ To calculate basic math opeartions
		  3   ------ To calculate simple interest 
		  4   ------ To calculate highest common factor of two numbers

		''')



def calculate(number1, sign, number2):

	"""Recieves two numbers, number1 and number2 
	   and peforms mathematical operations on them
	   depending on the mathematical operator pass
	   in which is refered as sign here """

	if sign == '*':
		return number1 * number2
	elif sign == '+':
		return number1 + number2

	elif sign == '/':
		return number1 / number2
	elif sign == '-':
		return number1 - number2



print(10/2)

def main():
	""" This function will keep displaying the menu
	    while the user makes choice on which calculation 
	    to perform """

	while True:
		menu() #Keep showing the instructions 
		try:
			choice = int(input('Enter what you want'))
		except Exception as e:
			print('Enter a choice ' + str(e))

		if choice == 2:# If choice is 2 it means the user want to perform just basic maths
			try:
				number1 = int(input('Enter first number'))
				sign = input("Enter mathematical sign")
				number2 = int(input('Enter second number'))
				result = calculate(number1, sign, number2)
				print("Result of {} {} {} is {}".format(number1, sign, number2, result))
			except BaseException as e:
				print('Please make sure to enter everything correctly')



		elif choice == 3:# If choice is 3 it means the user want to caculate simple interest
			try:
				currency = input('Enter your currency')
				principal = int(input('Enter the principal amount invested'))
				interest_rate = int(input('Enter the interest rate'))
				time = int(input('Enter the time or years'))
				interest = calculate_simple_interest(principal, interest_rate, time)

				print('The interest of {} for {} years at an interest rate of {} is {}{}'.\
					                  format(principal, time, interest_rate, interest, currency))

			except BaseException as e:
				print('Make sure to enter everything correctly')
			


		elif choice == 4:# If choice is 2 it means the user wants to calculate the highest common factor of two numbers
			try:
				number1 = int(input('Enter first number'))
				number2 = int(input('Enter second number'))

				result = calculate_highest_common_factor(number1, number2) 
				print('Hi highest common factor of {} and {} is {}'.format(number1, number2, result))

			except BaseException as e:
				print('Please make sure you entered everything correctly')
		else:
			print('Invalid choice')


if __name__ == '__main__':
	main()
