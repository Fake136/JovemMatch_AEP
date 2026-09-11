# Documentação Técnica – JovemMatch

## Arquitetura

- **Models**: Classes de domínio (Jovem, Vaga, Candidatura)
- **Repositories**: Acesso ao MongoDB (CRUD)
- **Services**: Regras de negócio e validações
- **Main**: Interface de linha de comando

## Banco de Dados

- MongoDB local
- Coleções: jovens, vagas, candidaturas
- Documentos complexos e relacionamentos por referência

## Cobertura de testes

```bash
pytest --cov=src --cov-report=term-missing --cov-report=html
```
