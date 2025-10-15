# Bloc ETS – Applications en Python

Ce dépôt regroupe l'ensemble des exercices et projets réalisés dans le cadre du **bloc ETS** du CESI, 
autour des **probabilités, statistiques appliquées et théorie des jeux**.

L'objectif est de mettre en pratique les notions vues en cours à travers des scripts Python 
exploitant notamment `scipy.stats`, `pandas`, `numpy` et `matplotlib`.

---

## Structure du projet

    BoucleETS/
    ├── Statistiques descriptives/
    │   └── PrositStatDesc.py       
    ├── Statistiques SI/
    │   ├── PrositStatiSI.py          
    │   └── server_usage_data.csv     
    ├── Théorie des jeux/
    │   ├── exo_proba.py              
    │   ├── exo_analyse_risque.py     
    │   └── exo_equilibre_nash.py      
    ├── main.py
    ├── LICENSE
    └── README.md

---
## Installation

### Prérequis

- Python 3.8+
- pip ou virtualenv

### Dépendances

Installer les bibliothèques nécessaires :

    pip install numpy scipy matplotlib pandas kagglehub

Ou utiliser l'environnement virtuel du projet :

    # Linux/Mac
    source .venv/bin/activate
    
    # Windows
    .venv\Scripts\activate
    
    pip install -r requirements.txt

---

