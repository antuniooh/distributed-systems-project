import time

class Decantador:
    def __init__(self):
        self.capacidade_maxima = 10
        self.tempo_repouso = 5
        self.quantidade_armazenada = 0
        self.esta_em_repouso = False
        self.tempo_inicio_processamento = None
        self.ciclos_processamento = 0

    def armazena_solucao(self, quantidade):
        quantidade_nao_armazenada = quantidade

        if quantidade + self.quantidade_armazenada <= self.capacidade_maxima:
            self.quantidade_armazenada += quantidade
            quantidade_nao_armazenada = 0
        return quantidade_nao_armazenada

    def processa_saida(self):

        #checa se passou 5 segundos e tira do modo repouso
        if self.esta_em_repouso and (time.time() > (self.tempo_inicio_processamento + self.tempo_repouso)):
            print("Decantador saiu do modo repouso")
            self.esta_em_repouso = False

        if not self.esta_em_repouso and self.quantidade_armazenada > 1:
            # quantidade solucao
            payload = {
                "quantidade_glicerina": self.quantidade_armazenada * 0.01,
                "quantidade_et_oh": self.quantidade_armazenada * 0.03,
                "quantidade_lavagem": self.quantidade_armazenada * 0.96,
                "total": self.quantidade_armazenada
            }
            self.tempo_inicio_processamento = time.time()
            self.esta_em_repouso = True
            print("Decantador iniciou o modo repouso")
            self.ciclos_processamento+=1
            self.quantidade_armazenada = 0
            return payload

        return {
                "quantidade_glicerina": 0,
                "quantidade_et_oh": 0,
                "quantidade_lavagem": 0,
                "total": 0
            }
        
    def to_output(self):
        return {
            "quantidade_armazenada": self.quantidade_armazenada,
            "esta_em_repouso": self.esta_em_repouso,
            "ciclos_processamento": self.ciclos_processamento
        }


