from schemas import SimulacaoCalculoSchema, SimulacaoSalvarSchema, SimulacaoBuscaSchema
from logger import logger
from controller import EvolucaoPatrimonio
from model import Session, Simulacao
from sqlalchemy.exc import IntegrityError
# from urllib.parse import unquote

def executa_calculo_simulacao(form: SimulacaoCalculoSchema):
    ''' Realiza o cálculo da simulação
    '''

    simulacao_evolucao = EvolucaoPatrimonio(
        primeiro_aporte = form.primeiro_aporte,
        aporte_mensal = form.aporte_mensal,
        tx_juros_anual = form.tx_juros_anual,
        periodo = form.periodo,
        tipo_periodo = form.tipo_periodo,
        gastos_mensais = form.gastos_mensais,
        data_simulacao= form.data_simulacao
    )

    logger.debug(f"Iniciando calculo da simulacao")
    try:
        return apresenta_resultado_simulacao(simulacao_evolucao), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível executar simulação :/"
        logger.warning(f"Erro ao calcular simulacao. {error_msg}")
        return {"error_code": 400, "message": error_msg}, 400

def salvar_simulacao_bd(form: SimulacaoSalvarSchema):
    ''' Adiciona uma nova simulação à base de dados
    '''
    
    simulacao = Simulacao(
        nome = form.nome,
        valor_inicial = form.valor_inicial,
        aporte_mensal = form.aporte_mensal,
        tx_anual = form.tx_anual,
        periodo = form.periodo,
        gasto_mensal = form.gasto_mensal,
        valor_final = form.valor_final
        )
    
    logger.debug(f"Adicionando/atualizando simulacao de nome: '{simulacao.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # Verifica se a simulação já existe
        simulacaoNoBD = session.query(Simulacao).filter(Simulacao.id == form.id).first()
        if simulacaoNoBD:
            # atualizando simulação
            simulacaoNoBD.nome = simulacao.nome
            simulacaoNoBD.valor_inicial = simulacao.valor_inicial
            simulacaoNoBD.aporte_mensal = simulacao.aporte_mensal
            simulacaoNoBD.tx_anual = simulacao.tx_anual
            simulacaoNoBD.periodo = simulacao.periodo
            simulacaoNoBD.gasto_mensal = simulacao.gasto_mensal
            simulacaoNoBD.valor_final = simulacao.valor_final
            logger.debug(f"Atualizada simulacao de nome: '{simulacao.nome}', id: '{simulacaoNoBD.id}'")
        else:
            # adicionando simulação
            session.add(simulacao)
            logger.debug(f"Adicionada simulacao de nome: '{simulacao.nome}', id: {simulacao.id}")
        
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return {"message": "Registro salvo/atualizado com sucesso.", "id": simulacao.id or simulacaoNoBD.id}, 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Simulação de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar simulacao '{simulacao.nome}', {error_msg}")
        return {"error_code": 409, "message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova simulação :/"
        logger.warning(f"Erro ao adicionar simulacao '{simulacao.nome}', {error_msg}")
        return {"error_code": 400, "message": error_msg}, 400

def deletar_simulacao(query: SimulacaoBuscaSchema):
    ''' Deleta uma simulação a partir do id da simulação informada
    '''

    # simulacao_nome = unquote(unquote(query.nome))
    simulacao_id = query.id

    logger.debug(f"Deletando dados sobre a simulacao #{simulacao_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Simulacao).filter(Simulacao.id == simulacao_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletada simulacao #{simulacao_id}")
        return {"message": "Simulação removida", "id": simulacao_id}, 200
    else:
        # se a simulação não foi encontrada
        error_msg = "Simulação não encontrada na base :/"
        logger.warning(f"Erro ao deletar simulação #'{simulacao_id}', {error_msg}")
        return {"error_code": 404, "message": error_msg}, 404

def apresenta_resultado_simulacao(simulacao: EvolucaoPatrimonio):
    ''' Define a forma de apresentação após o cálculo
    '''

    return {
        "taxa_juros_mensal": simulacao.get_taxa_juros_mensal(),
        "resultado_total_acumulado": simulacao.get_resultado_acumulado(),
        "total_investido": simulacao.get_total_investido(),
        "juros_recebidos": simulacao.get_total_juros_recebidos(),
        "perc_investido_vs_juros": simulacao.get_perc_investido_vs_juros(),
        "cobertura_gastos_pessoais": simulacao.get_cobertura_gastos_pessoais(),
        "juros_sobre_aporte": simulacao.get_juros_sobre_aportes_ultimo_mes(),
        "renda_passiva_estimada": simulacao.get_renda_passiva_estimada(),
        "evolucao_patrimonial": simulacao.get_evolucao_patrimonial()
    }

if __name__ == '__main__':
    pass