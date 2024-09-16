def recursiva(b,e):
    if e == 0:
        return 1
    return b * recursiva (b,e-1)

resultado = recursiva(2,3)
#print(resultado)

def fibonacci(f):
    if f == 0:
        return 0
    elif f == 1:
        return 1
    return fibonacci(f-1) + fibonacci(f-2)

resultado = fibonacci(10)
#print(resultado)

def contagem(c):
    if c < 10:
        return 1
    return 1 + contagem(c/10)

resultado = contagem(103)
#print(resultado)

def palindromo(p):
    if len(p) == 1 or len(p) == 0:
        return "é palindromo"
    elif p[0] != p[-1]:
        return "não é palindromo"

    return palindromo(p[1:-1])

resultado = palindromo('arara')
print (resultado)


