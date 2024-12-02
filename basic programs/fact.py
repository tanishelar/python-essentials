# Input: An integer number
num = 6

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Output: The factorial of the number
print(f"The factorial of {num} is {factorial}")

#2. Get Factorial of a Number using a Recursive Approach
# Python 3 program to find 
# factorial of given number
# def factorial(n):
    
#     # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))

#3. Find Factorials quickly using One liner (Using Ternary Operator)
#def factorial(n):

    # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1) 


# # Driver Code
# num = 5
# print ("Factorial of",num,"is",
#       factorial(num))

#Factorial Function in Maths
# In Python, math module contains a number of mathematical operations,
#  which can be performed with ease using the module. math.factorial() 
# function returns the factorial of desired number.
# Python 3 program to find
# factorial of given number
# import math

# def factorial(n):
#     return(math.factorial(n))


# # Driver Code
# num = 5
# print("Factorial of", num, "is",
#       factorial(num))

#Find the Factorial of a Number Using NumPy
# import numpy
# n=5
# x=numpy.prod([i for i in range(1,n+1)])
# print(x)

