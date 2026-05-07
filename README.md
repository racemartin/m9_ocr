# 🛡️ Fashion Insta — Analyse des Risques IA & RGPD

<div align="left">
  <img src="docs/images/fashion_insta_logo" width="200px" alt="Logo Fashion Insta">
</div>


Analyse des risques d’un système d’IA appliqué au retail fashion.

Ce repository contient plusieurs notebooks Jupyter permettant de construire progressivement une démarche complète de gouvernance, conformité RGPD, gestion des risques et pilotage d’un projet IA multimodal basé sur Azure OpenAI.


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

## 📘 01 — Étude du projet IA Fashion Insta

Notebook d’introduction présentant :

* le contexte métier
* l’architecture cible
* les enjeux IA
* les contraintes cloud Azure
* les problématiques RGPD
* les objectifs business
* les indicateurs de succès

Ce notebook sert de base documentaire au projet.

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
├── data/                 # Jeux de données
├── docs/                 # Documentation projet
├── models/               # Modèles IA
├── notebooks/            # Notebooks Jupyter
├── references/           # Sources et références
├── reports/              # Rapports générés
├── src/                  # Code source Python
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# 🚀 Installation

## Cloner le projet

```bash
git clone <repo-url>
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

