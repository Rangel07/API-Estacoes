from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from sql_alchemy import banco
from email.message import EmailMessage
import smtplib
from resources.hash import gerar_hashcode

class UserModel(banco.Model):
    __tablename__ = 'usuarios'

    user_id = banco.Column(banco.Integer, primary_key = True)
    login = banco.Column(banco.String(40), nullable=False, unique=True)
    apiKey = banco.Column(banco.String(40), nullable=False, unique=True)
    cargo = banco.Column(banco.String(40), nullable=False)
    email = banco.Column(banco.String(80), unique=True)


    def __init__(self, login, email, apiKey, cargo = 'base'):
        apiKey = gerar_hashcode()
        apiKey = self.verificar_apiKey(apiKey)
        self.cargo = cargo
        self.login = login
        self.apiKey = apiKey
        self.email = email

    def json(self):
        return {
            'user_id' : self.user_id,
            'login': self.login,
            'apiKey': self.apiKey
        }
    
    
    def send_email(self):
        msg = EmailMessage()
        msg.set_content('Seu cadastro foi realizado com sucesso! Esta é sua ApiKey, guarde-a bem! {}'.format(self.apiKey))
        msg['subject'] = 'Cadastrado!'
        msg['to'] = self.email
        # Requisitos: colocar credenciais GMAIL API
        user = ''
        msg['from'] = ''
        senha = ''
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, senha)
        server.send_message(msg)
        server.quit()
    
    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id = user_id).first() #SELECT * FROM users WHERE user_id = $user_id LIMIT 1
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login = login).first() #SELECT * FROM users WHERE user_id = $user_id LIMIT 1
        if user:
            return user
        return None

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email = email).first() #SELECT * FROM users WHERE user_id = $user_id LIMIT 1
        if user:
            return user
        return None

    @classmethod
    def verificar_apiKey(cls, apiKey):
        key = cls.query.filter_by(apiKey = apiKey).first()
        if key:
            return cls.verificar_apiKey(gerar_hashcode())
        else:
            return apiKey
    
    @classmethod
    @jwt_required()
    def verificar_admin(cls):
        payload = get_jwt_identity()
        busca = cls.query.filter_by(user_id = payload).first()
        if busca.cargo == 'admin':
            return True
        else:
            return False
    
    @classmethod
    @jwt_required()
    def verificar_estacao(cls):
        payload = get_jwt_identity()
        busca = cls.query.filter_by(user_id = payload).first()
        if busca.cargo == 'estacao':
            return True
        else:
            return False
        

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()