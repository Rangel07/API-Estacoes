from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.estacao import EstacaoModel
from models.usuario import UserModel
import traceback

class Estacoes(Resource):

    @jwt_required()
    def get(self):
        return {'estacoes' : [station.json() for station in EstacaoModel.query.all()]}

class Estacao(Resource):

    @jwt_required()
    def get(self, nome):
        station = EstacaoModel.find_estacao(nome)
        if station:
            return station.json()
        return {'message': 'Estação não encontrada.'}, 404

    @jwt_required()
    def post(self,nome):
        if UserModel.verificar_admin():
            if EstacaoModel.find_estacao(nome):
                return {"message": "A estação '{}' já existe".format(nome)}, 400
            station = EstacaoModel(nome)
            try:
                station.save_estacao()
                user = UserModel(login=nome,apiKey='',email=nome, cargo='estacao')
                user.save_user()
            except:
                user.delete_user()
                station.delete_estacao()
                traceback.print_exc()
                return {"message" : "Um erro interno ocorreu durante o cadastro de estação"}, 500
            return station.json(), 201
        else:
            return {"message" : "Acesso negado"}, 401

    @jwt_required()
    def delete(self, nome):
        if UserModel.verificar_admin():
            station = EstacaoModel.find_estacao(nome)
            user = UserModel.find_by_login(nome)
            if station:
                try:
                    user.delete_user()
                    station.delete_estacao()
                    return {"message":"Estação deletada com sucesso"}
                except:
                    return {"message" : "Ocorreu algum erro ao deletar a estação"}, 501
            return {"message" : "Estação não encontrada"}, 404
        else:
            return {"message" : "Acesso negado"}, 401