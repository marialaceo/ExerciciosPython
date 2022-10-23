
import math

# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

data = str(input('digite uma data no formato dd/mm/aaaa: '))

if (len(data) == 10 and data[2] == "/" and data[5] == "/"):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = data[6:]
    if (mes > 0 and mes < 13  and  len(ano) > 0 and len(ano) < 5):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            if dia > 0 and dia < 31:
                print('data válida')
            else:
                print('data inválida')
        if mes in [4, 6, 9, 11]:
            if dia > 0 and dia < 32:
                print('data válida')
            else:
                print('data inválida')
        if mes == 2:
            if int(ano) % 4 == 0 and int(ano) % 100 != 0 or int(ano) % 400 == 0:
                if dia > 0 and dia <= 29:
                    print(' data válida')
                else:
                    print('data inválida')
            else:
                if dia > 0 and dia <= 28:
                    print('data válida')
                else:
                    print('data inválida')
    else:
        print('data inválida')
else:
    print('formato inválido')