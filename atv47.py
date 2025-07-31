"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

# nome = input('digite seu nome: ')
# tamanhoNome = len(nome)
# idade = input('digite sua idade: ')

# if nome != '' and tamanhoNome >= 2 and idade != '':
#     print(10 * '-')
#     print(f'seu nome é {nome}')
#     print(f'seu nome invertido é {nome[::-1]}')
#     print('')
#     print(f'seu nome tem {tamanhoNome} letras')
#     print(f'a primeira letra do seu nome é {nome[:1]}')
#     print(f'a ultima letra do seu nome é {nome[tamanhoNome-1:tamanhoNome]}')
# else:
#     print('desculpe, voce deixou campos vazios')

nome = input('digite seu nome: ')
tamanhoNome = len(nome)
idade = input('digite sua idade: ')

if nome and idade:
    print(10 * '-')
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('seu nome contém espaços')
    else:
        print('seu nome não contém espaços')
    
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print('desculpe, voce deixou campos vazios')