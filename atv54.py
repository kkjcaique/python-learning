# question 1
"""
n_str = input('digite um número inteiro: ')

try:
    n_int = int(n_str)

    numero_par = n_int % 2 == 0

    if numero_par:
        print(f'{n_int} é um número par')
    else:
        print(f'{n_int} é um número ímpar')
except:
    print('o numero digitado não é inteiro')
"""

# question 2
"""
horario_str = input('qual é o horário atual onde você mora? ')
horario = int(horario_str)

if horario < 0 or horario > 23:
    print('o horário digitado está inválido')
elif horario >= 0 and horario <= 11:
    print('Bom dia')
elif horario <= 17:
    print('Boa tarde')
else:
    print('Boa noite')
"""
# question 3
"""
nome = input('digite seu primeiro nome por favor: ')
nome_curto = len(nome) <= 4
nome_medio = len(nome) == 5 or len(nome) == 6

if nome_curto:
    print('seu nome é curto')
elif nome_medio:
    print('seu nome é de um tamanho médio')
else:
    print('seu nome é longo')
"""