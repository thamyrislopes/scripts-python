nome = str(input('Digite o seu nome completo: ')).strip()
separa = nome.split()
print('Primeiro nome: {}'.format(separa[0]))
print('Último nome: {}'.format(separa[len(separa)-1]))