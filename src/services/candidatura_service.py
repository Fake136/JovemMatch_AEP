from typing import List, Optional
from src.models.candidatura import Candidatura
from src.repositories.candidatura_repository import CandidaturaRepository
from src.repositories.jovem_repository import JovemRepository
from src.repositories.vaga_repository import VagaRepository


class CandidaturaService:
    def __init__(
        self,
        repository: Optional[CandidaturaRepository] = None,
        jovem_repo: Optional[JovemRepository] = None,
        vaga_repo: Optional[VagaRepository] = None,
    ):
        self.repository = repository or CandidaturaRepository()
        self.jovem_repo = jovem_repo or JovemRepository()
        self.vaga_repo = vaga_repo or VagaRepository()

    def candidatar(self, jovem_id: str, vaga_id: str, mensagem: str = "") -> Candidatura:
        jovem = self.jovem_repo.buscar_por_id(jovem_id)
        if not jovem:
            raise ValueError("Jovem não encontrado")

        vaga = self.vaga_repo.buscar_por_id(vaga_id)
        if not vaga:
            raise ValueError("Vaga não encontrada")
        if not vaga.ativa:
            raise ValueError("Esta vaga não está mais ativa")

        existentes = self.repository.buscar_por_jovem(jovem_id)
        for c in existentes:
            if c.vaga_id == vaga_id:
                raise ValueError("Você já se candidatou a esta vaga")

        candidatura = Candidatura(
            jovem_id=jovem_id,
            vaga_id=vaga_id,
            status="pendente",
            mensagem=mensagem,
        )
        return self.repository.salvar(candidatura)

    def listar_todas(self) -> List[Candidatura]:
        return self.repository.listar_todas()

    def listar_por_jovem(self, jovem_id: str) -> List[Candidatura]:
        return self.repository.buscar_por_jovem(jovem_id)

    def listar_por_vaga(self, vaga_id: str) -> List[Candidatura]:
        return self.repository.buscar_por_vaga(vaga_id)

    def atualizar_status(self, id: str, novo_status: str) -> Optional[Candidatura]:
        status_validos = ["pendente", "aprovada", "rejeitada"]
        if novo_status not in status_validos:
            raise ValueError(f"Status inválido. Use: {status_validos}")

        candidatura = self.repository.buscar_por_id(id)
        if not candidatura:
            return None
        candidatura.status = novo_status
        return self.repository.salvar(candidatura)
