'''
EXERCÍCIO PROPOSTO

1. Crie três inputs que receba os três dados abaixo:
-Nome do tipo string

-Altura do tipo Float

-CPF do tipo inteiro

2. Exiba, através de um único print, as três informações para o usuário.
'''

# Criando as variáveis que armazenarão os dados digitados pelos usuários
nome = str(input("Qual o seu nome? "))
altura = float(input("Qual a sua altura? "))
cpf = int(input("Qual o número do seu CPF? "))

# Exibindo para o usuário as informações digitadas por ele
print("O seu nome é", nome, ", você tem", altura, "metros de altura e o número do seu CPF é", cpf, ".")