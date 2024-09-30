
""" PRIMEIRO """
# def calculo(x,n):
#     if n == 0:
#         return 1
#     return x * calculo(x, n-1)

# res = calculo(2,3)
# print(res)

# import random
# numeros = []
""" SEGUNDO """
# def numero(n):
#     for i in range(1,n+1):
#         i = random.randint(1,100)
#         numeros.append(i)
#     print(max(numeros), min(numeros))

# numero(10)


""" TERCEIRO """
# def frutas(a,b,c,d,e):
#     fruta = list((a,b,c,d,e))
#     n = input("digite uma fruta:")
#     if n in fruta:
#         return "sim"
#     else:
#         return "não"

# res = frutas("mamao","melao","goiaba","limao","manga")
# print(res)

""" QUARTO """
# import random
# numeros = []

# def calculo(n):
#     for i in range(1,n+1):
#         i = random.randint(1,10)
#         numeros.append(i)
#         result = sum(numeros) /n
#     print (result)

# calculo(10)
""" QUINTO """
# pessoas = []

# def pessoa(nome,idade,cidade):
#     pes = list((nome,idade,cidade))
#     pessoas.append(pes)

# def exibir_pessoas():   
#     for i in (pessoas):
#         print(f"Nome:{i[0]} - Idade:{i[1]} - cidade: {i[2]}")

# pessoa("filipe","23","saquarema")
# pessoa("yan","23","saquarema")
# pessoa("gabriel","16","saquarema")

# exibir_pessoas()
""" SEXTO """
# import random
# numeros = [22,33,44,55,65,55,66,77,1,3,3]

# def numero(n):
#     numero = []
#     for i in range(1,n+1):
#         i = random.randint(1,5)
#         numero.append(i)
#     for x in numero:
#         if x not in numeros:
#             numeros.append(x)
#     print(numero)        
#     print(numeros)

#numero(10)

# def numero(n):
#     numero = []
#     for i in range(1,n+1):
#         i = random.randint(1,10)
#         numero.append(i)
#     for x in numero:
#         if x not in numeros:
#             numeros.append(x)
#     print(numeros)

# numero(10)



""" SETIMO """

# semana = {
#     "segunda" : 0,
#     "terça" : 0,
#     "quarta" : 0,
#     "quinta" : 0,
#     "sexta" : 0
# }

# def trabalho():
#     for i in semana:
#         horas = float(input(f"digite as horas trabalhadas na {i}:"))
#         semana[i] = horas
#     total = sum(semana.values())
#     print(f"total de horas trabalhadas foram {total:.0f} horas")

# trabalho()

""" OITAVO """

# alunos = {}

# def add_aluno(p,n):
#     aluno = [n]
#     alunos[p] = aluno

# add_aluno("filipe",9)
# add_aluno("yan",10)
# add_aluno("yan",10)
# #print(alunos)

# def exibir_nota(p):
#     for i in alunos:
#         if i == p:
#             result = (f"o aluno {i} esta com nota {alunos.get(i)}")
#     print(result)

# exibir_nota("yan") 
# def atualizar_nota(p,n):
#     for i in alunos:
#         if i == p:
#             alunos.update({i:n})

# atualizar_nota("filipe",10)
# exibir_nota("filipe")

""" NONO """
# produtos = {
#     "sacola" : 20,
#     "vassoura" : 15,
#     "escova" : 22,
#     "sabao" : 50
# }

# def verificar(p):
#         if p in produtos:
#             print(f"temos {produtos.get(p)} {p} no estoque")
#         else:
#             print(f"nao temos {p} no estoque")


# verificar("sabao")

""" DECIMO """

# paises = ["japao","nigeria","angola","brasil","canada"]
# cidades = ["xinlin","nigaia","angila","bacaxa","cans"]


# dicionario = dict(zip(paises,cidades))
# print(dicionario)

""" DE-PRIMEIRO """

# estudantes = {"filipe": {
#                 "matematica" : 10,
#                 "portugues" : 9,
#                 "ciencias" : 8},
#             "yan" : {
#                 "matematica" : 10,
#                 "portugues" : 8,
#                 "ciencias" : 7},
#             "fabricio" : {
#                 "matematica" : 9,
#                 "portugues" : 9,
#                 "ciencias" : 9},  
#             "cleber" : {
#                 "matematica" : 10,
#                 "portugues" : 9,
#                 "ciencias" : 8},
#             }  
                
                
# def acessar():
#     for chave,valor in estudantes.items():
#         print(f"aluno: {chave}")
#         for i,x in valor.items():
#             print(f" \t {i} = {x}")



