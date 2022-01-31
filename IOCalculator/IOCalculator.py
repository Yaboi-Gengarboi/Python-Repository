# IOCalculator
# IOCalculator.py
# Created on 2022-01-30 by Justyn Durnford
# Last modified on 2022-01-30 by Justyn Durnford
# Program to go more in-depth with IO and math.

# Gets 2 numbers from the user and returns them in a list.
def getInput():
	x = float(input("Enter a number: "))
	y = float(input("Enter another number: "))
	return [x, y]

# Performs and prints several operations on 2 numbers.
def calculate(x, y):
	print(x, "+", y, "=", x + y)
	print(x, "-", y, "=", x - y)
	print(x, "*", y, "=", x * y)

	# Avoid a divide by 0 error.
	if y == 0:
		print(x, "/", y, "= NaN")
	else:
		print(x, "/", y, "=", x / y)

def main():
	list = getInput()
	calculate(list[0], list[1])

if __name__ == "__main__":
   main()
