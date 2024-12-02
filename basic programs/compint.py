# Python3 program to find compound
# interest for given values.


def compound_interest(principal, rate, time):

	# Calculates compound interest
	Amount = principal * (pow((1 + rate / 100), time))
	CI = Amount - principal
	print("Compound interest is", CI)


# Driver Code
compound_interest(10000, 10.25, 5)

#Compound Interest using for loop
# def compound_interest(principal, rate, time):
# 	Amount = principal
# 	for i in range(time):
# 		Amount = Amount * (1 + rate/100)
# 	CI = Amount - principal
# 	print("Compound interest is", CI)
# # Driver Code
# compound_interest(1200, 5.4, 2)
