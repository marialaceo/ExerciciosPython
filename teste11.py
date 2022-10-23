#flor= arredondar pra baixo ceil= arredondar pra cima trunc= cortar oq tiver depois da vírgula

#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

import math

numero = float(input('Digite um número qualquer: '))

decimal = numero - int(numero)
if decimal > 0:
    print('Esse número é decimal.')
elif decimal == 0:
    print('Esse número não é decimal.')