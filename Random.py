import random
a = random.randint(0, 20)
c = int(input('Guess Number: '))
print('Random number is',a)
if a == c:
    print("You guessed right")
elif c < a:
    print('You are wrong number is low')
elif c > a:
    print('You are wrong number is high')
else:
    print('There is a problem')

