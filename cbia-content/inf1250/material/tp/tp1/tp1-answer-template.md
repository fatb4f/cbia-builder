# INF1250 — TP1 — Gabarit de réponses (structure uniquement)

> **Dépôt** : document unique **PDF** ou **Word** (DOC/DOCX). **Aucune archive** (zip/tar/rar).  
> **Consigne** : répondre **dans l’ordre**, en indiquant clairement le **numéro** de chaque question. :contentReference[oaicite:1]{index=1}

---

## Question 1 — MusiReseau (modèle relationnel complet)

### 1.1 Hypothèses (si nécessaires)
- Hypothèse A :
- Hypothèse B :
- (Limiter aux hypothèses indispensables.)

### 1.2 Entités / relations de départ
- Entités imposées (Figure 1) : **Utilisateur**, **Amitié** :contentReference[oaicite:2]{index=2}
- Autres entités ajoutées (si applicable) :
  - (ex. Chanson, Artiste, …)

### 1.3 Modèle relationnel — relations proposées
> Pour **chaque relation** : nomRelation(attributs…) + **PK** + **FK**.

#### Relation: Utilisateur( … )
- Attributs :
- **PK** :
- **FK** :

#### Relation: Amitié( … )
- Attributs :
- **PK** :
- **FK** :
- Attributs de validité temporelle (début/fin) :

#### Relation: (Ajouter si nécessaire) __________( … )
- Attributs :
- **PK** :
- **FK** :

#### Relation: (Ajouter si nécessaire) __________( … )
- Attributs :
- **PK** :
- **FK** :

### 1.4 Résumé des clés (vue synthèse)
- PKs :
- FKs :

---

## Question 2 — Location de voitures (clé + algèbre relationnelle)

### 2.1 Proposition de clé pour la relation **Location**
- Clé proposée :
- Justification (2–5 lignes) :

### 2.2 Résultats demandés (à partir des Figures 2 et 3)

#### a) `UNION(Location1, Location2)`
- Schéma du résultat (attributs attendus) :
- Résultat (table) :

| IdLocation? | idClient | idVoiture | DateLocation | DateRetour | Kilométrage |
|---:|---:|---:|---|---|---:|
| | | | | | |

> Remarque : si un identifiant de location n’existe pas dans les données, ne pas l’inventer — utiliser uniquement les attributs présents. :contentReference[oaicite:3]{index=3}

#### b) `PROJECT(Location1, idClient, idVoiture, DateLocation)`
- Résultat (table) :

| idClient | idVoiture | DateLocation |
|---:|---:|---|
| | | |

---

## Question 3 — Expressions en algèbre relationnelle (Figure 2)

> Donner **les expressions** (pas les résultats). :contentReference[oaicite:4]{index=4}

### 3.1 Clients ayant loué après le **1er mars 2012**
- Résultat attendu : **Nom, Prénom, adresseCourriel** :contentReference[oaicite:5]{index=5}
- Expression algébrique :
- Notes (sélections / jointures utilisées) :

### 3.2 Voitures avec **> 100 000 km** OU **année < 2007**
- Résultat attendu : **idVoiture, Année, Kilométrage** :contentReference[oaicite:6]{index=6}
- Expression algébrique :
- Notes :

### 3.3 Toutes les locations avec description voiture, **inclure locations même si voiture manquante**, filtrer **DateLocation > 01-03-2012**
- Résultat attendu : **idVoiture, Marque, Modèle, idClient, DateLocation, DateRetour** :contentReference[oaicite:7]{index=7}
- Expression algébrique :
- Indiquer explicitement l’opérateur de jointure requis (p. ex. jointure externe) :
- Notes :

### 3.4 Nombre de locations par client
- Résultat attendu : **idClient, nom, prénom, nombreLocations** :contentReference[oaicite:8]{index=8}
- Expression algébrique (inclure groupement/agrégat selon la notation du cours) :
- Notes :

---

## Vérification finale (avant dépôt)
- [ ] Ordre Q1 → Q2 → Q3 respecté
- [ ] Chaque sous-partie est clairement titrée
- [ ] Aucune section hors-sujet
- [ ] Fichier unique (PDF/DOC/DOCX), pas d’archive :contentReference[oaicite:9]{index=9}

