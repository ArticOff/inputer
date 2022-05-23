# You can code here for the command '/exe'.

import random

def gen_number():
    return random.randint(1, 10)

def main():
    while True:
        number = gen_number()
        if input('(1/10): ') == str(number):
            print('You won!')
            break
        else:
            print('Retry...')

if __name__ == '__main__':
    main()