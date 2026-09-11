from typing import List, Optional
from src.repositories.base_repository import BaseRepository
from src.models.candidatura import Candidatura


class CandidaturaRepository(BaseRepository):
    def __init__(self):
        super().__init__("candidaturas")

    def salvar(self, candidatura: Candidatura) -> Candidatura:
        data = candidatura.to_dict()
        if candidatura._id:
            self.update(candidatura._id, data)
        else:
            novo_id = self.insert(data)
            candidatura._id = novo_id
        return candidatura

    def buscar_por_id(self, id: str) -> Optional[Candidatura]:
        doc = self.find_by_id(id)
        if doc:
            return Candidatura.from_dict(doc)
        return None

    def listar_todas(self) -> List[Candidatura]:
        docs = self.find_all()
        return [Candidatura.from_dict(doc) for doc in docs]

    def buscar_por_jovem(self, jovem_id: str) -> List[Candidatura]:
        docs = self.find_all({"jovem_id": jovem_id})
        return [Candidatura.from_dict(doc) for doc in docs]

    def buscar_por_vaga(self, vaga_id: str) -> List[Candidatura]:
        docs = self.find_all({"vaga_id": vaga_id})
        return [Candidatura.from_dict(doc) for doc in docs]

    def remover(self, id: str) -> bool:
        return self.delete(id)
