"""clientes = []

def adicionar_clientes(nome,telefone,email,endereço):
    cliente = []
    cliente = (nome,telefone,email,endereço)
    clientes.append(list(cliente))


adicionar_clientes("jose filipe","22 998573662","filipe.zakiler@gmail.com", "rua cavalcante")
adicionar_clientes("yan","22 997453432","yan.you@gmail.com","rua serra do mato grosso")

print (clientes)

def exibir_clientes():
    for i in clientes:
        print (i)
exibir_clientes()

def buscar_clientes(email):
    for clientes_encontrados in clientes:
        if email in clientes_encontrados:
            print (clientes_encontrados)

buscar_clientes("filipe.zakiler@gmail.com")

        
def remover_cliente(email):
    for cliente in clientes:
        if email in cliente:
            clientes.remove(cliente)
        
remover_cliente("filipe.zakiler@gmail.com")

print (clientes)"""

import time
clientes = []
def adicionar_clientes(nome,telefone,email,endereço):
    cliente = []
    cliente = (nome,telefone,email,endereço)
    clientes.append(list(cliente))

def exibir_clientes():
    for i in clientes:
        print (i)

def buscar_clientes(email):
    for clientes_encontrados in clientes:
        if email in clientes_encontrados:
            print (clientes_encontrados)
        
def remover_cliente(email):
    for cliente in clientes:
        if email in cliente:
            clientes.remove(cliente)


while True:
    busca = input("digite 1 para adicionar clientes, 2 para exibir clientes, 3 para buscar clientes, 4 para remover clientes ou 5 para sair")

    if busca == "1":
        nome = input("digite o nome")
        telefone = input("digite o telefone")
        email = input("digite o email")
        endereço = input("digite o endereço")
        adicionar_clientes(nome,telefone,email,endereço)
        continue

    elif busca == "2":
        exibir_clientes()
        time.sleep(3.0)
        continue

    elif busca == "3":
        email = input("digite o email")
        buscar_clientes(email)
        time.sleep(3.0)
        continue

    elif busca == "4":  
        email = input ("digite o email")    
        remover_cliente(email)
        continue

    elif busca == "5":
        break
    else:
        print ("digite corretamente")
        continue




