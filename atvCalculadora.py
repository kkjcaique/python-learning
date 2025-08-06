cond = True
while cond:
    n1_str = input('digite o primeiro número: ')
    n2_str = input('digite o segundo número: ')

    try:
        n1_float = float(n1_str)
        n2_float = float(n2_str)
    except:
        print('você digitou números inválidos.')
        continue
    
    op = input('qual operação matemática você deseja realizar?\n 1. Adiçâo\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n')

    if op == '1':
        print(f'a soma entre {n1_float} e {n2_float} é {n1_float + n2_float}')
    elif op == '2':
        print(f'a subtração entre {n1_float} e {n2_float} é {n1_float - n2_float}')
    elif op == '3':
        print(f'a multiplicação entre {n1_float} e {n2_float} é {n1_float * n2_float}')
    elif op == '4':
        if n2_float == 0:
            print('divisão impossivel por 0. digite os numeros novamente.')
            continue
        else:
            print(f'a divisão entre {n1_float} e {n2_float} é {n1_float / n2_float}')
    else:
        print('você não digitou nenhuma opção valida')