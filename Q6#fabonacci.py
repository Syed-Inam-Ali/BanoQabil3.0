'''Generate Fibonacci Series up to n terms:

Input:
Enter the number of terms: 6
Output:
Fibonacci Series up to 6 terms: 0, 1, 1, 2, 3, 5'''

n = int(input('Enter the number of terms:'))
a = 0
b = 1
print (a)
print (b)
for i in range(1,n-1):
 
    c = a+b
    print (c) 
    a = b
    b = c