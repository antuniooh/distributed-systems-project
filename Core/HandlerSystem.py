import json
import random
from time import sleep

import requests
from sympy import Q

import Infra.env as env


class HandlerSystem:
    def __init__(self):
        pass

    def depositar_tanque(self, quantidade, tanque, payload_parameter):
        payload = {
            payload_parameter: quantidade
        }
        requests.post(env.ENDPOINT_URL + tanque, json=payload)

    def depositar_oleo_residual(self):
        quantidade_oleo = random.randint(1, 2)
        self.depositar_tanque(quantidade_oleo, "/tanque_oleo", "quantidade_oleo")

    def transferir_oleo_residual(self):
        oleo_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/tanque_oleo")).content)
        retorno_ao_tanque = self.depositar_tanque_reator(oleo_transferencia)["quantidade_retorno_reator"]
        self.depositar_tanque(retorno_ao_tanque, "/tanque_oleo", "quantidade_oleo")


    def depositar_et_oh(self):
        quantidade_et_oh = 0.25
        self.depositar_tanque(quantidade_et_oh, "/tanque_etoh", "quantidade_et_oh")

    def transferir_et_oh(self):
        et_oh_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/tanque_etoh")).content)
        retorno_ao_tanque = self.depositar_tanque_reator(et_oh_transferencia)["quantidade_retorno_reator"]
        self.depositar_tanque(retorno_ao_tanque, "/tanque_etoh", "quantidade_et_oh")

    def depositar_na_oh(self):
        quantidade_na_oh = 0.5
        self.depositar_tanque(quantidade_na_oh, "/tanque_naoh", "quantidade_na_oh")

    def transferir_na_oh(self):
        na_oh_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/tanque_naoh")).content)
        retorno_ao_tanque = self.depositar_tanque_reator(na_oh_transferencia)["quantidade_retorno_reator"]
        self.depositar_tanque(retorno_ao_tanque, "/tanque_naoh", "quantidade_na_oh")
        

    def depositar_tanque_reator(self, payload={}):
        return json.loads((requests.post(env.ENDPOINT_URL + "/reator", json=payload)).content)

    def processo_reator(self):
        reator_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/reator")).content)

        # transferindo solucao do reator, respeitando a vazao de 1 segundo
        litros_transferencia = reator_transferencia["quantidade_solucao"]
        payload_decantador = {
            "quantidade_solucao": 1
        }
        while litros_transferencia:
            retorno_ao_reator = self.depositar_decantador(payload_decantador)["quantidade_retorno_decantador"]
            if retorno_ao_reator > 0:
                # devolver ao reator o q n foi processado
                self.retornar_solucao_ao_reator(retorno_ao_reator)
                litros_transferencia = 0
                break

            litros_transferencia -= 1
            sleep(1)
        
        # voltando reator ao estado normal
        requests.patch(env.ENDPOINT_URL + "/reator")

    def retornar_solucao_ao_reator(self, quantidade):
        self.depositar_tanque(quantidade * 0.25, "/reator", "quantidade_na_oh")
        self.depositar_tanque(quantidade * 0.25, "/reator", "quantidade_et_oh")
        self.depositar_tanque(quantidade * 0.5, "/reator", "quantidade_oleo")

    def depositar_decantador(self, payload={}):
        return json.loads((requests.post(env.ENDPOINT_URL + "/decantador", json=payload)).content)

    def depositar_secador_etoh(self, payload={}):
        requests.post(env.ENDPOINT_URL + "/secador_etoh", json=payload)

    def transferir_secador_etoh(self):
        et_oh_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/secador_etoh")).content)
        requests.post(env.ENDPOINT_URL + "/tanque_etoh", json=et_oh_transferencia)

    def depositar_tanque_glicerina(self, payload={}):
        requests.post(env.ENDPOINT_URL + "/tanque_glicerina", json=payload)

    def depositar_lavagem(self, payload={}):
        requests.post(env.ENDPOINT_URL + "/lavagem", json=payload)

    def transferir_lavagem(self):
        lavagem_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/lavagem")).content)
        self.depositar_secador_biodiesel(lavagem_transferencia)

    def depositar_secador_biodiesel(self, result_post):
        requests.post(env.ENDPOINT_URL + "/secador_biodiesel", json=result_post)

    def depositar_tanque_biodiesel(self, payload={}):
        requests.post(env.ENDPOINT_URL + "/tanque_biodiesel", json=payload)


    def processo_decantador(self):
        decantador_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/decantador")).content)

        # transferindo solucao do decantador para as outras peças
        if decantador_transferencia["quantidade_et_oh"] != 0:
            self.depositar_secador_etoh(decantador_transferencia)
        if decantador_transferencia["quantidade_glicerina"] != 0:
            self.depositar_tanque_glicerina(decantador_transferencia)
        if decantador_transferencia["quantidade_lavagem"] != 0:
            self.depositar_lavagem(decantador_transferencia)

    def transferir_secador_biodiesel(self):
        biodiesel_transferencia = json.loads((requests.put(env.ENDPOINT_URL + "/secador_biodiesel")).content)
        self.depositar_tanque_biodiesel(biodiesel_transferencia)

