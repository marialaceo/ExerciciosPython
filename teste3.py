#Faça um Programa que leia três números e mostre-os em ordem decrescente.#
a=int(input('digite um número:'))
b=int(input('digite um número:'))
c=int(input('digite um número:'))

if(a>b and a>c and b>c):
    print(a,b,c)
elif(a>b and a>c and c>b):
    print(a, c, b)
elif(b>a and b>c and a>c):
    print(b, a, c)
elif(b>a and b>c and c>a):
    print(b, c, a)
elif(c>a and c>b and a>b):
    print(c, a, b)
elif (c>a and c>b and b>a):
    print(c, b, a)
elif(a==b and a==c):
    print('são todos iguais')
elif(a==b and a>c):
    print('os dois primerios são iguais')
    print(a,b,c)
elif(a==c and a>b):
    print('o  primeiro e o ultimo são iguais')
    print(a, c, b)
elif(a==b and a<c):
    print('os dois primerios são iguais')
    print(c, a , b)
elif(a==c and a<b):
    print('o  primeiro e o ultimo são iguais')
    print(b, a, c)
elif(b==c and b>a ):
    print('os dois ultimos são iguais')
    print(b, c, a)
elif(b==c and b<a ):
    print('os dois ultimos são iguais')
    print(a, b, c)










