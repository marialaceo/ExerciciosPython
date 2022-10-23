#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:


salario=float(input('Digite seu salário:'))

if(salario<=280.00):
    reajuste=salario*1.2
elif(salario>280.00 and salario<=700.00):
    reajuste=salario*1.15
elif(salario>700.00 and salario<=1500.00):
    reajuste=salario*1.1
elif(salario>1500.00):
    reajuste=salario*1.05

percentual=((reajuste/salario)-1)*100
valorDoAumento=reajuste-salario

print('seu salário sem reajuste é R$ {:.2f}'.format(salario))
print('o percentual de aumento é:{}%'.format(round(percentual)))
print('o valor do aumento foi: R${:.2f}'.format(valorDoAumento))
print('seu novo salário é: R${:.2f}'.format(reajuste))




