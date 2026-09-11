from src.models.jovem import Jovem
from src.models.vaga import Vaga
from src.models.candidatura import Candidatura
from src.repositories.jovem_repository import JovemRepository
from src.repositories.vaga_repository import VagaRepository
from src.repositories.candidatura_repository import CandidaturaRepository


class TestJovemRepository:
    def test_salvar_e_buscar(self):
        repo = JovemRepository()
        jovem = Jovem(nome="Repo", email="repo@email.com", idade=23, habilidades=["Python"])
        salvo = repo.salvar(jovem)
        assert salvo._id is not None
        buscado = repo.buscar_por_id(salvo._id)
        assert buscado is not None
        assert buscado.nome == "Repo"

    def test_listar(self):
        repo = JovemRepository()
        repo.salvar(Jovem(nome="A", email="a@a.com", idade=20, habilidades=["X"]))
        lista = repo.listar_todos()
        assert len(lista) >= 1


class TestVagaRepository:
    def test_salvar_e_listar_ativas(self):
        repo = VagaRepository()
        vaga = Vaga(titulo="Vaga", empresa="Emp", descricao="Desc", habilidades_requeridas=["Python"])
        salvo = repo.salvar(vaga)
        ativas = repo.listar_ativas()
        assert any(v._id == salvo._id for v in ativas)


class TestCandidaturaRepository:
    def test_salvar(self):
        repo = CandidaturaRepository()
        cand = Candidatura(jovem_id="j1", vaga_id="v1", mensagem="Teste")
        salvo = repo.salvar(cand)
        assert salvo._id is not None
