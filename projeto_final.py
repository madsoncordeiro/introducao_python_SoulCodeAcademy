'''
EXERCÍCIO PROPOSTO

1. Deve se criar 5 funções diferentes, sendo elas somar, subtrair, dividir, multiplicar e listar.
2. Deve se criar um MENU com if else sendo que o usuário escolha qual função deve acessar. 
3. Ao ser escolhida a função, o usuário é direcionado a ela e insere os parâmetros que desejam realizar 
as operações.
4. As funções matemáticas devem receber os números para realizar a operação, realizar o cálculo e imprimir o 
resultado para o usuário.
Na função listar, deve-se criar uma lista de vantagens do python e imprimir para o usuário.
'''

# 1.
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

def listar_vantagens_python():
    vantagens = ([
        "\n1. Facilidade de aprendizado e utilização por diversos públicos. ", 
        "2. Versatilidade e uso para variados fins. ",
        "3. Trata-se de uma linguagem gratuita e de fonte aberta. ",
        "4. Pode ser usada em diversos sistemas operacionais. ",
        "5. Tem grande número de bibliotecas, o que amplia as suas possibilidades. "
    ])
    
    for vantagem in vantagens:
        print(vantagem)

# 2.
print("-------------------MENU-----------------------\n")
print("\nAqui está o menu do programa com as seguintes opções:\n")
print("1 - Realizar a operação de SOMA. ")
print("2 - Realizar a operação de SUBTRAÇÃO. ")
print("3 - Realizar a operação de DIVISÃO. ")
print("4 - Realizar a operação de MULTIPLICAÇÃO. ")
print("5 - Listar as vantagens da linguagem Python. ")
print("6 - Sair do programa. \n\n")
opcao_escolhida = int(input("Qual função você quer realizar? (Escolha o número correspondente) "))
if opcao_escolhida == 1:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print(numero1, "+", numero2, "=", somar(numero1, numero2))
elif opcao_escolhida == 2:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print(numero1, "-", numero2, "=", subtrair(numero1, numero2))
elif opcao_escolhida == 3:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print(numero1, "/", numero2, "=", dividir(numero1, numero2))
elif opcao_escolhida == 4:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print(numero1, "X", numero2, "=", multiplicar(numero1, numero2))
elif opcao_escolhida == 5:
    print(listar_vantagens_python())
else:
    print("\nSaindo do programa... ")