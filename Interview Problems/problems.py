"""
# Get list form user and swap elements as pwe your wish

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
in_str = input("Enter the string to Count the vowels:")
vowel = ['a', 'e', 'i', 'o', 'u']
str = in_str.lower()
countp = 0
countn = 0
for i in str:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
        countp += 1
    
if countp == 0:
    print("No Vowels found") 
else:
    print("Vowels found, No.",countp)
"""
