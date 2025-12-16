from schemas import apresenta_simulacoes, SimulacaoBuscaSchema, apresenta_simulacao
from logger import logger
from model import Session, Simulacao
from services import obter_meta_selic, obter_cdi_acumulado_12

def obter_lista_simulacoes():
    ''' Faz a busca por todas as Simulações cadastradas
    '''
    
    logger.debug(f"Coleta de simulacoes iniciada.")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    simulacoes = session.query(Simulacao).all()

    if not simulacoes:
        # se não há simulações cadastradas
        return {"simulacoes": []}, 200
    else:
        logger.debug(f"%d simulacoes econtradas" % len(simulacoes))
        # retorna a representação da simulação
        return apresenta_simulacoes(simulacoes), 200

def obter_simulacao(query: SimulacaoBuscaSchema):
    ''' Faz a busca por uma simulação a partir do id
    '''
    
    simulacao_id = query.id
    logger.debug(f"Coletando dados sobre a simulacao #{simulacao_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    simulacao = session.query(Simulacao).filter(Simulacao.id == simulacao_id).first()

    if not simulacao:
        # se a simulação não foi encontrada
        error_msg = "Simulação não encontrado na base :/"
        logger.warning(f"Erro ao buscar simulação '{simulacao_id}', {error_msg}")
        return {"error_code": 404, "message": error_msg}, 404
    else:
        logger.debug(f"Simulacao econtrada: '{simulacao.id}'")
        # retorna a representação da simulação
        return apresenta_simulacao(simulacao), 200

def obter_lista_taxas():
    ''' Faz a busca por todas as taxas disponíveis
    '''
    try:
        logger.debug(f"Coleta de taxas iniciada.")
        selic = obter_meta_selic()[0]
        cdi = obter_cdi_acumulado_12()[0]
        logger.debug(f"Coleta de taxas finalizada.")

        return {"taxas": [selic,cdi,]}, 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível obter lista de taxas. {e}"
        logger.warning(f"Erro. {error_msg}")
        return {"error_code": 400, "message": error_msg}, 400
    
if __name__ == '__main__':
    pass