def calculaDescontoIR(salarioBruto):
    if salarioBruto<=900:
        return 0
    elif salarioBruto<=1500:
        return salarioBruto*0.05
    elif salarioBruto<=2500:
        return salarioBruto*0.10
    else:
        return salarioBruto*0.20
    
def calcularFolhaPagamento(valorHora,qtdHoras):
    salarioBruto=valorHora*qtdHoras
    descontoIR=calculaDescontoIR(salarioBruto)
    descontoINSS=salarioBruto*0.03
    fgts=salarioBruto*0.11
    totalDescontos=descontoIR+descontoINSS
    salarioLiquido=salarioBruto - totalDescontos

    return salarioBruto,descontoIR,descontoINSS,fgts,totalDescontos,salarioLiquido

valorHora=float(input("Digite o valor da sua hora: "))
quantidadeHoras=float(input("Digite a quantidade de horas trabalhadas no mês : "))
resultados=calcularFolhaPagamento(valorHora, quantidadeHoras)

print(f"Salário Bruto: (R$ {valorHora} * {quantidadeHoras})        : R$ {resultados[0]:.2f}")
print(f"(-) IR ({resultados[1] / resultados[0] * 100:.0f}%)                     : R$ {resultados[1]:.2f}")
print(f"(-) INSS (3%)                 : R$ {resultados[2]:.2f}")
print(f"FGTS (11%)                      : R$ {resultados[3]:.2f}")
print(f"Total de descontos              : R$ {resultados[4]:.2f}")
print(f"        Salário Liquido                 : R$ {resultados[5]:.2f}")

