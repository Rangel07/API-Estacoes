from sql_alchemy import banco

class EstacaoModel(banco.Model):
    __tablename__ = 'estacoes'

    id_estacao = banco.Column(banco.Integer, primary_key = True)
    nome = banco.Column(banco.String(80))
    relatorios = banco.relationship('RelatorioModel')  # Lista de objetos estacoes

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {
            'id_estacao' : self.id_estacao,
            'nome': self.nome,
            'relatorios' : [relatorio.json() for relatorio in self.relatorios]
        }
    
    @classmethod
    def find_estacao(cls, nome):
        nome = cls.query.filter_by(nome = nome).first() #SELECT * FROM estacoes WHERE nome = $nome LIMIT 1
        if nome:
            return nome
        return None
    
    @classmethod
    def find_by_id(cls, id_estacao):
        id_estacao = cls.query.filter_by(id_estacao = id_estacao).first() #SELECT * FROM estacoes WHERE id_estacao = $id_estacao LIMIT 1
        if id_estacao:
            return id_estacao
        return None

    def save_estacao(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_estacao(self):
        #deletando os estacoes relacionados ao site
        [relatorio.delete_relatorio() for relatorio in self.relatorios]
        #deletando o site
        banco.session.delete(self)
        banco.session.commit()