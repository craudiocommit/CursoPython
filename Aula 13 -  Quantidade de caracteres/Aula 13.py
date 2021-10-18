"""
Cheando a quantidade de caracteres
função len() faz a contagem dos caracteres, a saida dessa função é int
"""

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 digitos')
else:
    print('Você foi cadastrado no sistema.')