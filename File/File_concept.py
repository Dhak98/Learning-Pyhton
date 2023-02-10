"""
fo = open("test1.txt","w")
fo.write("Sample Document it is used to understand the concept of File Handling\n")
fo.write("\n\n\nLooser only know the value of victory. Don't worry, do battle for victory")
fo.close

"""
"""
#To write a multi lines in txt file

fo = open("Multiline.txt","w")
my_content = ["Fistline\n","Secondline\n","Thirdline\n"]
fo.writelines(my_content)

"""
#concatenate new line using for loop

fo = open("txtforloop.txt","w")

my_content = ["The First Line\n","The Second Line\n","The Third Line\n"]

for lines in my_content:
    fo.write(lines+"\n")

fo.close