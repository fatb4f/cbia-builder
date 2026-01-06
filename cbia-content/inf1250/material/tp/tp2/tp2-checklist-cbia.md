# INF1250 — TP2 — CBIA Checklist (SQL DDL/DML)
- [ ] Rapport remis en **PDF** ou **DOC/DOCX** (document unique)
- [ ] Réponses dans l’ordre (Ex1 → Ex2 → Ex3)
- [ ] Chaque sous-question est clairement titrée


## B. Exigences TP2 (non négociables)
- [ ] Pour **chaque** commande/requête demandée :
- [ ] SQL fourni
- [ ] Explication brève
- [ ] **Résultat** du SGBD inclus
- [ ] Interdits respectés :
- [ ] Aucune procédure stockée
- [ ] Aucun déclencheur
- [ ] Transactions : non traitées (OK)


## C. Outil / SGBD
- [ ] MySQL 8.1+ utilisé (recommandé) **ou** SGBD alternatif assumé
- [ ] Version du SGBD indiquée dans le rapport


## D. DDL — Schéma (Exercice 1)
- [ ] `CREATE DATABASE jegere;` exécuté
- [ ] `USE jegere;` exécuté
- [ ] Tables créées selon la figure
- [ ] Contraintes présentes et cohérentes :
- [ ] PK
- [ ] FK (types compatibles + références valides)
- [ ] NOT NULL selon besoins
- [ ] Contraintes de domaine (CHECK si applicable)
- [ ] Unicité (UNIQUE) si applicable


## E. DML — Insertion (Exercice 1)
- [ ] Les `INSERT` couvrent toutes les lignes fournies
- [ ] Formats adaptés (dates, téléphone) sans perte d’information
- [ ] Aucun identifiant inventé


## F. SELECT — Recherches (Exercice 2)
### Ex2.1 Employés sur ≥ 2 projets
- [ ] Logique correcte (compter projets distincts si nécessaire)
- [ ] Résultat inclus


### Ex2.2 Étape actuelle de chaque projet
- [ ] Utilise une sous-requête `MAX(...)` ou équivalent
- [ ] **Aucun GROUP BY**
- [ ] Par projet : retourne nom + livrable de l’étape actuelle


### Ex2.3 Vérifier les dates des étapes vs dates du projet
- [ ] Requête “test” automatique (retourne violations ou indicateur)
- [ ] Résultat inclus


### Ex2.4 Heures totales + somme gagnée par employé
- [ ] Agrégats corrects (SUM heures, SUM heures*prix)
- [ ] Colonnes demandées présentes : idEmploye, nomEmploye, adresseCourriel, nbrHeures, sommeGagnée


## G. UPDATE/INSERT/DELETE — Mises à jour (Exercice 3)
- [ ] Ex3.1 : responsable projet 3 mis à jour
- [ ] Ex3.2 : fin étape 3 + ajout étape 4 (2 requêtes OK)
- [ ] Ex3.3 : prix/horaire Mme St-Jerome +12 $
- [ ] Ex3.4 : suppression projet 2 complète, **ordre d’exécution** explicite


## H. Règle GROUP BY (cours)
- [ ] Chaque `GROUP BY` contient un agrégat (MAX/MIN/AVG/COUNT/SUM)
- [ ] Pas de `GROUP BY` “nu” (ex.: `SELECT x,y ... GROUP BY x`)


## Verdict
- [ ] Conforme → prêt pour dépôt
- [ ] Non conforme → corriger les cases cochées
