"""
a=[5]
print(a)
print(type(a))

"""
"""
# Program for get input for list from user and print that list and print max and min number in the list

lst=[]
n=int(input("Enter elements for list: "))

for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(lst)

print(max(lst), "is a maximum number in the list")
print(min(lst), "is a minimum number in the list")

"""
