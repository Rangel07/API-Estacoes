from flask_restful import Resource, reqparse
from models.estacao import EstacaoModel
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from blocklist import blocklist
import traceback

atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required = True, help = "O campo 'login' precisa ser preenchido")
atributos.add_argument('apiKey', type=str)
atributos.add_argument('email', type=str)

class User(Resource):
    # /usuarios/{user_id}

    @jwt_required()
    def get(self, user_id):
        if UserModel.verificar_admin():
            user = UserModel.find_user(user_id)
            if user:
                return user.json()
            return {'message': 'Usuario nao encontrado'}, 404
        else:
            return {'message' : 'Acesso negado'}, 401

    @jwt_required()
    def delete(self, user_id):
        if UserModel.verificar_admin():
            user = UserModel.find_user(user_id)
            if user:
                try:
                    if user.cargo == 'estacao':
                        estacao = EstacaoModel.find_estacao(user.login)
                        estacao.delete_estacao()
                    user.delete_user()
                except:
                    return {"message" : "Um erro interno ocorreu ao deletar usuario"}, 500
                return {"message" : "Usuario deletado"} 
            return {'message' : 'Usuario não encontrado'}, 404
        else:
            return {"message" : "Acesso negado"}, 401

class StationUsers(Resource):

    @jwt_required()
    def get(self):
        if UserModel.verificar_admin():
            return {"estacoes" : [user.json() for user in UserModel.query.filter_by(cargo='estacao').all()]}
        else:
            return {"message" : "Acesso negado"}, 401
            
class UserRegister(Resource):
    # /cadastro
    def post(self):
        dados = atributos.parse_args()
        if not dados.get('email') or dados.get('email') is None:
            return {"message" : "O campo 'email' precisa ser preenchido"}, 400
        if UserModel.find_by_email(dados['email']):
            return {"message" : "O email {} já está em uso".format(dados['email'])}, 400
        if UserModel.find_by_login(dados['login']):
            return {"message" : "O login'{}' já está em uso".format(dados['login'])}, 400
        
        user = UserModel(**dados)
        try:
            user.save_user()
            user.send_email()
        except:
            user.delete_user()
            traceback.print_exc()
            return {"message" : "Um erro interno aconteceu no cadastro"}, 500
        return {"message" : "Usuario criado com sucesso!"}, 201 #Created

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.apiKey, dados['apiKey']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {"access_token" : token_de_acesso}, 200
        return {"message" : "Dados inválidos"}, 401 #Unauthorized

class UserLogout(Resource):
    
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] #JWT Token Identifier
        blocklist.add(jwt_id)
        return {"message": "Logout feito com sucesso!"}, 200
    
