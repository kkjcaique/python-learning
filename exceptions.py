numero = input('digite um numero: ')

try:
    print('numero str:', numero)
    numero_float = float(numero)
    print('float:', numero_float)
    print(f'o dobro de {numero} é {2 * numero_float:.2f}')
except:
    print('isso n é um numero')