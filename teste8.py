# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
# valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
# os demais valores,sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

print('Para calcular as raízes é preciso que informe o valor de (a,b,c)')
print('                                                                                   ')
ax = int(input('Digite o valor de a:'))
bx = int(input('Digite o valor de b:'))
cx = int(input('Digite o valor de c:'))

if (ax == 0):
    print('a equação não é do segundo grau')
elif (ax != 0):
    delta = math.pow(bx, 2) - 4 * (ax) * (cx)
    if (delta < 0):
        print('a equação não possui raízes reais')
    elif (delta == 0):
        print('a equação possui raízes iguais')
        x1 = (-bx + math.sqrt(delta)) / 2 * ax
        x2 = (-bx - math.sqrt(delta)) / 2 * ax
        print('As raízes dessa equação são {:.2f} e {:.2f}'.format(x1, x2))
    elif (delta > 0):
        print('a equação possui duas raízes')
        x1 = (-bx + math.sqrt(delta)) / 2 * ax
        x2 = (-bx - math.sqrt(delta)) / 2 * ax
        print('As raízes dessa equação são {:.2f} e {:.2f}'.format(x1, x2))
