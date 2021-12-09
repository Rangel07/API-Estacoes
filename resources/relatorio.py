from flask_jwt_extended.view_decorators import jwt_required
from models.relatorio import RelatorioModel
from flask_restful import Resource, reqparse
from models.usuario import UserModel


class RelatoriosEstacao(Resource):

    @jwt_required()
    def get(self):
        return {'relatorios' : [relatorio.json() for relatorio in RelatorioModel.query.all()]}

    lista_relatorios = reqparse.RequestParser()
    lista_relatorios.add_argument("lista",type=dict, action='append')

    @jwt_required()
    def post(self):
        if UserModel.verificar_estacao():
            lista = RelatoriosEstacao.lista_relatorios.parse_args()
            relatorios = lista["lista"]
            if relatorios:
                try:
                    for dados in relatorios:
                        relatorio = RelatorioModel(dados)
                        relatorio.save_relatorio()
                except:
                    return {"message" : "Não conseguiu salvar"}, 500

                return relatorios
            else:
                return {"message" : "O id específicado não existe"}, 400
        else:
            return {"message" : "Acesso negado"}, 401

class RelatorioEstacoesAdmin(Resource):

    @jwt_required()
    def get(self, commit_id):
        if UserModel.verificar_admin():
            relatorio = RelatorioModel.find_relatorio(commit_id)
            if relatorio:
                return relatorio.json()
            return {'message': 'Relatorio não encontrado'}, 404 # not found
        else:
            return {"message" : "Acesso negado"}, 401

    @jwt_required()
    def delete(self, commit_id):
        if UserModel.verificar_admin():
            relatorio = RelatorioModel.find_relatorio(commit_id)
            if relatorio:
                try:
                    relatorio.delete_relatorio()
                except:
                    return {"message" : "Um erro interno ocorreu ao deletar o relatório"}, 500
                return {"message" : "Relatorio deletado"}, 
            return {'message' : 'Relatorio não encontrado'}, 404
        else:
            return {"message" : "Acesso negado"}, 401
