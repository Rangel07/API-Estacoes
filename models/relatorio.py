from models.estacao import EstacaoModel
from sql_alchemy import banco

class RelatorioModel(banco.Model):
    __tablename__ = 'relatorios'

    commit_id = banco.Column(banco.Integer, primary_key=True)
    id_estacao = banco.Column(banco.Integer, banco.ForeignKey('estacoes.id_estacao'))
    nome_estacao = banco.Column(banco.String(80))
    dataHora = banco.Column(banco.String(80))
    umidade = banco.Column(banco.Float)
    pressaoAtmosferica = banco.Column(banco.Float)
    direcaoVento = banco.Column(banco.Float)
    velocidadeVento = banco.Column(banco.Float)
    pluviometro = banco.Column(banco.Float)
    radiacaoSolar = banco.Column(banco.Float)
    temperaturaAr = banco.Column(banco.Float)

    def __init__(self, dicio):
        self.id_estacao = dicio["id_estacao"]

        ### Relação de tabela
        try:
            query = EstacaoModel.query.filter_by(id_estacao = self.id_estacao).first()
            print(query.json()['nome'])
            self.nome_estacao = query.json()['nome']
        except:
            self.nome_estacao = None
        
        self.dataHora = dicio['dataHora']
        self.umidade = dicio['umidade']
        self.pressaoAtmosferica = dicio['pressaoAtmosferica']
        self.direcaoVento = dicio['direcaoVento']
        self.velocidadeVento = dicio['velocidadeVento']
        self.pluviometro = dicio['pluviometro']
        self.radiacaoSolar = dicio['radiacaoSolar']
        self.temperaturaAr = dicio['temperaturaAr']

    def json(self):
        return {
                'commit_id' : self.commit_id,
                'id_estacao' : self.id_estacao,
                'nome_estacao' : self.nome_estacao,
                'dataHora' : self.dataHora,
                'umidade': self.umidade,
                'pressaoAtmosferica' : self.pressaoAtmosferica,
                'direcaoVento' : self.direcaoVento,
                'velocidadeVento' : self.velocidadeVento,
                'pluviometro' : self.pluviometro,
                'radiacaoSolar' : self.radiacaoSolar,
                'temperaturaAr' : self.temperaturaAr
                }

    @classmethod
    def find_relatorio(cls, commit_id):
        relatorio = cls.query.filter_by(commit_id = commit_id).first()
        if commit_id:
            return relatorio
        return None

    def save_relatorio(self):
        banco.session.add(self)
        banco.session.commit()

    def update_relatorio(self, id_estacao, nome_estacao, dataHora, umidade, pressaoAtmosferica, velocidadeVento, pluviometro, temperaturaAr, direcaoVento, radiacaoSolar):
        self.id_estacao = id_estacao
        self.nome_estacao = nome_estacao
        self.dataHora = dataHora
        self.umidade = umidade
        self.pressaoAtmosferica = pressaoAtmosferica
        self.direcaoVento = direcaoVento
        self.velocidadeVento = velocidadeVento
        self.radiacaoSolar = radiacaoSolar
        self.pluviometro = pluviometro
        self.temperaturaAr = temperaturaAr
    
    def delete_relatorio(self):
        banco.session.delete(self)
        banco.session.commit()

    #DADOS
    """
    MIR1-101H (%)
    Relativa	
    PIR1-101H (mb)	
    Pressão Atmosférica	
    TIR1-101H (°C)	
    Temperatura do Ar	
    TIR2-101H (°C)	
    Temperatura Interna	
    TIR3-101H (°C)	
    Ponto de Orvalho	
    TIR4-101H (°C)	
    Sensação Térmica	
    RIR1-101H (W/m²)	
    Radiação Solar	ZIR1-101H (°)	
    Direção do Vento	
    SIR1-101H (Km/h)	
    Velocidade do Vento	LIR1-101H (mm/h)	
    Precipitação
    """
