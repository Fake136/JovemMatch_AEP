# JovemMatch

**Prova de Conceito (PoC)** – AEP 2026.2 – 6º Semestre  
**Curso:** Engenharia de Software – UniCesumar  
**Entrega:** Segunda Entrega

## Problema

Alto índice de desemprego entre jovens de 15 a 29 anos no Brasil.  
Muitos jovens têm dificuldade em encontrar oportunidades alinhadas às suas habilidades e formação.

## ODS Atendido

**ODS 8 – Trabalho decente e crescimento econômico**

## Solução

O **JovemMatch** conecta jovens a vagas de emprego com:

- Cadastro de jovens (habilidades, formação e experiência)
- Cadastro de vagas de emprego
- Candidaturas com controle de status
- **Matching inteligente** por habilidades em comum
- Busca de vagas por cidade
- Estatísticas do sistema

## Evolução em relação à 1ª entrega

| Funcionalidade | 1ª Entrega | 2ª Entrega |
|----------------|-------------|-------------|
| CRUD jovens / vagas / candidaturas | Sim | Sim |
| Matching por habilidades | Não | **Sim** |
| Atualizar status da candidatura | Não | **Sim** |
| Busca de vagas por cidade | Não | **Sim** |
| Estatísticas do sistema | Não | **Sim** |
| Documentação técnica completa | Básica | **Completa** |
| Metodologia (quadro de tarefas) | Não | **Sim** |

## Tecnologias

- Python 3.10+
- MongoDB (NoSQL) – Atlas ou local
- pymongo
- pytest + pytest-cov + mongomock
- Programação Orientada a Objetos (Models, Repositories, Services)

## Modelagem NoSQL (requisitos do 2º semestre)

**3 coleções com documentos complexos e relacionamentos:**

| Coleção | Estrutura |
|---------|-----------|
| `jovens` | `formacao` (objeto aninhado) + `experiencia` (lista de subdocumentos) |
| `vagas` | `localizacao` (objeto aninhado) + `habilidades_requeridas` (lista) |
| `candidaturas` | Referência por `jovem_id` e `vaga_id` + campo `status` |

Atende: múltiplas coleções, relacionamento entre coleções e objetos complexos (documentos aninhados / listas de subdocumentos).

## Como Executar

### 1. Pré-requisitos
- Python 3.10+
- MongoDB Atlas (recomendado) ou MongoDB local

### 2. Configurar o ambiente

```bash
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

Crie o arquivo `.env` na **raiz** do projeto:

```
MONGO_URI=mongodb+srv://USUARIO:SENHA@cluster.mongodb.net/?appName=hesame
DATABASE_NAME=jovemmatch_db
```

> Substitua pela sua connection string do Atlas (ou use `mongodb://localhost:27017` para ambiente local).

### 3. Popular o banco (seed)

```bash
python -m scripts.seed
```

### 4. Rodar a aplicação

```bash
python -m src.main
```

### 5. Testes automatizados e cobertura

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```

- **Cobertura obtida: ≥ 70%** (exigência da disciplina atendida)
- `src/main.py` é omitido da medição (interface interativa) via `.coveragerc`
- Relatório HTML gerado em: `htmlcov/index.html`

## Metodologia de trabalho (quadro de tarefas)

A equipe utilizou um **quadro de tarefas** no padrão Kanban (GitHub Projects / quadro equivalente), com três colunas:

| Coluna | Descrição |
|--------|-----------|
| **Backlog** | Itens planejados para a 2ª entrega |
| **Em andamento** | Itens em desenvolvimento |
| **Concluído** | Itens finalizados e validados |

### Cards / tarefas da 2ª entrega

1. Implementar matching inteligente por habilidades  
2. Atualizar status de candidatura (pendente / aprovada / rejeitada)  
3. Busca de vagas por cidade  
4. Estatísticas do sistema  
5. Expandir e ajustar testes automatizados  
6. Garantir cobertura de testes ≥ 70%  
7. Documentação técnica completa (`docs/documentacao.md`)  
8. Documentar metodologia (`docs/metodologia.md`)  
9. Atualizar README com evolução da 2ª entrega  
10. Gravar vídeo de demonstração (3 a 5 minutos)  
11. Criar tag `v2.0-segunda-entrega`  

O histórico de commits do repositório e os arquivos em `docs/` evidenciam a evolução incremental do trabalho.

Mais detalhes: [docs/metodologia.md](docs/metodologia.md)

## Documentação técnica

Arquitetura, modelagem NoSQL, fluxos e decisões técnicas:  
[docs/documentacao.md](docs/documentacao.md)

## Estrutura do projeto

```
JovemMatch/
├── data/                  # Dados de exemplo (JSON) para o seed
├── docs/
│   ├── documentacao.md    # Documentação técnica completa
│   └── metodologia.md     # Quadro de tarefas / metodologia
├── scripts/
│   └── seed.py            # Popula o banco
├── src/
│   ├── models/            # Classes de domínio (Jovem, Vaga, Candidatura)
│   ├── repositories/      # Acesso ao MongoDB (CRUD)
│   ├── services/          # Regras de negócio
│   ├── database.py
│   ├── config.py
│   └── main.py            # Interface CLI
├── tests/                 # Testes automatizados
├── .coveragerc
├── requirements.txt
└── README.md
```

## Equipe

| RA | Nome |
|----|------|
| 24042002-2 | Heitor Saueressig Mello |
| 24150613-2 | Luiz Eduardo Valério Semensato |
| 24224711-2 | Gabriel Lopes |

## Tags / Versões

- `v1.0-primeira-entrega` – versão inicial (1ª entrega)
- `v2.0-segunda-entrega` – versão final com evolução (2ª entrega)
