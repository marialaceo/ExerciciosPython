#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

LA=float(input('Digite o lado A do triângulo:'))
LB=float(input('Digite o lado B do triângulo:'))
LC=float(input('Digite o lado C do triângulo:'))

if(LA+LB>LC or LB+LC>LA or LA+LC>LB):
    print('Esses lados formam um triângulo.')
    if(LA==LB and LA==LC):
        print('Esse  triângulo é equilátero.')
    elif(LA==LB or LB==LC or LA==LC):
        print('Esse triângulo é isóceles.')
    elif(LA!=LB and LA!=LC and LB!=LC):
        print('Esse triângulo é escaleno.')
