numero = input('Digite um numero inteiro: ')
resto = numero % 2

if resto == 0:
    print('Esse número é par!')
else:
    print('Esse número é impar!')

try:
    numero = int(numero)
    print('Esse número é inteiro')
except:
    print('Esse número não é inteiro!')
