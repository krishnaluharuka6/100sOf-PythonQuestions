# program to count occurence of each character in the word "programming"

string = "programming"
dict = {}

for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

for i in dict:
    print(f"{i}: {dict[i]}")