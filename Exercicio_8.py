'''
EXERCÍCIO PROPOSTO

1. Crie um dicionário contendo dias da semana sendo dia1, dia2, dia3... as chaves e o dia seu valor. 
Ex: “dia1”: “domingo”.
2. Remova dois dos últimos dias da semana.
3. Remova segunda-feira pela sua chave.
4. Imprima chaves e valores do dicionário.
5. Imprima o dicionário final.
'''

# 1.
dias_semana = {"dia1":"domingo", "dia2":"segunda-feira", "dia3":"terça-feira", "dia4":"quarta-feira", 
"dia5":"quinta-feira", "dia6":"sexta-feira", "dia7":"sábado"}

# 2.
print(dias_semana)
print(dias_semana.popitem())
print(dias_semana.popitem())
print(dias_semana)

# 3.
del(dias_semana["dia2"])
print(dias_semana)

# 4.
print(dias_semana.keys())
print(dias_semana.values())

# 5.
print(dias_semana)