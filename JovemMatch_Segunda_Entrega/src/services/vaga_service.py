from typing import List, Optional
from src.models.vaga import Vaga
from src.repositories.vaga_repository import VagaRepository


class VagaService:
    def __init__(self, repository: Optional[VagaRepository] = None):
        self.repository = repository or VagaRepository()

    def cadastrar(
        self,
        titulo: str,
        empresa: str,
        descricao: str,
        habilidades_requeridas: List[str],
        salario: float = None,
        tipo_contrato: str = "CLT",
        localizacao: dict = None,
    ) -> Vaga:
        if not titulo or not titulo.strip():
            raise ValueError("Título da vaga é obrigatório")
        if not empresa or not empresa.strip():
            raise ValueError("Nome da empresa é obrigatório")
        if not habilidades_requeridas:
            raise ValueError("É necessário informar ao menos uma habilidade requerida")

        vaga = Vaga(
            titulo=titulo.strip(),
            empresa=empresa.strip(),
            descricao=descricao.strip() if descricao else "",
            habilidades_requeridas=habilidades_requeridas,
            salario=salario,
            tipo_contrato=tipo_contrato,
            localizacao=localizacao or {},
            ativa=True,
        )
        return self.repository.salvar(vaga)

    def buscar_por_id(self, id: str) -> Optional[Vaga]:
        return self.repository.buscar_por_id(id)

    def listar_todas(self) -> List[Vaga]:
        return self.repository.listar_todas()

    def listar_ativas(self) -> List[Vaga]:
        return self.repository.listar_ativas()

    def buscar_por_habilidade(self, habilidade: str) -> List[Vaga]:
        return self.repository.buscar_por_habilidade(habilidade)

    def buscar_por_cidade(self, cidade: str) -> List[Vaga]:
        """Busca vagas ativas por cidade (filtro avançado - 2ª entrega)."""
        cidade_norm = cidade.strip().lower()
        return [
            v for v in self.listar_ativas()
            if (v.localizacao or {}).get("cidade", "").lower() == cidade_norm
        ]

    def buscar_por_empresa(self, empresa: str) -> List[Vaga]:
        """Busca vagas por nome da empresa (filtro avançado - 2ª entrega)."""
        emp_norm = empresa.strip().lower()
        return [
            v for v in self.listar_ativas()
            if emp_norm in (v.empresa or "").lower()
        ]

    def remover(self, id: str) -> bool:
        return self.repository.remover(id)
