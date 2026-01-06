Module 2 : Concepts des bases de données, modèle relationnel et systèmes de gestion des bases de données

Réaliser le travail pratique 1
==============================

Présentation
------------

Cette activité est consacrée à la réalisation du travail pratique 1 qui compte pour 15 % de la note finale.

Vous devez rédiger un court rapport (en format « pdf » ou « Word »), que vous déposerez en utilisant l’outil de dépôt des travaux notés. Vous ne devez pas transmettre votre travail dans une archive zip, tar, rar ou autre. Suite à la correction du travail noté, il est possible d’envoyer un commentaire en utilisant le même outil de dépôt.

Si l’Université vous a assigné une date de remise pour ce travail, celle-ci est une suggestion. Il n’est pas nécessaire de remettre les travaux notés à une date pré-déterminée. Cependant, si vous tardez trop avant de remettre les travaux, vous pouvez avoir du mal à terminer le cours à temps.

Votre travail
-------------

*   Répondez aux questions dans l’ordre de leur présentation en indiquant bien le numéro de la question.
*   Déposez votre travail en utilisant l’outil de dépôt des travaux notés.

**Question 1**

Le nouveau site de réseautage **MusiReseau** vous a contacté pour développer une base de données qui sert à gérer l’information des utilisateurs du site qui vont partager ces goûts musicaux. On vous demande de prendre en compte les informations suivantes :

Il y a une liste de chansons disponibles d’où les utilisateurs pourront choisir celles qu’ils aiment. Pour chaque chanson disponible, **MusiReseau** veut avoir le titre, l’interprète, le compositeur, la langue, l’année de publication et le genre. Il est aussi important d’avoir l’information particulière à chaque artiste (Interprète ou compositeur), son nom, prénom, date de naissance, lieu de naissance et l’année de début comme artiste.

L’entreprise veut garder la trace de tous les utilisateurs du site. Ces informations concernent au moins l’id d’utilisateur, le nom, le sexe et l’adresse de courrier électronique. Il est optionnel d’inclure aussi l’âge et une description personnel.

Chaque utilisateur pourra donc sélectionner un ou plusieurs chansons qui feront partie de son catalogue musical, en gardant aussi la date d’inclusion de la chanson dans le catalogue.

Finalement, chaque utilisateur peut avoir des amis qui auront accès à son catalogue. Pour chaque « Amitié », **MusiReseau** veut garder les utilisateurs, la date de début et de fin.

