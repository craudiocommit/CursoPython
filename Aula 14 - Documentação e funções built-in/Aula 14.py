"""
SEMPRE LEIA A DOCUMENTAÇÃO DA LINGUAGEM
"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)

except:
    print('Tá querendo me enganar humano, tá achando que sou Atari?!')
