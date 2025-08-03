velocidade = 61
km_carro = 102

RADAR_1 = 60
LOCAL_RADAR = 100
RANGE_RADAR = 1

acima_velocidade = velocidade > RADAR_1
range_para_multa = km_carro >= (LOCAL_RADAR - RANGE_RADAR) and km_carro <= (LOCAL_RADAR + RANGE_RADAR)

if acima_velocidade and range_para_multa:
    print('o carro está acima da velocidade do radar e foi multado')
else:
    print('o carro está abaixo da velocidade do radar e não foi multado')