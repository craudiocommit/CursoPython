"""
Entrada de dados
"""
# Exemplo 1
nome = input('Qual seu nome? ')
idade = input('Qual a sua idade? ')

ano_nascimento = 2021-int(idade) # Aqui é necessário fazer um cast pra converter a string idade para inteiro

print() # Esse dá uma quebra de linha entre o input e o print.
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}.')


# Exemplo 2 - Dessa maneira ele vai juntar as strings, sem fazer a soma
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(numero_1 + numero_2)

# Exemplo 3 - Para fazer a soma é necessário fazer o cast no input
numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite outro número: ')
numero_2 = int

print(numero_1 + numero_2)