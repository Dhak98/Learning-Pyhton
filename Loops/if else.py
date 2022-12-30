"""
print("Hi, This is script to find the number is odd or even")
n = int(input("Enter the number: "))
if n%2 == 0:
    print(n,"is even number")
else:
    print(n,"is odd number")

print("Bye....")
"""
#####################################################################

"""
# Qus

A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.

# Answer

print("Get 10% discount for purchase Rs.1000 or Above")
price = 100
quan = int(input("Enter the number of Quantity you need: "))
tot = price*quan
if tot >= 1000:
    dtot = (tot / 100)*10
    dtot = tot-dtot 
    print("Price with 10% discount is", dtot)
else:
    print("Sorry, You are not eligible for Discount. Your cost is", tot)

""" 