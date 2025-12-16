from pydantic import BaseModel
from typing import Optional, List
from model.simulacao import Simulacao

class SimulacaoCalculoSchema(BaseModel):
    ''' Define como uma nova simulação para cálculo a ser inserida deve ser representada
    '''

    nome: str = "Paulo Henrique Raiol"
    primeiro_aporte: float = 1000
    aporte_mensal: float = 100
    tx_juros_anual: float = 0.10
    periodo: int = 24
    tipo_periodo: str = "M"
    gastos_mensais: float = 2000
    data_simulacao: Optional[str] = '07.06.2025'


class SimulacaoSalvarSchema(BaseModel):
    ''' Define como uma nova simulação a ser salva deve ser representada
    '''
    
    id: Optional[int | None] = 0
    nome: str = "Paulo Henrique Raiol"
    valor_inicial: float = 1000
    aporte_mensal: float = 200
    tx_anual: float = 0.10
    periodo: int = 24
    gasto_mensal: float = 2000
    valor_final: float = 6477.03


class SimulacaoBuscaSchema(BaseModel):
    ''' Define como deve ser a estrutura que representa a busca.
        Será feita apenas com base no nome do investidor.
    '''

    id: int = 1


class ListagemSimulacoesSchema(BaseModel):
    ''' Define como uma listagem de simulações será retornada.
    '''

    simulacoes:List[SimulacaoSalvarSchema]


class ListagemTaxaSchema(BaseModel):
    ''' Define como uma listagem de taxas/indices será retornada.
    '''

    taxas:List[dict]


def apresenta_simulacoes(simulacoes: List[Simulacao]):
    ''' Retorna uma representação das simulações salvas seguindo o schema definido em SimulacaoSalvaViewSchema.
    '''

    result = []
    for simulacao in simulacoes:
        result.append({
            "id": simulacao.id,
            "nome": simulacao.nome,
            "valor_inicial": simulacao.valor_inicial,
            "aporte_mensal": simulacao.aporte_mensal,
            "tx_anual": simulacao.tx_anual,
            "periodo": simulacao.periodo,
            "gasto_mensal": simulacao.gasto_mensal,
            "valor_final": simulacao.valor_final,
            "data_simulacao": simulacao.data_simulacao,
        })

    return {"simulacoes": result}

class SimulacaoSalvaViewSchema(BaseModel):
    ''' Define como a simulação salva será retornada
    '''
    
    id: int = 1
    nome: str = "Paulo Henrique Raiol"
    valor_inicial: float = 1000
    aporte_mensal: float = 200
    tx_anual: float = 0.10
    periodo: int = 24
    gasto_mensal: float = 2000
    valor_final: float = 6477.03
    data_simulacao: str = '07.06.2025'

class SimulacaoViewSchema(BaseModel):
    ''' Define como o resultado da simulação será retornado
    '''
    
    taxa_juros_mensal: float = 0.10
    resultado_total_acumulado: float = 3843.51
    total_investido: float = 3400.00
    juros_recebidos: float = 443.51
    perc_investido_vs_juros: dict = {'percentual_juros': 0, 'percentual_aportes': 0}
    cobertura_gastos_pessoais: dict = {'meses_cobertura': 12, 'anos_cobertura': 1}
    juros_sobre_aporte: float = 0.3
    renda_passiva_estimada: float = 30.65
    evolucao_patrimonial: dict = {'mensal': [{'mes': 1, 'data': '07.06.2025', 'saldo_inicial': 1000, 'aporte': 100, 'juros_periodo': 100, 'saldo_final': 3843.51}], 'anual': [{'ano': 1, 'data': '07.06.2026', 'saldo_inicial': 1000, 'aporte': 100, 'juros_periodo': 100, 'saldo_final': 3843.51}]}


class SimulacaoDelSchema(BaseModel):
    ''' Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    '''

    message: str
    id: str

class SimulacaoOperacaoConcluidaSchema(BaseModel):
    ''' Define como deve ser a estrutura do dado retornado após uma operação.
    '''

    message: str
    id: str

class MensagemOperacaoViewSchema(BaseModel):
    ''' Define estrutura genérica de mensagem para ser retornada
    '''

    message: str

def apresenta_simulacao(simulacao: Simulacao):
    ''' Retorna uma representação da simulacao seguindo o schema definido em SimulacaoSalvaViewSchema.
    '''

    return {
        "id": simulacao.id,
        "nome": simulacao.nome,
        "valor_inicial": simulacao.valor_inicial,
        "aporte_mensal": simulacao.aporte_mensal,
        "tx_anual": simulacao.tx_anual,
        "periodo": simulacao.periodo,
        "gasto_mensal": simulacao.gasto_mensal,
        "valor_final": simulacao.valor_final,
        "data_simulacao": simulacao.data_simulacao,
    }

if __name__ == '__main__':
    pass