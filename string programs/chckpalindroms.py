#Python Program to Check if a String is Palindrome or Not

# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "tanishelar"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

#check program if symmetry or not
# def is_palindrome(s):
#     return s == s[::-1]

# def is_symmetrical(s):
#     length = len(s)
#     mid = length // 2
#     if length % 2 == 0:
#         return s[:mid] == s[mid:]
#     else:
#         return s[:mid] == s[mid+1:]

# string = "checksym"
# if is_symmetrical(string):
#     print("The entered string is symmetrical")
# else:
#     print("The entered string is not symmetrical")

# if is_palindrome(string):
#     print("The entered string is palindrome")
# else:
#     print("The entered string is not palindrome")