import pytest
from src.services.jovem_service import JovemService
from src.services.vaga_service import VagaService
from src.services.candidatura_service import CandidaturaService


class TestJovemService:
    def test_cadastrar_sucesso(self):
        service = JovemService()
        jovem = service.cadastrar(nome="Maria", email="maria@email.com", idade=21, habilidades=["Python"])
        assert jovem._id is not None
        assert jovem.nome == "Maria"

    def test_idade_invalida(self):
        service = JovemService()
        with pytest.raises(ValueError, match="Idade deve estar entre 15 e 29"):
            service.cadastrar(nome="Idoso", email="idoso@email.com", idade=40, habilidades=["Java"])

    def test_email_invalido(self):
        service = JovemService()
        with pytest.raises(ValueError, match="E-mail inválido"):
            service.cadastrar(nome="Sem", email="sememail", idade=20, habilidades=["Python"])

    def test_email_duplicado(self):
        service = JovemService()
        service.cadastrar(nome="Primeiro", email="dup@email.com", idade=20, habilidades=["Python"])
        with pytest.raises(ValueError, match="Já existe um jovem"):
            service.cadastrar(nome="Segundo", email="dup@email.com", idade=22, habilidades=["Java"])

    def test_buscar_por_habilidade(self):
        service = JovemService()
        service.cadastrar(nome="Dev", email="dev@email.com", idade=22, habilidades=["Python", "Git"])
        lista = service.buscar_por_habilidade("Python")
        assert len(lista) >= 1


class TestVagaService:
    def test_cadastrar_sucesso(self):
        service = VagaService()
        vaga = service.cadastrar(titulo="Dev Python", empresa="Emp", descricao="Desc", habilidades_requeridas=["Python"])
        assert vaga._id is not None
        assert vaga.ativa is True

    def test_sem_habilidades(self):
        service = VagaService()
        with pytest.raises(ValueError, match="habilidade"):
            service.cadastrar(titulo="Vaga", empresa="Emp", descricao="Desc", habilidades_requeridas=[])

    def test_buscar_por_cidade(self):
        service = VagaService()
        service.cadastrar(
            titulo="Dev", empresa="Emp", descricao="D",
            habilidades_requeridas=["Python"],
            localizacao={"cidade": "Maringá", "estado": "PR"},
        )
        lista = service.buscar_por_cidade("Maringá")
        assert len(lista) >= 1

    def test_buscar_por_empresa(self):
        service = VagaService()
        service.cadastrar(titulo="Dev", empresa="TechInova", descricao="D", habilidades_requeridas=["Python"])
        lista = service.buscar_por_empresa("Tech")
        assert len(lista) >= 1


class TestCandidaturaService:
    def test_candidatar_sucesso(self):
        jovem_svc = JovemService()
        vaga_svc = VagaService()
        cand_svc = CandidaturaService()

        jovem = jovem_svc.cadastrar(nome="Cand", email="cand@email.com", idade=22, habilidades=["Python"])
        vaga = vaga_svc.cadastrar(titulo="Vaga", empresa="Emp", descricao="Desc", habilidades_requeridas=["Python"])

        cand = cand_svc.candidatar(jovem_id=jovem._id, vaga_id=vaga._id, mensagem="Quero!")
        assert cand._id is not None
        assert cand.status == "pendente"

    def test_jovem_inexistente(self):
        cand_svc = CandidaturaService()
        with pytest.raises(ValueError, match="Jovem não encontrado"):
            cand_svc.candidatar(jovem_id="000000000000000000000000", vaga_id="000000000000000000000001")

    def test_atualizar_status(self):
        jovem_svc = JovemService()
        vaga_svc = VagaService()
        cand_svc = CandidaturaService()

        jovem = jovem_svc.cadastrar(nome="St", email="st@email.com", idade=20, habilidades=["JS"])
        vaga = vaga_svc.cadastrar(titulo="V", empresa="E", descricao="D", habilidades_requeridas=["JS"])
        cand = cand_svc.candidatar(jovem_id=jovem._id, vaga_id=vaga._id)

        atualizada = cand_svc.atualizar_status(cand._id, "aprovada")
        assert atualizada is not None
        assert atualizada.status == "aprovada"

    def test_status_invalido(self):
        cand_svc = CandidaturaService()
        with pytest.raises(ValueError, match="Status inválido"):
            cand_svc.atualizar_status("000000000000000000000000", "xyz")

    def test_matching_por_habilidades(self):
        jovem_svc = JovemService()
        vaga_svc = VagaService()
        cand_svc = CandidaturaService()

        jovem = jovem_svc.cadastrar(
            nome="Match", email="match@email.com", idade=23,
            habilidades=["Python", "SQL", "Git"],
        )
        vaga_svc.cadastrar(titulo="Python Dev", empresa="A", descricao="D", habilidades_requeridas=["Python", "SQL"])
        vaga_svc.cadastrar(titulo="Java Dev", empresa="B", descricao="D", habilidades_requeridas=["Java"])

        resultados = cand_svc.matching_por_habilidades(jovem._id)
        assert len(resultados) >= 1
        assert resultados[0]["score"] >= 1
        assert "python" in [h.lower() for h in resultados[0]["habilidades_em_comum"]]

    def test_estatisticas(self):
        jovem_svc = JovemService()
        vaga_svc = VagaService()
        cand_svc = CandidaturaService()

        jovem_svc.cadastrar(nome="E1", email="e1@email.com", idade=20, habilidades=["Python"])
        vaga_svc.cadastrar(titulo="V1", empresa="E", descricao="D", habilidades_requeridas=["Python"])

        stats = cand_svc.estatisticas()
        assert stats["total_jovens"] >= 1
        assert stats["total_vagas"] >= 1
        assert "candidaturas_por_status" in stats
