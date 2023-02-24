"""
for i in range(0,6,1):
    for j in range(i):
        print("*",end="")
    print("")
"""
"""
def solve(s):
    print(s.capitalize())
solve(s=input())
"""
"""
#Get an arr size and ele for list from user and swap the element in list as per user wish.
arr = []
n = int(input("Enter how many elements you want in list:"))

for i in range(0,n):
    ele = int(input("Enter elements for list:"))
    arr.append(ele)
print(arr)
print("You can swap any elements in list. Please enter the postion of swap elements:")
pos1 = int(input())
pos2 = int(input())

arr[pos1],arr[pos2] = arr[pos2], arr[pos1]

print(arr)
"""
"""
# to find the min and largest element in list

arr = []
n = int(input("Enter how many elements you want in list:"))

for i in range(0,n):
    print("Enter elements for the position",i,"in the list: ", end="")
    ele = int(input())
    arr.append(ele)
    
print(arr)


small = min(arr)
lar = max(arr)

print("Smallest Element in arr is ", small)
print("Largest Element in arr is ", lar)

"""
# To find Fibonacci Series

n = int(input("Enter the number to find the fibonacci series: "))

n1, n2 = 0, 1
sum = 0

if n<=0:
    print("Please enter the number greter than 0")
else:
    for i in range(0, n):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
        