**Figure 1**

  ![Figure 1](https://m2.teluq.ca/pluginfile.php/1028531/mod_folder/content/0/Images/M2_figure1.svg)

En partant des entités Utilisateur et Amitié présentées à la Figure 1 et de la description des besoins du client :

Donnez le modèle relationnel complet en ajoutant des entités au besoin, incluez la liste des attributs. Donnez aussi la clé primaire et les clés étrangères par entité (vous pouvez ajouter des attributs au besoin aux entités définies).

**Question 2**

Le modèle suivant décrit un système de location de voitures. Voici les descriptions des entités et relations incluses dans le modèle :

**Personne** - Identifié par idClient, une personne est celui qui fait la location de la voiture.

**Voiture** - Identifié par idVoiture, cette entité représente la voiture à être louée par l’entreprise.

**Location** - Association entre Voiture et Personne qui indique un contrat de location d’une voiture par un client entre les dates y déterminées.

**Figure 2**

  ![Figure 2](https://m2.teluq.ca/pluginfile.php/1028531/mod_folder/content/0/Images/M2_figure2.svg)

**Figure 3**

Location 1

IdClient

IdVoiture

DateLocation

DateRetour

Kilométrage

1

2340

05-06-2012

Il n'y a pas de contenu

Il n'y a pas de contenu

2

2290

24-02-2012

26-02-2012

124

3

2398

24-02-2012

12-01-2012

1400

Location 2

IdClient

IdVoiture

DateLocation

DateRetour

Kilométrage

4

2340

25-04-2012

29-04-2012

293

6

2190

18-05-2012

26-05-2012

1456

3

2082

04-03-2012

12-03-2012

1400

En considérant la Figure 2 et les données de la Figure 3, répondez aux questions suivantes.

Proposez une clef pour la relation Location. Justifiez votre réponse.

Donnez les résultats des opérations de l’algèbre relationnelle suivantes : 

*   UNION (Location1, Location2)
*   PROJECT (Location1, idClient, idVoiture, DateLocation)

**Question 3**

En considérant la Figure 2, donnez les expressions en langage algébriques permettant de répondre aux questions suivantes : 

*   Quels clients ont loué une voiture après le 1er Mars 2012? _Résultat attendu : Nom, Prénom et adresseCourriel_.
*   Quelles sont les voitures qui ont plus de 100,000 kilomètres ou dont l’année est inférieure à 2007? _Résultat attendu : idVoiture, Année et Kilométrage_.
*   Donnez la liste de toutes les locations avec la description des voitures correspondantes. Il faut que toutes les locations apparaissent même si l’information concernant la voiture est manquante. Veuillez ne conserver que les locations effectuées après le 01-03-2012. _Résultat attendu : idVoiture, Marque, Modèle,_  
    _idClient, DateLocation, DateRetour_.
    
*   Donnez le nombre de locations par client. _Résultat attendu : idClient, nom, prénom, nombreLocations_

Modifié le: jeudi, 28 novembre 2024, 14:46

Navigation entre les pages de la formation
------------------------------------------

*   [Précédente](https://m2.teluq.ca/mod/page/view.php?id=144935 "Page précédente - Vérifier et pratiquer.")
*   [Haut](#ancreHautPage "Haut de la page.")
*   [Suivante](https://m2.teluq.ca/mod/page/view.php?id=144944 "Page suivante - Démarrer.")

Menu bas de page
----------------

*   [Plan du site](https://m2.teluq.ca/mod/page/view.php?id=145409 "Plan du site")
*   [Accessibilité](https://m2.teluq.ca/mod/url/view.php?id=145412 "Accessibilité")
*   [Soutien technique](https://m2.teluq.ca/mod/url/view.php?id=145415 "Soutien technique")

© Département Science et Technologie, Université TÉLUQ, 2024. Tous droits réservés.

//<!\[CDATA\[ var require = { baseUrl : 'https://m2.teluq.ca/lib/requirejs.php/1766003893/', // We only support AMD modules with an explicit define() statement. enforceDefine: true, skipDataMain: true, waitSeconds : 0, paths: { jquery: 'https://m2.teluq.ca/lib/javascript.php/1766003893/lib/jquery/jquery-3.6.1.min', jqueryui: 'https://m2.teluq.ca/lib/javascript.php/1766003893/lib/jquery/ui-1.13.2/jquery-ui.min', jqueryprivate: 'https://m2.teluq.ca/lib/javascript.php/1766003893/lib/requirejs/jquery-private' }, // Custom jquery config map. map: { // '\*' means all modules will get 'jqueryprivate' // for their 'jquery' dependency. '\*': { jquery: 'jqueryprivate' }, // Stub module for 'process'. This is a workaround for a bug in MathJax (see MDL-60458). '\*': { process: 'core/first' }, // 'jquery-private' wants the real jQuery module // though. If this line was not here, there would // be an unresolvable cyclic dependency. jqueryprivate: { jquery: 'jquery' } } }; //\]\]> //<!\[CDATA\[ M.util.js\_pending("core/first"); require(\['core/first'\], function() { require(\['core/prefetch'\]) ; require(\["media\_videojs/loader"\], function(loader) { loader.setUp('fr'); });; M.util.js\_pending('core\_courseformat/local/content/activity\_header'); require(\['core\_courseformat/local/content/activity\_header'\], function(amd) {amd.init(); M.util.js\_complete('core\_courseformat/local/content/activity\_header');});; require(\['jquery', 'message\_popup/notification\_popover\_controller'\], function($, Controller) { var container = $('#nav-notification-popover-container'); var controller = new Controller(container); controller.registerEventListeners(); controller.registerListNavigationEventListeners(); }); ; M.util.js\_pending('theme\_boost/loader'); require(\['theme\_boost/loader', 'theme\_boost/drawer'\], function(Loader, Drawer) { Drawer.init(); M.util.js\_complete('theme\_boost/loader'); }); require(\['theme\_modele\_teluq/scripts'\], function(mod) { mod.init(); jwplayer.key="pFShamVrJnnotoAb22icWMUjYHDXU8kZDnLaABMkWfo="; }); require(\['theme\_modele\_teluq/liens-a11y'\], function(mod){ mod.init(); }); require(\['theme\_modele\_teluq/scripts'\], function(mod) { mod.initGA(); mod.initMenuPrinc(); mod.initPanneauOnglets(); mod.initAccordeons(); mod.initVideo(); mod.initAudio(); mod.initQuiz(); mod.initSlick(); mod.initSchemaInteractif('animationSVG'); mod.initSchemaInteractif('blocsCliquables'); mod.initSchemaInteractif('blocsNonCliquables'); mod.initTeluqNote(); mod.initRetourHaut(); }); require(\['../../../theme/gabarit\_enfant/amd/src/scripts'\], function(mod) { mod.init(); }); ; M.util.js\_pending('filter\_oembed/oembed'); require(\['filter\_oembed/oembed'\], function(amd) {amd.init(); M.util.js\_complete('filter\_oembed/oembed');});; M.util.js\_pending('core/notification'); require(\['core/notification'\], function(amd) {amd.init(1028564, \[\]); M.util.js\_complete('core/notification');});; M.util.js\_pending('core/log'); require(\['core/log'\], function(amd) {amd.setConfig({"level":"warn"}); M.util.js\_complete('core/log');});; M.util.js\_pending('core/page\_global'); require(\['core/page\_global'\], function(amd) {amd.init(); M.util.js\_complete('core/page\_global');});; M.util.js\_pending('core/utility'); require(\['core/utility'\], function(amd) {M.util.js\_complete('core/utility');});; M.util.js\_pending('core/storage\_validation'); require(\['core/storage\_validation'\], function(amd) {amd.init(1767714757); M.util.js\_complete('core/storage\_validation');}); M.util.js\_complete("core/first"); }); //\]\]> //<!\[CDATA\[ M.str = {"moodle":{"lastmodified":"Modifi\\u00e9 le","name":"Nom","error":"Erreur","info":"Information","yes":"Oui","no":"Non","ok":"Ok","cancel":"Annuler","confirm":"Confirm\\u00e9","areyousure":"Voulez-vous vraiment continuer\\u00a0?","closebuttontitle":"Fermer","unknownerror":"Erreur inconnue","file":"Fichier","url":"URL","collapseall":"Tout replier","expandall":"Tout d\\u00e9plier"},"repository":{"type":"Type","size":"Taille","invalidjson":"Cha\\u00eene JSON non valide","nofilesattached":"Aucun fichier joint","filepicker":"S\\u00e9lecteur de fichiers","logout":"D\\u00e9connexion","nofilesavailable":"Aucun fichier disponible","norepositoriesavailable":"D\\u00e9sol\\u00e9, aucun de vos d\\u00e9p\\u00f4ts actuels ne peut retourner de fichiers dans le format requis.","fileexistsdialogheader":"Le fichier existe","fileexistsdialog\_editor":"Un fichier de ce nom a d\\u00e9j\\u00e0 \\u00e9t\\u00e9 joint au texte que vous modifiez.","fileexistsdialog\_filemanager":"Un fichier de ce nom a d\\u00e9j\\u00e0 \\u00e9t\\u00e9 joint","renameto":"Renommer \\u00e0 \\u00ab\\u00a0{$a}\\u00a0\\u00bb","referencesexist":"Il y a {$a} liens qui pointent vers ce fichier","select":"S\\u00e9lectionnez"},"admin":{"confirmdeletecomments":"Voulez-vous vraiment supprimer des commentaires\\u00a0?","confirmation":"Confirmation"},"debug":{"debuginfo":"Info de d\\u00e9bogage","line":"Ligne","stacktrace":"Trace de la pile"},"langconfig":{"labelsep":"&nbsp;"}}; //\]\]> //<!\[CDATA\[ (function() {Y.use("moodle-filter\_glossary-autolinker",function() {M.filter\_glossary.init\_filter\_autolinking({"courseid":0}); }); Y.use("moodle-filter\_mathjaxloader-loader",function() {M.filter\_mathjaxloader.configure({"mathjaxconfig":"MathJax.Hub.Config({\\r\\n config: \[\\"Accessible.js\\", \\"Safe.js\\"\],\\r\\n errorSettings: { message: \[\\"!\\"\] },\\r\\n skipStartupTypeset: true,\\r\\n messageStyle: \\"none\\"\\r\\n});\\r\\n","lang":"fr"}); }); M.util.help\_popups.setup(Y); M.util.js\_pending('random695d2fdae660612'); Y.on('domready', function() { M.util.js\_complete("init"); M.util.js\_complete('random695d2fdae660612'); }); })(); //\]\]>