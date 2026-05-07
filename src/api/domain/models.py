"""
src/api/domain/models.py
──────────────────────────────
Entités métier du projet Fashion Insta — Cadrage IA.
Couche domaine pure : aucune dépendance externe (pas de pandas, pas de streamlit).
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ── Constantes métier ──────────────────────────────────────────────────────────
HORAS_SEMANA: int = 40
JOURS_PAR_SEMAINE: int = 5


# ── Entités ────────────────────────────────────────────────────────────────────

@dataclass
class Profil:
    """Profil Data interne Fashion Insta (source : P11_Profils_Data.pdf)."""
    nom: str
    initiales: str
    effectif: int
    tjm_eur: float          # TJM individuel €/jour
    categorie: str          # 'Technique' | 'Métier' | 'Conformité'
    description: str

    @property
    def tjm_equipe(self) -> float:
        """Coût journalier total du groupe (TJM × effectif)."""
        return self.tjm_eur * self.effectif

    def cout_phase(self, taux: float, semaines: int) -> float:
        """
        Coût RH de ce profil pour une phase.
        taux     : implication 0.0–1.0
        semaines : durée de la phase en semaines
        """
        return self.tjm_eur * JOURS_PAR_SEMAINE * taux * self.effectif * semaines

    def heures_semaine_individu(self, taux: float) -> float:
        return HORAS_SEMANA * taux

    def heures_semaine_equipe(self, taux: float) -> float:
        return self.heures_semaine_individu(taux) * self.effectif


@dataclass
class Phase:
    """Phase du projet avec durée et livrable clé."""
    id: str             # 'P1' … 'P4'
    nom: str
    semaines: int       # 0 = ongoing (maintenance)
    debut: str          # e.g. 'S1'
    fin: str            # e.g. 'S4' ou 'ongoing'
    livrable_cle: str
    meetings: str = ""  # instances COPIL/COMEX

    @property
    def jours_ouvres(self) -> int:
        return self.semaines * JOURS_PAR_SEMAINE

    @property
    def is_ongoing(self) -> bool:
        return self.semaines == 0


@dataclass
class Implication:
    """
    Taux d'implication (0.0–1.0) d'un profil pour chaque phase.
    taux_par_phase : {'P1': 0.5, 'P2': 1.0, 'P3': 1.0, 'P4': 0.2}
    """
    profil_nom: str
    taux_par_phase: Dict[str, float]
    justifications: Dict[str, str] = field(default_factory=dict)
    # justifications : {'P1': 'Validation archi. — pas plein temps', ...}

    def taux(self, phase_id: str) -> float:
        return self.taux_par_phase.get(phase_id, 0.0)

    def justification(self, phase_id: str) -> str:
        return self.justifications.get(phase_id, "")


@dataclass
class Brique:
    """Brique technique de la solution IA end-to-end."""
    nom: str
    service_azure: str
    fonction_cle: str
    categorie_cout: str     # 'Compute'|'Storage'|'IA/API'|'Sécurité'|'Hors périmètre'
    complexite: Optional[int]  # 1–5  (None si hors périmètre)
    chiffrable: bool = True
    description_detail: str = ""


@dataclass
class RACIEntry:
    """
    Valeur RACI pour un (profil, brique) :
    4=Dév+Valid, 3=Dév, 2=Maint, 1=Valid, 0.5=Superv, 0=Non impliqué.
    """
    profil_nom: str
    brique_nom: str
    valeur: float   # 0 | 0.5 | 1 | 2 | 3 | 4

    EMOJI_MAP = {4.0: "🔨✅", 3.0: "🔨", 2.0: "🔧", 1.0: "✅", 0.5: "👁", 0.0: "—"}
    LABEL_MAP = {
        4.0: "Développement + Validation",
        3.0: "Développement",
        2.0: "Maintenance",
        1.0: "Validation",
        0.5: "Supervision",
        0.0: "Non impliqué",
    }

    @property
    def emoji(self) -> str:
        return self.EMOJI_MAP.get(self.valeur, "?")

    @property
    def label(self) -> str:
        return self.LABEL_MAP.get(self.valeur, "?")


@dataclass
class ServiceRecurrent:
    """Coût récurrent mensuel d'un service Azure en production."""
    nom: str
    categorie: str          # '💻 Compute'|'💾 Storage'|'🤖 IA/API'|'🛡️ Sécurité'|'👥 RH'
    cout_best_eur: float    # €/mois Best Case
    cout_worst_eur: float   # €/mois Worst Case
    justification: str

    @property
    def cout_moyen(self) -> float:
        return (self.cout_best_eur + self.cout_worst_eur) / 2

    @property
    def delta(self) -> float:
        """Écart Best/Worst — indicateur de risque."""
        return self.cout_worst_eur - self.cout_best_eur


@dataclass
class GainMarketing:
    """Gain annuel estimé par le marketing (source : étude interne)."""
    canal: str
    ca_base_eur: float
    taux_croissance: float  # 0.14 = +14%
    horizon_mois: int = 24  # délai avant gain plein

    @property
    def gain_annuel(self) -> float:
        return self.ca_base_eur * self.taux_croissance

    @property
    def gain_mensuel(self) -> float:
        return self.gain_annuel / 12


@dataclass
class ProjetConfig:
    """
    Objet racine regroupant toute la configuration d'un projet cadrage IA.
    Passé au CadrageService pour tous les calculs.
    """
    profils: List[Profil]
    phases: List[Phase]
    implications: List[Implication]
    briques: List[Brique]
    raci: List[RACIEntry]
    services_recurrents: List[ServiceRecurrent]
    gains_marketing: List[GainMarketing]
    nom_projet: str = "Fashion Insta — Recommandation IA"
    partenaire: str = "Microsoft Azure"

    # Index rapides (construits à l'init)
    def __post_init__(self):
        self._profil_map   = {p.nom: p for p in self.profils}
        self._phase_map    = {ph.id: ph for ph in self.phases}
        self._impl_map     = {i.profil_nom: i for i in self.implications}

    def get_profil(self, nom: str) -> Optional[Profil]:
        return self._profil_map.get(nom)

    def get_phase(self, phase_id: str) -> Optional[Phase]:
        return self._phase_map.get(phase_id)

    def get_implication(self, profil_nom: str) -> Optional[Implication]:
        return self._impl_map.get(profil_nom)

    def phases_developpement(self) -> List[Phase]:
        """Phases avec durée définie (hors maintenance ongoing)."""
        return [ph for ph in self.phases if not ph.is_ongoing]