# 🛡️ Fashion Insta — Étude financière et Analyse des Risques RGPD

<div align="left">
  <img src="docs/images/fashion_insta_logo.png" width="200px" alt="Logo Fashion Insta">
</div>


**Analyse des risques d’un système d’IA appliqué au retail fashion.**

Ce repository contient plusieurs notebooks Jupyter permettant de construire progressivement une démarche complète de gouvernance, conformité RGPD, gestion des risques et pilotage d’un projet IA multimodal basé sur Azure OpenAI.

## 📂 Documentation du projet

| Partie         | Description                                                                                                                                                                                                              | 
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Support de Presentation** | Développement d’une application mobile de recommandation d’articles vestimentaires basée sur des photos   <br/>[M9_Realisez_le_cadrage_d_un_projet_IA.pptx.pdf](docs/M9_Realisez_le_cadrage_d_un_projet_IA.pptx.pdf)     |
| **Notebooks 1/2** | Étude financière, organisationnelle & ROI du projet IA Fashion Insta                                                <br/>[01_FashionInsta_Cadrage_Projet_Couts_ROI.ipynb](notebooks/01_FashionInsta_Cadrage_Projet_Couts_ROI.ipynb) |  
| **Notebooks 2/2** | Analyse des Risques IA & RGPD                                                                                       <br/>[02_FashionInsta_Analyse_Risques.ipynb](notebooks/02_FashionInsta_Analyse_Risques.ipynb)      |  

---

# 🎯 Objectifs du projet

Le projet simule la mise en œuvre d’une plateforme IA de type **Fashion Insta** intégrant :

* recherche visuelle (Visual Search)
* recommandations intelligentes
* Virtual Try-On
* IA générative multimodale
* pipelines MLOps Azure
* gouvernance RGPD et conformité IA

L’objectif principal est de démontrer comment structurer un projet IA moderne :

* identification des risques
* analyse réglementaire
* priorisation de criticité
* plans de prévention
* reporting exécutif
* pilotage continu des risques

---

# 📚 Contenu des notebooks

## 📘 01 — Étude financière, organisationnelle & ROI du projet IA Fashion Insta

Premier notebook consacré à la structuration opérationnelle et financière du projet.

Il permet de modéliser les coûts, les ressources humaines, les responsabilités et la rentabilité prévisionnelle d’une plateforme IA multimodale appliquée au retail fashion.

### 📋 Contenu principal

#### Section 1 — Profils & TJM

* définition des rôles projet
* taux journaliers moyens (TJM)
* répartition des expertises
* estimation des charges humaines

#### Section 2 — Implication croisée : Profil × Phase

* matrice d’implication des équipes
* allocation des ressources par phase

#### Section 3 — Coûts RH détaillés par phase
* coûts détaillés par profil

#### Section 4 — Matrice RACI
#### Section 5 — Coûts récurrents mensuels (Production)
#### Section 6 — ROI & Projection de rentabilité
#### Section 7 — Synthèse exécutive COMEX

Ce notebook sert de base financière, organisationnelle et stratégique au projet.
---

## 📙 02 — Analyse des Risques IA & RGPD

Notebook principal de gouvernance et gestion des risques.

Il couvre l’intégralité du cycle d’analyse :

### 📋 Étape 1 — Description du projet

* QQOQCCP
* périmètre fonctionnel
* analyse SWOT / FFOM
* cartographie des acteurs
* architecture générale

### 🔎 Étape 2 — Identification des risques

* grille Spectre 7D
* inventaire des risques
* analyse données personnelles
* analyse confidentialité
* risques IA générative
* risques réglementaires

### 🎯 Étape 3 — Priorisation par criticité

* matrices Probabilité × Gravité
* cartographie visuelle des risques
* calculs AMDEC
* scoring des impacts
* classification des risques critiques

### 🛡️ Étape 4 — Plan de prévention

* stratégies de mitigation
* mesures correctives
* conformité RGPD
* gouvernance des données
* sécurité cloud Azure
* monitoring IA

### 📡 Étape 5 — Suivi continu

* reporting projet
* tableaux de bord
* radar de criticité
* évolution temporelle des risques
* synthèse exécutive COMEX

---

# 🧱 Technologies utilisées

## Data / IA

* Python
* Pandas
* NumPy
* Scikit-learn
* Azure OpenAI
* GPT-4V
* MLflow
* Azure ML Studio

## Visualisation

* Matplotlib
* HTML/CSS dans notebooks
* DataFrames stylisés
* Dashboards analytiques

## Gouvernance / Conformité

* RGPD
* EU AI Act
* Azure Purview
* RBAC
* anonymisation des données

---

# 📊 Livrables générés

Les notebooks produisent différents livrables de gouvernance :

* matrices SWOT
* matrices de criticité
* AMDEC
* inventaires des risques
* plans de prévention
* reporting exécutif
* dashboards visuels
* synthèses stratégiques

---

# 📁 Structure du repository

```text
.
├── docs/                 # Documentation projet
├── notebooks/            # Notebooks Jupyter
├── references/           # Sources et références
├── src/                  # Code source Python
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# 🚀 Installation

## Cloner le projet

```bash
git clone https://github.com/racemartin/m9_ocr.git
cd m9_ocr
```

## Créer un environnement virtuel

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

# 📦 Installation des dépendances

## Installation avec uv

```bash
uv sync
```

ou pour installer le projet en mode développement :

```bash
uv pip install -e .
```

---

# ▶️ Lancer Jupyter

```bash
uv run jupyter lab --no-browser --ip=0.0.0.0
```


Puis dans le navigateur ouvrir les notebooks dans le dossier :

```text
notebooks/
```

---

---

# ⚠️ Avertissement


Les données, scénarios et analyses peuvent contenir des éléments fictifs destinés à illustrer des problématiques réelles de gouvernance IA.

---

## 👤 Auteur

**Rafael Cerezo Martín**

* Email: [rafael.cerezo.martin@icloud.com](mailto:rafael.cerezo.martin@icloud.com)
* GitHub: [@racemartin](https://github.com/racemartin)

## 📄 Licence

MIT License - voir le fichier [LICENSE](https://www.google.com/search?q=LICENSE) pour plus de détails.

