"""
CONSTANTE = "Variáveis" que nao vao mudar 
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 90 #local em que o carro esta na estrada


RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #A distancia onde o radar pega


if velocidade > RADAR_1:
        print('Velocidade do carro passou do radar')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE):
    print('Carro multado tem radar 1')