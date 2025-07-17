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