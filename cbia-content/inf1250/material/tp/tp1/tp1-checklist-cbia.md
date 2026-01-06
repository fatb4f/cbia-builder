# INF1250 — TP1 — CBIA Checklist (conformité et exécution)

> Objectif : vérifier la **conformité au TP1** selon la feuille de route et l’énoncé.  
> Ce document **n’ajoute aucun contenu** et ne remplace pas les réponses.

---

## A. Conformité du dépôt
- [ ] **Un seul fichier** remis (PDF ou DOC/DOCX)
- [ ] **Aucune archive** (zip/tar/rar)
- [ ] Réponses présentées **dans l’ordre** des questions
- [ ] **Numérotation claire** (Q1, Q2, Q3 et sous-parties)

---

## B. Question 1 — Modèle relationnel (M2)
- [ ] Les **entités imposées** (Utilisateur, Amitié) sont présentes
- [ ] Chaque relation est donnée sous la forme : `Relation(attributs)`
- [ ] **Clé primaire (PK)** identifiée pour chaque relation
- [ ] **Clés étrangères (FK)** identifiées et cohérentes
- [ ] Les hypothèses sont **minimales** et explicitement indiquées
- [ ] Aucun attribut inventé sans justification

---

## C. Question 2 — Clé et algèbre relationnelle (M2)
### 2.1 Clé de la relation Location
- [ ] Une **clé unique** est proposée
- [ ] La justification est **courte et logique** (pas de SQL)

### 2.2 Opérations algébriques
- [ ] `UNION(Location1, Location2)` respecte la **compatibilité des schémas**
- [ ] `PROJECT(Location1, idClient, idVoiture, DateLocation)` est correcte
- [ ] Les résultats (tables) utilisent **uniquement les attributs demandés**
- [ ] Aucun identifiant ou donnée non fournie n’est inventé

---

## D. Question 3 — Expressions en algèbre relationnelle (M2)
> Les **expressions** sont exigées (pas les résultats).

### 3.1 Clients après le 1er mars 2012
- [ ] Sélection par date correcte
- [ ] Jointures nécessaires explicites
- [ ] Projection finale : Nom, Prénom, adresseCourriel

### 3.2 Voitures (> 100 000 km OU année < 2007)
- [ ] Condition logique correcte (OU)
- [ ] Projection : idVoiture, Année, Kilométrage

### 3.3 Toutes les locations, inclure voitures manquantes
- [ ] **Jointure externe** explicitement utilisée
- [ ] Filtre `DateLocation > 01-03-2012` appliqué
- [ ] Tous les attributs demandés présents

### 3.4 Nombre de locations par client
- [ ] Groupement correct (par client)
- [ ] Agrégat (compte) correctement exprimé
- [ ] Projection finale : idClient, nom, prénom, nombreLocations

---

## E. Qualité générale
- [ ] Notation algébrique **cohérente et lisible**
- [ ] Aucun SQL utilisé à la place de l’algèbre
- [ ] Aucune question omise
- [ ] Aucune section hors sujet

---

## Verdict CBIA
- [ ] **Conforme** → prêt pour dépôt
- [ ] **Non conforme** → corriger les points cochés

