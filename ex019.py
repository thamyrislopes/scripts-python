from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
'''Criar uma lista e, no Python, a lista fica entre colchetes.'''
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))