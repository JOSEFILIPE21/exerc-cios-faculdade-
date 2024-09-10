lista_tarefas = []
def adicionar_tarefas(lista_tarefas,descricao,status,prioridade):
    if not lista_tarefas:
        id = 1
    else:
        id = max((tarefa["id"]) for tarefa in lista_tarefas)+1

    tarefa = {
        "id" : id,
        "descricao" : descricao,
        "status" : status,
        "prioridade" : prioridade
        }
    lista_tarefas.append(tarefa)
adicionar_tarefas( lista_tarefas,"fazer arroz", "pendente", "alta")
adicionar_tarefas( lista_tarefas,"fazer feijao", "pendente", "media")
adicionar_tarefas( lista_tarefas,"fazer macarrao", "pendente", "media")
#print(lista_tarefas)

def vizualisar_tarefas(lista_tarefas):
    for i in lista_tarefas:
        result = ("ID:",i.get("id"),"/", "DESCRIÇÃO:",i.get("descricao"),"/", "STATUS:", i.get("status"),"/", "PRIORIDADE:", i.get("prioridade"))
        print(result)
#vizualisar_tarefas(lista_tarefas)
def filtrar_tarefas(lista_tarefas, status=None, prioridade=None ):
    for tarefa in lista_tarefas:
        if tarefa.get("status") == status or tarefa.get("prioridade") == prioridade:
            print(tarefa)
            return
    vizualisar_tarefas(lista_tarefas)
result = filtrar_tarefas(lista_tarefas, status=None, prioridade="media")
#print(result)

    
