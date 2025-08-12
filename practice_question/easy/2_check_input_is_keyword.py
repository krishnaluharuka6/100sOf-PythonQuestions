import keyword

user_input = input("Enter a word")

if keyword.iskeyword(user_input):
    print(f"{user_input} is python keyword")
else:
    print(f"{user_input} is not python keyword")