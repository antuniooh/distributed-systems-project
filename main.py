from Core.HandlerSystem import HandlerSystem
import threading

handler = HandlerSystem()

# depositos de insumos periodicos

def depositar_oleo_residual():
    # ajustar para os 10 segundos
    threading.Timer(10.0, depositar_oleo_residual).start()
    handler.depositar_oleo_residual()


def depositar_et_oh():
    threading.Timer(1, depositar_et_oh).start()
    handler.depositar_et_oh()


def depositar_na_oh():
    threading.Timer(1, depositar_na_oh).start()
    handler.depositar_na_oh()


# transferencias periodicas de acordo com a vazao

def transferir_oleo_residual():
    threading.Timer(1.0, transferir_oleo_residual).start()
    handler.transferir_oleo_residual()


def transferir_et_oh():
    threading.Timer(1.0, transferir_et_oh).start()
    handler.transferir_et_oh()


def transferir_na_oh():
    threading.Timer(1.0, transferir_na_oh).start()
    handler.transferir_na_oh()


def processo_reator():
    threading.Timer(1.0, processo_reator).start()
    handler.processo_reator()


def processo_decantador():
    threading.Timer(1.0, processo_decantador).start()
    handler.processo_decantador()


def transfere_secador_etoh():
    threading.Timer(1.0, transfere_secador_etoh).start()
    handler.transferir_secador_etoh()


def transfere_lavagem():
    threading.Timer(1.0, transfere_lavagem).start()
    handler.transferir_lavagem()


def transfere_secador_biodiesel():
    threading.Timer(1.0, transfere_secador_biodiesel).start()
    handler.transferir_secador_biodiesel()


def start_fluxo():
    # periodicamente enviar os insumos
    depositar_oleo_residual()
    depositar_et_oh()
    depositar_na_oh()

    # # periodicamente transferir os insumos entre os componentes
    transferir_oleo_residual()
    transferir_et_oh()
    transferir_na_oh()

    # periodicamente o reator processa
    processo_reator()
    processo_decantador()

    transfere_secador_etoh()
    transfere_lavagem()
    transfere_secador_biodiesel()


start_fluxo()

