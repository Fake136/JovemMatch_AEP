"""
Script de seed - Popula o banco de dados com dados de exemplo.
Execute: python -m scripts.seed
"""

import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.database import get_database, close_connection
from src.models.jovem import Jovem
from src.models.vaga import Vaga
from src.models.candidatura import Candidatura
from src.repositories.jovem_repository import JovemRepository
from src.repositories.vaga_repository import VagaRepository
from src.repositories.candidatura_repository import CandidaturaRepository


def carregar_json(nome_arquivo: str):
    caminho = os.path.join(os.path.dirname(__file__), "..", "data", nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def limpar_colecoes():
    print("Limpando coleções existentes...")
    db = get_database()
    for col in ["jovens", "vagas", "candidaturas"]:
        result = db[col].delete_many({})
        print(f"  - {col}: {result.deleted_count} documento(s) removido(s)")


def popular_jovens() -> list:
    print("\nCadastrando jovens...")
    repo = JovemRepository()
    dados = carregar_json("jovens.json")
    jovens = []
    for item in dados:
        jovem = Jovem(
            nome=item["nome"],
            email=item["email"],
            idade=item["idade"],
            habilidades=item["habilidades"],
            formacao=item.get("formacao", {}),
            experiencia=item.get("experiencia", []),
            cidade=item.get("cidade", ""),
            estado=item.get("estado", ""),
        )
        jovem = repo.salvar(jovem)
        jovens.append(jovem)
        print(f"  [OK] {jovem.nome} (ID: {jovem._id})")
    return jovens


def popular_vagas() -> list:
    print("\nCadastrando vagas...")
    repo = VagaRepository()
    dados = carregar_json("vagas.json")
    vagas = []
    for item in dados:
        vaga = Vaga(
            titulo=item["titulo"],
            empresa=item["empresa"],
            descricao=item["descricao"],
            habilidades_requeridas=item["habilidades_requeridas"],
            salario=item.get("salario"),
            tipo_contrato=item.get("tipo_contrato", "CLT"),
            localizacao=item.get("localizacao", {}),
            ativa=item.get("ativa", True),
        )
        vaga = repo.salvar(vaga)
        vagas.append(vaga)
        print(f"  [OK] {vaga.titulo} - {vaga.empresa} (ID: {vaga._id})")
    return vagas


def popular_candidaturas(jovens: list, vagas: list):
    print("\nCriando candidaturas de exemplo...")
    repo = CandidaturaRepository()

    exemplos = [
        (0, 0, "Tenho experiência com Python e estou motivado!"),
        (1, 1, "Adoro React e quero contribuir com o time."),
        (2, 3, "Experiência prévia com Java e Spring."),
        (3, 2, "Interesse em análise de dados."),
    ]

    for idx_j, idx_v, msg in exemplos:
        cand = Candidatura(
            jovem_id=jovens[idx_j]._id,
            vaga_id=vagas[idx_v]._id,
            status="pendente",
            mensagem=msg,
        )
        cand = repo.salvar(cand)
        print(f"  [OK] {jovens[idx_j].nome} -> {vagas[idx_v].titulo} (ID: {cand._id})")


def main():
    print("=" * 50)
    print("  JovemMatch - Seed do Banco de Dados")
    print("=" * 50)

    try:
        db = get_database()
        db.command("ping")
        print(f"[OK] Conectado ao banco: {db.name}")
    except Exception as e:
        print(f"[ERRO] Falha na conexão com MongoDB: {e}")
        print("Verifique se o MongoDB está rodando (mongodb://localhost:27017)")
        print("E se o arquivo .env está configurado corretamente.")
        return

    limpar_colecoes()
    jovens = popular_jovens()
    vagas = popular_vagas()
    popular_candidaturas(jovens, vagas)

    print("\n" + "=" * 50)
    print("  Seed concluído com sucesso!")
    print(f"  Jovens: {len(jovens)} | Vagas: {len(vagas)} | Candidaturas: 4")
    print("=" * 50)

    close_connection()


if __name__ == "__main__":
    main()
