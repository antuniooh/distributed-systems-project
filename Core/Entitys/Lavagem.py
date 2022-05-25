class Lavagem:
    def __init__(self):
        self.vazao = 1.5
        self.porcentagem_perda = 0.075 # 3 lavagem em sequencia
        self.perda_total = 0
        self.quantidade_armazenada = 0
        self.quantidade_transferida = 0

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

        self.quantidade_transferida+=quantidade_transferencia
        return quantidade_transferencia

    def to_output(self):
        return {
            "perda_total": self.perda_total,
            "quantidade_armazenada": self.quantidade_armazenada
        }
