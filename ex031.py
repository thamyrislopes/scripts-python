d = float(input('Digite a distância da viagem em KM: '))
'''if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45'''
v = d * 0.50 if d <= 200 else d * 0.45
print('Preço da passagem: R$ {:.2f}'.format(v))