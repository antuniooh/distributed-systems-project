import json

from flask import Flask, request, render_template
import flask
from flask_cors import CORS, cross_origin

from Entitys.Decantador import Decantador
from Entitys.Lavagem import Lavagem
from Entitys.Reator import Reator
from Entitys.Secador import Secador
from Entitys.Tanque import Tanque


app = Flask(__name__, template_folder='../', static_folder="../")
CORS(app, support_credentials=True)

tanque_oleo = Tanque(vazao=0.75)
tanque_etoh = Tanque()
tanque_naoh = Tanque()
tanque_glicerina = Tanque()
reator = Reator()
decantador = Decantador()
secador_etoh = Secador()
secador_biodiesel = Secador()
lavagem = Lavagem()
tanque_biodiesel = Tanque()


@app.route("/dashboard", methods=['GET'])
def get_dashboard():
    return render_template("./index.html")

@app.route("/biodiesel_planta", methods=['GET'])
def get_biodiesel_planta():
    response = flask.jsonify({
        "tanque_oleo": tanque_oleo.to_output(),
        "tanque_etoh": tanque_etoh.to_output(),
        "tanque_naoh": tanque_naoh.to_output(),
        "tanque_glicerina": tanque_glicerina.to_output(),
        "reator": reator.to_output(),
        "decantador": decantador.to_output(),
        "secador_etoh": secador_etoh.to_output(),
        "secador_biodiesel": secador_biodiesel.to_output(),
        "lavagem": lavagem.to_output(),
        "tanque_biodiesel": tanque_biodiesel.to_output()
    })
    return response


# metodos tanque oleo residual

@app.route("/tanque_oleo", methods=['POST'])
def post_incomes_oleo():
    return {
        "quantidade_oleo": tanque_oleo.depositar_insumo(float(request.json["quantidade_oleo"]))
    }


@app.route("/tanque_oleo", methods=['PUT'])
def put_incomes_oleo():
    return {
        "quantidade_oleo": tanque_oleo.transferir_baseado_vazao()
    }


@app.route("/tanque_oleo", methods=['GET'])
def get_oleo():
    return tanque_oleo.__dict__


# metodos tanque et oh

@app.route("/tanque_etoh", methods=['POST'])
def post_incomes_etoh():
    return {
        "quantidade_et_oh": tanque_etoh.depositar_insumo(float(request.json["quantidade_et_oh"]))
    }


@app.route("/tanque_etoh", methods=['PUT'])
def put_incomes_etoh():
    return {
        "quantidade_et_oh": tanque_oleo.transferir_baseado_vazao()
    }


@app.route("/tanque_etoh", methods=['GET'])
def get_et_oh():
    return tanque_etoh.__dict__


# metodos tanque na oh

@app.route("/tanque_naoh", methods=['POST'])
def post_incomes_naoh():
    return {
        "quantidade_na_oh": tanque_naoh.depositar_insumo(float(request.json["quantidade_na_oh"]))
    }


@app.route("/tanque_naoh", methods=['PUT'])
def put_incomes_naoh():
    return {
        "quantidade_na_oh": tanque_naoh.transferir_baseado_vazao()
    }


@app.route("/tanque_naoh", methods=['GET'])
def get_na_oh():
    return tanque_naoh.__dict__


# metodos reator

@app.route("/reator", methods=['POST'])
def post_incomes_reator():
    return {
        "quantidade_retorno_reator": reator.depositar_insumo_recebido(request.json)
    }


@app.route("/reator", methods=['PUT'])
def put_incomes_reator():
    return reator.checar_proporcao_acionamento()


@app.route("/reator", methods=['PATCH'])
def patch_incomes_reator():
    return reator.finalizar_transferencia()


@app.route("/reator", methods=['GET'])
def get_reator():
    return reator.__dict__


# metodos decantador

@app.route("/decantador", methods=['POST'])
def post_incomes_decantador():
    return {
        "quantidade_retorno_decantador": decantador.armazena_solucao(float(request.json["quantidade_solucao"]))
    }


@app.route("/decantador", methods=['PUT'])
def put_incomes_decantador():
    return decantador.processa_saida()


@app.route("/decantador", methods=['GET'])
def get_decntador():
    return decantador.__dict__


@app.route("/tanque_glicerina", methods=['POST'])
def get_incomes_glicerina():
    return {
        "quantidade_glicerina": tanque_glicerina.depositar_insumo(float(request.json["quantidade_glicerina"]))
    }


@app.route("/tanque_glicerina", methods=['GET'])
def get_glicerina():
    return tanque_glicerina.__dict__


# metodos secador

@app.route("/secador_etoh", methods=['POST'])
def get_incomes_secador_etoh():
    return {
        "quantidade_et_oh": secador_etoh.depositar(float(request.json["quantidade_et_oh"]))
    }


@app.route("/secador_etoh", methods=['PUT'])
def put_incomes_secador_etoh():
    return {
        "quantidade_et_oh": secador_etoh.transferir_baseado_vazao()
    }


@app.route("/secador_etoh", methods=['GET'])
def get_secador_etoh():
    return secador_etoh.__dict__


# meotdos lavagem


@app.route("/lavagem", methods=['POST'])
def get_incomes_lavagem():
    return {
        "quantidade_lavagem": lavagem.depositar(float(request.json["quantidade_lavagem"]))
    }


@app.route("/lavagem", methods=['PUT'])
def put_incomes_lavagem():
    return {
        "quantidade_lavagem": lavagem.transferir_baseado_vazao()
    }


@app.route("/lavagem", methods=['GET'])
def get_lavagem():
    return lavagem.__dict__


@app.route("/secador_biodiesel", methods=['POST'])
def post_incomes_secador_biodiesel():
    return {
        "quantidade_biodiesel": secador_biodiesel.depositar(float(request.json["quantidade_lavagem"]))
    }

@app.route("/secador_biodiesel", methods=['PUT'])
def put_incomes_secador_biodiesel():
    return {
        "quantidade_biodiesel": secador_biodiesel.transferir_baseado_vazao()
    }


@app.route("/secador_biodiesel", methods=['GET'])
def get_secador_biodiesel():
    return secador_biodiesel.__dict__


@app.route("/tanque_biodiesel", methods=['POST'])
def get_incomes_tanque_biodiesel():
    return {
        "quantidade_biodiesel": tanque_biodiesel.depositar_insumo(float(request.json["quantidade_biodiesel"]))
    }


@app.route("/tanque_biodiesel", methods=['GET'])
def get_tanque_biodiesel():
    return tanque_biodiesel.__dict__
