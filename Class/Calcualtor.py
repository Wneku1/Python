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

    for i in range(len(split_expr)):
        if split_expr[i] == '(':
            isBracket = True
            complex = []
            w = i
            while split_expr[w] != ')':
                complex.append(split_expr[w])
                w += 1
            complexNumber.append(complex)

        elif split_expr[i] == ')':
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


expr = input("Really Simple Calculator: \n")
parsed = parsing(expr)

if parsed[0] == '+':
    print(parsed[1] + parsed[2])
elif parsed[0] == '-':
    print(parsed[1] - parsed[2])
elif parsed[0] == '*':
    print(parsed[1] * parsed[2])
elif parsed[0] == '/':
    print(parsed[1] / parsed[2])
