from resources.estacao import Estacao, Estacoes
from resources.relatorio import RelatoriosEstacao, RelatorioEstacoesAdmin
from resources.usuario import User, UserLogin, UserLogout, UserRegister, StationUsers
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blocklist import blocklist
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_ALGORITHM'] = 'RS256'
#Requisitos: criar um par de chaves RS256
app.config['JWT_PRIVATE_KEY'] = open('rs256.pem').read()
app.config['JWT_PUBLIC_KEY'] = open('rs256.pub').read()

api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def criaBanco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blocklist(self, token):
    return token['jti'] in blocklist

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({"message" : "You have been logged out"}), 401

api.add_resource(RelatoriosEstacao, '/relatorios')
api.add_resource(RelatorioEstacoesAdmin, '/adm_relatorio/<int:commit_id>')
api.add_resource(Estacoes, '/estacoes')
api.add_resource(Estacao, '/estacao/<string:nome>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(StationUsers, '/usuarios/estacoes')

				
if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    host_conteiner = subprocess.check_output('hostname -i', shell=True).decode('utf-8')[:-1]
    app.run(host=''+host_conteiner ,port=5000,debug=False)
