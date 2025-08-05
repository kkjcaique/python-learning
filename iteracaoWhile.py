nome = 'caique'
tamanho_nome = len(nome)

# print(f'{nome}')
# print(tamanho_nome)
# print(nome[3])

nova_string = ''
cont = 0
while cont < tamanho_nome:
    nova_string += '*' + nome[cont]
    cont += 1

print(nova_string)