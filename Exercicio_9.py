'''
EXERCÍCIO PROPOSTO

1. Crie uma função que receba dois parâmetros e realize sua soma, subtração, multiplicação e divisão. 
2. Informe esses resultados através de um print ao usuário dentro da função.
'''

# 1.
def operacoes(a, b):
    soma = a + b
    print("A soma de a + b é igual a", soma, ".")
    subtracao = a - b
    print("A subtracao de a - b é igual a", subtracao, ".")
    multiplicacao = a * b
    print("A multiplicação de a X b é igual a", multiplicacao, ".")
    divisao = a / b
    print("A divisão de a por b é igual a", divisao, ".")

# 2.
operacoes(10, 2)