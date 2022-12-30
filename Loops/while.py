"""
print("Do you want to print the even number untill you want: ")
i=1
enum = int(input("Enter the end number: "))
print("The even numbers untill",enum)
while i <= enum:
    if i%2 == 0:
        print(i)
    i += 1

"""
"""
print("Do you want to print the odd number untill you want: ")
i=1
enum = int(input("Enter the end number: "))
print("The odd numbers untill",enum)
while i <= enum:
    if i%2 != 0:
        print(i)
    i += 1
    
"""
##########################################################################################

"""
# Qus

Take 10 integers from keyboard using loop and print their average value on the screen.

# Answer :

sum = 0
tum = 10
while tum>0:
    print("Enter the number: ")
    num = int(input())
    sum = sum + num
    tum = tum - 1
print("Average is", sum/10)

"""

