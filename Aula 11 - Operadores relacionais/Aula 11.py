"""
Operadores Relacionais
==  Igualdade
>   maior que
>=  maior que ou igual a
<   menor que
<=  menor que ou igual a
!=  Diferente 
"""

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

#Limite para pegar empréstimo
#idade_limite = 18 # Usando critério de menor de idade
idade_menor = 20 # Usando faixa de idade
idade_maior = 30 # Usando faixa de idade

if idade >= idade_menor and idade <= idade_maior: # Usando o operador lógico AND
    print(f'{nome} pode pegar um empréstimo')
else:
    print(f'{nome} não pode pegar um empréstimo')
