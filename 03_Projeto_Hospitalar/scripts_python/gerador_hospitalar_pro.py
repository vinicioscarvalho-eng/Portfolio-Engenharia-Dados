import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')
QTD_REGISTROS = 10000  # O volume que vai impressionar no Power BI

# Configurações de Negócio
convenios = ['Unimed', 'Bradesco', 'Amil', 'SUS', 'Sulamérica', 'Notre Dame']
alas = {
    'UTI': {'custo_diaria': 2500, 'permanencia': (3, 15)},
    'Enfermaria': {'custo_diaria': 800, 'permanencia': (1, 7)},
    'Pediatria': {'custo_diaria': 1200, 'permanencia': (1, 5)},
    'Maternidade': {'custo_diaria': 1800, 'permanencia': (2, 4)}
}

data_lista = []

print(f"🚀 Iniciando a geração de {QTD_REGISTROS} atendimentos... Isso pode levar alguns segundos.")

for i in range(QTD_REGISTROS):
    id_atendimento = i + 1
    paciente = fake.name()
    convenio = random.choice(convenios)
    ala = random.choice(list(alas.keys()))
    
    # Lógica de Datas
    data_entrada = fake.date_between(start_date='-2y', end_date='today')
    dias_internado = random.randint(alas[ala]['permanencia'][0], alas[ala]['permanencia'][1])
    data_saida = data_entrada + timedelta(days=dias_internado)
    
    # Lógica Financeira (Diária x Dias + variação aleatória de medicamentos/exames)
    custo_base = alas[ala]['custo_diaria'] * dias_internado
    valor_total = custo_base + random.uniform(500, 3000)
    
    # Lógica de Glosa (Probabilidade de 15% de erro no faturamento)
    status_glosa = 'SIM' if random.random() < 0.15 else 'NAO'
    
    # Motivo da Internação (Para usarmos em filtros no Power BI)
    motivos = ['Cirurgia', 'Exames Complexos', 'Emergência', 'Tratamento Contínuo', 'Check-up']
    motivo = random.choice(motivos)

    data_lista.append([
        id_atendimento, paciente, convenio, ala, 
        data_entrada, data_saida, round(valor_total, 2), status_glosa, motivo
    ])

# Criando o DataFrame
colunas = [
    'ID_ATENDIMENTO', 'PACIENTE', 'CONVENIO', 'ALA', 
    'DATA_ENTRADA', 'DATA_SAIDA', 'VALOR_TOTAL', 'STATUS_GLOSA', 'MOTIVO'
]
df = pd.DataFrame(data_lista, columns=colunas)

# Salvando
df.to_csv('base_hospitalar_10k.csv', index=False, encoding='utf-8-sig')

print(f"✅ Sucesso! O arquivo 'base_hospitalar_10k.csv' foi gerado com {len(df)} linhas.")
print("💡 Dica do Lead: Agora temos dados suficientes para ver tendências mensais no Power BI!")