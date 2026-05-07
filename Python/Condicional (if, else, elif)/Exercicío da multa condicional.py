# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem anunciando que o motorista foi multado.
# O valor da multa é cobrado em R$ 5,00 por km acima de 80 km/h.

vel = int (input ('Forneça a velocidade do veículo: '))
if vel<= 80:
    print ('O automóvel não atingiu uma velocidade superior a presuposta, logo não há multa.')
else:
    multa = (vel - 80) * 5
    print (f'Por conta do automóvel estar atuando a uma velocidade maior que a permitida, uma multa será acionada no valor de R$ {multa:.2f}')
print (f'A velocidade informada do veículo era de {vel}km/h.')
a = int (input ('Digite 1 se deseja saber mais sobre a multa: '))
if a == 1:
    print ('A multa é gerada àqueles que ultrapassam a velocidade limite no valor de R$ 5,00 por km/h acima de 80 km/h.')
