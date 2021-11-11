horario = int(input('Digite a hora do dia: '))

if horario < 12:
    print('Bom dia')
elif horario < 18:
    print('Boa tarde')
else:
    print('Boa noite')
