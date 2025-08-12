# write a program to print the word "python" in reverse using for loop

text ="python"
for i in text[-1::-1]: #here i used slicing concept
    print(i, end="")

print("\n")




# using reverse method of string
list=list(text)
list.reverse()
text=",".join(list)
text=text.replace(",","")
print(text)



# using while loop write a program to reverse each word of the sentence
sentence = "Hello World"
words = sentence.split(" ")
for word in words:
    i=len(word)-1
    while i>=0:
        print(word[i], end="")
        i -= 1
    print(end=" ")
print()


for x in sentence[::-1]:
    print(x, end="")
