from typing import List, Optional
from src.repositories.base_repository import BaseRepository
from src.models.vaga import Vaga


class VagaRepository(BaseRepository):
    def __init__(self):
        super().__init__("vagas")

    def salvar(self, vaga: Vaga) -> Vaga:
        data = vaga.to_dict()
        if vaga._id:
            self.update(vaga._id, data)
        else:
            novo_id = self.insert(data)
            vaga._id = novo_id
        return vaga

    def buscar_por_id(self, id: str) -> Optional[Vaga]:
        doc = self.find_by_id(id)
        if doc:
            return Vaga.from_dict(doc)
        return None

    def listar_todas(self) -> List[Vaga]:
        docs = self.find_all()
        return [Vaga.from_dict(doc) for doc in docs]

    def listar_ativas(self) -> List[Vaga]:
        docs = self.find_all({"ativa": True})
        return [Vaga.from_dict(doc) for doc in docs]

    def buscar_por_habilidade(self, habilidade: str) -> List[Vaga]:
        docs = self.find_all({"habilidades_requeridas": habilidade, "ativa": True})
        return [Vaga.from_dict(doc) for doc in docs]

    def remover(self, id: str) -> bool:
        return self.delete(id)
