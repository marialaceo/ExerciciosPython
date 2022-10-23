import math

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

oper = str(input('qual operação deseja efetuar + - * ou /: '))

if oper == "+":
    resultado = num1 + num2
elif oper == "-":
    resultado = num1 - num2
elif oper == "*":
    resultado = num1 * num2
elif oper == "/":
    resultado = num1 / num2
elif oper != "+" and oper != "-" and oper != "*" and oper != "/":
    print('Símbolo errado')

if resultado % 2 == 0:
    print('É par')
else:
    print(" É impar")
if resultado >= 0:
    print("É positivo")
else:
    print("É negativo")

if resultado - int(resultado) == 0:
    print("Não é decimal")
else:
    print("É decimal")