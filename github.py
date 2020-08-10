#Question 1
minute = int(input('minute: '))
salary = int(input('salary: '))
def deduct(minute, salary):
    """takes in the minute empolyee resumes to work, and the salary of the empolyee."""

if minute < 30:
    print('Welcome to work')
elif minute >= 30 and minute <= 44:
    a = minute - 30
    b = salary - 500
    print('You are late by',a,'minutes')
    print('Your salary will be',b, 'naira')
    print("Don't be late again")

elif minute >= 45 and minute <= 59:
    a = minute - 30
    b = salary - 700
    print('You are late by', a, 'minutes')
    print('Your salary will be', b, 'naira')
    print("Don't be late again")

elif minute >= 60:
    a = minute - 30
    b = salary - 1000
    print('You are late by', a, 'minutes')
    print('Your salary will be', b, 'naira')
    print("Don't be late again")

else:
    print("Report to Manager's office")




#Question 2
c = int(input('number: '))
d = int(input('factor: '))
def factor_check(number, factor):
    """takes in number, factor and check if it is a factor of the number"""
if c % d == 0:
    print(True)
else:
    print(False)
