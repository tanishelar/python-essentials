#Python Program to Find Sum of Array
# Iterating through the array and 
# adding each element to the sum variable and finally 
# displaying the sum.

# Python 3 code to find sum
# of elements in given array


def _sum(arr):

	# initialize a variable
	# to store the sum
	# while iterating through
	# the array later
	sum = 0

	# iterate through the array
	# and add each element to the sum variable
	# one at a time
	for i in arr:
		sum = sum + i

	return(sum)


# main function
if __name__ == "__main__":
	# input values to list
	arr = [12, 3, 4, 15]

	# calculating length of array
	n = len(arr)
	# calling function ans store the sum in ans
	ans = _sum(arr)
	# display sum
	print('Sum of the array is ', ans)

#Python Program to Find Sum of Array Using sum()
# Python 3 code to find sum
# of elements in given array

# input values to list
# arr = [12, 3, 4, 15]

# # sum() is an inbuilt function in python that adds
# # all the elements in list,set and tuples and returns
# # the value
# ans = sum(arr)

# # display sum
# print('Sum of the array is ', ans)

#Python Program to Find Sum of Array Using reduce method
# Using the reduce method. Array.reduce() method is used to iterate over the array and get the summarized result from all elements of array.
# from functools import reduce
# # Python 3 code to find sum
# # of elements in given array


# def _sum(arr):

# 	# iterate over array
# 	# using reduce and get 
# 	# sum on accumulator
# 	sum = reduce(lambda a, b: a+b, arr) 

# 	return(sum)


# # driver function
# arr = []
# # input values to list
# arr = [12, 3, 4, 15]

# # calculating length of array
# n = len(arr)

# ans = _sum(arr)

# # display sum
# print('Sum of the array is ', ans)
