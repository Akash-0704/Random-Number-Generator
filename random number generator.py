import random

while True:
    randnum=random.randint(0,10)
    x = int(input('Enter a number between 1 to 10: '))
    if x==randnum:
        print('correct')
        option = input('continue?(y/n): ')
        if option=='y':
            continue
        else:
            break

    else:
        print('incorrect')
        option = input('continue?(y/n):')
        if option=='y':
            continue
        else:
            break
    