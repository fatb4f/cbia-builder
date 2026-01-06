Module 3 : Le langage SQL et les sous-langages DDL et DML

Réaliser le travail pratique 2
==============================

Présentation
------------

Cette activité est consacrée à la réalisation du travail pratique 2 qui compte pour 25 % de la note finale. Le travail consiste à utiliser le langage SQL pour créer un schéma de base de données et pour faire des recherches dans la base. Pour réaliser ce travail, vous devez utiliser le logiciel MySQL, que vous installerez dans votre ordinateur en suivant les consignes du guide d’installation présenté ci-dessous.

Vous devez rédiger un court rapport (en format « pdf » ou « Word »), que vous déposerez en utilisant l’outil de dépôt des travaux notés.

Quand on vous demande de produire une requête SQL, **vous devez non seulement fournir la requête, mais aussi une brève explication ainsi que le résultat de votre requête.** Si vos réponses ne sont pas complètes, vous pouvez perdre une partie ou la totalité des points.

Vous devez commencer par installer MySQL
----------------------------------------

On vous invite à installer MySQL sur votre machine dès maintenant si ce n’est pas déjà fait.

*   [Installation de MySQL 8.1.0 (ou ultérieur) sur un PC Windows](https://m2.teluq.ca/pluginfile.php/1028531/mod_folder/content/0/Installantion%20sql/Windows-Installation%20de%20MySQL%20Community%20Server%20version%208.1.docx)
*   [Installation de MySQL 8.1.0 (ou ultérieur) sur un Mac](https://m2.teluq.ca/pluginfile.php/1028531/mod_folder/content/0/Installantion%20sql/MACOS-Installation%20de%20MySQL%20Community%20Server%20version%208.1.docx)

Documentation MySQL
-------------------

La syntaxe du SGBD MySQL est disponible en ligne et en français.  
[Le manuel de la version 8.1.0 :](https://downloads.mysql.com/docs/refman-8.1-en.a4.pdf)

Consignes supplémentaires
-------------------------

*   Dans tous les cas, incluez avec votre solution le résultat de vos requêtes.
*   Vous ne devez pas utiliser de [procédures stockées](http://fr.wikipedia.org/wiki/Proc%C3%A9dure_stock%C3%A9e) ou de [déclencheur](http://fr.wikipedia.org/wiki/D%C3%A9clencheur). Il n’est pas nécessaire de vous préoccuper des [transactions](http://fr.wikipedia.org/wiki/Transaction_(base_de_donn%C3%A9es)) même si elles pourraient être souhaitables dans la pratique.
*   Vous pouvez utiliser des requêtes GROUP BY, mais celles-ci doivent comporter un agrégat (MAX, MIN, AVG, COUNT, SUM). Par exemple, cette requête n’est pas acceptable dans ce cours bien qu’elle puisse être acceptée par MySQL : SELECT x,y FROM table GROUP BY x.
*   Il est permis d’utiliser un SGBD autre que MySQL (par ex. Oracle ou SQLite), mais vous assumez alors la responsabilité de tous les problèmes techniques que vous rencontrez.

Contenu du travail
------------------

L’entreprise **JeGère** fait le développement de logiciel pour des entreprises au Québec. Pour faire la gestion des projets elle utilise un système informatique qui permet de faire le suivi de chaque projet, ses étapes, ses responsables, ses participants, entre autres.

À chaque projet on donne un identificateur unique (un numéro entre 0 et 4000) et un responsable qui est un employé de l’entreprise. De plus, l’entreprise garde le nom, la date de début et de fin du chaque projet.

Un projet est divisé par des étapes. Chaque étape a un livrable, une date de début et une date de fin. Cependant, l’entreprise a déjà quelques étapes définies qui peuvent être utilisées dans plusieurs projets.

Finalement un projet a des ressources humaines qui travaillent un nombre d’heures dans le projet et qui ont un prix par heure déterminé.

**Figure 1**

  ![Figure 1 - Modele Gestion de projets](https://m2.teluq.ca/pluginfile.php/1028531/mod_folder/content/0/Images/ModeleGestionDeProjets.png)

**Exercice 1 - Définition du schéma (Question 1 à 3)**

À l’aide du langage SQL de MySQL, faites et exécutez les commandes SQL suivantes pour :

*   Créez le schéma ’jegere’ (indice : CREATE DATABASE jegere ;) puis sélectionnez-le (indice : USE jegere; ).
*   Créez les tables de la Figure 1, en incluant les contraintes d’unicité de clé, référentielles, de domaine et de non-nullité. (Indice : CREATE TABLE)
    
    Par exemple, vous aurez
    
    CREATE TABLE IF NOT EXISTS jegere.Projet (  
        idProjet INT NOT NULL,  
        idClient INT NOT NULL,  
        nomProjetVARCHAR(45) NOT NULL,  
        dateDebut DATE,  
        dateFin DATE,  
        idResponsableINT NOT NULL,  
        PRIMARY KEY (idProjet),  
        FOREIGN KEY (idClient ) REFERENCES jegere.Client (idClient ),  
        FOREIGN KEY (idResponsable ) REFERENCES jegere.Employe (idEmploye )  
    ) ;
    
*   Générez les commandes pour insérer l’information suivante. Il est permis de reformater les données, par exemple lors de l’insertion des dates.
    
    **Client**
    
    idClient
    
    nomClient
    
    adresse
    
    telephone
    
    adresseCourriel
    
    321
    
    Financière Quebec
    
    1234 Rue La Montagne, Trois Rivières, QC
    
    819 3765244
    
    info@fquebec.qc.ca
    
    345
    
    Services Comptables Garneau
    
    8721 Rue St Laurent, Montreal, QC
    
    514 3217896
    
    services@comptablegarneau.ca
    
    **Employe**
    
    idEmploye
    
    nomEmploye
    
    adresse
    
    Telephone
    
    adresseCourriel
    
    1876
    
    Martin Rey
    
    3345 Avenue Poirier, Montreal, QC
    
    514 9871245
    
    martin.rey@jegere.ca
    
    2231
    
    Jean Pierre Bordeau
    
    2309 Boulevard Pie XII, Quebec, QC
    
    418 6573298
    
    jean.bordeau@jegere.ca
    
    4354
    
    Louise Gagnon
    
    2101 Blvd Bois Franc, Trois Rivières, QC
    
    819 6574028
    
    louise.gagnon@jegere.ca
    
    1212
    
    Marie St-Jerome
    
    1111 Avenue Jean François, Montreal, QC
    
    514 4932876
    
    marie.stjerome@jegere.ca
    
    **Projet**
    
    idProjet
    
    idClient
    
    nomProjet
    
    dateDebut
    
    dateFin
    
    idResponsable
    
    1
    
    321
    
    Développement du site web
    
    01/08/2011
    
    1876
    
    2
    
    321
    
    Maintenance du système de ressources humaines
    
    01/05/2012
    
    23/07/2012
    
    2231
    
    3
    
    345
    
    Développement du système de gestion de fournisseurs
    
    01/11/2011
    
    2231
    
    **RessourcesProjet**
    
    idProjet
    
    idEmploye
    
    nbrHeure
    
    PrixHeure
    
    1
    
    1876
    
    500
    
    65
    
    1
    
    4354
    
    2000
    
    31
    
    2
    
    2231
    
    250
    
    55
    
    3
    
    2231
    
    500
    
    65
    
    3
    
    1212
    
    3000
    
    35
    
    3
    
    1876
    
    2000
    
    35
    
    **Etape**
    
    idEtape
    
    nomEtape
    
    Livrable
    
    1
    
    Démarrage
    
    Définition du base de projet (objectifs, chef du projet)
    
    2
    
    Prévision
    
    Planification du projet (périmètre, activités, ressources requis, coûts)
    
    3
    
    Réalisation
    
    Exécution du plan du projet
    
    4
    
    Surveillance et Maîtrise
    
    Rapport de performance
    
    5
    
    Clôture
    
    Document de clôture du projet
    
    **EtapexProjet**
    
    idEtape
    
    idProjet
    
    dateDebut
    
    dateFin
    
    1
    
    1
    
    01/07/2011
    
    01/09/2011
    
    2
    
    1
    
    02/09/2011
    
    30/11/2011
    
    3
    
    1
    
    01/12/2011
    
    07/07/2012
    
    4
    
    1
    
    08/07/2012
    
    1
    
    2
    
    01/05/2012
    
    10/05/2012
    
    2
    
    2
    
    11/05/2012
    
    01/06/2012
    
    3
    
    2
    
    02/06/2012
    
    01/07/2012
    
    4
    
    2
    
    01/07/2012
    
    21/07/2012
    
    5
    
    2
    
    22/07/2012
    
    23/07/2012
    
    1
    
    3
    
    01/11/2011
    
    20/01/2012
    
    2
    
    3
    
    21/01/2012
    
    01/04/2012
    
    3
    
    3
    
    02/04/2012
    

**Exercice 2 - Recherches de données**

Écrivez avec le langage SQL les requêtes pour :

*   Trouver les employés qui ont travaillé sur au moins 2 projets.
*   Donner le nom et le livrable de l’étape actuelle de chaque projet de l’entreprise. (L’étape actuelle est la dernière étape pour laquelle nous avons des données.)
    
    Indices :
    
    *   Vous pouvez utiliser la syntaxe SELECT x,y FROM … WHERE y = (SELECT MAX(z) FROM … WHERE …).
    *   Vous ne devez pas utiliser un GROUP BY.
    *   Étant donné un identifiant de projet (idProjet), vous voulez trouver la valeur maximale de l’identifiant d’étape (idEtape).
*   Vérifier que les étapes de chaque projet ont été faites entre les dates de début et de fin du projet. Précision : écrivez une requête qui permet de vérifier automatiquement si c’est le cas. On ne vous demande pas d’ajouter cette contrainte à la base de données.
*   Donner le nombre d’heures total travaillés et la somme totale gagnée par employé dans tous les projets, en incluant le nom de l’employé et l’adresseCourriel. (Résultat attendu : idemploye, nomEmploye, adresseCourriel, nbrHeures, somme gagnée).

Vous devez exécuter les requêtes et inclure la réponse du SGBD. Expliquez votre solution.

**Exercice 3 - Mises à jour de données**

Le projet 3 a eu des modifications importantes, donnez les commandes pour modifier l’information dans la base de données :

*   Le responsable du projet a changé et il est maintenant Mme St-Jerome.
*   L’étape 3 vient de finir, donc l’étape 4 a été ajoutée au projet. (Vous pouvez utiliser deux requêtes SQL pour résoudre ce problème.)
*   Le taux horaire de Mme St-Jerome a augmenté de 12 $.
*   Le projet 2 doit être supprimé complètement, donnez les commandes et l’ordre d’exécution de ces commandes.

Vous devez exécuter les requêtes et inclure la réponse du SGBD. Expliquez votre solution.

Modifié le: jeudi, 28 novembre 2024, 15:13

Navigation entre les pages de la formation
------------------------------------------

*   [Précédente](https://m2.teluq.ca/mod/page/view.php?id=144950 "Page précédente - Vérifier et pratiquer.")
*   [Haut](#ancreHautPage "Haut de la page.")
*   [Suivante](https://m2.teluq.ca/mod/page/view.php?id=144959 "Page suivante - Démarrer.")

Menu bas de page
----------------

*   [Plan du site](https://m2.teluq.ca/mod/page/view.php?id=145409 "Plan du site")
*   [Accessibilité](https://m2.teluq.ca/mod/url/view.php?id=145412 "Accessibilité")
*   [Soutien technique](https://m2.teluq.ca/mod/url/view.php?id=145415 "Soutien technique")

© Département Science et Technologie, Université TÉLUQ, 2024. Tous droits réservés.

//<!\[CDATA\[ var require = { baseUrl : 'https://m2.teluq.ca/lib/requirejs.php/1766003893/', // We only support AMD modules with an explicit define() statement. enforceDefine: true, skipDataMain: true, waitSeconds : 0, paths: { jquery: 'https://m2.teluq.ca/lib/javascript.php/1766003893/lib/jquery/jquery-3.6.1.min', jqueryui: 'https://m2.teluq.ca/lib/javascript.php/1766003893/lib/jquery/ui-1.13.2/jquery-ui.min', jqueryprivate: 'https://m2.teluq.ca/lib/javascript.php/1766003893/lib/requirejs/jquery-private' }, // Custom jquery config map. map: { // '\*' means all modules will get 'jqueryprivate' // for their 'jquery' dependency. '\*': { jquery: 'jqueryprivate' }, // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458). '\*': { process: 'core/first' }, // 'jquery-private' wants the real jQuery module // though. If this line was not here, there would // be an unresolvable cyclic dependency. jqueryprivate: { jquery: 'jquery' } } }; //\]\]> //<!\[CDATA\[ M.util.js\_pending("core/first"); require(\['core/first'\], function() { require(\['core/prefetch'\]) ; require(\["media\_videojs/loader"\], function(loader) { loader.setUp('fr'); });; M.util.js\_pending('core\_courseformat/local/content/activity\_header'); require(\['core\_courseformat/local/content/activity\_header'\], function(amd) {amd.init(); M.util.js\_complete('core\_courseformat/local/content/activity\_header');});; require(\['jquery', 'message\_popup/notification\_popover\_controller'\], function($, Controller) { var container = $('#nav-notification-popover-container'); var controller = new Controller(container); controller.registerEventListeners(); controller.registerListNavigationEventListeners(); }); ; M.util.js\_pending('theme\_boost/loader'); require(\['theme\_boost/loader', 'theme\_boost/drawer'\], function(Loader, Drawer) { Drawer.init(); M.util.js\_complete('theme\_boost/loader'); }); require(\['theme\_modele\_teluq/scripts'\], function(mod) { mod.init(); jwplayer.key="pFShamVrJnnotoAb22icWMUjYHDXU8kZDnLaABMkWfo="; }); require(\['theme\_modele\_teluq/liens-a11y'\], function(mod){ mod.init(); }); require(\['theme\_modele\_teluq/scripts'\], function(mod) { mod.initGA(); mod.initMenuPrinc(); mod.initPanneauOnglets(); mod.initAccordeons(); mod.initVideo(); mod.initAudio(); mod.initQuiz(); mod.initSlick(); mod.initSchemaInteractif('animationSVG'); mod.initSchemaInteractif('blocsCliquables'); mod.initSchemaInteractif('blocsNonCliquables'); mod.initTeluqNote(); mod.initRetourHaut(); }); require(\['../../../theme/gabarit\_enfant/amd/src/scripts'\], function(mod) { mod.init(); }); ; M.util.js\_pending('filter\_oembed/oembed'); require(\['filter\_oembed/oembed'\], function(amd) {amd.init(); M.util.js\_complete('filter\_oembed/oembed');});; M.util.js\_pending('core/notification'); require(\['core/notification'\], function(amd) {amd.init(1028582, \[\]); M.util.js\_complete('core/notification');});; M.util.js\_pending('core/log'); require(\['core/log'\], function(amd) {amd.setConfig({"level":"warn"}); M.util.js\_complete('core/log');});; M.util.js\_pending('core/page\_global'); require(\['core/page\_global'\], function(amd) {amd.init(); M.util.js\_complete('core/page\_global');});; M.util.js\_pending('core/utility'); require(\['core/utility'\], function(amd) {M.util.js\_complete('core/utility');});; M.util.js\_pending('core/storage\_validation'); require(\['core/storage\_validation'\], function(amd) {amd.init(1767714757); M.util.js\_complete('core/storage\_validation');}); M.util.js\_complete("core/first"); }); //\]\]> //<!\[CDATA\[ M.str = {"moodle":{"lastmodified":"Modifi\\u00e9 le","name":"Nom","error":"Erreur","info":"Information","yes":"Oui","no":"Non","ok":"Ok","cancel":"Annuler","confirm":"Confirm\\u00e9","areyousure":"Voulez-vous vraiment continuer\\u00a0?","closebuttontitle":"Fermer","unknownerror":"Erreur inconnue","file":"Fichier","url":"URL","collapseall":"Tout replier","expandall":"Tout d\\u00e9plier"},"repository":{"type":"Type","size":"Taille","invalidjson":"Cha\\u00eene JSON non valide","nofilesattached":"Aucun fichier joint","filepicker":"S\\u00e9lecteur de fichiers","logout":"D\\u00e9connexion","nofilesavailable":"Aucun fichier disponible","norepositoriesavailable":"D\\u00e9sol\\u00e9, aucun de vos d\\u00e9p\\u00f4ts actuels ne peut retourner de fichiers dans le format requis.","fileexistsdialogheader":"Le fichier existe","fileexistsdialog\_editor":"Un fichier de ce nom a d\\u00e9j\\u00e0 \\u00e9t\\u00e9 joint au texte que vous modifiez.","fileexistsdialog\_filemanager":"Un fichier de ce nom a d\\u00e9j\\u00e0 \\u00e9t\\u00e9 joint","renameto":"Renommer \\u00e0 \\u00ab\\u00a0{$a}\\u00a0\\u00bb","referencesexist":"Il y a {$a} liens qui pointent vers ce fichier","select":"S\\u00e9lectionnez"},"admin":{"confirmdeletecomments":"Voulez-vous vraiment supprimer des commentaires\\u00a0?","confirmation":"Confirmation"},"debug":{"debuginfo":"Info de d\\u00e9bogage","line":"Ligne","stacktrace":"Trace de la pile"},"langconfig":{"labelsep":"&nbsp;"}}; //\]\]> //<!\[CDATA\[ (function() {Y.use("moodle-filter\_glossary-autolinker",function() {M.filter\_glossary.init\_filter\_autolinking({"courseid":0}); }); Y.use("moodle-filter\_mathjaxloader-loader",function() {M.filter\_mathjaxloader.configure({"mathjaxconfig":"MathJax.Hub.Config({\\r\\n config: \[\\"Accessible.js\\", \\"Safe.js\\"\],\\r\\n errorSettings: { message: \[\\"!\\"\] },\\r\\n skipStartupTypeset: true,\\r\\n messageStyle: \\"none\\"\\r\\n});\\r\\n","lang":"fr"}); }); M.util.help\_popups.setup(Y); M.util.js\_pending('random695d3333a7bf612'); Y.on('domready', function() { M.util.js\_complete("init"); M.util.js\_complete('random695d3333a7bf612'); }); })(); //\]\]>