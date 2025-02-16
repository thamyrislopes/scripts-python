'''import random
n1 = random.randint(0, 5)
n2 = int(input('Digite um número de 0 a 5: '))
if n1 == n2:
    print('Parabéns! Você acertou o número que o computador escolheu!')
else:
    print('Ihh... você não acertou o número que o computador escolheu!')
print('Computador: {} X Você: {}'.format(n1, n2))'''

from random import randint
from time import sleep #Faz o computador "dormir" por alguns segundos
computador = randint(0, 5)
print('-=-' * 20)
print('Vou mostrar um número entre 0 e 5. Será que você acerta?')
print('-=-' * 20)
jogador = int(input('Qual foi o número escolhido? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS! Você venceu!')
else: 
    print('GANHEI! Eu escolhi o número {} e não no {}.'.format(computador, jogador))

    
