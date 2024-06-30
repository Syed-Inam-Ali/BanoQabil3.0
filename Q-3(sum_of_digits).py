"""Create a program that calculates the sum of the digits of a given number. For example, if
the input is 12345, the output should be 15."""

num = list(input("Enter digits you wanna find sum: "))
sum=0
for i in range(0,len(num)+1):
     sum+=i
print(f"sum of the given digits are : {sum}")
