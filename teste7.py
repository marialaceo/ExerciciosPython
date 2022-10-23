#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))

media = (nota1 + nota2 + nota3) / 3

if(media>=0.00 and media<=4.00):
    print('Sua média é {:.2f} e o conceito é \033[31mE\033[m. Você está\033[31m REPROVADO \033[m'.format(media) )
elif(media>4.00 and media<=6.00):
    print('Sua média é {:.2f} e o conceito é \033[31mD\033[m. Você está\033[31m REPROVADO \033[m'.format(media))
elif(media>6.00 and media<=7.50):
    print('Sua média é {:.2f} e o conceito é \033[32mC\033[m. Você está\033[32m APROVADO \033[m'.format(media))
elif(media>7.50 and media<=9.00):
    print('Sua média é {:.2f} e o conceito é \033[32mB\033[m. Você está\033[32m APROVADO \033[m'.format(media))
elif(media>9.00 and media<=10.00):
    print('Sua média é {:.2f} e o conceito é \033[32mA\033[m. Você está\033[32m APROVADO \033[m'.format(media))
