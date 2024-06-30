# Author: [Syed Inam Ali]
# Roll Number: [03463319859]
# Email: [inamali19891989@gmail.com]
# Write a program that checks if a given number is prime or not. Display an appropriate message.
Num = int(input("Enter Any Number:"))
if Num%2!=0 and Num%3!=0 and Num%5!=0 and Num%7!=0:
    print(f"The input Number {Num} is a Prime Number")
else:
    print(f"The input Number {Num} is not a Prime Number")


