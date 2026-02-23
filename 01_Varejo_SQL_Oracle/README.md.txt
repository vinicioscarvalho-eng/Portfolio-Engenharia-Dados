# 🏕️ Análise de Estoque e Vendas: Varejo de Aventura

![Status](https://img.shields.io/badge/Status-Concluído-green) ![SQL](https://img.shields.io/badge/Tech-Oracle%20SQL-orange)

## 📋 Sobre o Projeto
Este projeto simula um cenário real de análise de dados para um e-commerce de equipamentos de aventura. O objetivo foi identificar **ineficiências no estoque** e calcular indicadores de venda, utilizando SQL puro para resolver problemas de negócio comuns.

## 💼 Desafios de Negócio Resolvidos

### 1. Análise de Rentabilidade
**Pergunta:** Quais categorias geram o maior ticket médio por pedido?
**Solução:** Agrupamento por categoria e cálculo da média de vendas.

![Gráfico Ticket Médio](1_ticket_medio.png)
*(Resultado: Categorias de Escalada e Camping lideram o ticket médio)*

---

### 2. Identificação de Estoque "Fantasma"
**Pergunta:** Existem produtos com alto estoque físico, mas sem saída de vendas?
**Problema Técnico:** Produtos sem vendas desapareceriam de um relatório comum (`INNER JOIN`).
**Solução SQL:** Uso de `LEFT JOIN` + `COALESCE` para identificar itens nulos e `HAVING` para filtrar o resultado.

![Produtos Encalhados](2_resultado_analise.png)
*(Resultado: O item 'Saco de Dormir' possui 60 unidades paradas e 0 vendas)*

## 🛠️ Tecnologias Utilizadas
* **Banco de Dados:** Oracle Database
* **Linguagem:** SQL (DQL e DDL)
* **Técnicas:** `LEFT JOIN`, `COALESCE`, `HAVING`, Funções de Agregação.

## 🚀 Como Executar
1. Execute o script `script_varejo.sql` no seu banco de dados.
2. Rode as queries comentadas ao final do arquivo.

---
*Nota: A massa de dados foi gerada com auxílio de IA para simulação de cenários.*