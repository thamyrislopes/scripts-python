'''v = float(input('Digite a velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print('Você ultrapassou os 80Km/h e foi multado! Valor da multa: R$ {:.2f}'.format(m))'''

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')