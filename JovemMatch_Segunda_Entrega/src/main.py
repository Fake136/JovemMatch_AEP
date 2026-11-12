"""
JovemMatch - Prova de Conceito
ODS 8: Trabalho decente e crescimento econômico
Segunda Entrega - AEP 2026.2 6S
"""

from src.services.jovem_service import JovemService
from src.services.vaga_service import VagaService
from src.services.candidatura_service import CandidaturaService
from src.database import get_database, close_connection


def exibir_menu():
    print("\n" + "=" * 55)
    print("       JOVEMMATCH - Sistema de Emprego Jovem")
    print("       ODS 8 - Trabalho Decente | 2ª Entrega")
    print("=" * 55)
    print("1.  Cadastrar Jovem")
    print("2.  Listar Jovens")
    print("3.  Cadastrar Vaga")
    print("4.  Listar Vagas Ativas")
    print("5.  Candidatar-se a uma Vaga")
    print("6.  Listar Candidaturas")
    print("7.  Buscar Jovens por Habilidade")
    print("8.  Matching inteligente (vagas para jovem)")
    print("9.  Atualizar status de candidatura")
    print("10. Buscar vagas por cidade")
    print("11. Estatísticas do sistema")
    print("0.  Sair")
    print("=" * 55)


def cadastrar_jovem(service: JovemService):
    print("\n--- Cadastro de Jovem ---")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    idade = int(input("Idade (15-29): ").strip())
    habilidades = input("Habilidades (separadas por vírgula): ").strip()
    lista_hab = [h.strip() for h in habilidades.split(",") if h.strip()]
    cidade = input("Cidade: ").strip()
    estado = input("Estado (sigla): ").strip()
    try:
        jovem = service.cadastrar(
            nome=nome, email=email, idade=idade,
            habilidades=lista_hab, cidade=cidade, estado=estado,
        )
        print(f"\n[OK] Jovem cadastrado! ID: {jovem._id}")
    except ValueError as e:
        print(f"\n[ERRO] {e}")


def listar_jovens(service: JovemService):
    print("\n--- Lista de Jovens ---")
    jovens = service.listar_todos()
    if not jovens:
        print("Nenhum jovem cadastrado.")
        return
    for j in jovens:
        print(f"\nID: {j._id}")
        print(f"  Nome: {j.nome} | Idade: {j.idade} | E-mail: {j.email}")
        print(f"  Habilidades: {', '.join(j.habilidades)}")
        print(f"  Local: {j.cidade}/{j.estado}")


def cadastrar_vaga(service: VagaService):
    print("\n--- Cadastro de Vaga ---")
    titulo = input("Título da vaga: ").strip()
    empresa = input("Empresa: ").strip()
    descricao = input("Descrição: ").strip()
    habilidades = input("Habilidades requeridas (separadas por vírgula): ").strip()
    lista_hab = [h.strip() for h in habilidades.split(",") if h.strip()]
    salario_str = input("Salário (opcional, Enter para pular): ").strip()
    salario = float(salario_str) if salario_str else None
    cidade = input("Cidade: ").strip()
    estado = input("Estado (sigla): ").strip()
    try:
        vaga = service.cadastrar(
            titulo=titulo, empresa=empresa, descricao=descricao,
            habilidades_requeridas=lista_hab, salario=salario,
            localizacao={"cidade": cidade, "estado": estado},
        )
        print(f"\n[OK] Vaga cadastrada! ID: {vaga._id}")
    except ValueError as e:
        print(f"\n[ERRO] {e}")


def listar_vagas(service: VagaService):
    print("\n--- Vagas Ativas ---")
    vagas = service.listar_ativas()
    if not vagas:
        print("Nenhuma vaga ativa.")
        return
    for v in vagas:
        print(f"\nID: {v._id}")
        print(f"  {v.titulo} - {v.empresa}")
        print(f"  Habilidades: {', '.join(v.habilidades_requeridas)}")
        loc = v.localizacao or {}
        print(f"  Local: {loc.get('cidade', '')}/{loc.get('estado', '')}")
        if v.salario:
            print(f"  Salário: R$ {v.salario:,.2f}")


def candidatar(service: CandidaturaService):
    print("\n--- Nova Candidatura ---")
    jovem_id = input("ID do Jovem: ").strip()
    vaga_id = input("ID da Vaga: ").strip()
    mensagem = input("Mensagem (opcional): ").strip()
    try:
        cand = service.candidatar(jovem_id=jovem_id, vaga_id=vaga_id, mensagem=mensagem)
        print(f"\n[OK] Candidatura realizada! ID: {cand._id} | Status: {cand.status}")
    except ValueError as e:
        print(f"\n[ERRO] {e}")


