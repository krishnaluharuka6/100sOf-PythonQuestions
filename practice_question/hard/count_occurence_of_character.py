# write a program to count occurrences of the character "s" in the string "success"


string = "success"
i = 0
count = 0
while i < len(string):
    if string[i] == 's':
        count += 1
    i += 1

print(count)