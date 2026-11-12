from typing import List, Optional, Dict, Any
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

    def matching_por_habilidades(self, jovem_id: str) -> List[Dict[str, Any]]:
        """
        Matching inteligente (2ª entrega):
        sugere vagas ativas com base nas habilidades em comum com o jovem.
        Retorna lista ordenada pela quantidade de habilidades compatíveis.
        """
        jovem = self.jovem_repo.buscar_por_id(jovem_id)
        if not jovem:
            raise ValueError("Jovem não encontrado")

        hab_jovem = {h.strip().lower() for h in (jovem.habilidades or [])}
        if not hab_jovem:
            return []

        resultados = []
        for vaga in self.vaga_repo.listar_ativas():
            hab_vaga = {h.strip().lower() for h in (vaga.habilidades_requeridas or [])}
            comuns = hab_jovem.intersection(hab_vaga)
            if comuns:
                resultados.append({
                    "vaga": vaga,
                    "habilidades_em_comum": sorted(comuns),
                    "score": len(comuns),
                })

        resultados.sort(key=lambda x: x["score"], reverse=True)
        return resultados

    def estatisticas(self) -> Dict[str, Any]:
        """Estatísticas do sistema (2ª entrega)."""
        candidaturas = self.listar_todas()
        por_status = {"pendente": 0, "aprovada": 0, "rejeitada": 0}
        for c in candidaturas:
            if c.status in por_status:
                por_status[c.status] += 1
            else:
                por_status[c.status] = por_status.get(c.status, 0) + 1

        return {
            "total_jovens": len(self.jovem_repo.listar_todos()),
            "total_vagas": len(self.vaga_repo.listar_todas()),
            "vagas_ativas": len(self.vaga_repo.listar_ativas()),
            "total_candidaturas": len(candidaturas),
            "candidaturas_por_status": por_status,
        }
