from typing import Optional, Dict, Any
from datetime import datetime, timezone


class Candidatura:
    def __init__(
        self,
        jovem_id: str,
        vaga_id: str,
        status: str = "pendente",
        mensagem: str = "",
        _id: Optional[str] = None,
        criado_em: Optional[datetime] = None,
    ):
        self._id = _id
        self.jovem_id = jovem_id
        self.vaga_id = vaga_id
        self.status = status
        self.mensagem = mensagem
        self.criado_em = criado_em or datetime.now(timezone.utc)

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "jovem_id": self.jovem_id,
            "vaga_id": self.vaga_id,
            "status": self.status,
            "mensagem": self.mensagem,
            "criado_em": self.criado_em,
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Candidatura":
        return cls(
            _id=str(data["_id"]) if data.get("_id") else None,
            jovem_id=str(data.get("jovem_id", "")),
            vaga_id=str(data.get("vaga_id", "")),
            status=data.get("status", "pendente"),
            mensagem=data.get("mensagem", ""),
            criado_em=data.get("criado_em"),
        )

    def __repr__(self):
        return f"Candidatura(jovem_id={self.jovem_id}, vaga_id={self.vaga_id}, status={self.status})"
