import math

a = float(input("digite a área desejada:"))
area = a * 1.1
lit = (area / 6)
# -----------------------------------------------------------------------------------------------------#
latas = math.ceil(lit / 18)
galao = math.ceil(lit / 3.6)
custo = latas * 80.0
custo2 = galao * 25.0
# ------------------------------------------------------------------------------------------------------#
if latas == 1:
    print('Você precisará de {} lata, e isso custará R$ {:.2f} '.format(latas, custo))
else:
    print('Você precisará de {} latas, e isso custará R$ {:.2f} '.format(latas, custo))
if galao == 1:
    print('Você precisará de {} galão, e isso custará R$ {:.2f}'.format(galao, custo2))
else:
    print('Você precisará de {} galões, e isso custará R$ {:.2f}'.format(galao, custo2))
# ------------------------------------------------------------------------------------------------------#
latas = int(lit // 18)
galao = math.ceil((lit % 18) / 3.6)
custo3 = (latas * 80.0) + galao * 25.0
# ------------------------------------------------------------------------------------------------------#
if latas > 1 and galao > 1:
    print('Você precisará de {} latas, {} galões, e isso custará R$ {:.2f}'.format(latas, galao, custo3))
elif (latas == 1 and galao == 1):
    print('Você precisará de {} lata, {} galão, e isso custará R$ {:.2f}'.format(latas, galao, custo3))
elif (latas == 1 and galao > 1):
    print('Você precisará de {} lata, {} galões, e isso custará R$ {:.2f}'.format(latas, galao, custo3))
elif (latas > 1 and galao == 1):
    print('Você precisará de {} latas, {} galão, e isso custará R$ {:.2f}'.format(latas, galao, custo3))
elif (latas == 0 and galao == 1):
    print('Você precisará de {} galão, e isso custará R$ {:.2f}'.format(galao, custo3))
elif (latas == 0 and galao > 1):
    print('Você precisará de {} galões, e isso custará R$ {:.2f}'.format(galao, custo3))
elif (latas == 1 and galao == 0):
    print('Você precisará de {} lata, e isso custará R$ {:.2f}'.format(latas, custo3))
elif (latas > 1 and galao == 0):
    print('Você precisará de {} latas, e isso custará R$ {:.2f}'.format(latas, custo3))
