'''---just a work---'''
import random
say = input('what i want to say:')
guess = int(say)
secret = random.randint(1,10)
time = 1
if guess == secret:
    print('you are right' + ' wow')
else:
    print('go on ' + 'my bro')
while guess != secret and time < 3:
    if guess > secret:                         #elseif?
        print('high')
    else:
        print('low')
    say = input('agin:')
    guess = int(say)
    time = time + 1
if time < 3:
    print('well')
else:
    print(secret)



