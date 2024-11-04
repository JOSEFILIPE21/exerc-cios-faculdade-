#EXERCICIO1

import os

with open('mensagem.txt','w') as arquivo:
    arquivo.write("escrevendo alguma coisa\n")
    arquivo.write("escrevendo outra coisa\n")
    arquivo.write("escrevendo qualquer coisa")

with open('mensagem.txt','r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)



#EXERCICIO 2

with open('frase_usuario.txt','w') as arquivo:
    arquivo.write(input("digite uma frase: "))

with open('frase_usuario.txt','r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)