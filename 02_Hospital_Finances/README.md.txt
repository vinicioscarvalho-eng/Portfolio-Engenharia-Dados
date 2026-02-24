# 🏥 Data Analytics: Auditoria Financeira e Eficiência Hospitalar

Este projeto simula um ambiente real de **Data Warehouse Hospitalar**, focado em resolver dores latentes da gestão de saúde: a eficiência de ocupação de leitos e a saúde financeira (ciclo de receita).

---

## 🚀 Contexto do Projeto
A base de dados foi estruturada utilizando o modelo **Star Schema** (Esquema Estrela), facilitando a performance em consultas analíticas. O projeto foca em identificar anomalias de custos e gargalos operacionais em diferentes alas hospitalares (UTI, Enfermaria, Pediatria, etc.).

---

## 🛠️ Tecnologias Utilizadas
* **Banco de Dados:** Oracle SQL
* **Conceitos:** DDL, DML, Window Functions, Agregações Complexas, Joins e Filtros de Grupo.

---

## 🤖 Metodologia e Uso de IA
Para garantir a eficiência no desenvolvimento e a qualidade da massa de dados simulada:
* **Scripts de Estrutura (DDL):** As instruções de `CREATE TABLE` e as definições de constraints foram refinadas com o auxílio de **Inteligência Artificial**.
* **Massa de Dados (DML):** Os comandos de `INSERT` manuais foram gerados via **IA**, permitindo criar cenários de negócio realistas com variações propositais de glosas, datas e valores para validar as queries analíticas.

---

## 📊 Estrutura de Dados
O modelo é composto por:
* **DIM_CONVENIO:** Cadastro de operadoras de saúde e tipos de plano.
* **DIM_LEITO:** Estrutura física do hospital dividida por alas (UTI, Enfermaria, Pediatria).
* **FATO_ATENDIMENTOS:** Registro centralizador de movimentações, valores e status de faturamento (Glosas).

---

## 🔍 Perguntas de Negócio Respondidas

### 1. Eficiência de Ocupação por Leito
**Objetivo:** Identificar o giro de leitos e o tempo médio que um paciente ocupa a estrutura.
* **Técnica:** `AVG`, `GROUP BY` e matemática de datas.

### 2. Comparação de Custo vs. Média da Ala
**Objetivo:** Detectar se um atendimento específico fugiu do padrão financeiro do setor.
* **Técnica:** **Window Functions** (`AVG() OVER (PARTITION BY ...)`). Este é o diferencial técnico do projeto, permitindo comparar um dado individual com o agregado sem "perder" a linha original.

### 3. Detecção de Anomalias Financeiras
**Objetivo:** Quantificar em valores monetários o desvio de cada paciente em relação à média.
* **Técnica:** Operações aritméticas entre colunas e funções analíticas.

### 4. Gestão de Ciclo de Receita (Glosas por Convênio)
**Objetivo:** Identificar quais convênios possuem a maior taxa de glosa (procedimentos não pagos).
* **Técnica:** Soma Condicional (`SUM(CASE WHEN...)`) e cálculo de percentual dinâmico.

### 5. Ranking de Setores de Alta Performance
**Objetivo:** Filtrar alas que superaram o faturamento de R$ 15.000,00.
* **Técnica:** Cláusula `HAVING` para filtro de agregados pós-agrupamento.

---

## 📈 Insights Obtidos
* Identificamos que a ala de **Maternidade/UTI** possui o maior ticket médio, porém com picos de anomalia que precisam de auditoria clínica.
* O convênio com maior taxa de glosa foi identificado, permitindo ao time de faturamento revisar os protocolos de envio de guias.
* A média de permanência foi correlacionada com o custo, revelando que internações mais longas nem sempre são as mais rentáveis devido ao custo operacional fixo do leito.