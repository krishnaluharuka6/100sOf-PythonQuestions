# program to calculate the factorial of a given number such as 5

# this was solved using recursion
def factorial(n): 
    f = 1
    if(n==1 or n==0):
        return 1
    else:
        f = n * factorial(n-1)
    return f

fact = factorial(5)
print(fact)



# this is solved using for loop
n=5
facto = 1
for i in range(1,n+1):
    facto *= i
print(facto)

