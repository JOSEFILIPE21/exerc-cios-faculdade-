import time
clientes = {}
def adicionar_cliente(nome,telefone,email,endereco):
    cliente = []
    cliente = (nome,telefone,email,endereco)
    clientes.append(list(cliente))
    print ("cliente {nome} cadastrado!")

def exibir_clientes():
    for i in clientes:
        print (f"nome: {i[0]}, telefone: {i[1]}, email: {i[2]}, endereco: {i[3]}")

def buscar_cliente(email):
    for clientes_encontrados in clientes:
        if email in clientes_encontrados:
            print ((f"nome: {clientes_encontrados[0]}, telefone: {clientes_encontrados[1]}, email: {clientes_encontrados[2]}, endereco: {clientes_encontrados[3]}"))
        
def remover_cliente(email):
    for cliente in clientes:
        if email in cliente:
            clientes.remove(cliente)
            print(f"cliente com email: {email} foi removido")
        else: print("cliente nao encontrado")


while True:
    busca = input("digite 1 para adicionar clientes, 2 para exibir clientes, 3 para buscar clientes, 4 para remover clientes ou 5 para sair: ")

    if busca == "1":
        nome = input("digite o nome: ")
        telefone = input("digite o telefone: ")
        email = input("digite o email: ")
        endereco = input("digite o endereço: ")
        adicionar_cliente(nome,telefone,email,endereco)

    elif busca == "2":
        exibir_clientes()
        time.sleep(3.0)

    elif busca == "3":
        email = input("digite o email: ")
        buscar_cliente(email)
        time.sleep(3.0)

    elif busca == "4":  
        email = input ("digite o email: ")    
        remover_cliente(email)

    elif busca == "5":
        break
    else:
        print ("digite corretamente: ")