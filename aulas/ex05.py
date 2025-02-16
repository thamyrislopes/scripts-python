n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Dgitite a segunda nota: '))
m = (n1 + n2)/2
print('MÉDIA: {:.1f}'.format(m))
print('PARABÉNS!' if m >= 7.0 else 'ESTUDE MAIS!')
'''if m >= 7.0:
    print('A sua média foi boa! Parabéns! :)')
else:
    print('A sua média foi ruim! Estude mais!')'''