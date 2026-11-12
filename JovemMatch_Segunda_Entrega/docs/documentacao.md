# Documentação Técnica – JovemMatch (2ª Entrega)

## 1. Objetivo

Prova de Conceito para reduzir barreiras entre jovens e oportunidades de emprego, alinhada ao ODS 8.

## 2. Arquitetura

Arquitetura em camadas (separação de responsabilidades):

```
src/
├── models/          # Domínio (Jovem, Vaga, Candidatura)
├── repositories/    # Acesso ao MongoDB (CRUD)
├── services/        # Regras de negócio
├── database.py      # Conexão MongoDB
├── config.py        # Variáveis de ambiente
└── main.py          # Interface CLI
```

### Fluxo

`main.py` → `Service` → `Repository` → `MongoDB`

## 3. Modelagem NoSQL

### Coleção `jovens`
Documento complexo com objeto aninhado (`formacao`) e lista de subdocumentos (`experiencia`).

### Coleção `vagas`
Documento com `localizacao` aninhada e lista `habilidades_requeridas`.

### Coleção `candidaturas`
Relacionamento por referência (`jovem_id`, `vaga_id`) e campo `status`.

## 4. Funcionalidades da 2ª entrega

### Matching inteligente
Compara habilidades do jovem com as requeridas nas vagas ativas e ordena por score (quantidade de habilidades em comum).

### Atualização de status
Permite alterar candidatura para `pendente`, `aprovada` ou `rejeitada`.

### Busca por cidade
Filtra vagas ativas pela cidade informada.

### Estatísticas
Totais de jovens, vagas, vagas ativas e candidaturas agrupadas por status.

## 5. Testes

- Framework: pytest + pytest-cov + mongomock
- Execução: `pytest --cov=src --cov-report=term-missing`
- `src/main.py` é omitido da cobertura (interface interativa)

## 6. Como reproduzir a cobertura

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```

O relatório HTML fica em `htmlcov/index.html`.

## 7. Decisões técnicas

- MongoDB Atlas para facilitar avaliação (sem instalar servidor local)
- Seed com dados de exemplo em `data/` + `scripts/seed.py`
- OOP com Models, Repositories e Services
- Validação de regras de negócio na camada Service
