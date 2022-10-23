import math

print('+ - soma')
print('- - subtração')
print('* - multiplicação')
print('/ - divisão')
print('^ - x^y')
print('^^ - x^2')
print('sen - seno(x)')
print('cos - cosseno(x)')
print('tan - tangente(x)')
print("arcsen - arco seno")
print('arccos - arco cosseno')
print('arctan - arco tangente')
print('raiz - raiz quadrada')
print('pi - número pi - obs: ultilize o pi na área que pede o número')
print('e - número euler - obs: ultilize o e na área que pede o número')
print('log - logarítmo na base 10')
print('ln - logarítmo natural (base e)')
print('neg - transformar o número em um número negativo')
print('c - apagar')
print('off - encerrar a operação')


num = str(input('digite um número:'))
op = str(input('digite a operação:'))

if op == "+" :
    num1 = str(input('digite um número:'))
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num1 == "e":
        num1 = "0"
        num1 = float(num)
        num1 = math.e
    if num1 == "pi":
        num1 = "0"
        num1 = float(num1)
        num1 = math.pi
    if num1 == "e":
        num1 = "0"
        num1 = float(num1)
        num1 = math.e
    num1 = float(num1)
    num = float(num)
    resultado = num + num1
    print(resultado)
elif op == "-":
    num1 = float(input('digite um número:'))
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    if num1 == "pi":
        num1 = "0"
        num1 = float(num1)
        num1 = math.pi
    if num1 == "e":
        num1 = "0"
        num1 = float(num1)
        num1 = math.e
    num1 = float(num1)
    num = float(num)
    resultado = num - num1
    print(resultado)
elif op == "*":
    num1 = float(input('digite um número:'))
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    if num1 == "pi":
        num1 = "0"
        num1 = float(num1)
        num1 = math.pi
    if num1 == "e":
        num1 = "0"
        num1 = float(num1)
        num1 = math.e
    num = float(num)
    num1 = float(num1)
    resultado = num * num1
    print(resultado)
elif op == "/":
    num1 = float(input('digite um número:'))
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    if num1 == "pi":
        num1 = "0"
        num1 = float(num1)
        num1 = math.pi
    if num1 == "e":
        num1 = "0"
        num1 = float(num1)
        num1 = math.e
    num1 = float(num1)
    num = float(num)
    resultado = num / num1
    print(resultado)
elif op == "^":
    num1 = float(input('digite um número:'))
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    if num1 == "pi":
        num1 = "0"
        num1 = float(num1)
        num1 = math.pi
    if num1 == "e":
        num1 = "0"
        num1 = float(num1)
        num1 = math.e
    num1 = float(num1)
    num = float(num)
    resultado = math.pow(num, num1)
    print(resultado)
elif op == "^^":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float
    resultado = math.pow(num,2)
    print(resultado)
elif op == "sen":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.sin(math.radians(num))
    print(resultado)
elif op == "cos":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.cos(math.radians(num))
    print(resultado)
elif op == "arcsen":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.asin(math.radians(num))
    print(resultado)
elif op == "arccos":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.acos(math.radians(num))
    print(resultado)
elif op == "arctan":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.atan(math.radians(num))
    print(resultado)
elif op == "raiz":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.sqrt(num)
    print(resultado)
elif op == "log":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.log10(num)
    print(resultado)
elif op == "ln":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = math.log1p(num)
    print(resultado)
elif op == "neg":
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = num * (-1)
    print(resultado)
elif op == "c":
    print('0')
    num = str(input('digite um número:'))
    if num == "pi":
        num = "0"
        num = float(num)
        num = math.pi
    if num == "e":
        num = "0"
        num = float(num)
        num = math.e
    num = float(num)
    resultado = num
elif op == "off":
    print('encerrou a operação')
elif op != "+" and op != "-" and op != "*" and op != "/" and op != "c" and op != "^" and op != "^^" and op != "sen" and op != "cos" and op !="tan"  and op != "arcsen" and op != "arccos" and op != "arctan" and op != "raiz"  and op != "log" and op != "ln" and op != "neg":
    print('erro')


while op == "+" or op == "-" or op == "c" or op == "*" or op == "/" or op == "^" or op == "^^" or op == "sen" or op == "cos" or op == "tan" or op == "arcsen" or op == "arccos" or op == "arctan" or op == "raiz"  or op == "log" or op == "ln" or op == "neg" or op == "off":
    op = str(input('digite a operação:'))
    if op == "+":
        num=str(input('digite um número:'))
        if num == "pi":
            num = "0"
            num = float(num)
            num = math.pi
        if num == "e":
            num = "0"
            num = float(num)
            num = math.e
        num = float(num)
        resultado = resultado + num
        print(resultado)
    elif op == "-":
        num=str(input('digite um número:'))
        if num == "pi":
            num = "0"
            num = float(num)
            num = math.pi
        if num == "e":
            num = "0"
            num = float(num)
            num = math.e
        num = float(num)
        resultado = resultado - num
        print(resultado)
    elif op == "*":
        num=str(input('digite um número:'))
        if num == "pi":
            num = "0"
            num = float(num)
            num = math.pi
        if num == "e":
            num = "0"
            num = float(num)
            num = math.e
        num = float(num)
        resultado = resultado * num
        print(resultado)
    elif op == "/":
        num=str(input('digite um número:'))
        if num == "pi":
            num = "0"
            num = float(num)
            num = math.pi
        if num == "e":
            num = "0"
            num = float(num)
            num = math.e
        num = float(num)
        resultado = resultado / num
        print(resultado)
    elif op == "^":
        num=str(input('digite um número:'))
        if num == "pi":
            num = "0"
            num = float(num)
            num = math.pi
        if num == "e":
            num = "0"
            num = float(num)
            num = math.e
        num = float(num)
        resultado = math.pow(resultado, num)
        print(resultado)
    elif op == "^^":
        resultado = math.pow(resultado)
        print(resultado)
    elif op == "sen":
        resultado = math.sin(math.radians(resultado))
        print(resultado)
    elif op == "cos":
        resultado = math.cos(math.radians(resultado))
        print(resultado)
    elif op == "arcsen":
        resultado = math.asin(math.radians(resultado))
        print(resultado)
    elif op == "arccos":
        resultado = math.acos(math.radians(resultado))
        print(resultado)
    elif op == "arctan":
        resultado = math.atan(math.radians(resultado))
        print(resultado)
    elif op == "raiz":
        resultado = math.sqrt(resultado)
        print(resultado)
    elif op == "log":
        resultado = math.log10(resultado)
        print(resultado)
    elif op == "ln":
        resultado = math.log1p(resultado)
        print(resultado)
    elif op == "neg":
        resultado = resultado * (-1)
        print(resultado)
    elif op == "c":
        print('0')
        num = str(input('digite um número:'))
        if num == "pi":
            num = "0"
            num = float(num)
            num = math.pi
        if num == "e":
            num = "0"
            num = float(num)
            num = math.e
            num = float(num)
        resultado = num
    elif op == "off":
        print('encerrou a operação')
    elif op != "+" and op != "-" and op != "*" and op != "/" and op != "c" and op != "^" and op != "^^" and op != "sen" and op != "cos" and op != "tan" and op != "arcsen" and op != "arccos" and op != "arctan" and op != "raiz" and op != "log" and op != "ln" and op != "neg":
        print('digite apenas operações válidas')
