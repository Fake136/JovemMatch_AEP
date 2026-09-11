from typing import List, Optional, Dict, Any
from datetime import datetime


class Jovem:
    def __init__(
        self,
        nome: str,
        email: str,
        idade: int,
        habilidades: List[str],
        formacao: Optional[Dict[str, Any]] = None,
        experiencia: Optional[List[Dict[str, Any]]] = None,
        cidade: str = "",
        estado: str = "",
        _id: Optional[str] = None,
        criado_em: Optional[datetime] = None,
    ):
        self._id = _id
        self.nome = nome
        self.email = email
        self.idade = idade
        self.habilidades = habilidades or []
        self.formacao = formacao or {}
        self.experiencia = experiencia or []
        self.cidade = cidade
        self.estado = estado
        self.criado_em = criado_em or datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade,
            "habilidades": self.habilidades,
            "formacao": self.formacao,
            "experiencia": self.experiencia,
            "cidade": self.cidade,
            "estado": self.estado,
            "criado_em": self.criado_em,
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Jovem":
        return cls(
            _id=str(data["_id"]) if data.get("_id") else None,
            nome=data.get("nome", ""),
            email=data.get("email", ""),
            idade=data.get("idade", 0),
            habilidades=data.get("habilidades", []),
            formacao=data.get("formacao", {}),
            experiencia=data.get("experiencia", []),
            cidade=data.get("cidade", ""),
            estado=data.get("estado", ""),
            criado_em=data.get("criado_em"),
        )

    def __repr__(self):
        return f"Jovem(nome={self.nome}, email={self.email})"
