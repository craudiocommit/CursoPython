"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso de uma pessoa. - OK
* Criar variável com ano o ano atual (int) - OK
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual) - OK
* Obter o IMC da pessa com 2 casas decimais (peso e na altura da pessoa) - OK
* Exibir um texto com todos os valores na tela suando F-Strings (com as chaves) 
"""

# Feito sozinho
nome = 'Pedrinho da Silva'
idade = 40
altura = 1.98
peso = 92.3
anoAtual = 2021

anoDeNascimento = anoAtual - idade
IMC = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}kg.\nO IMC de {nome} é {IMC:.2f}.\n{nome} nasceu em {anoDeNascimento}')


# Correção
nome = 'Pedrinho da Silva'
idade = 40
altura = 1.98
peso = 92.3
anoAtual = 2021

anoDeNascimento = anoAtual - idade
IMC = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {IMC:.2f}.')
print(f'{nome} nasceu em {anoDeNascimento}')