# write a program to count number of vowels in the word education


count=0
for i in "education":
    if(i == 'a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count += 1

print(f"{count}")