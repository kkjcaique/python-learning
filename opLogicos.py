# entrada = input('"E" para entrar ; "S" para sair: ')
# senha_digitada = input('digite sua senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# # OPERADOR LÓGICO AND
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# OPERADOR LÓGICO OR

# entrada = input('E - Entrar // S - Sair > ')
# senha_digitada = input('digite sua senha > ')
# senha_correta = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_correta:
#     print('você logou')

# senha = input('senha > ') or 'sem senha'
# print(senha)

# OPERADOR LÓGICO NOT - INVERTER EXPRESSÕES

# senha = input('senha > ')
# if senha != '123456':
#     print('voce logou')
# else:
#     print('senha incorreta')

# OPERADOR IN - ESTA EM

# nome = 'Caique'
# print(nome[0])
# print(nome[-2])
# print('Caí' not in nome)
# print('Caí' in nome)

nome = input('digite seu nome > ')
encontrar = input('digite o que deseja encontrar > ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{nome} não contém {encontrar}')

# OPERADOR NOT IN - NÃO ESTA EM

