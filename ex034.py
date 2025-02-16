sal = float(input('Digite o salário: R$'))
a1 = sal * 0.10
a2 = sal * 0.15
if sal > 1250:
    sal = sal + a1
    print('Salário atualizado, com o aumento de 10%: R${:.2f}'.format(sal))
else:
    sal = sal + a2
    print('Salário atualizado, com o aumento de 15%: R${:.2f}'.format(sal))