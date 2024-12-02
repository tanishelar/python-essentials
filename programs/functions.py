# def fun():
#     print('Hello')

# fun()

# def add(num1: int,num2: int) -> int:
#     num3 = num1 + num2 
#     return num3

# num1, num2 = 13, 47
# ans = add(num1,num2)
# print(f'THE SUM OF {num1} and {num2} is {ans}.')

# Python program to
# demonstrate accessing of
# variables of nested functions

# def f1():
#     s = 'Hi Tanii'
    
#     def f2():
#         print(s)
#     f2()

# f1()

#recursive functions in python
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(4))

#subtraction of numbers
def subnum(a,b):
    return a-b

#main code
a = 100
b = 98
r = subnum(a,b)
print(r)