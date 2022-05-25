class Reator:
    def __init__(self):
        self.litros_processamento_por_segundo = 5
        self.quantidade_armazenada_oleo = 0
        self.proporcao_armazenada_oleo = 0
        self.quantidade_armazenada_na_oh = 0
        self.proporcao_armazenada_na_oh = 0
        self.quantidade_armazenada_et_oh = 0
        self.proporcao_armazenada_et_oh = 0
        self.quantidade_total = 0
        self.vazao = 1
        self.ciclos_processamento = 0
        self.estado = "Ligado"
    
    def to_output(self):
        return {
            "quantidade_armazenada_oleo": self.quantidade_armazenada_oleo,
            "quantidade_armazenada_na_oh": self.quantidade_armazenada_na_oh,
            "quantidade_armazenada_et_oh": self.quantidade_armazenada_et_oh,
            "quantidade_total": self.quantidade_total,
            "estado": self.estado,
            "ciclos_processamento": self.ciclos_processamento
        }

    def finalizar_transferencia(self):
        self.estado = "Ligado"
        return self.estado

    def depositar_insumo_recebido(self, payload):
        quantidade_a_ser_retornada = 0

        if "quantidade_et_oh" in payload:
            quantidade_a_ser_retornada = self.depositar_et_oh(float(payload["quantidade_et_oh"]))
        elif "quantidade_na_oh" in payload:
            quantidade_a_ser_retornada = self.depositar_na_oh(float(payload["quantidade_na_oh"]))
        elif "quantidade_oleo" in payload:
            quantidade_a_ser_retornada = self.depositar_oleo(float(payload["quantidade_oleo"]))

        return quantidade_a_ser_retornada

    def depositar_oleo(self, quantidade):
        quantidade_nao_armazenada = quantidade

        if self.quantidade_armazenada_oleo < 2.5:
            if self.quantidade_armazenada_oleo + quantidade > 2.5:
                quantidade_nao_armazenada = quantidade - (2.5 - self.quantidade_armazenada_oleo)
                self.quantidade_armazenada_oleo = 2.5
            else:
                self.quantidade_armazenada_oleo += quantidade
                quantidade_nao_armazenada = 0
            self.quantidade_total += quantidade - quantidade_nao_armazenada
            self.proporcao_armazenada_oleo = (self.quantidade_armazenada_oleo / self.litros_processamento_por_segundo) * 100
        return quantidade_nao_armazenada

    def depositar_na_oh(self, quantidade):
        quantidade_nao_armazenada = quantidade

        if self.quantidade_armazenada_na_oh < 1.25:
            if self.quantidade_armazenada_na_oh + quantidade > 1.25:
                quantidade_nao_armazenada = quantidade - (1.25 - self.quantidade_armazenada_na_oh)
                self.quantidade_armazenada_na_oh = 1.25
            else:
                self.quantidade_armazenada_na_oh += quantidade
                quantidade_nao_armazenada = 0
            self.quantidade_total += quantidade - quantidade_nao_armazenada
            self.proporcao_armazenada_na_oh = (self.quantidade_armazenada_na_oh / self.litros_processamento_por_segundo) * 100
        return quantidade_nao_armazenada

    def depositar_et_oh(self, quantidade):
        quantidade_nao_armazenada = quantidade

        if self.quantidade_armazenada_et_oh < 1.25:
            if self.quantidade_armazenada_et_oh + quantidade > 1.25:
                quantidade_nao_armazenada = quantidade - (1.25 - self.quantidade_armazenada_et_oh)
                self.quantidade_armazenada_et_oh = 1.25
            else:
                self.quantidade_armazenada_et_oh += quantidade
                quantidade_nao_armazenada = 0
            self.quantidade_total += quantidade - quantidade_nao_armazenada
            self.proporcao_armazenada_et_oh = (self.quantidade_armazenada_et_oh / self.litros_processamento_por_segundo) * 100
        return quantidade_nao_armazenada

    def checar_proporcao_acionamento(self):
        if self.quantidade_total != 0:
            porcentagem_na_oh = self.proporcao_armazenada_na_oh == 25
            porcentagem_et_oh = self.proporcao_armazenada_et_oh == 25
            porcentagem_oleo = self.proporcao_armazenada_oleo == 50

            if porcentagem_na_oh and porcentagem_et_oh and porcentagem_oleo:
                print("Porcentagem atingida...")
                print("Acionando processamento reator")

                if self.estado != "Em Transferencia":
                    return self.processar()

        return {
            "quantidade_solucao": 0
        }

    def processar(self):
        # 5 litros
        quantidade_processada = 5

        self.quantidade_total = 0
        self.quantidade_armazenada_oleo = 0
        self.quantidade_armazenada_et_oh = 0
        self.quantidade_armazenada_na_oh = 0

        self.estado = "Em Transferencia"
        self.ciclos_processamento += 1

        return {
            "quantidade_solucao": int(quantidade_processada)
        }
