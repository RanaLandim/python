def calcular_desconto_ir(salario_bruto):
    return (
        0 if salario_bruto <= 900
        else salario_bruto * 0.05 if salario_bruto <= 1500
        else salario_bruto * 0.10 if salario_bruto <= 2500
        else salario_bruto * 0.20
    )

valor_hora = float(input("Digite o valor da sua hora: "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quantidade_horas
desconto_ir = calcular_desconto_ir(salario_bruto)
desconto_inss = salario_bruto * 0.03
fgts = salario_bruto * 0.11
total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

# Imprime todos os resultados usando list comprehension para formatar a saída
resultados = [
    f"Salário Bruto: (R$ {valor_hora} * {quantidade_horas})        : R$ {salario_bruto:.2f}",
    f"(-) IR ({desconto_ir / salario_bruto * 100:.0f}%)                     : R$ {desconto_ir:.2f}",
    f"(-) INSS (3%)                 : R$ {desconto_inss:.2f}",
    f"FGTS (11%)                      : R$ {fgts:.2f}",
    f"Total de descontos              : R$ {total_descontos:.2f}",
    f"        Salário Liquido                 : R$ {salario_liquido:.2f}"
]

print("\n".join(resultados))