# def alterar(p,m,n):
#     for chave, valor in estudantes.items():
#         if p in estudantes:
#             for i,x in chave.items():
#                 if m in valor:
#                     i[x] = n

# def alterar(p,m,n):
#     if p in estudantes and m in estudantes[p]:
#         estudantes[p][m] = n


# acessar()
# alterar("fabricio","ciencias",7)
# acessar()

""" DE-SEGUNDO """

# numeros = [1,2,3,4,5,6,7,8,9,10]

# def soma(numeros):
#     num = []
#     for i in numeros:
#         if i %2 == 0:
#             num.append(i)
#     print(sum(num))

# soma(numeros)

""" DE-TERCEIRA """

# produtos = {
#     "play5" : 2500,
#     "telefone" : 1500,
#     "nootbook" : 3000,
#     "computador" : 5000,
# }

# def dicionario(produtos):
#     preço = max(produtos.values())
#     for i in produtos:
#         if produtos[i] == preço:
#             print(f"o {i} é o produto mais caro custando R${preço}")

# dicionario(produtos)

""" DE-QUARTO """

# lista = [1,2,3,4,5,6,7,8,9,10]

# def lista_op(lista, nun=None):
#     if nun == None:
#         print(lista)
#     else:
#         lista_m = lista * nun
#         print(lista_m)

# lista_op(lista,2 )

""" DE-QUINTO """

# produtos = {
#     "play5" : 25,
#     "telefone" : 15,
#     "nootbook" : 30,
#     "computador" : 5,
# }

# produtos_ven = {
#     "play5" : 5,
#     "telefone" : 25,
#     "nootbook" : 3,
#     "computador" : 6,
# }

# def estoque(produtos,produtos_ven):
#     for i in produtos:
#         for v in produtos_ven:
#             if i == v:
#                 if produtos[i] < produtos_ven[v]:
#                     print(f"não temos {produtos_ven[v]} {i} no estoque ")
#                 if produtos[i] > produtos_ven[v]:
#                     produtos[i] = produtos[i] - produtos_ven[v]
#     print(produtos)

# estoque(produtos, produtos_ven)

""" DE-SEXTO """

# estudantes = [{"filipe": [10,9,8,8]},
#              {"yan" : [10,10,9,9]},
#              {"fabricio" : [8,8,8,8]},
#              {"cleber" : [9,9,9,9]},
# ]  
# media_estudantes = {}


# def calculo_media(estudantes):
#     for estudante in estudantes:
#         for chave in estudante :
#             media = sum(estudante[chave]) / len(estudante[chave])
#             media_estudantes.update({chave : media})


# calculo_media(estudantes)
# print(media_estudantes)

""" DE-SETIMO """

# numeros = [1,2,3,4,5,6,7,8,9,10]


# def busca_binaria_recursiva(lista, elemento, inicio=0, fim=None):

#     inicio = numeros[0]
#     fim = numeros[-1]
#     meio = (inicio + fim) // 2

#     if lista[meio] == elemento:
#         print(meio)
#     elif lista[meio] > elemento:
#         return busca_binaria_recursiva(lista, elemento, inicio, meio - 1)
#     else:
#         return busca_binaria_recursiva(lista, elemento, meio + 1, fim)

# busca_binaria_recursiva(numeros,6)

""" DE-OITAVO """

livros = []

def cadastrar_livro(titulo,autor,quant,codigo):
    livros.append({
        "titulo" : titulo,
        "autor" : autor,
        "quant" : quant,
        "codigo" : codigo
    })

cadastrar_livro("ze comeia","yan",4,"L001")
cadastrar_livro("vegete(o pirata)","filipe",99,"L002")

def buscar_livro(codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            return print(livro["titulo"])
    return print(f"não existe um livro com o codigo {codigo} ")

buscar_livro("L002")
buscar_livro("L003")

def atualizar_livro(codigo,quant):
    for livro in livros:
        if livro["codigo"] == codigo:
            livro["quant"] = quant
            return print(f"temos {livro['quant']} livros do {livro['titulo']} em estoque agora")
    return print(f"não existe um livro com o codigo {codigo} ")

atualizar_livro("L002",9)
atualizar_livro("L003",56)

def remover_livro(codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            livros.remove(livro)
            return print(f"o livro {livro['titulo']} foi removido")
    return print(f"não existe um livro com o codigo {codigo} ")

remover_livro("L001")
remover_livro("L003")

def listar_livros(livros):
    for livro in livros:
        print(f"{livro}\n")
    return

listar_livros(livros)
