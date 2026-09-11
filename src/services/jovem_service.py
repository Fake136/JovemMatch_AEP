from typing import List, Optional
from src.models.jovem import Jovem
from src.repositories.jovem_repository import JovemRepository


class JovemService:
    def __init__(self, repository: Optional[JovemRepository] = None):
        self.repository = repository or JovemRepository()

    def cadastrar(
        self,
        nome: str,
        email: str,
        idade: int,
        habilidades: List[str],
        formacao: dict = None,
        experiencia: list = None,
        cidade: str = "",
        estado: str = "",
    ) -> Jovem:
        if not nome or not nome.strip():
            raise ValueError("Nome é obrigatório")
        if not email or "@" not in email:
            raise ValueError("E-mail inválido")
        if idade < 15 or idade > 29:
            raise ValueError("Idade deve estar entre 15 e 29 anos (público-alvo)")

        existente = self.repository.buscar_por_email(email)
        if existente:
            raise ValueError(f"Já existe um jovem cadastrado com o e-mail {email}")

        jovem = Jovem(
            nome=nome.strip(),
            email=email.strip().lower(),
            idade=idade,
            habilidades=habilidades or [],
            formacao=formacao or {},
            experiencia=experiencia or [],
            cidade=cidade,
            estado=estado,
        )
        return self.repository.salvar(jovem)

    def buscar_por_id(self, id: str) -> Optional[Jovem]:
        return self.repository.buscar_por_id(id)

    def listar_todos(self) -> List[Jovem]:
        return self.repository.listar_todos()

    def buscar_por_habilidade(self, habilidade: str) -> List[Jovem]:
        return self.repository.buscar_por_habilidade(habilidade)

    def remover(self, id: str) -> bool:
        return self.repository.remover(id)
