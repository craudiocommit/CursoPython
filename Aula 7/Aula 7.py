# Introdução à String

nome = 'Claudio Juior'
idade = 33
altura = 1.70
e_maior = idade > 18
peso = 82
imc = peso / altura ** 2

# Jeitos diferentes de concatenar
print(nome, 'tem', idade, 'anos de idade', (f'e seu IMC é {imc:.1f}'))
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.1f}')
print('{} tem {} anos de idade e seu IMC é {:.1f}'.format(nome,idade,imc))
