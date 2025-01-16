class FolhaPagamento:
    def __init__(self, valor_hora, quantidade_horas):
        self.valor_hora = valor_hora
        self.quantidade_horas = quantidade_horas
        self.salario_bruto = self.valor_hora * self.quantidade_horas
        self.desconto_ir = self.calcular_desconto_ir()
        self.desconto_inss = self.salario_bruto * 0.03
        self.fgts = self.salario_bruto * 0.11
        self.total_descontos = self.desconto_ir + self.desconto_inss
        self.salario_liquido = self.salario_bruto - self.total_descontos

    def calcular_desconto_ir(self):
        if self.salario_bruto <= 900:
            return 0
        elif self.salario_bruto <= 1500:
            return self.salario_bruto * 0.05
        elif self.salario_bruto <= 2500:
            return self.salario_bruto * 0.10
        else:
            return self.salario_bruto * 0.20

    def exibir_resultados(self):
        print(f"Salário Bruto: (R$ {self.valor_hora} * {self.quantidade_horas})        : R$ {self.salario_bruto:.2f}")
        print(f"(-) IR ({self.desconto_ir / self.salario_bruto * 100:.0f}%)                     : R$ {self.desconto_ir:.2f}")
        print(f"(-) INSS (3%)                 : R$ {self.desconto_inss:.2f}")
        print(f"FGTS (11%)                      : R$ {self.fgts:.2f}")
        print(f"Total de descontos              : R$ {self.total_descontos:.2f}")
        print(f"        Salário Liquido                 : R$ {self.salario_liquido:.2f}")

valor_hora = float(input("Digite o valor da sua hora: "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
folha = FolhaPagamento(valor_hora, quantidade_horas)
folha.exibir_resultados()
