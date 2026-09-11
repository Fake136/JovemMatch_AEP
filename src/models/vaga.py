from typing import List, Optional, Dict, Any
from datetime import datetime


class Vaga:
    def __init__(
        self,
        titulo: str,
        empresa: str,
        descricao: str,
        habilidades_requeridas: List[str],
        salario: Optional[float] = None,
        tipo_contrato: str = "CLT",
        localizacao: Optional[Dict[str, str]] = None,
        ativa: bool = True,
        _id: Optional[str] = None,
        criado_em: Optional[datetime] = None,
    ):
        self._id = _id
        self.titulo = titulo
        self.empresa = empresa
        self.descricao = descricao
        self.habilidades_requeridas = habilidades_requeridas or []
        self.salario = salario
        self.tipo_contrato = tipo_contrato
        self.localizacao = localizacao or {}
        self.ativa = ativa
        self.criado_em = criado_em or datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "titulo": self.titulo,
            "empresa": self.empresa,
            "descricao": self.descricao,
            "habilidades_requeridas": self.habilidades_requeridas,
            "salario": self.salario,
            "tipo_contrato": self.tipo_contrato,
            "localizacao": self.localizacao,
            "ativa": self.ativa,
            "criado_em": self.criado_em,
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Vaga":
        return cls(
            _id=str(data["_id"]) if data.get("_id") else None,
            titulo=data.get("titulo", ""),
            empresa=data.get("empresa", ""),
            descricao=data.get("descricao", ""),
            habilidades_requeridas=data.get("habilidades_requeridas", []),
            salario=data.get("salario"),
            tipo_contrato=data.get("tipo_contrato", "CLT"),
            localizacao=data.get("localizacao", {}),
            ativa=data.get("ativa", True),
            criado_em=data.get("criado_em"),
        )

    def __repr__(self):
        return f"Vaga(titulo={self.titulo}, empresa={self.empresa})"
