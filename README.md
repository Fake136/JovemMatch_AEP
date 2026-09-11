# JovemMatch

**Prova de Conceito (PoC)** – AEP 2026.2 – 6º Semestre  
**Curso:** Engenharia de Software – UniCesumar

## Problema

Alto índice de desemprego entre jovens de 15 a 29 anos no Brasil. Muitos jovens têm dificuldade em encontrar oportunidades alinhadas às suas habilidades.

## ODS Atendido

**ODS 8 – Trabalho decente e crescimento econômico**

## Solução

Sistema que permite cadastrar jovens, cadastrar vagas de emprego e realizar candidaturas (matching básico).

## Tecnologias

- Python 3.10+
- MongoDB (NoSQL)
- pymongo
- pytest + pytest-cov
- Programação Orientada a Objetos

## Modelagem NoSQL

**3 coleções:**

- `jovens` → documentos complexos (formacao aninhada + lista de experiencias)
- `vagas` → documentos com localizacao aninhada + lista de habilidades
- `candidaturas` → relacionamento por referência (jovem_id + vaga_id)

## Como Executar

### 1. Pré-requisitos
- Python 3.10+
- MongoDB rodando localmente (Compass)

### 2. Configurar

```bash
python -m venv venv
venv\Scripts\activate          # Windows CMD/PowerShell
# ou: source venv/Scripts/activate   # Git Bash

pip install -r requirements.txt
```

Crie o arquivo `.env` na raiz:

```
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=jovemmatch_db
```

### 3. Popular o banco

```bash
python -m scripts.seed
```

### 4. Rodar a aplicação

```bash
python -m src.main
```

### 5. Rodar testes e cobertura

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```

## Equipe

| RA | Nome |
|----|------|
| 24042002-2 | Heitor Saueressig Mello |
| 24150613-2 | Luiz Eduardo Valério Semensato |
| 24224711-2 | Gabriel Lopes |

## Tag da entrega

`v1.0-primeira-entrega`
