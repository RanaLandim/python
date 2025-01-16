#Solicita o valor da hora e a quantidade de horas trabalhadas
valorHora = float(input("Digite o valor da sua hora: "))
quantidadeHoras = float(input("Digite a quantidade de horas trabalhadas no mês: "))

#Calcula salárioBruto
salarioBruto= valorHora*quantidadeHoras;

#Calcula o desconto do imposto de renda
if salarioBruto <=900:
    descontoIR = 0
elif salarioBruto <=1500:
    descontoIR= salarioBruto*0.05
elif salarioBruto<=2500:
    descontoIR=salarioBruto*0.10
else:
        descontoIR=salarioBruto*0.20

#Calcula o desconto do INSS (3%)
descontoINSS = salarioBruto*0.03

#Calcula o valor do FGTS (11%)
fgts = salarioBruto*0.11

#Calcula o total de descontos
totalDescontos = descontoIR+descontoINSS

#Calcula o salário liquido
salarioLiquido = salarioBruto-totalDescontos

#Exibe os resultados

print(f"Salário Bruto : (R$ {valorHora}*{quantidadeHoras})  : R$ {salarioBruto:.2f}")
print(f"(-) IR({descontoIR/salarioBruto*100:.0f}%)      :R$ {descontoIR:.2f}")
print(f"(-) INSS (3%)       :R${descontoINSS:.2f}")
print(f"Total de descontos              : R$ {totalDescontos:.2f}")
print(f"        Salário Liquido                 : R$ {salarioLiquido:.2f}")
