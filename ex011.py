l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
area = a*l
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². Para pintar essa parede, você vai precisar de {} litros de tinta'.format(l,a, area, area/2))