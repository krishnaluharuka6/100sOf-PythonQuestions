# check if a given number such as 7 is prime 

n = 7
for i in range(2, (n//2)+1):
    if(n%i == 0):
        print(i)
        print("Not prime")
        break
    elif(i==n//2):
        print("Prime")

# or range is 

num=7
is_prime= True
for i in range(2,int(num ** 0.5)+1):
    if(num%i==0):
        is_prime=False

if(is_prime == True):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
