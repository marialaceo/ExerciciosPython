#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
 #       Salário Bruto: (5 * 220)        : R$ 1100,00
  #      (-) IR (5%)                     : R$   55,00
   #     (-) INSS ( 10%)                 : R$  110,00
    #    FGTS (11%)                      : R$  121,00
     #   Total de descontos              : R$  165,00
      #  Salário Liquido                 : R$  935,00
ValorHora=float(input('Digite o valor da sua hora:'))
HoraPorMes=int(input('Digite quantas horas por mês você trabalha:'))

SalarioBruto=ValorHora*HoraPorMes
FGTS=(SalarioBruto*0.11)
INSS=(SalarioBruto*0.1)
Sindicato=(SalarioBruto*0.03)

print('Salário Bruto: ({} * {})                    : R$ {:.2f} '.format(ValorHora, HoraPorMes, SalarioBruto))

if(SalarioBruto<=900.00):
        IR=float(0.00)
        print('(-) IR (isento)                                : R$ {:.2f}'.format(IR))
elif(SalarioBruto>900.00 and SalarioBruto<=1500.00):
        IR=(SalarioBruto*0.05)
        print('(-) IR (5%)                                    : R$ {:.2f}'.format(IR))
elif(SalarioBruto>1500.00 and SalarioBruto<=2500.00):
        IR=(SalarioBruto*0.1)
        print('(-) IR (10%)                                   : R$ {:.2f}'.format(IR))
elif(SalarioBruto>2500.00):
        IR=(SalarioBruto*0.2)
        print('(-) IR (20%)                                   : R$ {:.2f}'.format(IR))

print('INSS (10%)                                     : R$ {:.2f}'.format(INSS))
print('FGTS (11%)                                     : R$ {:.2f}'.format(FGTS))

TotalDeDescontos=(FGTS+IR+INSS+Sindicato)
print('Total de Descontos                             : R$ {:.2f}'.format(TotalDeDescontos))

SalarioLiquido=SalarioBruto-TotalDeDescontos
print('Salário Liquido                                : R$ {:.2f}'.format(SalarioLiquido))


