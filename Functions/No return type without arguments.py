print("If you want Addition, press 1" "\nIf you want Substracion, press 2","\nIf you want Multiplication, press 3","\nIf you want Division, press 4")
n = int(input("Enter what you want: "))
if n == 1:
    def add():
        a = int(input("Enter the Number 1: "))
        b = int(input("Enter the Number 2: "))
        c = a+b
        print("Total",c)
    add()
elif n == 2:
    def sub():
        a = int(input("Enter the Number 1: "))
        b = int(input("Enter the Number 2: "))
        c = a-b
        print("Total",c)
    sub()
elif n == 3:
    def mul():
        a = int(input("Enter the Number 1: "))
        b = int(input("Enter the Number 2: "))
        c = a*b
        print("Total",c)
    mul()
elif n == 4:
    def div():
        a = int(input("Enter the Number 1: "))
        b = int(input("Enter the Number 2: "))
        c = a/b
        print("Total",c)
    div()
else:
    print("Please, Enter what you want correctly...........")



