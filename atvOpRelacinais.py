valor1 = input('digite um valor > ')
valor2 = input('digite outro valor > ')

if valor1 > valor2:
    print(f'{valor1=} é maior que {valor2=}')
elif valor2 > valor1:
    print(f'{valor2=} é maior que {valor1=}')
else:
    print(f'{valor1=} é igual ao {valor2=}')
