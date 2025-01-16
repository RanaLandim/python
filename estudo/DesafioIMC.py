nome = 'Rana Landim'
altura = 1.62
peso = 68.0
imc = peso/(altura*altura)

print(nome, 'tem ', altura, 'de altura, pesa ', peso ,' quilos e seu IMC é ', imc)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2= f'{peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)