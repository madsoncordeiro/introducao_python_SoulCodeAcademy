'''
EXERCÍCIO PROPOSTO

1. Crie uma string contendo o alfabeto com letras maiúsculas separado por espaços.
2. Percorra e imprima essa string com enumerate.
3. Substitua os espaços por traço. “-” e imprima para o usuário.
'''

# 1.
alfabeto = "A B C D E F G H I J K L M N O P Q R S T U V X W Y Z"

# 2.
for k, v in enumerate(alfabeto):
    print(k, v)

# 3.
print(alfabeto.replace(" ", "-"))