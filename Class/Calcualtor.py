from Python.Class.Complex import Complex
import re as rexpr


def parsing(text):
    token_map = ('\+', '\-',
                 '\*', '/',
                 '(', ')', 'i')
    split_expr = rexpr.findall('[\d.]+|[%s]' % ''.join(token_map), text)

    complexNumber = []
    allEq = []
    isBracket = False
    complex = []

    for i in range(len(split_expr)):
        if split_expr[i] == '(':
            isBracket = True
            complex.append(split_expr[i])
        elif isBracket is True:
            complex.append(split_expr[i])
            if split_expr[i] == ')':
                complexNumber.append(complex)
                complex = []
                isBracket = False
        elif isBracket is False:
            allEq.append(split_expr[i])

    for cn in complexNumber:
        temporaryComplex = Complex()
        for i in range(len(cn)):
            if cn[i] == '(':
                temporaryComplex.re = float(cn[i + 1])
            elif cn[i] == '+':
                temporaryComplex.im = float(cn[i + 1])
            elif cn[i] == '-':
                temporaryComplex.im = -float(cn[i + 1])
        allEq.append(temporaryComplex)
    return allEq

print("\nSample input: (2 + 1i) + ( 3 + 4i) \n")
expr = input("Really Simple Calculator: \n")

parsed = parsing(expr)

for i in range(len(parsed)):
    if '+' == parsed[i]:
        print(parsed[i+1] + parsed[i+2])
    elif '-' == parsed[i]:
        print(parsed[i+1] - parsed[i+2])
    elif '*' == parsed[i]:
        print(parsed[i+1] * parsed[i+2])
    elif '/' == parsed[i]:
        print(parsed[i+1] / parsed[i+2])

