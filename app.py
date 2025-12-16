from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from schemas import SimulacaoViewSchema, ErrorSchema, SimulacaoCalculoSchema, SimulacaoOperacaoConcluidaSchema, SimulacaoSalvarSchema, ListagemSimulacoesSchema, SimulacaoBuscaSchema, SimulacaoDelSchema, SimulacaoSalvaViewSchema, ListagemTaxaSchema
from controller import executores, buscadores
from flask_cors import CORS

info = Info(title="API Simulador de Investimentos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Redireciona para documentação Swagger")
simulacao_tag = Tag(name="Simulação", description="cálculo, adição, visualização e remoção de simulações na base")


@app.get('/', tags=[home_tag])
def home():
    ''' Redireciona para /openapi/swagger.
    '''

    return redirect('/openapi/swagger')

@app.post('/calculo_simulacao', tags=[simulacao_tag], responses={"200": SimulacaoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def rota_calculo_simulacao(form: SimulacaoCalculoSchema):
    ''' Realiza o cálculo da simulação do investimento
        Retorna uma representação calculada da simulação
    '''

    return executores.executa_calculo_simulacao(form)

@app.put('/salva_simulacao', tags=[simulacao_tag], responses={"200": SimulacaoOperacaoConcluidaSchema, "409": ErrorSchema, "400": ErrorSchema})
def rota_salva_simulacao(form: SimulacaoSalvarSchema):
    ''' Adiciona ou atualiza uma simulação na base de dados
        Retorna uma mensagem confirmando a operação
    '''

    return executores.salvar_simulacao_bd(form)


@app.get('/obter_simulacoes', tags=[simulacao_tag], responses={"200": ListagemSimulacoesSchema, "404": ErrorSchema})
def rota_obter_simulacoes():
    ''' Retorna todas as simulações salvas
        Retorna uma representação da listagem de simulações.
    '''

    return buscadores.obter_lista_simulacoes()


@app.get('/obter_simulacao', tags=[simulacao_tag], responses={"200": SimulacaoSalvaViewSchema, "404": ErrorSchema})
def get_simulacao(query: SimulacaoBuscaSchema):
    ''' Retorna simulação salva a partir do id do investidor
        Retorna uma representação da simulação salva
    '''

    return buscadores.obter_simulacao(query)


@app.delete('/deleta_simulacao', tags=[simulacao_tag], responses={"200": SimulacaoDelSchema, "404": ErrorSchema})
def rota_deleta_simulacao(query: SimulacaoBuscaSchema):
    ''' Deleta uma simulação a partir do id do investidor informado
        Retorna uma mensagem de confirmação da remoção.
    '''

    return executores.deletar_simulacao(query)

@app.get('/obter_taxas', tags=[simulacao_tag], responses={"200": ListagemTaxaSchema, "400": ErrorSchema})
def rota_obter_taxas():
    ''' Retorna todas as taxas/indice para fazer simulação
    '''

    return buscadores.obter_lista_taxas()