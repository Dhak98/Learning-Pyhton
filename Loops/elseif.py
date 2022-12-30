"""
# Qus: Take two int values from user and print greatest among them.

print("Enter the two number to find which is greater")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num1," is greater among them")
elif num2 > num1:
    print(num2," is greater among them")
else:
    print("Are you kidding, both are equal numbers")

print("Thank you ......")

"""
#####################################################################

"""
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

# Ans:

mark = int(input("Enter the mark to find the grade: "))
if mark < 25:
    print("Your grade is F")
elif mark == 25 and mark < 45:
    print("Your grade is E")
elif mark == 45 and mark < 50:
    print("Your grade is D")
elif mark == 50 and mark < 60:
    print("Your grade is c")
elif mark == 60 and mark < 80:
    print("Your grade is B")
else:
    print("Your grade is A") 

"""
#############################################################################

"""
# Qus : Take input of age of 3 people by user and determine oldest and youngest among them.

Ans :-


print("Tell your age it find who is younger and older among them")

age1 = int(input("Enter the age John :"))
age2 = int(input("Enter the age Peter :"))
age3 = int(input("Enter the age Emily :"))

if age1 < age2 and age1 < age3:
    print("John your age is", age1 ,"and you are young among them")
elif age2 < age1:
    print("Peter your age is", age2 ,"and you are young among them")
else:
    print(" Emily your age is", age3 ,"and you are young among them")
if age1 > age2 and age1 > age3:
    print(" John your age is", age1 ,"and you are Older among them")
elif age2 > age1:
    print("Peter your age is", age2 ,"and you are older among them")
else :
    print(" Emily your age is", age3 ,"and you are older among them")

"""
#####################################################################################

"""
# Qus:

A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.

# Ans:

print("Are allowed to exam , you can check here")
print("* 75 % or above need to attend exam")
ch = int(input("Enter the Number of classes held: "))
ca = int(input("Enter the Number of classes attended: "))
percentage = (ca/ch)*100
print("Your attendence percentage is",int(percentage))
if percentage > 75:
    print("You are alowed to attend the exam")
elif percentage == 75:
    print("You are alowed to attend the exam")
else:
    print("Sorry!... You are not allowed, Better Luck Next Time")

"""
##################################################################################################

"""
# Qus

Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".

# Ans


age = int(input("Enter the age: "))
sex = input("Enter you Gender( M or F ): ")
ms = input("Enter you Marital Status( Y or N ): ")
if sex == 'f':
    print("You are allowed to work on urban areas only...")
elif sex == 'm' and age >= 20 and age <= 40:
    print("You can work anywhere")
elif sex == 'm' and age >= 40 and age <= 60:
    print("You are allowed to work on urban areas only...")
else:
    print("ERROR")

"""