from typing import List, Optional
from src.repositories.base_repository import BaseRepository
from src.models.jovem import Jovem


class JovemRepository(BaseRepository):
    def __init__(self):
        super().__init__("jovens")

    def salvar(self, jovem: Jovem) -> Jovem:
        data = jovem.to_dict()
        if jovem._id:
            self.update(jovem._id, data)
        else:
            novo_id = self.insert(data)
            jovem._id = novo_id
        return jovem

    def buscar_por_id(self, id: str) -> Optional[Jovem]:
        doc = self.find_by_id(id)
        if doc:
            return Jovem.from_dict(doc)
        return None

    def listar_todos(self) -> List[Jovem]:
        docs = self.find_all()
        return [Jovem.from_dict(doc) for doc in docs]

    def buscar_por_email(self, email: str) -> Optional[Jovem]:
        docs = self.find_all({"email": email})
        if docs:
            return Jovem.from_dict(docs[0])
        return None

    def buscar_por_habilidade(self, habilidade: str) -> List[Jovem]:
        docs = self.find_all({"habilidades": habilidade})
        return [Jovem.from_dict(doc) for doc in docs]

    def remover(self, id: str) -> bool:
        return self.delete(id)
