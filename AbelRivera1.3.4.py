from __future__ import print_function 
import random

def guess_once():
    secret = random.randint(1, 1000)
    print('Tengo un numero entre 1 and 1000.')
    guess = int(raw_input('Adivina: '))
    if guess != secret:
        print('Incorrecto, mi numero es ', secret, '.', sep='')
    else:
        print('Correcto, mi numero es', guess, end='!\n')