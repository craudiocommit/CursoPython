"""
Condições IF, ELIF, ELSE e Booleans
"""

"""
hierarquia da condição do bloco
"""

if False:
    print('Verdadeiro.')
    print('teste teste 2')
elif True:
    print('Agora é verdadeiro.')
    nome = input('Qual seu nome? ')

    print(f'Seu nome é {nome}.')

elif False:
    print('Mais uma verdadeira.')
    print(22 + 22)
else:
    print('Não é verdadeiro.')
    print('Olá')