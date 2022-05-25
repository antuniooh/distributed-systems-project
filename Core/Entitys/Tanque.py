

class Tanque:
    def __init__(self, vazao=1):
        self.vazao = vazao
        self.quantidade_armazenada = 0

    def depositar_insumo(self, quantidade):
        self.quantidade_armazenada += quantidade
        return self.quantidade_armazenada

    def transferir_baseado_vazao(self):
        quantidade_transferencia = 0

        # remove so o q a vazao suporta
        if self.quantidade_armazenada >= self.vazao:
            self.quantidade_armazenada -= self.vazao
            quantidade_transferencia = self.vazao
        else:
            quantidade_transferencia = self.quantidade_armazenada
            self.quantidade_armazenada = 0
        return quantidade_transferencia

    def to_output(self):
        return {
            "quantidade_armazenada": self.quantidade_armazenada
        }
