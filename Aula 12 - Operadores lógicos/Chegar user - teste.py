"""
Checando um usuário e senha
"""


usuario = input('Nome de usuário: ')
senha = input('Senha do usuário ')


usuario_bd = 'zezinho'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')