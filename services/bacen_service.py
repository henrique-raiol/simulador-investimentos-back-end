import requests
from logger import logger

def obter_meta_selic():
    ''' Retorna a meta da selic vigente
    '''
    # URL da API do Banco Central (Série 432 - Meta Selic definida pelo COPOM)
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados: dict = response.json()[0]
            dados['taxa'] = 'meta_selic'
            return dados, 200
        else:
            logger.warning(f"Erro na requisição API BACEN. Retornando dados padrão. {response.status_code}")
            return {'data': '01/01/2026', 'valor': '10.00', 'taxa': 'meta_selic'}, 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível executar a requisição da SELIC junto ao BACEN. {e}"
        logger.warning(f"Erro. {error_msg}")
        return {"error_code": 400, "message": error_msg}, 400

def obter_cdi_acumulado_12():
    ''' Retorna o CDI acumulado nos últimos 12 meses
    '''
    # URL da API do Banco Central (Série 4391 - CDI Acumulado)
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4391/dados/ultimos/12?formato=json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados_lista = response.json()
            valor_acumulado = sum(float(item['valor']) for item in dados_lista)
            return {
                'data': dados_lista[0]['data'],
                'valor': f"{valor_acumulado:.2f}",
                'taxa': 'cdi_acumulado_12_meses'
            }, 200
        else:
            logger.warning(f"Erro na requisição API BACEN. Retornando dados padrão. {response.status_code}")
            return {'data': '01/01/2026', 'valor': '10.00', 'taxa': 'cdi_acumulado_12_meses'}, 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível executar a requisição do CDI junto ao BACEN. {e}"
        logger.warning(f"Erro. {error_msg}")
        return {"error_code": 400, "message": error_msg}, 400

if __name__ == "__main__":
    pass