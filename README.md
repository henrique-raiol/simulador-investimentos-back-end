# Simulador de Investimentos (Back-end)
### Por Paulo Henrique Raiol

Este projeto de back-end compõe a entrega do MVP da sprint de Arquitetura de Software do Curso de Engenharia de Software da PUC-Rio.

O objetivo deste projeto é a **realização do cálculo de rentabilidade futura** de investimentos em renda fixa com evolução mensal. Utilizando variáveis como aporte inicial, aporte mensal, escolher taxas reais de mercado (Selic ou CDI acumulado nos 12 meses), prazo em meses ou anos e estimativa de gastos mensais.

Ele retorna o valor final, total investido e total de juros ganhos. Também análises adicionais como percentual de juros em relação ao investido, cobertura de gastos mensais utilizando o investimento, cálculo de renda passiva com base na taxa de juros informada, equivalência dos juros recebidos em relação ao aporte mensal.

## 🚀 Funcionalidades da API

- **Cálculo de Rentabilidade:** Projeta a evolução patrimonial mensal com base em aportes e juros compostos.
- **Integração com BACEN:** Consulta automática das taxas oficiais via API pública do Banco Central:
  - Taxa Selic (Meta)
  - CDI (Acumulado 12 meses)
- **Análises Financeiras:** Retorna métricas como cobertura de gastos, renda passiva estimada e proporção Juros/Aporte.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Flask** (Framework Web)
- **Requests** (Consumo de APIs Externas)
- **Docker** (Containerização)

## 📦 Como executar

Este projeto foi desenhado para rodar em conjunto com o Front-end via **Docker Compose**. 
> **Recomendação:** Siga as instruções de execução presentes no repositório do Front-end para subir todo o ambiente (Full Stack) de uma vez.

### Execução Manual (Sem Docker)

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```bash
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```bash
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```bash
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

### Execução via Docker (Container Único)
```bash
docker build -t simulador-backend .
docker run -p 5000:5000 simulador-backend
```
---
Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
