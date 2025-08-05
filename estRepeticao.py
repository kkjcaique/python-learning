# WHILE
"""
contador = 0

while contador < 10:
    contador += 1
    print(contador )

print('acabou')
"""

"""
contador = 0

while contador <= 10:
    contador += 1

    if contador == 6:
        continue

    print(contador)

    if contador == 10:
        break
"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('end')

#