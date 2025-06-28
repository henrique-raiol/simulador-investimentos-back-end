from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Simulacao(Base):
    __tablename__ = 'simulacao'

    id = Column("pk_simulacao", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    valor_inicial = Column(Float)
    aporte_mensal = Column(Float)
    tx_anual = Column(Float)
    periodo = Column(Integer)
    gasto_mensal = Column(Float)
    valor_final = Column(Float)
    data_simulacao = Column(String(10))
    data_insercao = Column(DateTime)
    # data_simulacao = Column(String(10), default=datetime.now().strftime("%d.%m.%Y"))
    # data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome: str, valor_inicial: float, aporte_mensal: float, 
                 tx_anual: float, periodo: int, gasto_mensal: float, valor_final: float,
                 data_simulacao: str = None, data_insercao:Union[DateTime, None] = None):
        
        ''' Cria a simulação

            Arguments:
                id: id no banco de dados
                nome: nome do investidor
                valor_inicial: investimento/aporte inicial
                aporte_mensal: investimento/aporte mensal
                tx_anual: taxa anual de rentabilidade em decimal
                periodo: periodo em meses
                gasto_mensal: gasto mensal com despesas
                valor_final: valor final com a rentabilidade
                data_simulacao: data de quando o produto foi inserido à base no formato dd.mm.aaaa
                data_insercao: data e hora de quando o produto foi inserido à base
        '''
        self.nome = nome
        self.valor_inicial = valor_inicial
        self.aporte_mensal = aporte_mensal
        self.tx_anual = tx_anual
        self.periodo = periodo
        self.gasto_mensal = gasto_mensal
        self.valor_final = valor_final

        # se não for informada, será o data exata da inserção no banco
        if data_simulacao:
            self.data_simulacao = data_simulacao
        else:
            self.data_simulacao = datetime.now().strftime("%d.%m.%Y")

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
        else:
            self.data_insercao = datetime.now()

if __name__ == '__main__':
    pass