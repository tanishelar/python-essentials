#Python Program for simple interest
# for given principal amount, time and
# rate of interest.


def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
    
    si = (p * t * r)/100
    
    print('The Simple Interest is', si)
    return si
    
# Driver code
simple_interest(8, 6, 8)

#Program for simple interest with Taking input from user
# # Python3 program to find simple interest
# #  principal amount, time and
# # rate of interest taken from user.


# def simple_interest(p,t,r):
#     print('The principal is', p)
#     print('The time period is', t)
#     print('The rate of interest is',r)
    
#     si = (p * t * r)/100
    
#     print('The Simple Interest is', si)
    
    
# # Driver code
# P = int(input("Enter the principal amount :"))
# T = int(input("Enter the time period :"))
# R = int(input("Enter the rate of interest :"))
# simple_interest(P,T,R)
