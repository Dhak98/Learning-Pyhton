#Program to count each vowel in dictonary

input_string = input("Enter the String: ")
input_string = input_string.casefold()

vowels = "aeiou"

vowelsdata = {}.fromkeys(vowels, 0)

for charcter in input_string:
    if charcter in vowels:
        vowelsdata[charcter] += 1

for vowels in vowelsdata:
    print(vowels," => ", vowelsdata[vowels])

