#Find largest element in an array Using traditional Approach
# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


def largest(arr, n):

	# Initialize maximum element
	max = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

#Find largest element in an array Using built-in function max()
# Python3 program to find maximum
# in arr[] of size n
# def largest(arr, n):
# 	ans = max(arr)
# 	return ans;

# # Driver code
# if __name__ == '__main__':
# 	arr = [10, 324, 45, 90, 9808]
# 	n = len(arr)
# 	print ("Largest in given array ", largest(arr, n))

#Find largest element in an array Using sort() function
# Python3 program to find maximum
# in arr[] of size n

# def largest(arr, n):

# 	# Sort the array
# 	arr.sort()

# 	# The last element of the
# 	# array is the largest element
# 	return arr[n-1]
# 	# or return arr[-1]

# # Driver Code
# arr = [10, 324, 45, 90, 9808]
# n = len(arr)
# Ans = largest(arr, n)
# print("Largest in given array ", Ans)

