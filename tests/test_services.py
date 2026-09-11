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
