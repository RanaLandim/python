valor_hora = float(input("Digite o valor da sua hora: "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quantidade_horas
desconto_ir = (
    (lambda x: 0 if x <= 900 else (x * 0.05 if x <= 1500 else (x * 0.10 if x <= 2500 else x * 0.20)))(salario_bruto)
)
desconto_inss = salario_bruto * 0.03
fgts = salario_bruto * 0.11
total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: (R$ {valor_hora} * {quantidade_horas})        : R$ {salario_bruto:.2f}")
print(f"(-) IR ({desconto_ir / salario_bruto * 100:.0f}%)                     : R$ {desconto_ir:.2f}")
print(f"(-) INSS (3%)                 : R$ {desconto_inss:.2f}")
print(f"FGTS (11%)                      : R$ {fgts:.2f}")
print(f"Total de descontos              : R$ {total_descontos:.2f}")
print(f"        Salário Liquido                 : R$ {salario_liquido:.2f}")
