op = True
while op:
    n1_str = input('digite o primeiro número: ')
    n2_str = input('digite o segundo número: ')

    try:
        n1_float = float(n1_str)
        n2_float = float(n2_str)
    except:
        print('você digitou números inválidos.')
        continue
    
    input('qual operação matemática você deseja realizar? / 1. Adição / ')