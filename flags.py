condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('if')
else:
    print('else')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('não passou no if')
else:
    print('passou no if')