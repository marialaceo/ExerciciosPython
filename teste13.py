cont=int(0)
print('Responda respectivamente as perguntas abaixo:')
print('Telefonou para a vítima?')
print('Esteve no local do crime?')
print('Mora perto da vítima?')
print('Devia para a vítima?')
print('Já trabalhou com a vítima?')
for(c) in range(5):
    resposta= str(input('digite sua resposta:'))
    if resposta == "sim":
        cont=(cont+1)
    elif resposta != "sim" and resposta != "não":
        print('Resposta inválida')
if cont > 4:
    print('Assassino')
elif cont >=3 and cont <= 4:
    print('cumplice')
elif cont == 2:
    print('suspeito')
elif cont < 2 :
    print('inocente')
