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