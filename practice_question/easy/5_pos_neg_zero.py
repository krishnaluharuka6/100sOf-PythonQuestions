number = input("Enter a number")

if int(number) > 0:
    print("Positive")
elif int(number) == 0:
    print("Zero")
elif int(number) < 0:
    print("Negative")
else:
    print("Invalid input")