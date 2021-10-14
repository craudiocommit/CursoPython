"""
Operadores lógicos:
and - (Verdadeiro E Verdadeiro) = Verdadeiro || (Verdadeiro E False) = False
or -  (Verdadeiro OU Verdadeiro) = Verdadeiro || (Verdadeiro OU False) = Verdadeiro
not - (Inversor) - Exemplo 1
in - ( Verifica a existencia de) - Exemplo 2
not in (Inverte a expressão) - Exemplo 3
"""

# Exemplo 1

a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')


# Exemplo 2

nome = 'Claudio'
if 'u' in nome:
    print('Existe a letra U no seu nome.')

else:
    print('Não existe a letra U no seu nome.')

# Exemplo 3

nome = 'Claudio.'

if 'dio' not in nome:
    print('Tem sim.')
else:
    print('Não tem.')