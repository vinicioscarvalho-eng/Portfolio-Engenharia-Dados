# 🏥 Projeto 03 — Dashboard Hospitalar

## Descrição

Projeto de análise de dados com foco na gestão operacional e financeira de um hospital fictício com 10.000 registros de atendimento. O objetivo é transformar dados brutos em informações relevantes para tomada de decisão, cobrindo indicadores como faturamento mensal, variação percentual de receita, taxa de glosa por convênio e ocupação por ala.

---

## Problema de Negócio

Hospitais lidam diariamente com grandes volumes de dados financeiros e operacionais. Sem uma visão consolidada, é difícil responder perguntas como:

- O faturamento está crescendo ou caindo mês a mês?
- Qual é a taxa de glosa e como ela varia por convênio?
- Qual ala concentra mais dias de internação?

Este projeto simula um ambiente real de análise hospitalar, respondendo essas perguntas através de uma pipeline de dados estruturada.

---

## Arquitetura do Projeto

```
Python (geração dos dados)
        ↓
Oracle Database (armazenamento e transformação via SQL)
        ↓
Views SQL (camada analítica)
        ↓
Power BI (visualização e dashboards)
        ↓
GitHub (versionamento e portfólio)
```

**Tecnologias utilizadas:**
- **Python** — geração dos 10.000 registros simulados via script (`gerador_hospitalar_pro.py`)
- **Oracle Database (Oracle XE)** — banco de dados relacional local
- **SQL (Oracle SQL)** — criação de tabela, views e funções analíticas (Window Functions)
- **Power BI Desktop** — construção do dashboard interativo
- **VS Code** — ambiente de desenvolvimento com extensão Oracle SQL Developer
- **Git + GitHub** — versionamento e publicação do portfólio

---

## Estrutura de Arquivos

```
03_Projeto_Hospitalar/
│
├── dashboard/
│   └── dashboard_pbi_projeto_03.pbix       # Dashboard Power BI
│
├── scripts_python/
│   ├── base_hospitalar_10k.csv             # Base de dados gerada
│   └── gerador_hospitalar_pro.py           # Script de geração dos dados
│
├── scripts_sql/
│   ├── scripts_sql_usados.sql              # DDL da tabela e criação das Views
│   └── arquivo_teste_automatizacao.sql     # Script de testes
│
├── atualizar_projeto.bat                   # Script de atualização automática no GitHub
└── README.md
```

---

## Modelo de Dados

**Tabela principal:** `FATO_HOSPITAL_10K`

| Coluna | Tipo | Descrição |
|---|---|---|
| ID_ATENDIMENTO | NUMBER | Identificador único do atendimento |
| PACIENTE | VARCHAR2 | Nome do paciente |
| CONVENIO | VARCHAR2 | Convênio do paciente |
| ALA | VARCHAR2 | Ala de internação (UTI, Enfermaria, Pediatria, Maternidade) |
| DATA_ENTRADA | DATE | Data de entrada do paciente |
| DATA_SAIDA | DATE | Data de saída do paciente |
| VALOR_TOTAL | NUMBER | Valor total do atendimento |
| STATUS_GLOSA | VARCHAR2 | Indica se houve glosa (SIM/NAO) |
| MOTIVO | VARCHAR2 | Motivo do atendimento |

---

## Views SQL Criadas

### VW_FINANCEIRO_10K
Visão financeira por convênio e mês. Consolida faturamento total, valor glosado e percentual de glosa mensal.

> **Aprendizado registrado:** durante o desenvolvimento, identificamos que o cálculo de porcentagem estava sendo feito duas vezes — uma vez no SQL com `* 100` e novamente pelo Power BI ao formatar a coluna como porcentagem. Isso gerou valores absurdos como 2160% no dashboard. A correção foi remover o `* 100` da query SQL, centralizando a lógica na fonte e deixando o Power BI responsável apenas pela formatação visual.

### VW_OPERACIONAL_10K
Visão operacional por ala e motivo de atendimento. Consolida número de atendimentos, média de dias internados e média de valor por atendimento.

### VW_PERCENTUAL_VARIACAO_FATURAMENTO
View analítica construída com **CTE + Window Function LAG()** para calcular a variação percentual do faturamento mês a mês. Permite identificar se o hospital está em tendência de crescimento ou queda de receita.

```sql
-- Estrutura simplificada da lógica aplicada
WITH faturamento_mensal AS (
    SELECT
        EXTRACT(MONTH FROM DATA_SAIDA) AS MES,
        SUM(VALOR_TOTAL) AS VALOR_TOTAL
    FROM FATO_HOSPITAL_10K
    GROUP BY EXTRACT(MONTH FROM DATA_SAIDA)
)
SELECT
    MES,
    VALOR_TOTAL,
    LAG(VALOR_TOTAL) OVER (ORDER BY MES) AS VALOR_TOTAL_ANTERIOR,
    ROUND((VALOR_TOTAL - LAG(VALOR_TOTAL) OVER (ORDER BY MES))
        / LAG(VALOR_TOTAL) OVER (ORDER BY MES) * 100, 2) AS VARIACAO_PERCENTUAL
FROM faturamento_mensal
ORDER BY MES ASC;
```

---

## Dashboard — Visão Geral

O dashboard foi construído no Power BI Desktop conectado diretamente ao Oracle Database via JDBC. Conta com filtros interativos por **ano** e **convênio**, e os seguintes visuais:

- **Faturamento Mensal** — evolução do faturamento ao longo dos 12 meses
- **Variação Percentual de Faturamento** — crescimento ou queda mês a mês com base na função analítica LAG()
- **Percentual de Glosa Mensal** — indicador de eficiência financeira
- **Dias Internados por Ala** — distribuição operacional por setor

---

## Principais Aprendizados Técnicos

- Modelagem de dados com tabela fato e camada analítica via Views SQL
- Uso de **Window Functions** (`LAG()`) para análise de tendência temporal
- Uso de **CTEs** para separar responsabilidades dentro de uma query complexa
- Identificação e correção de erro de dupla contagem entre SQL e Power BI
- Criação de coluna calculada em DAX com `FORMAT(DATE())` para exibição de nomes de meses no Power BI
- Boas práticas de nomenclatura de objetos (`VW_` para views) e organização de repositório
- Versionamento contínuo com Git e automação via script `.bat`

---

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/vinicioscarvalho-eng/Portfolio-Engenharia-Dados
```
2. Execute o script Python para gerar a base de dados: `gerador_hospitalar_pro.py`
3. No Oracle Database, execute o arquivo `scripts_sql_usados.sql` para criar a tabela e as Views
4. Abra o arquivo `dashboard_pbi_projeto_03.pbix` no Power BI Desktop e atualize a conexão com o seu banco local

---

## Autor

**Vinicios Carvalho**
Estudante de Análise de Dados | SQL · Python · Power BI

🔗 [GitHub](https://github.com/vinicioscarvalho-eng/Portfolio-Engenharia-Dados)