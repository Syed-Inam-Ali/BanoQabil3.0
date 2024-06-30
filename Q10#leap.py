'''Check Leap Year:

Input:
Enter a year: 2020
Output:
2020 is a leap year.'''

year = int(input('Enter a year:'))
if year % 4 ==0:
    print(f'{year} is a leap year.')