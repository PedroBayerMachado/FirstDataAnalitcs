import pandas as pd
import random
from faker import Faker

fake = Faker("pt_BR")

# Número de usuários
num_usuarios = 120

# Listas possíveis
sexos = ["Masculino", "Feminino"]
planos = ["Mensal", "Trimestral", "Anual", None]
treinos = ["Musculação", "Cardio", "Crossfit", "Yoga", "Funcional"]
ativos = ["Sim", "Não"]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Campinas", "Santos", "Brasília"]

# Lista para armazenar os dados
dados = []

for i in range(1, num_usuarios + 1):
    nome = fake.first_name() + " " + fake.last_name()
    idade = random.randint(18, 60)
    sexo = random.choice(sexos)
    peso = round(random.uniform(50, 100), 1) if random.random() > 0.1 else None  # 10% nulos
    altura = round(random.uniform(1.55, 1.90), 2) if random.random() > 0.1 else None  # 10% nulos
    plano = random.choice(planos)
    treino = random.choice(treinos)
    frequencia = random.randint(1, 6)
    ativo = random.choice(ativos)
    cidade = random.choice(cidades)
    satisfacao = random.randint(1, 10) if random.random() > 0.1 else None  # 10% nulos
    data_inscricao = fake.date_between(start_date='-3y', end_date='today')
    
    dados.append([
        i, nome, idade, sexo, peso, altura, plano, treino,
        frequencia, ativo, cidade, satisfacao, data_inscricao
    ])

# Criar DataFrame
colunas = ["ID_Aluno","Nome","Idade","Sexo","Peso_kg","Altura_m","Plano",
           "Treino","Frequencia_Semanal","Ativo","Cidade","Satisfacao","Data_Inscricao"]
df = pd.DataFrame(dados, columns=colunas)

# Salvar CSV
df.to_csv("academia_meteshape_120.csv", index=False, encoding="utf-8-sig")

print("CSV criado: academia_meteshape_120.csv")
