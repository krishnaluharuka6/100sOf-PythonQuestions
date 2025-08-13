# count consonant in a string "learning"

string = "learning"
vowel = "aeiou"
count = 0
i = 0
while i < len(string):
    if string[i].lower() not in vowel and string[i].isalpha():
        count += 1
    i += 1

print(f"Number of consonant in a string is {count}")