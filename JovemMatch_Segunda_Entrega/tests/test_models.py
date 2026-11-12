from src.models.jovem import Jovem
from src.models.vaga import Vaga
from src.models.candidatura import Candidatura


class TestJovem:
    def test_criar_jovem(self):
        jovem = Jovem(nome="Teste", email="teste@email.com", idade=20, habilidades=["Python"])
        assert jovem.nome == "Teste"
        assert jovem.email == "teste@email.com"
        assert "Python" in jovem.habilidades

    def test_to_dict(self):
        jovem = Jovem(nome="Ana", email="ana@email.com", idade=22, habilidades=["Python", "SQL"])
        data = jovem.to_dict()
        assert data["nome"] == "Ana"
        assert data["habilidades"] == ["Python", "SQL"]

    def test_from_dict(self):
        data = {"_id": "abc123", "nome": "Bruno", "email": "bruno@email.com", "idade": 19, "habilidades": ["JS"]}
        jovem = Jovem.from_dict(data)
        assert jovem._id == "abc123"
        assert jovem.nome == "Bruno"


class TestVaga:
    def test_criar_vaga(self):
        vaga = Vaga(titulo="Dev Python", empresa="Tech", descricao="Vaga júnior", habilidades_requeridas=["Python"], salario=3000.0)
        assert vaga.titulo == "Dev Python"
        assert vaga.ativa is True

    def test_to_dict_from_dict(self):
        vaga = Vaga(titulo="Frontend", empresa="Web", descricao="React", habilidades_requeridas=["React"])
        data = vaga.to_dict()
        vaga2 = Vaga.from_dict(data)
        assert vaga2.titulo == "Frontend"


class TestCandidatura:
    def test_criar_candidatura(self):
        cand = Candidatura(jovem_id="j1", vaga_id="v1", mensagem="Olá!")
        assert cand.status == "pendente"
        assert cand.mensagem == "Olá!"
