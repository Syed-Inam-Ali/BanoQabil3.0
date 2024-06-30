#Find the Factorial of a Number:
n =int(input("Enter a Number: "))
num = 1
for i in range(1,n+1):
    num*=i
print(f"Factorial of {n} is:",num)