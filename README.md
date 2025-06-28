# Simulador de Investimentos
### Por Paulo Henrique Raiol

Este projeto de back-end compõe a entrega do MVP da sprint de Desenvolvimento Full Satck Básico da Curso de Engenharia de Software da PUC-Rio.

O objetivo deste projeto é a **realização do cálculo de rentabilidade futura** de investimentos em renda fixa com evolução mensal. Utilizando variáveis como aporte inicial, aporte mensal, taxa de juros ao ano, prazo em meses ou anos e estimativa de gastos mensais.

Ele retorna o valor final, total investido e total de juros ganhos. Também análises adicionais como percentual de juros em relação ao investido, cobertura de gastos mensais utilizando o investimento, cálculo de renda passiva com base na taxa de juros informada, equivalência dos juros recebidos em relação ao aporte mensal.

---
## Como executar 

> Este projeto foi desenvolvido utilizando Python 3.11.9

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
