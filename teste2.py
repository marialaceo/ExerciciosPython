num=int(input('digite um número:'))
if(num>=0):
    print('\033[42m{} é positivo\033[m' .format(num))
else:
    print('\033[41m{} é negativo\033[m'.format(num))