# JovemMatch

**Prova de Conceito (PoC)** – AEP 2026.2 – 6º Semestre  
**Curso:** Engenharia de Software – UniCesumar  
**Entrega:** Segunda Entrega (`v2.0-segunda-entrega`)

## Problema

Alto índice de desemprego entre jovens de 15 a 29 anos no Brasil. Muitos jovens têm dificuldade em encontrar oportunidades alinhadas às suas habilidades.

## ODS Atendido

**ODS 8 – Trabalho decente e crescimento econômico**

## Solução

O **JovemMatch** conecta jovens a vagas de emprego com:

- Cadastro de jovens (habilidades, formação e experiência)
- Cadastro de vagas
- Candidaturas com controle de status
- **Matching inteligente** por habilidades em comum
- Busca de vagas por cidade
- Estatísticas do sistema

## Evolução em relação à 1ª entrega

| Funcionalidade | 1ª Entrega | 2ª Entrega |
|----------------|-------------|-------------|
| CRUD jovens/vagas/candidaturas | Sim | Sim |
| Matching por habilidades | Não | **Sim** |
| Atualizar status da candidatura | Não | **Sim** |
| Busca de vagas por cidade | Não | **Sim** |
| Estatísticas | Não | **Sim** |
| Documentação técnica completa | Básica | **Completa** |
| Metodologia (quadro de tarefas) | Não | **Sim** |

## Tecnologias

- Python 3.10+
- MongoDB (NoSQL) – Atlas ou local
- pymongo
- pytest + pytest-cov
- Programação Orientada a Objetos (Models, Repositories, Services)

## Modelagem NoSQL

**3 coleções com documentos complexos e relacionamentos:**

- `jovens` → `formacao` (objeto aninhado) + `experiencia` (lista de subdocumentos)
- `vagas` → `localizacao` (objeto aninhado) + `habilidades_requeridas` (lista)
- `candidaturas` → referência por `jovem_id` e `vaga_id` + status

## Como Executar

### 1. Pré-requisitos
- Python 3.10+
- MongoDB Atlas (recomendado) ou MongoDB local

### 2. Configurar

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

Crie o arquivo `.env` na raiz (use `.env.example` como modelo):

```
MONGO_URI=mongodb+srv://USUARIO:SENHA@cluster.mongodb.net/?appName=hesame
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

### 5. Testes e cobertura

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```

Cobertura mínima exigida: **70%** (main.py excluído via `.coveragerc`).

## Metodologia de trabalho

Utilizamos **GitHub Projects** como quadro de tarefas (Backlog / Em andamento / Concluído).  
Detalhes em: [docs/metodologia.md](docs/metodologia.md)

## Documentação técnica

Veja [docs/documentacao.md](docs/documentacao.md) para arquitetura, modelagem e decisões técnicas.

## Equipe

| RA | Nome |
|----|------|
| 24042002-2 | Heitor Saueressig Mello |
| 24150613-2 | Luiz Eduardo Valério Semensato |
| 24224711-2 | Gabriel Lopes |

## Tags

- `v1.0-primeira-entrega` – versão inicial
- `v2.0-segunda-entrega` – versão final com evolução
