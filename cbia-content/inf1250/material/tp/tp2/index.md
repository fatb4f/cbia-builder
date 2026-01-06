# INF1250 — TP2 — Index (scaffold)


**Autorité** : Feuille de route (TELUQ) + Énoncé TP2 (Module 3).
**Pondération** : 25 %.
**Portée** : SQL (DDL + DML + requêtes) avec exécution sur SGBD.


## Exigences clés (TP2)
- Installer **MySQL 8.1.0 ou ultérieur** (recommandé). Un autre SGBD est permis, mais vous assumez les risques techniques.
- Remettre un **court rapport** (PDF ou Word).
- Pour **chaque requête SQL demandée** : fournir
1) la requête,
2) une **brève explication**,
3) le **résultat** retourné par le SGBD.
- Inclure le résultat **dans tous les cas**.
- Interdits : **procédures stockées**, **déclencheurs**.
- GROUP BY : permis **uniquement** avec un **agrégat** (MAX/MIN/AVG/COUNT/SUM).


## Structure du TP
- **Exercice 1 — Définition du schéma (Questions 1 à 3)**
- Q1: `CREATE DATABASE` + `USE`
- Q2: `CREATE TABLE` + contraintes (PK/FK/UNIQUE/CHECK/NOT NULL)
- Q3: `INSERT` des données fournies
- **Exercice 2 — Recherches de données** (requêtes SELECT)
- **Exercice 3 — Mises à jour de données** (UPDATE/INSERT/DELETE + ordre d’exécution)


## Livrables CBIA (dans ce dossier)
- `tp2-answer-template.md` : gabarit de réponses (structure + sections “SQL / Explication / Résultat”).
- `tp2-checklist-cbia.md` : checklist conformité + exécution (sans solutions).