def listar_candidaturas(service: CandidaturaService):
    print("\n--- Lista de Candidaturas ---")
    cands = service.listar_todas()
    if not cands:
        print("Nenhuma candidatura registrada.")
        return
    for c in cands:
        print(f"\nID: {c._id}")
        print(f"  Jovem ID: {c.jovem_id}")
        print(f"  Vaga ID:  {c.vaga_id}")
        print(f"  Status:   {c.status}")
        if c.mensagem:
            print(f"  Mensagem: {c.mensagem}")


def buscar_por_habilidade(service: JovemService):
    print("\n--- Buscar Jovens por Habilidade ---")
    habilidade = input("Habilidade: ").strip()
    jovens = service.buscar_por_habilidade(habilidade)
    if not jovens:
        print(f"Nenhum jovem encontrado com a habilidade '{habilidade}'.")
        return
    print(f"\nJovens com '{habilidade}':")
    for j in jovens:
        print(f"  - {j.nome} ({j.email}) - {', '.join(j.habilidades)}")


def matching(service: CandidaturaService):
    print("\n--- Matching Inteligente ---")
    jovem_id = input("ID do Jovem: ").strip()
    try:
        resultados = service.matching_por_habilidades(jovem_id)
        if not resultados:
            print("Nenhuma vaga compatível encontrada.")
            return
        print(f"\nVagas sugeridas ({len(resultados)}):")
        for item in resultados:
            v = item["vaga"]
            print(f"\n  Score: {item['score']} | {v.titulo} - {v.empresa}")
            print(f"  Habilidades em comum: {', '.join(item['habilidades_em_comum'])}")
            print(f"  ID da vaga: {v._id}")
    except ValueError as e:
        print(f"\n[ERRO] {e}")


def atualizar_status(service: CandidaturaService):
    print("\n--- Atualizar Status da Candidatura ---")
    cand_id = input("ID da Candidatura: ").strip()
    print("Status possíveis: pendente | aprovada | rejeitada")
    novo = input("Novo status: ").strip().lower()
    try:
        cand = service.atualizar_status(cand_id, novo)
        if not cand:
            print("[ERRO] Candidatura não encontrada.")
            return
        print(f"\n[OK] Status atualizado para: {cand.status}")
    except ValueError as e:
        print(f"\n[ERRO] {e}")


def buscar_vagas_cidade(service: VagaService):
    print("\n--- Buscar Vagas por Cidade ---")
    cidade = input("Cidade: ").strip()
    vagas = service.buscar_por_cidade(cidade)
    if not vagas:
        print(f"Nenhuma vaga ativa em '{cidade}'.")
        return
    print(f"\nVagas em {cidade}:")
    for v in vagas:
        print(f"  - {v.titulo} ({v.empresa}) | ID: {v._id}")


def estatisticas(service: CandidaturaService):
    print("\n--- Estatísticas do Sistema ---")
    stats = service.estatisticas()
    print(f"  Total de jovens:        {stats['total_jovens']}")
    print(f"  Total de vagas:         {stats['total_vagas']}")
    print(f"  Vagas ativas:           {stats['vagas_ativas']}")
    print(f"  Total de candidaturas:  {stats['total_candidaturas']}")
    print("  Candidaturas por status:")
    for status, qtd in stats["candidaturas_por_status"].items():
        print(f"    - {status}: {qtd}")


def main():
    try:
        db = get_database()
        db.command("ping")
        print("[OK] Conectado ao MongoDB com sucesso!")
    except Exception as e:
        print(f"[ERRO] Não foi possível conectar ao MongoDB: {e}")
        print("Verifique o arquivo .env e se o MongoDB/Atlas está acessível.")
        return

    jovem_service = JovemService()
    vaga_service = VagaService()
    candidatura_service = CandidaturaService()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_jovem(jovem_service)
        elif opcao == "2":
            listar_jovens(jovem_service)
        elif opcao == "3":
            cadastrar_vaga(vaga_service)
        elif opcao == "4":
            listar_vagas(vaga_service)
        elif opcao == "5":
            candidatar(candidatura_service)
        elif opcao == "6":
            listar_candidaturas(candidatura_service)
        elif opcao == "7":
            buscar_por_habilidade(jovem_service)
        elif opcao == "8":
            matching(candidatura_service)
        elif opcao == "9":
            atualizar_status(candidatura_service)
        elif opcao == "10":
            buscar_vagas_cidade(vaga_service)
        elif opcao == "11":
            estatisticas(candidatura_service)
        elif opcao == "0":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

    close_connection()


if __name__ == "__main__":
    main()
