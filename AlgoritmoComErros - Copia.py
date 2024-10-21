#  Aqui está um algoritmo que contém erros e exceções intencionais.
#  A ideia é identificar os problemas e corrigir o código.
import string

def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media

def exibir_media(notas):
    media = calcular_media(notas)
    if media > 7:
        print(f"Parabéns! Sua média é {media} e você foi aprovado.")
    else:
        print(f"Sua média é {media}. Infelizmente, você não foi aprovado.")

# Programa principal
try:
    numero_notas = int(input("Quantas notas você vai inserir? "))
    notas = []
    
    for i in range(numero_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    
    exibir_media(notas)
    
except ZeroDivisionError:
    print("Erro: Divisão por zero. Não é possível calcular a média sem notas.")
except ValueError:
    
    print("Erro: Valor inválido. Certifique-se de digitar um número válido.")
except KeyError:
    print("Erro: Chave inválida.")
finally:
    print("Programa finalizado.")

def verificar_senha(senha):
    num = []
    numero = string.digits
    for i in senha:
        if i in numero:
            num.append(i)
    if len(num) >= 1 and len(senha) >= 8:
        print("senha autorizada")
    else:
        raise ValueError

try:
    verificar_senha("abcde123")

except ValueError:
    print("Erro: verifique se a senha está dentro do padrão ")
except TypeError:
    print("Erro: verifique se a variavel senha foi passada corretamente.")
except Exception as error:
    print(error)

def transferencia(saldo,valor):
    if saldo < valor:
        raise ValueError
    else:
        print("transaçao autorizada")

try:
    transferencia(1500,1000)

except ValueError:
    print("Erro: saldo insuficiente")
except TypeError:
    print("Erro: verifique se a variavel da transaçao foi passada corretamente.")
