class Secador:
    def __init__(self):
        self.vazao = 0.2 # processam 0.2 litros por segundo -> rever
        self.tempo_por_litro = 5
        self.perda_total = 0
        self.porcentagem_perda = 0.05
        self.quantidade_armazenada = 0

    def depositar(self, quantidade):
        self.quantidade_armazenada += quantidade * (1 - self.porcentagem_perda)
        self.perda_total += quantidade * self.porcentagem_perda

        return self.quantidade_armazenada

    def transferir_baseado_vazao(self):
        quantidade_transferencia = 0
        if self.quantidade_armazenada >= self.vazao:
            self.quantidade_armazenada -= self.vazao
            quantidade_transferencia = self.vazao
        else:
            quantidade_transferencia = self.quantidade_armazenada
            self.quantidade_armazenada = 0
        return quantidade_transferencia

    def to_output(self):
        return {
            "perda_total": self.perda_total,
            "quantidade_armazenada": self.quantidade_armazenada
        }
