import math
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EvolucaoPatrimonio:
    ''' Cálculo juros compostos com evolução
    '''

    def __init__(self, primeiro_aporte = 1000, aporte_mensal = 200, tx_juros_anual = 0.10, periodo = 36, tipo_periodo = 'M', gastos_mensais = 2000, data_simulacao = datetime.now().strftime("%d.%m.%Y")):
        self.__primeiro_aporte = primeiro_aporte
        self.__aporte_mensal = aporte_mensal
        self.__tx_juros_anual = tx_juros_anual
        self.__periodo = periodo if tipo_periodo == 'M' else periodo * 12
        self.__gastos_mensais = gastos_mensais
        self.__data_inicial = data_simulacao if data_simulacao == '' else datetime.strptime(data_simulacao, "%d.%m.%Y")

        self.__saldo_atual = primeiro_aporte
        self.__total_investido = primeiro_aporte
        self.__total_juros_ganhos = 0
        self.__evolucao_patrimonial_mensal = []
        self.__evolucao_patrimonial_anual = []

        self.__calculo_rentabilidade()

    def get_taxa_juros_mensal(self):
        return (1 + self.__tx_juros_anual)**(1/12) - 1
    
    def __calculo_rentabilidade(self):
        data_atual = self.__data_inicial
        juros_do_mes = 0
        tx_juros_mensal = self.get_taxa_juros_mensal()
        saldo_inicial_mensal = self.__primeiro_aporte
        saldo_inicial_anual = self.__primeiro_aporte
        total_juros_ganhos_anual_anterior = 0

        for m in range(self.__periodo):
            mes_atual = m + 1
            data_atual = data_atual + relativedelta(months=1)

            juros_do_mes = self.__saldo_atual * tx_juros_mensal
            self.__saldo_atual = self.__saldo_atual + juros_do_mes
            self.__saldo_atual = self.__saldo_atual + self.__aporte_mensal

            self.__total_juros_ganhos = self.__total_juros_ganhos + juros_do_mes
            self.__total_investido = self.__total_investido + self.__aporte_mensal

            # Evolução Patrimonial Mensal
            self.__evolucao_patrimonial_mensal.append({
                'mes': mes_atual,
                'data': data_atual.strftime("%d.%m.%Y"),
                'saldo_inicial': saldo_inicial_mensal,
                'aporte': self.__aporte_mensal,
                'juros_periodo': juros_do_mes,
                'saldo_final': self.__saldo_atual
            })

            # Evolução Patrimonial Anual
            if (mes_atual % 12 == 0 or mes_atual == self.__periodo):
                self.__evolucao_patrimonial_anual.append({
                    'ano': math.ceil(mes_atual / 12),
                    'data': data_atual.strftime("%d.%m.%Y"),
                    'saldo_inicial': saldo_inicial_anual,
                    'aporte': self.__aporte_mensal * 12,
                    'juros_periodo': self.__total_juros_ganhos - total_juros_ganhos_anual_anterior,
                    'saldo_final': self.__saldo_atual
                })
                total_juros_ganhos_anual_anterior = self.__total_juros_ganhos
                saldo_inicial_anual = self.__saldo_atual

            saldo_inicial_mensal = self.__saldo_atual
    
    def get_resultado_acumulado(self):
        ''' Resultado da simulação de patrimônio:
            Resultado final após todos os aportes e juros acumulados durante o período
        '''
        return self.__saldo_atual
    
    def get_total_investido(self):
        ''' Total investido:
            Aqui você consultado o quanto você investiu sem somar os juros
        '''
        return self.__total_investido
    
    def get_evolucao_patrimonial(self):
        ''' Evolução patrimonial por mês e ano:
            Este dicionário contém a evolução do patrimônio por mês e ano junto com a rentabilidade 
        '''
        return {'mensal': self.__evolucao_patrimonial_mensal, 'anual': self.__evolucao_patrimonial_anual}
    
    def get_total_juros_recebidos(self):
        ''' Resultado de todos os juros recebidos
        '''
        return self.__saldo_atual - self.__total_investido

    def get_perc_investido_vs_juros(self):
        ''' Percentual do Patrimônio Originado de Juros:
            Esta métrica mostra qual porcentagem do patrimônio final foi gerada pelos juros compostos 
            e qual porcentagem veio dos aportes (valor inicial + aportes mensais)
        '''
        total_em_juros = self.get_total_juros_recebidos()
        percentual_de_juros = (total_em_juros / self.__saldo_atual) * 100
        percentual_de_aportes = (self.__total_investido / self.__saldo_atual) * 100

        return {'percentual_juros': round(percentual_de_juros, 2), 'percentual_aportes': round(percentual_de_aportes, 2)}

    def get_cobertura_gastos_pessoais(self):
        ''' Cobertura de Custos Pessoais pelo Patrimônio:
            Esta métrica estima por quantos meses ou anos o patrimônio acumulado poderia cobrir 
            um determinado custo de vida mensal, caso o usuário parasse de fazer novos aportes e vivesse 
            apenas daquele montante
        '''
        meses_cobertura = int(round(self.__saldo_atual / self.__gastos_mensais, 0))
        anos_cobertura = int(round(meses_cobertura / 12, 0))
        return {'meses_cobertura': meses_cobertura, 'anos_cobertura': anos_cobertura}
    
    def get_juros_sobre_aportes_ultimo_mes(self):
        ''' Juros do último mês sobre aporte: 
            Esta métrica mostra o quanto dos juros ganhos no último mês equivalem dos aportes mensais.
            Por exemplo: Se você aporta R$100/mês e no último mês você teve uma rentabilidade de R$50 então os juros
            equivalem a 0.5x do seu aporte mensal.
        '''
        return self.get_evolucao_patrimonial()['mensal'][-1]['juros_periodo'] / self.__aporte_mensal
    
    def get_renda_passiva_estimada(self):
        ''' Renda Passiva Mensal Estimada com o Patrimônio Final:
            Uma estimativa de quanto o "Valor Final Acumulado" poderia gerar de renda passiva mensal, 
            considerando a taxa de juros mensal utilizada na simulação, se você parasse de fazer novos aportes.
        '''
        return self.__saldo_atual * self.get_taxa_juros_mensal()

if __name__ == '__main__':
    pass