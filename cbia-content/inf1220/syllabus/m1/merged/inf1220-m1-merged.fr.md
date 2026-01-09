# INF1220 — Module 1 (M1)

## Table of contents

- [Module 1: Algorithme et pseudocode](#module-1-algorithme-et-pseudocode)
- [Modèle du cours](#modele-du-cours)
- [Robot conversationnel et intelligence artificielle](#robot-conversationnel-et-intelligence-artificielle)
- [Autoévaluation](#autoevaluation)
- [Java pas à pas](#java-pas-a-pas)
- [Les ordinateurs et leurs langages](#les-ordinateurs-et-leurs-langages)
- [Les algorithmes](#les-algorithmes)
- [Les algorithmes : conception et syntaxe](#les-algorithmes-conception-et-syntaxe)
- [Les algorithmes: les structures de contrôle](#les-algorithmes-les-structures-de-controle)
- [Les problèmes difficiles](#les-problemes-difficiles)
- [Complexité algorithmique](#complexite-algorithmique)
- [Les erreurs communes](#les-erreurs-communes)
- [Présentation du pseudocode](#presentation-du-pseudocode)
- [Exercices sur les algorithmes](#exercices-sur-les-algorithmes)
- [Travail noté 1](#travail-note-1)

## Module 1: Algorithme et pseudocode


*   [Pourquoi ce premier module ?](#pourquoi-ce-premier-module-)
*   [Planification du temps](#planification-du-temps)

Module 1 [#](#module-1)
=======================

Le module 1 pose les bases de l’algorithmique et du raisonnement informatique. Il vous initie à la notion d’algorithme : une suite d’instructions précises permettant de résoudre un problème, à l’image d’une recette de cuisine. Vous apprendrez à décrire ces solutions en pseudocode, un langage intermédiaire entre le français et la programmation, pour exprimer clairement chaque étape sans vous soucier de la syntaxe d’un langage particulier.

Au fil du module, vous découvrirez :

*   Comment identifier les composants essentiels d’un algorithme (entrées, sorties, instructions, conditions, boucles).
*   Comment rédiger des algorithmes simples en pseudocode, en français.
*   Les bases de la complexité algorithmique (notation grand-O, comparaison d’approches).
*   L’importance de la rigueur, de la précision et de la pratique pour progresser.
*   Un aperçu historique des langages de programmation et de l’évolution des ordinateurs.

De nombreux exemples concrets et exercices d’autoévaluation vous permettront d’appliquer ces concepts et de développer votre capacité à raisonner de façon logique et méthodique, compétence essentielle pour la suite du cours et pour toute démarche informatique.

Pourquoi ce premier module ? [#](#pourquoi-ce-premier-module-)
--------------------------------------------------------------

Vous êtes peut-être surpris que le premier module ne débute pas immédiatement avec de la programmation Java. Nous croyons qu’il est essentiel d’établir au préalable des concepts plus fondamentaux. Notre objectif n’est pas de simplement vous aidez à apprendre la programmation en général, mais de vous donner des bases solides.

Il est difficile d’apprendre à programmer sans savoir ce qu’est un algorithme. Vous devez bien maîtriser cette notion fondamentale.

Planification du temps [#](#planification-du-temps)
---------------------------------------------------

Assurez-vous de bien planifier votre temps. N’oubliez pas de consacrer environ 9 heures par semaine au cous. Le cours nécessite plus d’une journée par semaine, pendant quinze semaine.

Nous vous suggérons de consacrer (au maximum) les trois premières semaines du cours au premier module (environ 27 heures). Assurez-vous de remettre le premier travail noté à la fin de la troisième semaine ou avant.

**Vous ne devriez pas prendre plus de trois semaines**. Le cours est riche en contenu, si vous prenez plus de trois semaines pour le premier module vous risquez de manquer de temps pour le reste du cours.

 [![Previous](/inf1220-hugo/svg/backward.svg "Modules") Modules](/inf1220-hugo/docs/modules/) [Modèle du cours ![Next](/inf1220-hugo/svg/forward.svg "Modèle du cours")](/inf1220-hugo/docs/modules/module1/teluq/) 


*   [Pourquoi ce premier module ?](#pourquoi-ce-premier-module-)
*   [Planification du temps](#planification-du-temps)

## Modèle du cours


*   [Le modèle de l’Université TÉLUQ](#le-modèle-de-luniversité-téluq)
*   [Apprentissage par vidéo](#apprentissage-par-vidéo)
*   [Python, JavaScript, C#, C++, Go, Rust, etc.](#python-javascript-c-c-go-rust-etc)
*   [Soyez informé !](#soyez-informé-)
*   [Les reports de la date de fin de cours](#les-reports-de-la-date-de-fin-de-cours)
*   [Planifier votre temps](#planifier-votre-temps)
*   [Exigences du cours](#exigences-du-cours)
*   [Navigateur web](#navigateur-web)
*   [Encadrement et suivi](#encadrement-et-suivi)
*   [Réseaux sociaux](#réseaux-sociaux)
*   [Plagiat](#plagiat)
*   [Cahier et notes](#cahier-et-notes)

Le modèle pédagogique du cours [#](#le-mod%c3%a8le-p%c3%a9dagogique-du-cours)
=============================================================================

Le cours INF 1220 est autoportant. Cela signifie que vous êtes capable, de manière autonome, de réaliser toutes les activités du cours. Il est important de bien comprendre ce modèle avant de débuter si vous n’êtes pas familier avec les cours en ligne de ce type.

Le modèle de l’Université TÉLUQ [#](#le-mod%c3%a8le-de-luniversit%c3%a9-t%c3%a9luq)
-----------------------------------------------------------------------------------

Plusieurs étudiants inscrits au cours INF 1220 en sont en leur premier cours à l’Université TÉLUQ. À l’Université TÉLUQ, nous offrons un enseignement personnalisé : vous débutez et terminez le cours à une date qui vous convient, vous faites les travaux au sein du cours à votre rythme. Le cours est conçu pour être autoportant : un travail pédagogique substantiel a été fait afin que l’étudiant autonome puisse compléter le cours par lui-même, sans aide. Un professeur ou une personne tutrice est là pour répondre à vos questions lorsque vous êtes devant une impasse après avoir fait les lectures et vos recherches, à tous les moments de votre parcours. Ce modèle diffère de celui des Universités traditionnelles où il y a de rencontres de groupes hebdomadaires et où tous les étudiants cheminent en même temps. Les deux modèles ont des forces et des faiblesses. L’Université TÉLUQ offre plus de flexibilité, mais son modèle exige plus d’autonomie intellectuelle de la part des étudiants.

Mener à terme un cours à l’Université TÉLUQ exige de la persévérance et de la motivation, ainsi que de l’autonomie et de la discipline. En vous inscrivant à un cours à distance, vous adoptez un modèle différent de celui d’un cours sur campus. Vous devez organiser votre apprentissage de manière autonome, en utilisant les ressources didactiques et d’encadrement mises à votre disposition, à l’endroit et au moment de votre choix.

Le professeur est préoccupé par le fait que l’apprentissage s’effectue de façon autonome. Tout le cours est créé en fonction de cet objectif. Nous croyons que le résultat est une formation de qualité axée sur l’autonomie et l’indépendance d’esprit.

Apprentissage par vidéo [#](#apprentissage-par-vid%c3%a9o)
----------------------------------------------------------

Certains étudiants préfèrent lire, d’autres préfèrent regarder des vidéos. Nous croyons que les deux modes de diffusion (écrit et vidéo) ont leur place en enseignement.

L’Université TÉLUQ est un précurseur dans l’enseignement avec la vidéo. Longtemps, lors de l’inscription à un cours, on pouvait recevoir des cassettes vidéos (VHS). L’Université TÉLUQ a même porté son propre poste de télévision appelé [Canal Savoir](https://fr.wikipedia.org/wiki/CFTU-DT).

Quelques cours à l’Université TÉLUQ sont toujours diffusés principalement avec des vidéos. Dans la plupart des cas, cependant, les cours utilisent des notes de cours. C’est le cas du cours INF 1220. Le langage écrit a plusieurs avantages, notamment le fait d’être plus accessible.

Un texte peut être lu rapidement. S’il est possible de modifier la vitesse de diffusion d’une vidéo, il demeure plus difficile de faire rapidement des sauts et des retours. Il est relativement aisé de faire des recherches dans un document écrit, et plus difficile dans une vidéo.

Dans le cas du cours INF 1220, l’utilisation plus intensive de la vidéo n’est pas jugée souhaitable pour deux raisons outre l’accessibilité. Tout d’abord, il existe un grand éventail de vidéos de grande qualité déjà disponibles et répondant bien au besoin du cours. Nous jugeons qu’il n’y aurait pas de sens à produire du contenu redondant. Dans certains cas spécifiques, nous avons produit des vidéos, mais dans l’ensemble, il est préférable de renvoyer les étudiants qui souhaitent du contenu vidéo à ce qui est déjà en place. Par ailleurs, avec des décennies d’expérience en pédagogie universitaire, nous savons que l’utilisation à grand volume de la vidéo a des limites. Nous croyons qu’il est beaucoup plus utile d’amener les étudiants à programmer le plus possible, tout en se référant à du contenu écrit. Personne n’apprend vraiment à programmer en regardant des vidéos. On apprend à programmer en lisant du code et en programmant. Et il est difficile de faire des recherches techniques au sein d’un enregistrement vidéo.

Certains étudiants préfèrent écouter et regarder plutôt que de lire. Nous sommes conscients que la lecture d’un manuel portant sur la programmation peut sembler rébarbative. Par contre, la lecture technique fait partie intégrante de l’activité de programmation. Il est absolument essentiel de pouvoir lire des documents techniques et des descriptions formelles. En somme, si la vidéo peut être utilisée, elle ne peut remplacer la lecture en programmation.

Python, JavaScript, C#, C++, Go, Rust, etc. [#](#python-javascript-c-c-go-rust-etc)
-----------------------------------------------------------------------------------

Certains étudiants souhaitent apprendre un autre langage que Java. Nous vous encourageons à étudier plus d’un langage de programmation, surtout si vous souhaitez faire carrière en informatique. Dans le cadre de ce cours, nous allons cibler un seul langage.

Certains étudiants souhaitent apprendre le C#. Il est particulièrement facile de passer du Java au C#. En effet, le C# peut être vu comme une variante du Java. La syntaxe est souvent quasiment identique et les pratiques de programmation sont équivalentes.

Dans le cadre d’une carrière dans l’industrie du logiciel, il peut être dommage de se limiter à une seule technologie, un seul langage de programmation. Les choix technologiques évoluent et les offres d’emploi diffèrent d’un moment à l’autre. On s’attend à ce qu’un diplômé universitaire maîtrise plusieurs technologies, plusieurs langages.

Si vous souhaitez étudier le langage Python, vous pourrez prendre le cours INF 2020 Programmation d’applications avec Python. Si vous souhaitez étudier le langage Go, vous pourrez prendre le cours INF 2007 Programmation avancée.

Soyez informé ! [#](#soyez-inform%c3%a9-)
-----------------------------------------

Si ce n’est pas déjà fait, [prenez le temps de lire la description du cours sur le site web de la TÉLUQ](https://www.teluq.ca/site/etudes/offre/cours/TELUQ/INF%201220/). Vous y trouverez notamment la grille d’équivalence entre les notes numériques et les lettres. Une telle grille répond notamment à la question « quelle est la note de passage ». Observez bien cependant que la note de passage n’est pas suffisante généralement pour progresser normalement au sein d’un programme universitaire et obtenir un diplôme.

Nous vous rappelons que lorsque vous suivez un cours, vous devez lire les courriels de l’Université. L’information pertinente concernant le cours, votre inscription, etc. peut y être acheminée. Si vous ne prenez pas vos messages dans votre boîte courriel TÉLUQ, il peut vous manquer des informations importantes.

Important: En commençant, prenez en note la date de fin de cours. Vous devez avoir remis les travaux d’ici cette date. Si vous avez besoin d’un report de la date de fin de cours, peut-être à cause d’empêchements médicaux ou familiaux, vous devez joindre l’Université (pas le professeur) pour établir votre situation et obtenir un report. Vous ne pouvez pas obtenir un report après la date de fin de cours. En aucun cas est-ce que l’enseignant peut modifier votre date de fin de cours.

Votre date de fin de cours est inscrite dans votre dossier et vous pouvez la trouver sur le portail étudiant et sur la documentation qu’on vous a remise lors de votre inscription. Il est possible que votre examen ait lieu des semaines ou même des mois après votre date de fin de cours: cela ne constitue pas une extension de votre date de fin de cours. Tout travail remis après votre date de fin de cours pourra recevoir la note de zéro. En tout temps, la note « incomplet » peut être attribuée à un travail qui n’est pas remis après votre date de fin de cours, même si vous n’avez pas encore passé l’examen.

Vous ne devriez jamais avoir à nous demander jusqu’à quelle heure précise lors de la dernière journée de votre cours vous avez pour compléter vos travaux. Prenez le temps de planifier votre travail. Avec la possibilité de report et la flexibilité offerte par la TÉLUQ, il n’y a pas d’excuse pour terminer le cours à la dernière heure.

Les reports de la date de fin de cours [#](#les-reports-de-la-date-de-fin-de-cours)
-----------------------------------------------------------------------------------

À la TÉLUQ, chaque étudiant a sa propre date de fin de cours. Les professeurs ne peuvent pas modifier ces dates, quelle que soit votre situation. Les dates des examens sont fixées par l’Université. Les professeurs conçoivent les examens, mais leur déroulement est géré par l’Université. La période suivant la date de fin de cours, où votre dossier est fermé et où vous risquez de recevoir un incomplet, est également gérée par l’Université. Vous devez donc contacter l’Université si vous avez besoin de plus de temps. Il est inutile d’écrire aux professeurs à ce sujet.

Il est de votre responsabilité de respecter les délais et de réaliser les travaux selon l’échéancier prévu dans le cours. En cas de difficultés (familiales, médicales, situation de handicap), vous devez en informer l’Université, et non le professeur. Sinon, une bonne organisation est essentielle.

La gestion efficace de votre temps est une compétence clé pour réussir vos études universitaires. Le cours est conçu pour vous y aider en structurant les activités en modules avec des échéances suggérées. Toutefois, c’est à vous de vous organiser.

Planifier votre temps [#](#planifier-votre-temps)
-------------------------------------------------

Le niveau de difficulté du cours augmente progressivement. Les premiers travaux sont plus accessibles, mais environ un tiers du cours devrait être consacré aux deux derniers modules, qui sont plus avancés. Si vous passez trop de temps sur les lectures et les travaux initiaux, vous pourriez être surpris par la difficulté et le volume de travail des dernières parties.

Exigences du cours [#](#exigences-du-cours)
-------------------------------------------

Le cours INF 1220 n’est pas un cours facile.

1.  Dans certaines disciplines, lire suffit pour préparer les travaux. En programmation, la lecture seule est insuffisante. Un manuel ne vous apprendra pas à programmer. Vous devez lire, faire des exercices, relire, et répéter ce processus. Apprendre à programmer demande du travail et de la persévérance. La présence de nombreux travaux dans le cours vise à vous encourager à travailler régulièrement et à pratiquer.
    
2.  Prévoyez environ 9 heures de travail par semaine pendant 15 semaines pour réussir ce cours. Chaque travail noté demande plusieurs heures, tout comme la préparation et l’étude préalables. Il est normal de consacrer des dizaines d’heures pour compléter un module et son travail noté. Si vous n’avez pas entre 5 et 15 heures par semaine à consacrer au cours, vous risquez de ne pas réussir.
    
3.  Le cours inclut des lectures et des activités d’autoévaluation (par exemple, des problèmes avec solutions cachées). Vous devez obligatoirement réaliser ces lectures et activités avant les travaux notés. Des vidéos explicatives sont également disponibles : visionnez-les et revisionnez-les au besoin. Tenter de passer directement aux travaux notés sans préparation est voué à l’échec. Faire uniquement le minimum pour compléter les travaux notés ne suffira pas pour réussir l’examen. Vous devez pratiquer la programmation, apprendre à penser comme un programmeur et maîtriser le Java grâce à une étude rigoureuse.
    
4.  Si un travail noté exige d’expliquer votre solution, cette consigne est impérative. Ne pas la respecter peut entraîner une note de zéro.
    
5.  Votre code doit être fonctionnel et valide, sinon une note de zéro peut être attribuée. La réussite de ce cours repose sur votre capacité à programmer.
    
6.  Il est fortement recommandé de faire des recherches autonomes en ligne (YouTube, etc.) pour compléter le manuel, les notes de cours et les activités. La recherche en ligne est une composante essentielle du développement logiciel aujourd’hui. Prévoyez plusieurs heures pour explorer des ressources complémentaires selon vos besoins.
    

Ne débutez pas ce cours si vous n'avez pas les préalables mathématiques nécessaires.

Le cours INF 1220 a été développé en prenant pour acquis que vous avez fait les mathématiques avancées au secondaire et au collégial. Il fait partie d'un cursus en informatique de niveau universitaire. Si vous n'étiez pas « fort en math » au secondaire, il est possible que vous trouviez le cours trop difficile. Il est de votre responsabilité de faire une mise à niveau au besoin avant de débuter le cours INF 1220.

Navigateur web [#](#navigateur-web)
-----------------------------------

Vous pouvez suivre ce cours avec pratiquement n'importe quel navigateur web. Par contre, pour que les formules mathématiques s'affichent correctement, vous devez utiliser un navigateur supportant la norme MathML. Les navigateurs Chrome, Edge, Firefox et Safari font bien l'affaire.

Il y a peu de formules mathématiques dans ce cours, et il est donc parfaitement possible de travailler sans un support correct des formules mathématiques. Par contre, si vous avez besoin de bien suivre nos consignes et rappels mathématiques, vous devriez sans doute adopter, au moins temporairement, un des navigateurs supportant MathML (par ex., Chrome, Edge, Firefox et Safari).

Encadrement et suivi [#](#encadrement-et-suivi)
-----------------------------------------------

Prenez connaissance de la documentation fournie par l'université. Vous y trouverez le nom et l'adresse courriel de la personne qui vous encadre. Après avoir fait les lectures, vous pouvez écrire vos questions à cette personne. Assurez-vous de respecter les consignes énoncées dans la présentation du cours : vous devez mettre « \[INF1220\] » dans l'objet du courriel et vous devez utiliser une adresse de courriel à votre nom afin que nous puissions vous identifier. Vos courriels devraient comprendre des questions précises, bien détaillées. Vous devriez commencer expliquer ce que vous avez fait, ce que vous comprenez. Il peut être utile de faire référence aux lectures que vous avez faites. N'oubliez pas que les lectures au sein du manuel sont obligatoires. Par exemple, si vous avez du mal avec une notion couverte par le manuel, vous devriez faire une référence à cette section. N'hésitez pas à joindre des saisies d'écran pour illustrer vos propos. Nous nous ferons un plaisir de répondre à vos questions par courriel, mais tel qu'expliqué dans la présentation du cours, nous n’offrons pas d’enseignement par vidéoconférence au sein du cours INF 1220.

Réseaux sociaux [#](#r%c3%a9seaux-sociaux)
------------------------------------------

Attention: Il est strictement défendu de demander des indices aux autres étudiants du cours concernant les travaux notés et l'examen. Il est aussi défendu de donner des indices concernant les travaux notés.

Plagiat [#](#plagiat)
---------------------

Nous mettons bien entendu à jour les travaux notés et les examens. Dans le cas des travaux notés, vous pouvez toujours remettre la version que vous avez débutée sans pénalité dans le cas où les travaux sont mis à jour pendant votre travail. Par contre, soyez avisé que nous portons une attention particulière au plagiat. Si votre travail ressemble trop à un autre travail remis, nous pourrons alors procéder à un examen oral, pour vérifier si vous avez effectivement fait le travail par vous-même. Dans le cas des examens, nous tentons de les offrir en présence avec surveillance. Quand ce n'est pas possible, nous varions autant que possible le contenu des examens et nous utilisons d'autres mesures à notre disposition pour contrer le plagiat.

Le plagiat peut avoir des conséquences sévères. Une note permanente peut être ajoutée à votre dossier et à votre relevé de notes. Le plagiat peut mener à votre exclusion du programme universitaire où vous avez été admis.

Cahier et notes [#](#cahier-et-notes)
-------------------------------------

Je vous suggère fortement de prendre un cahier (en papier) et un bon crayon et de prendre des notes tout au long du cours. Je sais que ça semble vieillot, mais il s’agit d’une méthode éprouvée.

 [![Previous](/inf1220-hugo/svg/backward.svg "Module 1: Algorithme et pseudocode") Module 1: Algorithme et pseudocode](/inf1220-hugo/docs/modules/module1/) [Robot conversationnel et intelligence artificielle ![Next](/inf1220-hugo/svg/forward.svg "Robot conversationnel et intelligence artificielle")](/inf1220-hugo/docs/modules/module1/robot/) 


*   [Le modèle de l’Université TÉLUQ](#le-modèle-de-luniversité-téluq)
*   [Apprentissage par vidéo](#apprentissage-par-vidéo)
*   [Python, JavaScript, C#, C++, Go, Rust, etc.](#python-javascript-c-c-go-rust-etc)
*   [Soyez informé !](#soyez-informé-)
*   [Les reports de la date de fin de cours](#les-reports-de-la-date-de-fin-de-cours)
*   [Planifier votre temps](#planifier-votre-temps)
*   [Exigences du cours](#exigences-du-cours)
*   [Navigateur web](#navigateur-web)
*   [Encadrement et suivi](#encadrement-et-suivi)
*   [Réseaux sociaux](#réseaux-sociaux)
*   [Plagiat](#plagiat)
*   [Cahier et notes](#cahier-et-notes)

## Robot conversationnel et intelligence artificielle


*   [Robot](#robot)

Robot conversationnel et intelligence artificielle [#](#robot-conversationnel-et-intelligence-artificielle)
===========================================================================================================

L’intelligence artificielle (IA) transforme profondément le domaine de la programmation, redéfinissant la manière dont les développeurs conçoivent, écrivent et maintiennent le code. Les outils basés sur l’IA, comme les assistants de codage (par exemple, GitHub Copilot), permettent d’automatiser des tâches répétitives, telles que la génération de code boilerplate ou la complétion automatique de fonctions. Ces outils s’appuient sur des modèles de langage avancés, entraînés sur d’immenses bases de données de code, pour proposer des suggestions contextuelles précises. Cette assistance accélère le processus de développement, permettant aux programmeurs de se concentrer sur des aspects plus créatifs et complexes de leurs projets, tout en réduisant les erreurs humaines.

Au-delà de l’écriture de code, l’IA joue un rôle croissant dans le débogage et l’optimisation. Les systèmes d’IA peuvent analyser des programmes pour identifier des bugs, des vulnérabilités de sécurité ou des inefficacités, souvent plus rapidement qu’un humain. Par exemple, des outils comme DeepCode ou SonarQube utilisent l’apprentissage automatique pour détecter des anomalies dans le code et suggérer des corrections. De plus, l’IA aide à optimiser les performances en proposant des algorithmes plus efficaces ou en ajustant automatiquement les configurations des systèmes. Cette capacité à diagnostiquer et améliorer le code renforce la qualité des logiciels et réduit le temps consacré à la maintenance.

L’IA démocratise également la programmation en abaissant les barrières à l’entrée. Les interfaces conversationnelles et les outils no-code/low-code, alimentés par l’IA, permettent à des non-programmeurs de créer des applications en décrivant leurs besoins en langage naturel. Des plateformes comme Bubble ou OutSystems exploitent l’IA pour traduire ces descriptions en code fonctionnel. Cette évolution ouvre la programmation à un public plus large, favorisant l’innovation dans des domaines variés, mais soulève aussi des questions sur la dépendance aux outils automatisés et la compréhension réelle des concepts sous-jacents par les utilisateurs.

Je vous invite à regarder cette vidéo sur YouTube à ce sujet. YouTube offre une version avec sous-titres traduits et je vous offre une transcription en français.

Transcription traduite en français

Hum, d’accord, je suis enthousiaste d’être ici aujourd’hui pour vous parler du logiciel à l’ère de l’IA. On m’a dit que beaucoup d’entre vous sont étudiants, en licence, master, doctorat, et ainsi de suite, et que vous êtes sur le point d’entrer dans l’industrie. Je pense que c’est un moment extrêmement unique et très intéressant pour rejoindre l’industrie en ce moment. Fondamentalement, la raison en est que le logiciel change à nouveau. Je dis « à nouveau » parce que j’ai déjà donné cette conférence, mais le problème est que le logiciel ne cesse de changer. J’ai donc beaucoup de matériel pour créer de nouvelles conférences, et je pense que ce changement est assez fondamental. Grossièrement, le logiciel n’a pas beaucoup changé à un niveau aussi fondamental depuis 70 ans, puis il a changé, je pense, deux fois de manière assez rapide ces dernières années. Il y a donc une énorme quantité de travail à faire, une énorme quantité de logiciels à écrire et à réécrire.

Le paysage du logiciel

Examinons peut-être le domaine du logiciel. Si nous considérons cela comme une carte du logiciel, il existe un outil vraiment cool appelé « Map of GitHub ». C’est un peu comme tout le logiciel qui a été écrit, des instructions pour l’ordinateur afin d’exécuter des tâches dans l’espace numérique. Si vous zoomez, ce sont tous différents types de dépôts, et c’est tout le code qui a été écrit. Il y a quelques années, j’ai observé que le logiciel changeait, qu’il y avait un nouveau type de logiciel, et je l’ai appelé « logiciel 2.0 » à l’époque. L’idée était que le logiciel 1.0 est le code que vous écrivez pour l’ordinateur, tandis que le logiciel 2.0 concerne les réseaux neuronaux, en particulier les poids d’un réseau neuronal. Vous n’écrivez pas ce code directement, vous ajustez plutôt les ensembles de données, puis vous exécutez un optimiseur pour créer les paramètres de ce réseau neuronal. À l’époque, les réseaux neuronaux étaient perçus comme un simple classificateur différent, comme un arbre de décision ou quelque chose comme ça. Je pense que ce cadre était beaucoup plus approprié.

Maintenant, nous avons l’équivalent de GitHub dans le domaine du logiciel 2.0. Je pense que Hugging Face est fondamentalement l’équivalent de GitHub pour le logiciel 2.0. Il y a aussi Model Atlas, où vous pouvez visualiser tout le code écrit, si vous êtes curieux. D’ailleurs, le grand cercle au centre représente les paramètres de Flux, le générateur d’images. Chaque fois que quelqu’un ajuste un modèle au-dessus de Flux, vous créez en quelque sorte un « commit » dans cet espace, et vous obtenez un générateur d’images différent.

En résumé, le logiciel 1.0 est le code informatique qui programme un ordinateur, le logiciel 2.0 sont les poids qui programment les réseaux neuronaux. Voici un exemple avec AlexNet, un réseau neuronal de reconnaissance d’images. Jusqu’à récemment, tous les réseaux neuronaux que nous connaissions étaient des ordinateurs à fonction fixe, comme de l’image aux catégories. Ce qui a changé, et je pense que c’est un changement fondamental, c’est que les réseaux neuronaux sont devenus programmables avec les grands modèles de langage (LLM). Je vois cela comme quelque chose de nouveau et unique, un nouveau type d’ordinateur. À mon avis, cela mérite une nouvelle désignation : le logiciel 3.0. Vos invites (prompts) sont maintenant des programmes qui programment le LLM, et, chose remarquable, ces invites sont écrites en anglais, ce qui en fait un langage de programmation très intéressant.

Exemple : classification de sentiments

Pour illustrer la différence, si vous faites une classification de sentiments, vous pouvez imaginer écrire une certaine quantité de code Python pour effectuer cette classification, ou entraîner un réseau neuronal, ou encore utiliser une invite pour un grand modèle de langage. Voici une invite courte, et vous pouvez imaginer la modifier pour programmer l’ordinateur d’une manière légèrement différente. Nous avons donc le logiciel 1.0, le logiciel 2.0, et je pense que nous voyons maintenant que beaucoup de code sur GitHub n’est plus seulement du code, il y a aussi beaucoup de texte en anglais entrelacé avec le code. Une nouvelle catégorie de code émerge, non seulement un nouveau paradigme de programmation, mais aussi, ce qui est remarquable, dans notre langue native, l’anglais.

Quand cela m’a frappé il y a quelques années, j’ai tweeté à ce sujet, et cela a capté l’attention de beaucoup de monde. C’est actuellement mon tweet épinglé : nous programmons maintenant les ordinateurs en anglais. Chez Tesla, nous travaillions sur le pilote automatique, et nous essayions de faire conduire la voiture. J’ai montré une diapositive à l’époque où les entrées de la voiture passaient par une pile logicielle pour produire la direction et l’accélération. J’avais observé qu’il y avait une tonne de code C++ dans le pilote automatique, qui était du logiciel 1.0, et qu’il y avait aussi des réseaux neuronaux pour la reconnaissance d’images. Au fil du temps, à mesure que nous améliorions le pilote automatique, le réseau neuronal gagnait en capacité et en taille, et tout le code C++ était supprimé. Beaucoup des capacités et fonctionnalités initialement écrites en 1.0 ont été migrées vers le 2.0. Par exemple, l’assemblage des informations entre les images des différentes caméras et dans le temps était effectué par un réseau neuronal, ce qui nous a permis de supprimer beaucoup de code. La pile logicielle 2.0 a littéralement dévoré la pile logicielle du pilote automatique.

Je trouvais cela vraiment remarquable à l’époque, et je pense que nous voyons la même chose aujourd’hui, où un nouveau type de logiciel dévore la pile. Nous avons trois paradigmes de programmation complètement différents, et si vous entrez dans l’industrie, il est très utile d’être à l’aise avec chacun d’eux, car ils ont tous leurs avantages et inconvénients. Vous devrez décider si une fonctionnalité doit être programmée en 1.0, 2.0 ou 3.0. Allez-vous entraîner un réseau neuronal, simplement utiliser une invite pour un LLM, ou écrire un code explicite ? Nous devons tous prendre ces décisions et potentiellement passer fluidement d’un paradigme à l’autre.

Les grands modèles de langage (LLM)

Passons maintenant à la première partie, où je veux parler des LLM, de la manière de penser à ce nouveau paradigme et à son écosystème. Qu’est-ce que cet nouvel ordinateur, à quoi ressemble-t-il, et à quoi ressemble l’écosystème ? J’ai été frappé par une citation d’Andrew Ng, il y a plusieurs années, qui disait que l’IA est la nouvelle électricité. Je pense que cela capture quelque chose de très intéressant, car les LLM ont actuellement des propriétés d’utilité publique. Les laboratoires de LLM, comme OpenAI, Gemini, Anthropic, etc., investissent des capitaux pour entraîner les LLM, ce qui équivaut à construire un réseau. Ensuite, il y a des dépenses opérationnelles pour fournir cette intelligence via des API à nous tous, à travers un accès mesuré où nous payons par million de jetons ou quelque chose comme ça. Nous avons beaucoup d’exigences similaires à celles d’une utilité publique : faible latence, haute disponibilité, qualité constante, etc.

Dans l’électricité, vous auriez un commutateur de transfert pour passer de la grille à l’énergie solaire, une batterie ou un générateur. Dans les LLM, nous avons peut-être OpenRouter, qui permet de basculer facilement entre différents types de LLM existants. Comme les LLM sont des logiciels, ils ne rivalisent pas pour l’espace physique, donc il est acceptable d’avoir, disons, six fournisseurs d’électricité, et vous pouvez passer de l’un à l’autre, car ils ne concurrencent pas de manière aussi directe. Ce qui est aussi fascinant, c’est que récemment, plusieurs LLM ont connu des pannes, et les gens se sont retrouvés bloqués, incapables de travailler. Quand les LLM de pointe tombent en panne, c’est comme une baisse d’intelligence dans le monde, un peu comme une tension instable dans le réseau, et la planète devient simplement moins intelligente. Plus nous dépendons de ces modèles, ce qui est déjà dramatique, plus cela va croître.

Mais les LLM n’ont pas seulement des propriétés d’utilité publique. Ils ont aussi des propriétés de fabriques (fabs), car les investissements nécessaires pour construire un LLM sont considérables, pas seulement comme construire une centrale électrique. La technologie évolue rapidement, avec des arbres technologiques complexes, de la recherche et du développement, et des secrets centralisés dans les laboratoires de LLM. Cependant, l’analogie devient un peu floue, car, comme je l’ai mentionné, il s’agit de logiciel, et le logiciel est moins défendable car il est très malléable.

Je pense que l’analogie qui a le plus de sens est que les LLM ont de fortes similitudes avec les systèmes d’exploitation. Ce n’est pas juste de l’électricité ou de l’eau qui sort d’un robinet comme une commodité. Ce sont des écosystèmes logiciels de plus en plus complexes, pas juste des commodités simples comme l’électricité. L’écosystème se forme de manière très similaire, avec quelques fournisseurs à source fermée, comme Windows ou Mac OS, et une alternative open source comme Linux. Pour les LLM, nous avons quelques fournisseurs à source fermée en compétition, et peut-être que l’écosystème LLaMA est actuellement une approximation de quelque chose qui pourrait devenir comme Linux. C’est encore très tôt, car ce ne sont que des LLM simples, mais nous commençons à voir qu’ils vont devenir beaucoup plus compliqués, avec l’utilisation d’outils, la multimodalité, et comment tout cela fonctionne.

Quand j’ai réalisé cela il y a un moment, j’ai essayé de le schématiser, et il m’a semblé que les LLM sont comme un nouveau système d’exploitation. Le LLM est une sorte d’équivalent du CPU, les fenêtres de contexte sont comme la mémoire, et le LLM orchestre la mémoire et le calcul pour résoudre des problèmes, en utilisant toutes ces capacités. Cela ressemble beaucoup à un système d’exploitation de ce point de vue.

Pour donner un exemple, si je veux télécharger une application, disons VS Code, je peux le télécharger et l’exécuter sur Windows, Linux ou Mac. De la même manière, je peux prendre une application LLM comme Cursor et l’exécuter sur GPT, Claude ou la série Gemini, juste en sélectionnant une option dans un menu déroulant. Nous sommes dans une ère, disons des années 1960, où le calcul des LLM est encore très coûteux pour ce nouveau type d’ordinateur, ce qui oblige les LLM à être centralisés dans le cloud. Nous sommes tous des clients qui interagissent avec eux via le réseau, et aucun de nous n’a une utilisation complète de ces ordinateurs. Cela rend logique d’utiliser le partage de temps, où nous sommes tous une dimension du lot quand ils exécutent l’ordinateur dans le cloud. C’est ainsi que les ordinateurs fonctionnaient à cette époque : les systèmes d’exploitation étaient dans le cloud, tout était diffusé, et il y avait du traitement par lots.

La révolution de l’informatique personnelle n’a pas encore eu lieu, car ce n’est pas économique, ça n’a pas de sens. Mais certaines personnes essaient, et il s’avère que les Mac Minis, par exemple, sont très adaptés pour certains LLM, car si vous faites une inférence par lot, tout est très limité par la mémoire. Cela fonctionne, et ce sont peut-être des signes précoces de l’informatique personnelle, mais cela n’a pas vraiment eu lieu. Ce n’est pas clair à quoi cela ressemblera. Peut-être que certains d’entre vous inventeront ce que c’est, comment ça fonctionne, ou ce que ça devrait être.

Une autre analogie : chaque fois que je parle à ChatGPT ou à un LLM directement en texte, j’ai l’impression de parler à un système d’exploitation via le terminal. C’est du texte, c’est un accès direct au système d’exploitation. Une interface graphique (GUI) n’a pas encore été inventée de manière générale. Est-ce que ChatGPT devrait avoir une GUI différente des simples bulles de texte ? Certaines applications ont des GUI, mais il n’y a pas de GUI générale pour toutes les tâches.

Les LLM diffèrent des systèmes d’exploitation de manière assez unique. J’ai écrit sur une propriété qui me semble très différente cette fois-ci : les LLM inversent la direction de la diffusion technologique, qui est généralement présente dans la technologie. Par exemple, avec l’électricité, la cryptographie, l’informatique, l’aviation, l’internet, le GPS, beaucoup de technologies transformatrices nouvelles et coûteuses étaient d’abord utilisées par les gouvernements et les entreprises, avant de se diffuser aux consommateurs. Mais avec les LLM, c’est l’inverse. Avec les premiers ordinateurs, il s’agissait de balistique et d’usage militaire, mais avec les LLM, il s’agit de savoir comment faire bouillir un œuf. C’est fascinant que nous ayons un nouvel ordinateur magique qui m’aide à faire bouillir un œuf, et non à aider le gouvernement à faire quelque chose de fou comme de la balistique militaire ou une technologie spéciale. Les entreprises et les gouvernements sont en retard sur l’adoption de ces technologies par rapport à nous tous. Cela informe peut-être certaines utilisations de la technologie, comme où se trouvent les premières applications.

Résumé

Les LLM sont des systèmes d’exploitation complexes, comparables à l’informatique des années 1960, et nous refaisons l’informatique à nouveau. Ils sont actuellement disponibles via le partage de temps et distribués comme une utilité publique. Ce qui est nouveau et sans précédent, c’est qu’ils ne sont pas entre les mains de quelques gouvernements et entreprises, mais entre les mains de nous tous, car nous avons tous un ordinateur, et c’est juste du logiciel. ChatGPT a été envoyé à nos ordinateurs, à des milliards de personnes, instantanément et du jour au lendemain, ce qui est insensé. Maintenant, c’est à nous d’entrer dans l’industrie et de programmer ces ordinateurs. C’est assez remarquable.

Psychologie des LLM

Avant de programmer les LLM, nous devons réfléchir à ce qu’ils sont. J’aime parler de leur psychologie. Je vois les LLM comme des esprits humains, des simulations stochastiques de personnes, où le simulateur est un transformateur autorégressif. C’est un réseau neuronal qui avance token par token, avec presque la même quantité de calcul pour chaque token. Ce simulateur est ajusté à tout le texte que nous avons sur internet, et ainsi de suite, ce qui lui donne une psychologie émergente semblable à celle des humains.

La première chose que vous remarquez, c’est que les LLM ont une connaissance encyclopédique et une mémoire impressionnante. Ils peuvent se souvenir de beaucoup plus de choses qu’un individu humain, car ils ont lu énormément. Cela me rappelle le film Rain Man, que je recommande vivement. Dustin Hoffman y joue un savant autiste avec une mémoire presque parfaite, capable de lire un annuaire téléphonique et de se souvenir de tous les noms et numéros. Les LLM sont similaires : ils peuvent se souvenir de hachages SHA et de toutes sortes de choses très facilement. Ils ont donc des superpouvoirs à certains égards.

Mais ils ont aussi des déficits cognitifs. Ils hallucinent beaucoup, inventent des choses, et n’ont pas un très bon modèle interne de connaissance de soi, bien que cela s’améliore. Ils affichent une intelligence inégale : ils sont surhumains dans certains domaines de résolution de problèmes, mais font des erreurs qu’aucun humain ne ferait, comme insister que 9.11 est supérieur à 9.9 ou qu’il y a deux « r » dans « strawberry ». Ce sont des exemples célèbres, mais il y a des aspérités sur lesquelles on peut trébucher.

Ils souffrent aussi d’une sorte d’amnésie rétrograde. Si un collègue rejoint votre organisation, il apprendra au fil du temps à connaître l’organisation, gagnera du contexte, rentrera chez lui, dormira, consolidera ses connaissances et développera une expertise. Les LLM ne le font pas nativement, et ce n’est pas quelque chose qui a été résolu dans la recherche et développement des LLM. Les fenêtres de contexte sont comme une mémoire de travail, et vous devez programmer cette mémoire de travail assez directement, car ils ne deviennent pas plus intelligents par défaut. Beaucoup de gens se trompent sur ces analogies. Je recommande de regarder les films Memento et 50 First Dates, où les protagonistes ont leurs poids fixés et leurs fenêtres de contexte effacées chaque matin, ce qui rend le travail ou les relations problématiques.

Il y a aussi des limitations liées à la sécurité. Les LLM sont assez crédules, vulnérables aux risques d’injection de prompts, et peuvent divulguer vos données. Il y a donc de nombreuses considérations liées à la sécurité.

En résumé, vous devez considérer cette chose surhumaine avec des déficits cognitifs et des problèmes, tout en étant extrêmement utile. Comment les programmer et contourner leurs déficits tout en profitant de leurs superpouvoirs ?

Opportunités avec les LLM

Passons maintenant aux opportunités d’utilisation de ces modèles et à certaines des plus grandes opportunités. Ce n’est pas une liste exhaustive, juste quelques éléments que je trouve intéressants pour cette conférence.

Applications à autonomie partielle

Je suis enthousiaste à propos de ce que j’appelle les applications à autonomie partielle. Prenons l’exemple du codage. Vous pouvez aller directement sur ChatGPT, copier-coller du code, des rapports de bogues, obtenir du code et tout copier-coller. Pourquoi faire cela ? Pourquoi aller directement au système d’exploitation ? Il est beaucoup plus logique d’avoir une application dédiée. Beaucoup d’entre vous utilisent probablement Cursor, que j’utilise aussi. Cursor est un très bon exemple d’une application LLM précoce avec des propriétés utiles pour toutes les applications LLM.

Vous remarquerez que nous avons une interface traditionnelle qui permet à un humain de faire tout le travail manuellement comme avant, mais en plus, nous avons cette intégration LLM qui permet d’avancer par plus gros morceaux. Voici quelques propriétés des applications LLM que je trouve utiles à souligner :

Les LLM gèrent une grande partie de la gestion du contexte.

Ils orchestrent plusieurs appels aux LLM. Dans le cas de Cursor, il y a des modèles d’embedding pour tous vos fichiers, des modèles de chat, des modèles qui appliquent des différences au code, et tout cela est orchestré pour vous.

Une interface graphique spécifique à l’application est très importante. Vous ne voulez pas parler directement au système d’exploitation en texte. Le texte est difficile à lire, interpréter et comprendre, et vous ne voulez pas prendre certaines actions nativement en texte. Il est beaucoup plus facile de voir une différence en rouge et vert, de voir ce qui est ajouté ou soustrait, et d’utiliser des commandes comme Cmd+Y pour accepter ou Cmd+N pour rejeter, plutôt que de devoir l’écrire en texte. Une interface graphique permet à un humain d’auditer le travail de ces systèmes faillibles et d’aller plus vite.

Ce que j’appelle le curseur d’autonomie. Dans Cursor, vous pouvez faire une complétion par tabulation, où vous êtes principalement en charge. Vous pouvez sélectionner un morceau de code et utiliser Cmd+K pour modifier juste ce morceau, Cmd+L pour modifier tout le fichier, ou Cmd+I pour laisser l’application faire ce qu’elle veut dans tout le dépôt, ce qui est la version agentique à pleine autonomie. Vous contrôlez ce curseur d’autonomie, et selon la complexité de la tâche, vous pouvez ajuster le niveau d’autonomie que vous êtes prêt à céder.

Un autre exemple d’application LLM réussie est Perplexity. Elle possède des fonctionnalités similaires à celles que j’ai mentionnées pour Cursor. Elle regroupe beaucoup d’informations, orchestre plusieurs LLM, et a une interface graphique qui permet d’auditer une partie de son travail, comme citer des sources que vous pouvez inspecter. Elle a aussi un curseur d’autonomie : vous pouvez faire une recherche rapide, une recherche approfondie, ou une recherche très approfondie et revenir 10 minutes plus tard. Ce sont différents niveaux d’autonomie que vous cédez à l’outil.

Je me demande à quoi cela ressemble si beaucoup de logiciels deviennent partiellement autonomes. Pour ceux d’entre vous qui maintiennent des produits et services, comment allez-vous rendre vos produits et services partiellement autonomes ? Un LLM peut-il voir tout ce qu’un humain peut voir ? Un LLM peut-il agir de toutes les manières dont un humain pourrait agir ? Les humains peuvent-ils superviser et rester dans la boucle de cette activité, car ce sont des systèmes faillibles qui ne sont pas encore parfaits ? À quoi ressemble une différence dans Photoshop, par exemple ? Beaucoup de logiciels traditionnels ont actuellement des interrupteurs et des éléments conçus pour les humains. Tout cela doit changer et devenir accessible aux LLM.

Un point que je veux souligner avec beaucoup de ces applications LLM, qui ne reçoit peut-être pas autant d’attention qu’il le devrait, est que nous coopérons maintenant avec des IA. Habituellement, elles génèrent, et nous, humains, vérifions. Il est dans notre intérêt de faire tourner cette boucle le plus rapidement possible pour accomplir beaucoup de travail. Il y a deux façons principales d’y parvenir :

Accélérer la vérification. Les interfaces graphiques sont extrêmement importantes pour cela, car elles exploitent le GPU de votre vision par ordinateur dans votre tête. Lire du texte est laborieux et pas amusant, mais regarder des choses est amusant et constitue une autoroute vers votre cerveau. Les interfaces graphiques sont donc très utiles pour auditer les systèmes et pour les représentations visuelles en général.

Garder l’IA en laisse. Beaucoup de gens s’emballent trop avec les agents IA. Ce n’est pas utile de recevoir une différence de 10 000 lignes de code dans mon dépôt. Je reste le goulot d’étranglement, même si ces 10 000 lignes sortent instantanément. Je dois m’assurer que cela n’introduit pas de bogues, que c’est correct, et qu’il n’y a pas de problèmes de sécurité. Il est dans notre intérêt de faire tourner ce flux très rapidement et de garder l’IA en laisse, car elle devient trop réactive.

Quand je fais du codage assisté par IA, si je code tranquillement, tout va bien, mais si j’essaie d’avancer dans mon travail, ce n’est pas génial d’avoir un agent trop réactif qui fait tout. Je travaille toujours sur de petits morceaux incrémentiels, je veux m’assurer que tout va bien, je veux faire tourner cette boucle très rapidement, et je travaille sur des choses concrètes et uniques. Beaucoup d’entre vous développent probablement des façons similaires de travailler avec les LLM. J’ai aussi vu plusieurs articles de blog qui tentent de développer ces meilleures pratiques pour travailler avec les LLM. J’en ai lu un récemment qui était assez bon, discutant de certaines techniques, notamment sur la manière de garder l’IA en laisse. Par exemple, si votre invite est vague, l’IA pourrait ne pas faire exactement ce que vous vouliez, et la vérification échouera. Vous demanderez autre chose, et si la vérification échoue, vous commencerez à tourner en rond. Il est donc plus logique de passer un peu plus de temps à être plus précis dans vos invites, ce qui augmente la probabilité d’une vérification réussie, et vous pouvez avancer.

Dans mon propre travail, je m’intéresse actuellement à ce que l’éducation pourrait être avec l’IA et les LLM. Beaucoup de mes réflexions portent sur la manière de garder l’IA en laisse. Je ne pense pas que cela fonctionne de dire à ChatGPT « Hey, enseigne-moi la physique ». L’IA se perd dans les bois. Pour moi, ce sont deux applications distinctes : une pour un enseignant qui crée des cours, et une qui prend ces cours et les sert aux étudiants. Dans les deux cas, nous avons cet artefact intermédiaire d’un cours qui est auditable, nous pouvons nous assurer qu’il est bon, cohérent, et l’IA est gardée en laisse par rapport à un certain programme, une certaine progression de projets, etc. C’est une façon de garder l’IA en laisse, et je pense que cela a beaucoup plus de chances de fonctionner.

Une autre analogie à laquelle je fais référence est mon expérience chez Tesla, où j’ai travaillé pendant cinq ans sur un produit à autonomie partielle, qui partage beaucoup de caractéristiques. Par exemple, dans le tableau de bord, il y a l’interface graphique du pilote automatique, qui montre ce que le réseau neuronal voit. Nous avions le curseur d’autonomie, et au fil de mon temps là-bas, nous faisions de plus en plus de tâches autonomes pour l’utilisateur. Une petite histoire : la première fois que j’ai conduit un véhicule autonome, c’était en 2013. Un ami qui travaillait chez Waymo m’a proposé de faire un tour à Palo Alto. J’ai pris une photo avec Google Glass à l’époque – beaucoup d’entre vous sont si jeunes que vous ne savez peut-être même pas ce que c’est. Nous sommes montés dans la voiture, avons fait un trajet d’environ 30 minutes sur les autoroutes et les rues de Palo Alto, et ce trajet était parfait, sans aucune intervention. C’était en 2013, il y a 12 ans, et cela m’a frappé, car à l’époque, après ce trajet parfait, j’ai pensé que la conduite autonome était imminente. Mais nous sommes en 2025, et nous travaillons toujours sur l’autonomie, sur les agents de conduite. Même maintenant, nous n’avons pas vraiment résolu le problème. Vous voyez peut-être des Waymo circuler sans conducteur, mais il y a encore beaucoup de téléopération et d’humains dans la boucle. Nous n’avons pas encore déclaré le succès, mais je pense que cela va réussir à ce stade, mais cela a pris beaucoup de temps.

Le logiciel est vraiment complexe, tout comme la conduite. Quand je vois des affirmations comme « 2025 est l’année des agents », je m’inquiète. Je pense que c’est la décennie des agents, et cela va prendre du temps. Nous avons besoin d’humains dans la boucle, nous devons le faire prudemment. Soyons sérieux, c’est du logiciel.

Une autre analogie que je considère toujours est l’armure d’Iron Man. J’adore Iron Man, je pense que c’est tellement juste à bien des égards concernant la technologie et comment elle va se déployer. Ce que j’aime dans l’armure d’Iron Man, c’est qu’elle est à la fois une augmentation – Tony Stark peut la piloter – et un agent. Dans certains films, l’armure est assez autonome, peut voler et trouver Tony, etc. C’est le curseur d’autonomie : nous pouvons construire des augmentations ou des agents, et nous voulons faire un peu des deux. Mais à ce stade, en travaillant avec des LLM faillibles, je dirais qu’il s’agit moins de robots Iron Man et plus de combinaisons Iron Man. Il s’agit moins de construire des démos flashy d’agents autonomes et plus de construire des produits à autonomie partielle. Ces produits ont des interfaces graphiques personnalisées et une expérience utilisateur, conçus pour que la boucle de génération-vérification humaine soit très rapide, tout en gardant à l’esprit qu’il est en principe possible d’automatiser ce travail. Il devrait y avoir un curseur d’autonomie dans votre produit, et vous devriez réfléchir à comment faire glisser ce curseur pour rendre votre produit plus autonome avec le temps.

Programmation en anglais

Passons à une autre dimension que je trouve très unique. Non seulement il y a un nouveau type de langage de programmation qui permet l’autonomie dans les logiciels, mais comme je l’ai mentionné, il est programmé en anglais, qui est une interface naturelle. Soudain, tout le monde est programmeur, car tout le monde parle une langue naturelle comme l’anglais. C’est extrêmement optimiste et très intéressant pour moi, et totalement sans précédent. Avant, il fallait passer cinq à dix ans à étudier pour pouvoir faire quelque chose en logiciel. Ce n’est plus le cas.

Quelqu’un a-t-il entendu parler du « vibe coding » ? C’est un tweet qui a introduit ce concept, et on m’a dit que c’est maintenant un mème majeur. Une anecdote amusante : je suis sur Twitter depuis environ 15 ans, et je n’ai toujours aucune idée de quel tweet va devenir viral et lequel va passer inaperçu. Je pensais que ce tweet allait être dans la deuxième catégorie, juste une pensée spontanée, mais il est devenu un mème total. Je ne peux pas vraiment prévoir, mais je suppose qu’il a touché une corde sensible et donné un nom à quelque chose que tout le monde ressentait mais ne pouvait pas exprimer en mots. Maintenant, il y a même une page Wikipédia pour ça.

Tom Wolf de Hugging Face a partagé une vidéo magnifique que j’adore, montrant des enfants en train de faire du vibe coding. Je trouve cette vidéo tellement saine. Comment peut-on regarder cette vidéo et se sentir mal à propos de l’avenir ? L’avenir est prometteur. Je pense que cela deviendra une porte d’entrée vers le développement logiciel. Je ne suis pas pessimiste quant à l’avenir de cette génération.

J’ai aussi essayé le vibe coding, car c’est tellement amusant. C’est génial quand vous voulez construire quelque chose de super personnalisé qui n’existe pas et que vous voulez juste tenter le coup un samedi. J’ai construit une application iOS, et je ne sais pas programmer en Swift, mais j’ai été choqué de pouvoir construire une application super basique. Je ne vais pas l’expliquer, c’est vraiment idiot, mais c’était juste une journée de travail, et ça fonctionnait sur mon téléphone le même jour. J’étais comme « Wow, c’est incroyable ». Je n’ai pas eu à lire des manuels sur Swift pendant cinq jours pour commencer.

J’ai aussi fait du vibe coding pour une application appelée MenuGen, qui est en ligne sur menu.app. J’avais ce problème où j’arrive dans un restaurant, je lis le menu, et je n’ai aucune idée de ce que sont les plats, et j’ai besoin d’images. Ça n’existait pas, alors je me suis dit « Je vais le coder en mode vibe ». Vous allez sur menu.app, prenez une photo d’un menu, et MenuGen génère les images. Tout le monde reçoit 5 $ de crédits gratuits en s’inscrivant, ce qui est un centre de coûts majeur dans ma vie. Cette application me fait perdre beaucoup d’argent.

Ce qui est fascinant avec MenuGen, c’est que coder la partie vibe coding était la partie facile. La plupart des difficultés sont survenues quand j’ai essayé de la rendre réelle, avec l’authentification, les paiements, le nom de domaine, et le déploiement sur Vercel. Tout cela n’était pas du code, c’était du DevOps, cliquer sur des choses dans le navigateur, et c’était extrêmement lent, ça a pris une autre semaine. J’avais une démo de MenuGen fonctionnant sur mon ordinateur portable en quelques heures, mais il m’a fallu une semaine pour la rendre réelle, car c’était vraiment agaçant. Par exemple, ajouter une connexion Google à votre page web implique une énorme quantité d’instructions d’une bibliothèque comme Clerk, me disant d’aller à telle URL, de cliquer sur tel menu déroulant, de choisir ceci, d’aller là et de cliquer sur ça. C’est comme si un ordinateur me disait quoi faire. Pourquoi est-ce que je fais ça ? Fais-le toi-même !

Construire pour les agents

La dernière partie de ma conférence se concentre sur la possibilité de construire pour les agents. Je ne veux pas faire ce travail, les agents peuvent-ils le faire ? Grossièrement, je pense qu’il y a une nouvelle catégorie de consommateurs et de manipulateurs d’informations numériques. Avant, c’étaient juste les humains via les interfaces graphiques ou les ordinateurs via les API. Maintenant, nous avons une chose complètement nouvelle : les agents. Ce sont des ordinateurs, mais ils sont un peu comme des humains, des esprits humains sur internet, et ils doivent interagir avec notre infrastructure logicielle. Pouvons-nous construire pour eux ? C’est une nouveauté.

Par exemple, vous pouvez avoir un fichier robots.txt sur votre domaine pour indiquer aux robots d’indexation comment se comporter sur votre site. De la même manière, vous pourriez avoir un fichier llm.txt, un simple fichier Markdown expliquant à un LLM de quoi parle ce domaine. C’est très lisible pour un LLM. S’il devait récupérer le HTML de votre page web et essayer de le parser, ce serait très sujet aux erreurs et difficile. Nous pouvons parler directement aux LLM, ça vaut le coup.

Une grande quantité de documentation est actuellement écrite pour les humains, avec des listes, du texte en gras, des images, ce qui n’est pas directement accessible aux LLM. Certains services commencent à transformer leurs documentations pour qu’elles soient spécifiquement destinées aux LLM. Vercel et Stripe, par exemple, sont des pionniers ici, mais j’en ai vu d’autres. Ils proposent leur documentation en Markdown, qui est super facile à comprendre pour les LLM. C’est génial.

Un exemple simple de mon expérience : certains d’entre vous connaissent peut-être 3Blue1Brown, qui fait de magnifiques vidéos d’animation sur YouTube. Il a écrit une bibliothèque appelée Manim, et je voulais faire mes propres animations. Il y a une documentation extensive sur l’utilisation de Manim, mais je ne voulais pas la lire. J’ai donc copié-collé tout le contenu dans un LLM, décrit ce que je voulais, et ça a fonctionné directement. Le LLM m’a créé une animation exactement comme je le voulais, et j’étais comme « Wow, c’est incroyable ». Si nous rendons les documentations lisibles pour les LLM, cela va débloquer une énorme quantité d’utilisations, et je pense que c’est merveilleux et que ça devrait se faire plus souvent.

Malheureusement, il ne s’agit pas seulement de prendre vos documentations et de les mettre en Markdown, ce qui est la partie facile. Il faut aussi modifier les documentations, car chaque fois qu’elles disent « cliquez ici », c’est mauvais. Un LLM ne peut pas nativement prendre cette action pour le moment. Vercel, par exemple, remplace chaque occurrence de « cliquez » par une commande curl équivalente que votre agent LLM pourrait exécuter à votre place. Je trouve cela très intéressant. Il y a aussi le protocole de contexte de modèle d’Anthropic, une autre façon de parler directement aux agents en tant que nouveaux consommateurs et manipulateurs d’informations numériques. Je suis très optimiste sur ces idées.

J’aime aussi plusieurs petits outils ici et là qui aident à ingérer des données dans des formats très adaptés aux LLM. Par exemple, quand je vais sur un dépôt GitHub comme mon dépôt nanoGPT, je ne peux pas le donner à un LLM et poser des questions, car c’est une interface humaine sur GitHub. Mais si vous changez l’URL de GitHub à GetIngest, cela concatène tous les fichiers en un seul texte géant, crée une structure de répertoire, etc., et c’est prêt à être copié-collé dans votre LLM préféré. Un exemple encore plus frappant est DeepWiki, où ce n’est pas juste le contenu brut des fichiers. Devon, par exemple, analyse le dépôt GitHub et construit toute une page de documentation pour votre dépôt, ce qui est encore plus utile à copier-coller dans votre LLM.

J’adore tous ces petits outils où vous changez simplement l’URL, et ça rend quelque chose accessible à un LLM. C’est très bien, et il devrait y en avoir beaucoup plus. Une note supplémentaire : il est tout à fait possible que dans le futur – et même aujourd’hui – les LLM puissent naviguer et cliquer sur des choses. Mais je pense toujours qu’il vaut la peine de rencontrer les LLM à mi-chemin et de faciliter leur accès à toutes ces informations, car c’est encore assez coûteux et beaucoup plus difficile. Il y aura une longue traîne de logiciels qui ne s’adapteront pas, car ce ne sont pas des dépôts ou des infrastructures numériques très actifs. Nous aurons besoin de ces outils, mais pour tous les autres, je pense qu’il vaut la peine de trouver un point de rencontre.

Conclusion

Quel moment incroyable pour entrer dans l’industrie ! Nous devons réécrire une tonne de code, qui sera écrit par des professionnels et des codeurs. Les LLM sont un peu comme des utilités publiques, un peu comme des fabriques, mais surtout comme des systèmes d’exploitation. C’est tellement tôt, c’est comme les années 1960 des systèmes d’exploitation, et beaucoup d’analogies se croisent. Ces LLM sont comme des esprits humains faillibles avec lesquels nous devons apprendre à travailler. Pour le faire correctement, nous devons ajuster notre infrastructure en conséquence.

Quand vous construisez des applications LLM, j’ai décrit certaines façons de travailler efficacement avec ces LLM et certains outils qui rendent cela possible, ainsi que comment faire tourner cette boucle très rapidement pour créer des produits à autonomie partielle. Beaucoup de code devra aussi être écrit plus directement pour les agents. En revenant à l’analogie de l’armure d’Iron Man, je pense que sur la prochaine décennie, nous allons faire glisser le curseur d’autonomie de gauche à droite, et il sera très intéressant de voir à quoi cela ressemble. J’ai hâte de le construire avec vous tous. Merci.

Après avoir écouté la vidéo, je vous invite à réfléchir aux questions suivantes.

1.  Comment les paradigmes du logiciel 1.0, 2.0 et 3.0 diffèrent-ils dans leur approche de la programmation, et quelles implications cela a-t-il pour les choix que vous feriez en tant que développeur face à une tâche spécifique ?
    
2.  En quoi l’analogie des grands modèles de langage (LLM) avec un système d’exploitation vous aide-t-elle à comprendre leur rôle dans le développement logiciel actuel, et quelles limites cette analogie pourrait-elle avoir ?
    
3.  Quels problèmes éthiques ou pratiques pourraient surgir de l’utilisation croissante de la programmation en langage naturel, comme le « vibe coding », et comment les développeurs peuvent-ils y répondre pour garantir des applications fiables et accessibles ?
    

Robot [#](#robot)
-----------------

Dans ce cours, vous êtes encouragé à utiliser l’intelligence artificielle pour mieux apprendre à programmer. [L’Université TÉLUQ met à votre disposition un robot conversationnel dédié au cours](https://rc-inf1220.teluq.ca/#). Ce robot, basé sur des technologies avancées d’IA, vous permettra d’obtenir des réponses personnalisées à vos questions, de clarifier des concepts complexes et de recevoir des exemples de code pertinents. En interagissant avec cet outil, vous pourrez approfondir votre compréhension des notions abordées, pratiquer vos compétences en programmation et progresser à votre rythme, tout en bénéficiant d’un soutien adapté à vos besoins. Vous pouvez aussi utiliser d’autres outils comme ChatGPT, copilot, Grok, etc.

Le cours INF 1220 a probablement été le premier cours au Québec à disposer d’un robot conversationnel. Je vous invite à consulter cet article par madame Roy de Radio-Canada:

*   [IA à l’université : mieux comprendre pour mieux se préparer](https://ici.radio-canada.ca/nouvelle/2067576/teluq-universite-laval-ia-chatgpt-robot)

Pour maximiser l’efficacité de ces outils d’intelligence artificielle, il est recommandé de poser des questions précises et bien formulées. Par exemple, demandez des explications sur des erreurs de code spécifiques, des suggestions pour optimiser vos programmes ou des éclaircissements sur des concepts théoriques. Ces outils peuvent également vous aider à explorer des approches alternatives pour résoudre des problèmes de programmation, renforçant ainsi votre créativité et votre autonomie. En combinant l’utilisation de ces ressources avec les activités du cours, vous développerez des compétences solides et une meilleure confiance en vos capacités de programmation.

 [![Previous](/inf1220-hugo/svg/backward.svg "Modèle du cours") Modèle du cours](/inf1220-hugo/docs/modules/module1/teluq/) [Autoévaluation ![Next](/inf1220-hugo/svg/forward.svg "Autoévaluation")](/inf1220-hugo/docs/modules/module1/autoevaluation/) 


*   [Robot](#robot)

## Autoévaluation


*   [Connaissances technologiques](#connaissances-technologiques)
*   [Mathématiques](#mathématiques)
*   [Autoévaluation (mathématiques)](#autoévaluation-mathématiques)
*   [Autoévaluation (aptitude en programmation)](#autoévaluation-aptitude-en-programmation)

*   [Maîtrise de l’anglais](#maîtrise-de-langlais)
*   [Un cours difficile ?](#un-cours-difficile-)

Autoévaluation [#](#auto%c3%a9valuation)
========================================

Avant de débuter le cours, il est important de faire le point sur votre préparation. Je vous invite donc à faire une autoévaluation.

Connaissances technologiques [#](#connaissances-technologiques)
---------------------------------------------------------------

Le cours ne nécessite pas une connaissance approfondie du fonctionnement des ordinateurs, mais il est utile d’avoir une certaine connaissance de base. Vous devriez savoir que les ordinateurs disposent d’un processeur, de mémoire, de disques, etc. et qu’ils fonctionnent à l’aide d’un système d’exploitation. Si vous ne vous êtes jamais intéressés à ces concepts de base, il peut être utile que vous preniez un peu de votre temps pour faire des recherches sur ces questions. Il peut être difficile de suivre ce cours si vous ne savez vraiment pas ce qu’est un processeur ou de la mémoire informatique.

Mathématiques [#](#math%c3%a9matiques)
--------------------------------------

Pour pouvoir faire de l’informatique, il convient de connaître les mathématiques. La division euclidienne, par exemple, offre une perspective fondamentale sur la décomposition des nombres. Elle ne se limite pas à un calcul, mais exprime une relation entre un dividende, un diviseur, un quotient et un reste. Considérons \\( 75 \\div 8 \\) : le quotient est \\( 9 \\) et le reste \\( 3 \\), car \\( 8 \\times 9 = 72 \\) et \\( 75 - 72 = 3 \\). De même, pour \\( 20 \\div 6 \\), le quotient est \\( 3 \\) et le reste \\( 2 \\). Le reste, toujours inférieur au diviseur, capture l’excédent d’une division imparfaite. Cette idée devient puissante lorsqu’on remarque, par exemple, que si \\( x \\div y \\) laisse un reste de \\( 1 \\), alors \\( x - 1 \\) est un multiple de \\( y \\), révélant une propriété intrinsèque de divisibilité. Les nombres se déclinent en catégories – entiers, réels, rationnels, irrationnels – chacune porteuse de propriétés distinctes. Le nombre \\( \\sqrt{2} \\), réel et irrationnel, défie toute représentation fractionnaire, incarnant une rupture avec les nombres rationnels. Le théorème fondamental de l’arithmétique, quant à lui, établit que tout entier positif supérieur à \\( 1 \\) se factorise de manière unique en nombres premiers. Ainsi, \\( 28 = 2^2 \\times 7 \\). Si \\( x \\) divise un nombre impair \\( z \\), alors \\( x \\) est nécessairement impair, car un diviseur pair engendrerait un résultat pair, contredisant l’hypothèse. Les opérations algébriques, régies par un ordre de priorité, reflètent une logique de structuration des calculs. Les parenthèses redéfinissent cet ordre, comme dans \\( (2 + 3) \\times 5 = 25 \\), où l’addition prime, contrairement à \\( 2 + 3 \\times 5 = 17 \\), où la multiplication domine. Les exposants et les logarithmes sont un exemple de fonction inverse : nous avons que \\( \\log\_3(81) = 4 \\) car \\( 3^4 = 81 \\). La propriété \\( \\frac{\\log x}{\\log b} = \\log\_b x \\) est fort utile. La factorielle, comme \\( 4! = 4 \\times 3 \\times 2 \\times 1 = 24 \\), quantifie les arrangements possibles. Pour la probabilité d’obtenir une somme de \\( 7 \\) avec deux dés, on recense les cas favorables \\( (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) \\), soit 6, sur 36 résultats, donnant \\( \\frac{6}{36} = \\frac{1}{6} \\). On peut trier les objects selon différents ordres. L’ordre lexicographique, appliqué à des nombres comme \\( 3, 30, 4 \\), les trie comme des chaînes \\( 3, 30, 4 \\), illustrant une logique de classement importée du langage. La notion de nombre en base \\( b \\) désigne la manière dont un nombre est représenté dans un système de numération où \\( b \\) est le nombre d’unités distinctes utilisées, appelées chiffres. Nous utilisons normalement des nombres en base 10, mais d’autres bases sont utilisées en informatique.

**Si vous n'avez pas fait les mathématiques du collégial ou pris un cours d'appoint équivalent, vous ne pouvez pas suivre INF 1220**. Si on vous demande de suivre un cours d'appoint en mathématiques, vous devez suivre ce cours d'appoint **avant** de vous inscrire à INF 1220. Il est de votre responsabilité d'y voir.

Si vous avez réussi les mathématiques du collégial il y a trop longtemps, vous devez soit les réviser, soit prendre un cours d'appoint. On s'attend à ce que les étudiants de ce cours, et les étudiants qui adoptent un cheminement en informatique généralement, aient de longue date une aisance mathématique. Par exemple, si vous avez complété vos études secondaires au Québec récemment, on s'attend à ce que vous apparteniez aux profils Technico-Science ou Sciences Naturelles plutôt que Culture, Société et Technique.

Autoévaluation (mathématiques) [#](#auto%c3%a9valuation-math%c3%a9matiques)
---------------------------------------------------------------------------

Faites l'autoévaluation mathématique suivante avant de continuer au sein du cours. Ces questions devraient être faciles, même évidentes, si vous avez une préparation adéquate.

Quiz de mathématiques
=====================

Répondez à chaque question pour tester vos connaissances. Un retour vous sera fourni après chaque réponse.

Score : 0 / 0

Soumettre

Recommencer


Si ces questions ne sont pas faciles pour vous, ne continuez pas dans ce cours!!! Vous devez soit réviser vos mathématiques de base, et peut-être suivre un cours d'appoint tout en poursuivant des études complémentaires sur une base autonome.

Certains étudiants qui n'ont pas la préparation suffisante décident de tout de même poursuivre dans le cours sans pour autant prévoir du temps supplémentaire pour l'étude de la matière vue au secondaire et au collégial. Malheureusement pour eux, ils se rendent souvent compte qu'ils vont faire face à des difficultés alors qu'il n'est plus possible d'abandonner le cours sans pénalité. Parfois, ces étudiants s'attendaient à tort que le cours leur permette de combler les failles dans leur préparation, ou bien alors ils ne prennent pas sérieusement nos avertissements. Soyez responsable et évitez donc les ennuis: assurez-vous d'avoir une préparation adéquate avant de poursuivre dans le cours !

Autoévaluation (aptitude en programmation) [#](#auto%c3%a9valuation-aptitude-en-programmation)
----------------------------------------------------------------------------------------------

Pour se préparer au cours INF 1220, il est crucial de développer une rigueur intellectuelle et une capacité à raisonner de manière abstraite, deux qualités indispensables à la programmation. Programmer ne se limite pas à écrire des lignes de code : c’est un exercice de pensée structurée qui exige de décomposer un problème en étapes logiques, de les traduire en instructions précises et de vérifier méticuleusement leur exactitude. Un programme fonctionne ou échoue sans demi-mesure, ce qui impose une discipline constante : écrire, tester, corriger, puis tester à nouveau. La patience et l’attention aux détails sont essentielles, car une simple erreur, comme une virgule mal placée, peut compromettre un programme entier. S’entraîner à résoudre des problèmes logiques, comme déterminer qui de Jean ou Pierre arrive en premier au travail dans un énoncé où Jean est immédiatement suivi par Pierre, aide à affûter cette précision. Si de tels énoncés semblent opaques ou exigent un effort disproportionné, il peut être utile de renforcer ses bases en logique avant d’aborder le cours.

Question 1 [#](#question-1)
===========================

_Jean et Pierre travaillent ensemble. Jean s’assure d’être toujours immédiatement suivi par Pierre quand ils arrivent au travail. Qui arrive le premier au travail ?_

Problème de logique : qui arrive le premier ?
=============================================

Jean et Pierre travaillent ensemble. Jean s’assure d’être toujours immédiatement suivi par Pierre quand ils arrivent au travail. Qui arrive le premier au travail ?

 Jean Pierre  Les deux

Soumettre


Si cet énoncé ne vous semble pas clair et que vous ne trouvez pas immédiatement la bonne réponse, il est probable que vous ne devriez pas suivre le cours INF 1220.

Question 2 [#](#question-2)
===========================

Supposons que vous disposiez d’un livre ayant des pages numérotées (1, 2, 3, …). Vous souhaitez lire toutes les pages. Vous appliquez la recette suivante.

Vous disposez d’un calepin (effaçable) où vous pouvez écrire un nombre entier, et un seul nombre entier. Vous écrivez sur le calepin le nombre zéro (0). Vous passez ensuite à l’étape A.

*   Étape A : Vous prenez le calepin, vous consultez le nombre qui y est écrit, vous lui ajoutez un, et vous écrivez le résultat sur le calepin. Par exemple, si la valeur lue est “0”, vous la remplacez par “1”. Vous passez ensuite à l’étape B.
*   Étape B : Vous prenez le calepin, vous consultez le nombre qui y est écrit, vous allez à la page correspondante au nombre lu dans le livre, vous lisez la page en question. Vous passez ensuite à l’étape C.
*   Étape C : Vous prenez le calepin, vous consultez le nombre qui y est écrit. Si le nombre lu excède le nombre de pages du livre, vous terminez la recette et vous fermez définitivement le livre. Autrement, vous retournez à l’étape A.

> Essayez d’appliquer cette recette avec un livre comptant cinq pages. Que constatez-vous ?

Utilisez cette application pour explorer le problème.

Simulation de l'algorithme de lecture
=====================================

Étape : Initialisation  
Calepin : 0  
Pages lues : Aucune

Prochaine étape Réinitialiser


Cette recette est erronée. Si vous êtes incapable de voir l’erreur rapidement, ou si ça vous demande beaucoup d’effort, il est possible que vous n’ayez pas de bonnes aptitudes pour la programmation et que le cours INF 1220 ne soit pas pour vous. Cela ne signifie pas que vous ne puissiez pas apprendre à programmer, mais le cours INF 1220 a été pensé en fonction d’étudiants qui ont un certain degré de préparation.

Si vous n’avez pas les aptitudes requises, le cours peut vous paraître inaccessible. Il est possible que vous deviez consacrer beaucoup plus que 9 heures par semaine pour réussir le cours. Vous devez garder à l’esprit que le cours INF 1220 est un cours d’informatique universitaire offert au sein d’un cursus scientifique menant à des diplômes en informatique.

Maîtrise de l’anglais [#](#ma%c3%aetrise-de-langlais)
-----------------------------------------------------

Le site web du cours, ses travaux, ses vidéos et ses exercices, ainsi que notre manuel (Java pas à pas) et notre manuel de référence sont tous en français. Par contre, l'anglais est un incontournable en informatique. De temps en temps, nous allons donc vous offrir des liens vers des ressources (optionnelles) en anglais.

Si vous ne maîtrisez pas l'anglais, vous devez savoir qu'il est essentiellement impossible de faire carrière ou d'avancer dans le domaine de l'informatique sans une maîtrise élémentaire de l'anglais.

L'informatique s'est développée d'abord et avant tout dans les pays anglophones (principalement la Grande-Bretagne et les États-Unis). La grande puissance Américaine domine le domaine de l'informatique. S'il est possible d'utiliser des ordinateurs sans maîtriser l'anglais, il n'est pas envisageable de développer du logiciel sans maîtriser l'anglais.

Un cours difficile ? [#](#un-cours-difficile-)
----------------------------------------------

Le cours est un cours d'informatique universitaire, il est conçu de manière à vous préparer à suivre une formation plus poussée en informatique. Il ne s'agit donc pas d'un cours technique qui vise à vous former pour un travail pratique et immédiat. On ne cherche pas à apprendre la programmation le plus rapidement possible, mais bien à établir des bases solides en étudiant les principes de base comme la notion d'algorithme. Notre objectif premier est de vous préparer à des cours plus avancés en informatique. Il ne s'agit donc pas d'un cours grand public. Nous y utilisons une terminologie propre à l'informatique. Nous n'évitons pas les mathématiques. Le contenu du cours, la charge de travail, l'ampleur de travaux et la composition de l'examen sont comparables à ce que vous trouvez au sein de cours d'introduction à la programmation dans les universités québécoises. Il s'agit tout de même d'un cours d'introduction: si avez pris des cours de programmation auparavant, ou que vous avez une longue expérience avec la programmation informatique, ce cours n'est sans doute pas pour vous.

La quasi-totalité des nos étudiants au sein du cours INF 1220 viennent de trois programmes: développement logiciel (0127), informatique appliquée (4128) et majeure en informatique (6010). Sur 250 étudiants par année, il y a environ 5 échecs et 20 abandons. Nous travaillons continuellement pour améliorer le taux de réussite de nos étudiants, mais rien ne peut remplacer un engagement sérieux de la part des étudiants. Ceci étant dit, nous sommes fiers du fait que parmi les étudiants qui terminent le cours, la grande majorité apprécient beaucoup le cours. Il s'agit souvent d'un des cours les mieux évalués au sein de notre université.

Voici quelques commentaires de nos étudiants :

1.  _INF 1220 une vraie initiation au paradigme OO pour moi, et j'ai aussi réalisé que mon cours sur Udemy était insuffisant, voire médiocre..._
2.  _J'ai un bac en administration et ce cours est de loin le cours le plus difficile que j'ai suivi. Il a parfois fallu que je cherche longtemps sur Internet, et j'ai souvent été frustré par le Java, mais maintenant que j'ai terminé le cours, j'ai vraiment l'impression d'avoir appris à programmer._

Le taux de réussite du cours est d'environ 80%. En d'autres termes, de tous les étudiants qui s'inscrivent et cheminent dans le cours, 80% auront la note de passage.

Nous croyons que si vous vous engagez pleinement dans le cours et que vous avez la préparation et les aptitudes nécessaires, vous serez satisfait de votre expérience.

 [![Previous](/inf1220-hugo/svg/backward.svg "Robot conversationnel et intelligence artificielle") Robot conversationnel et intelligence artificielle](/inf1220-hugo/docs/modules/module1/robot/) [Java pas à pas ![Next](/inf1220-hugo/svg/forward.svg "Java pas à pas")](/inf1220-hugo/docs/modules/module1/pasapas/) 


*   [Connaissances technologiques](#connaissances-technologiques)
*   [Mathématiques](#mathématiques)
*   [Autoévaluation (mathématiques)](#autoévaluation-mathématiques)
*   [Autoévaluation (aptitude en programmation)](#autoévaluation-aptitude-en-programmation)

*   [Maîtrise de l’anglais](#maîtrise-de-langlais)
*   [Un cours difficile ?](#un-cours-difficile-)

## Java pas à pas


Java pas à pas [#](#java-pas-%c3%a0-pas)
========================================

Vous devez vous procurer le manuel Java pas à pas. Vous avez accès [au document PDF](https://raw.githubusercontent.com/RobertGodin/JavaPasAPas/master/JavaPasAPas.pdf). Si vous devez lire un document PDF, nous vous encourageons à charger le fichier sur votre machine et à l’ouvrir au sein d’un outil dédié (par ex. Adobe Acrobat). Il n’est pas très pratique de lire un document PDF au sein d’un navigateur web.

[Vous pouvez aussi acheter la version papier du manuel Java pas à pas chez Amazon](https://www.amazon.ca/Java-pas-Introduction-programmation-langage/dp/B0CR7RW87Y/) pour une somme modeste :

[![](https://m.media-amazon.com/images/I/61tnblFlmmL._SL1499_.jpg)](https://www.amazon.ca/Java-pas-Introduction-programmation-langage/dp/B0CR7RW87Y/)

Nous vous invitons maintenant à lire le chapitre suivants _Concepts de base_ (chapitre 1) du manuel Java pas à pas par Robert Godin et Daniel Lemire. Le chapitre comprend plusieurs exemples et exercices. Vous devez compléter les exercices du manuel.

Après votre lecture du chapitre, répondez aux questions suivantes.

*   Décrivez les principales composantes matérielles d’un ordinateur typique, telles que le processeur, la mémoire centrale et les unités périphériques. Expliquez brièvement le rôle du bus dans la communication entre ces composantes.
*   Expliquez le fonctionnement de base du processeur central (CPU) dans l’exécution d’un programme. Décrivez le cycle de traitement (chercher et exécuter une instruction) et donnez un exemple simple d’instruction que le processeur pourrait exécuter.
*   Quelles sont les caractéristiques principales de la mémoire centrale (RAM) en termes de rapidité et de volatilité ? Expliquez pourquoi un programme doit être chargé dans la mémoire centrale avant son exécution et ce qui se passe en cas d’interruption de courant.
*   Distinguez les périphériques d’entrée, de sortie et d’entrée/sortie. À l’aide d’exemples concrets (comme le clavier, l’écran ou le disque dur), expliquez comment ces périphériques permettent l’échange d’informations entre l’ordinateur et le monde extérieur.
*   Quelle est la différence entre le matériel (hardware) et le logiciel (software) ? Décrivez le rôle du système d’exploitation dans la gestion des ressources d’un ordinateur, en citant un exemple de système d’exploitation mentionné dans le chapitre.
*   Expliquez ce qu’est le langage binaire et pourquoi il est utilisé dans les ordinateurs. À l’aide d’un exemple, montrez comment l’entier décimal 42 est représenté en binaire sur 8 bits, en détaillant le calcul.
*   Décrivez le processus de compilation dans le contexte de la programmation Java. Expliquez pourquoi il est nécessaire de traduire un programme Java en langage machine avant son exécution par le processeur.
*   Expliquez ce qu’est un système de gestion de fichiers et son rôle dans l’organisation des données en mémoire secondaire. À l’aide d’un exemple de chemin de fichier sous Windows (comme C:\\Users\\Robert\\Documents\\HelloWorld.java), décrivez comment un fichier est localisé.
*   Qu’est-ce que le pseudo-parallélisme dans un système monoprocesseur ? Expliquez comment le système d’exploitation crée l’illusion d’une exécution simultanée de plusieurs programmes, et précisez en quoi cela diffère du parallélisme réel dans un système multi-cœur.

Plusieurs étudiants trouvent qu’il est plus aisé de faire les lectures dans le manuel Java pas à pas après avoir terminé la lecture du module sur notre site web. Vous pouvez choisir quand il vous convient le mieux d’utiliser le manuel Java pas à pas.

 [![Previous](/inf1220-hugo/svg/backward.svg "Autoévaluation") Autoévaluation](/inf1220-hugo/docs/modules/module1/autoevaluation/) [Les ordinateurs et leurs langages ![Next](/inf1220-hugo/svg/forward.svg "Les ordinateurs et leurs langages")](/inf1220-hugo/docs/modules/module1/ordinateurs/)

## Les ordinateurs et leurs langages


*   [Programmation orientée objet](#programmation-orientée-objet)
*   [Java](#java)
    *   [Nombres irrationnels](#nombres-irrationnels)
    *   [Mathématiques et programmation](#mathématiques-et-programmation)
    *   [Style de codage](#style-de-codage)
    *   [Premier ordinateur](#premier-ordinateur)
    *   [Lisp](#lisp)
    *   [Écrire une implémentation d’Emacs en C](#écrire-une-implémentation-demacs-en-c)
    *   [Les débuts de l’Internet](#les-débuts-de-linternet)
    *   [Elon Musk, Steve Jobs, Jeff Bezos](#elon-musk-steve-jobs-jeff-bezos)
    *   [Travailler dur et intelligemment](#travailler-dur-et-intelligemment)
    *   [Open source](#open-source)
    *   [Java](#java-1)
    *   [Machine virtuelle Java](#machine-virtuelle-java)
    *   [Android](#android)
    *   [Conseils](#conseils)
*   [Résumé de l’architecture des ordinateurs et de l’abstraction des langages](#résumé-de-larchitecture-des-ordinateurs-et-de-labstraction-des-langages)
*   [Langage machine](#langage-machine)
*   [API](#api)
*   [Taille des processeurs et des transistors](#taille-des-processeurs-et-des-transistors)
*   [Unités de mesures](#unités-de-mesures)
    *   [Fréquence (vitesse du processeur)](#fréquence-vitesse-du-processeur)
    *   [Temps](#temps)
    *   [Stockage et mémoire](#stockage-et-mémoire)
    *   [Binaire](#binaire)

Court historique des langages de programmation [#](#court-historique-des-langages-de-programmation)
===================================================================================================

L’idée de programmer des machines remonte au 19e siècle, époque marquée par l’émergence des premières machines de calcul et d’automatisation. Dès 1801, les métiers à tisser Jacquard utilisaient des cartes perforées pour programmer des motifs textiles, préfigurant les concepts de codage. Cependant, c’est au milieu du 19e siècle qu’un jalon historique est posé avec les travaux d’Ada Lovelace (1815-1852) sur la machine analytique de Charles Babbage. Considérée comme la première programmeuse, elle rédigea des notes détaillées incluant un algorithme pour calculer les nombres de Bernoulli, démontrant qu’une machine pouvait exécuter des instructions complexes. Le langage Ada, créé dans les années 1980, rend hommage à cette contribution pionnière.

L’avènement des ordinateurs modernes dans les années 1940-1950 marque un tournant décisif. Les premiers langages de programmation apparaissent pour répondre aux besoins de calcul scientifique, commercial et logique. Parmi eux, FORTRAN (1954) facilite les calculs scientifiques, LISP (1958) introduit des concepts d’intelligence artificielle et de traitement symbolique, et COBOL (1959) s’impose dans la gestion des données commerciales. Ces langages, bien que rudimentaires comparés aux standards actuels, posent les bases des paradigmes de programmation modernes.

Le langage ALGOL (Algorithmic Language) est un langage de programmation développé à la fin des années 1950, conçu pour exprimer des algorithmes de manière claire et structurée. Créé par un comité international de chercheurs, dont John Backus et Peter Naur, ALGOL a été introduit avec sa première version, ALGOL 58, suivie par ALGOL 60, qui est devenue la plus influente. Son objectif était de fournir un langage universel pour décrire des algorithmes, à la fois pour la recherche scientifique et l’enseignement, tout en servant de base pour le développement de compilateurs ALGOL se distingue par plusieurs innovations. Il introduit une syntaxe formelle, décrite par la notation de Backus-Naur (BNF), qui permet de définir précisément la structure du langage. Il propose des concepts comme la programmation structurée, avec des blocs de code délimités, des boucles et des conditionnelles bien définies, ainsi que la récursivité. Contrairement à des langages comme FORTRAN, orientés vers le calcul numérique, ALGOL privilégie la lisibilité et la généralité, ce qui en fait un précurseur des langages modernes. Bien qu’ALGOL n’ait pas été largement adopté dans l’industrie, il a eu une influence majeure. Des langages comme Pascal, C et Simula en sont directement inspirés. Simula, en particulier, a étendu ALGOL en y intégrant les concepts de classes et d’objets, posant les bases de la programmation orientée objet. ALGOL reste ainsi une étape clé dans l’histoire de l’informatique, reconnu pour sa rigueur conceptuelle et son impact sur la conception des langages de programmation.

Notation de Backus-Naur

La notation de Backus-Naur (BNF) est une méthode formelle pour décrire la syntaxe d’un langage, qu’il s’agisse de langages de programmation, de protocoles ou de formats de données. Développée par John Backus et Peter Naur pour le langage ALGOL 60, elle définit les règles grammaticales d’un langage de manière précise et concise. BNF utilise des règles de production pour spécifier comment des symboles (terminaux et non-terminaux) peuvent être combinés pour former des constructions valides. Elle est essentielle pour concevoir des compilateurs et des analyseurs syntaxiques.

*   _Symboles terminaux_ : Éléments de base du langage, comme des mots-clés, des opérateurs ou des caractères (par exemple, `if`, `+`, `1`).
*   _Symboles non-terminaux_ : Catégories ou abstractions représentant des structures du langage (par exemple, `<expression>`, `<instruction>`).
*   _Règles de production_ : Définissent comment un symbole non-terminal peut être remplacé par une combinaison de terminaux et/ou non-terminaux, sous la forme `<symbole> ::= définition`.
*   _Méta-symboles_ : BNF utilise `::=` pour indiquer une définition et `|` pour exprimer des alternatives.

Une règle s’écrit ainsi :

    <nom_du_symbole> ::= séquence_de_symboles | autre_séquence
    

*   Le côté gauche (`<nom_du_symbole>`) est un non-terminal.
*   Le côté droit décrit les combinaisons possibles de terminaux et non-terminaux.
*   Le symbole `|` sépare les alternatives.

Par exemple, pour définir la syntaxe d’un nombre entier (composé de chiffres de 0 à 9) :

    <chiffre> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    <nombre_entier> ::= <chiffre> | <chiffre> <nombre_entier>
    

*   `<chiffre>` est un symbole terminal parmi `"0"`, `"1"`, …, `"9"`.
*   `<nombre_entier>` est soit un `<chiffre>`, soit un `<chiffre>` suivi d’un autre `<nombre_entier>` (permettant des nombres comme `42` ou `123`).
*   La règle est récursive.

BNF permet de définir la syntaxe des langages de manière non ambiguë, facilitant la création d’analyseurs syntaxiques pour les compilateurs. Elle est utilisée pour des formats de données (par exemple, JSON) ou des protocoles réseau. Des variantes comme EBNF (Extended BNF) ajoutent des fonctionnalités comme la répétition ou les expressions optionnelles.

Au fil des décennies, les langages évoluent pour offrir plus d’abstraction, de flexibilité et d’accessibilité. Dans les années 1980 et 1990, des langages comme C++ (1983), Python (1991), Java (1995), JavaScript (1995) et PHP (1995) voient le jour, chacun répondant à des besoins spécifiques : performance pour C++, simplicité pour Python, portabilité pour Java, interactivité web pour JavaScript, ou développement web dynamique pour PHP. Aujourd’hui, ces langages dominent l’industrie, comme le montre le classement 2017 de l’IEEE Spectrum, qui reflète leur popularité et leur polyvalence.

Tous ces langages partagent un objectif commun : permettre aux programmeurs de décrire des solutions à des problèmes en s’éloignant progressivement des contraintes du matériel. Pour comprendre leur rôle, il est essentiel de se pencher sur le fonctionnement des ordinateurs.

Programmation orientée objet [#](#programmation-orient%c3%a9e-objet)
--------------------------------------------------------------------

La programmation orientée objet trouve ses origines dans les années 1960 avec le langage Simula, développé en Norvège par Ole-Johan Dahl et Kristen Nygaard. Simula introduit les concepts de classes et d’objets pour modéliser des entités du monde réel, ouvrant la voie à une nouvelle façon de structurer les programmes.

Ole-Johan Dahl et Kristen Nygaard ont développé Simula dans les années 1960 avec pour motivation principale de créer un langage capable de modéliser et de simuler des systèmes complexes du monde réel. Travaillant au Centre de calcul norvégien à Oslo, ils cherchaient à résoudre des problèmes liés à la simulation de processus, notamment dans des domaines comme la recherche opérationnelle et la gestion de systèmes dynamiques. Leur objectif était de concevoir un outil permettant de représenter des entités concrètes (comme des objets physiques ou des processus) et leurs interactions de manière intuitive.

Simula, initialement conçu comme une extension du langage ALGOL, a introduit les concepts de classes et d’objets pour répondre à ce besoin. Nygaard, en particulier, était motivé par la nécessité de modéliser des systèmes où de multiples entités agissaient simultanément, comme dans les simulations de flux de trafic ou de réseaux de communication. Dahl, quant à lui, apportait une rigueur mathématique pour structurer ces idées dans un cadre formel. Leur vision était de rendre la programmation plus proche de la pensée humaine, en représentant les concepts du monde réel directement dans le code, ce qui a jeté les bases de la programmation orientée objet.

Dans les années 1980, le langage Smalltalk, conçu par Alan Kay et son équipe chez Xerox PARC, popularise la programmation orientée objet en mettant l’accent sur l’interaction entre objets, l’héritage et le message passing. Smalltalk influence profondément la conception des langages modernes.

Alan Kay a conçu le langage Smalltalk avec son équipe chez Xerox PARC dans les années 1970 pour explorer de nouvelles façons de rendre l’informatique plus accessible, flexible et intuitive. Sa motivation principale était de créer un environnement où les utilisateurs, y compris les enfants, pourraient manipuler des objets graphiques et apprendre à programmer de manière interactive. Il voulait que l’ordinateur devienne un « media personnel », aussi malléable qu’un carnet de notes, permettant l’expérimentation, la simulation et la construction de connaissances.

Smalltalk a été pensé comme un outil pédagogique, inspiré par les idées de Seymour Papert sur l’apprentissage par la manipulation et la découverte. Alan Kay cherchait à démocratiser la programmation et à rendre le logiciel aussi modulaire et réutilisable que les objets du monde réel, d’où l’accent mis sur les objets, les messages et l’interactivité.

Je vous invite à regarder la vidéo suivante par le père de la programmation orientée objet.

Transcription traduite en français0:40 Merci. Eh bien, je présume que la plupart d’entre vous ont veillé toute la nuit. Je n’imagine pas voir autant de programmeurs à huit heures du matin.

0:58 Je suppose que c’est la plus grande salle de bain dans laquelle j’ai jamais donné une conférence. C’était juste un test pour voir si vous pouviez me comprendre. En fait, je ne me comprends pas moi-même ici.

1:14 Je n’étais pas revenu à cette conférence depuis la première édition. Quand j’ai été invité à donner cette présentation, je me demandais si je devais accepter ou non, et quoi faire. Il m’est venu à l’esprit que cette conférence, à ce moment précis, se situe au cœur du vingt-cinquième anniversaire de Smalltalk.

1:58 L’interpréteur d’une page que j’ai écrit il y a quelques semaines, il y a vingt-cinq ans, et la première version fonctionnelle, réalisée quelques semaines plus tard, il y a vingt-cinq ans, placent cet événement à peu près au centre. Voyons si je peux afficher notre devise. Puis-je avoir la première diapositive, s’il vous plaît ?

2:31 Je ne vais pas donner une conférence historique, car j’ai enfin rempli ces obligations lors de la conférence sur l’histoire des langages de programmation il y a quelques années. Mais j’ai pensé qu’il pourrait être intéressant, pour ceux qui n’ont pas programmé ces vingt-cinq ou trente dernières années, de faire un voyage de deux minutes.

3:00 Ces images remontent à 1973 et 1974 chez Xerox PARC. Elles montrent certains des premiers enfants avec lesquels nous avons travaillé. La musique que vous entendrez dans cet extrait a été composée par un membre de notre groupe, Chris Jeffers. Elle s’appelle _The Happy Hacker_, au cas où vous voudriez un thème musical. Elle est jouée en synthèse FM en temps réel que nous avons développée pour l’ordinateur Alto.

3:29 C’est le précurseur des stations de travail et du Macintosh, sans aucun matériel de synthèse sonore supplémentaire, car pourquoi en avoir si votre ordinateur est bien conçu ?

3:48 Avant de lancer cet extrait, voyons, juste pour le plaisir, combien de personnes dans cette salle aujourd’hui ont participé à l’expérience Smalltalk chez Xerox PARC entre 1971 et 1983 environ. Pouvez-vous vous lever ? Voyons combien nous sommes. Y a-t-il quelqu’un sans cheveux gris ? Merci.

4:19 Bien, lançons cet extrait.

5:19 C’était l’état des choses il y a environ vingt-cinq ans. En introduction, j’ai essayé de trouver comment aborder cette conférence. J’ai fini par me souvenir d’un article de Dijkstra. Combien d’entre vous ont rencontré Dijkstra ? Vous savez probablement que l’arrogance en informatique se mesure en nano-Dijkstras.

5:58 Il a écrit un article intitulé _Sur le fait que l’Atlantique a deux rives_. Il parlait des différences entre les approches de l’informatique en Europe, surtout aux Pays-Bas, et aux États-Unis. Aux États-Unis, nous n’étions pas assez mathématiques. En Hollande, si vous êtes professeur titulaire, vous êtes nommé par la reine. Il y a beaucoup d’autres distinctions importantes entre ces deux cultures.

6:44 J’ai écrit une réponse intitulée _Sur le fait que la plupart des logiciels dans le monde sont écrits d’un seul côté de l’Atlantique_. Avec mon diplôme en mathématiques, j’expliquais que les ordinateurs forment une nouvelle forme de mathématiques. On ne peut pas les juger selon les mathématiques classiques. Ceux qui essaient se livrent à une forme d’autosatisfaction sans s’en rendre compte.

7:29 C’était une sorte de mathématiques pratiques, un équilibre entre créer des structures cohérentes, bien plus vastes que tout ce que les mathématiques classiques ont jamais envisagé, et gérer les mêmes problèmes que les mathématiques de grande échelle : convaincre qu’on a couvert tous les cas.

8:00 Un mathématicien nommé Euler a produit vingt gros volumes de spéculations, dont la plupart étaient justes, mais presque toutes ses preuves étaient erronées. De nombreux doctorats en mathématiques au dernier siècle ont consisté à examiner les livres d’Euler, démontrer qu’une preuve était mauvaise, supposer que son intuition était correcte et trouver une preuve plus convaincante. Le débogage existe aussi en mathématiques.

8:50 Le plus important dans le travail orienté objet ou tout type de programmation, c’est un mélange exquis entre beauté et praticité. Il n’y a aucune raison de sacrifier l’un ou l’autre. Ceux qui le font ne comprennent pas vraiment ce qu’est l’informatique. C’est comme dire que j’ai de grandes idées pour des peintures, mais je vais utiliser un pinceau sans peinture. Mes idées seront représentées par les gestes que je fais sur le papier. Ne dites pas ça à un artiste du vingtième siècle, il pourrait en faire une vidéo et l’exposer dans un musée.

9:45 J’avais du mal à décider de quoi parler. Les techniciens semblent toujours en savoir tellement. Mais il est intéressant de regarder ce qui se fait dans le monde sous le nom de programmation orientée objet. On m’a montré des morceaux de code très étranges au fil des années, y compris par des universitaires, qui disaient que c’était du code écrit dans un langage orienté objet.

10:26 J’ai inventé le terme _orienté objet_, et je peux vous dire que je n’avais pas C++ en tête.

10:43 J’ai beaucoup des mêmes sentiments à propos de Smalltalk que je vais essayer d’exprimer ici. Il y a une chose vraiment importante à propos de Smalltalk et de certains langages similaires dont nous devrions prêter une attention particulière. Cela n’a presque rien à voir avec la syntaxe ou la bibliothèque de superclasses accumulée, qui sont souvent considérées comme le langage lui-même, comme s’il avait été décrété par des dieux sur l’Olympe.

11:31 Je veux parler de ma réaction personnelle lorsque j’ai commencé à y réfléchir dans les années 1960. Plutôt que de faire une conférence historique, je vais essayer de voir si ces réactions et intuitions ont encore une place aujourd’hui.

12:08 Dans les années 1960, les choses étaient très mécaniques. Il y avait un sentiment de mécanisme simple, car les ordinateurs étaient aussi grands que cette salle. Celui sur lequel Ivan Sutherland a créé Sketchpad était l’un des derniers aux États-Unis à avoir son propre toit : c’était le bâtiment lui-même.

12:38 Mais les programmes étaient assez petits et avaient beaucoup en commun avec leurs ancêtres mathématiques. Une façon de penser à la sémantique des mathématiques basées sur la logique est comme des engrenages qui s’emboîtent. Tout doit s’adapter, et si tout est compatible à la fin, vous obtenez la rotation finale de l’arbre que vous voulez.

13:14 Une analogie pour ces programmes des années 1960 est une niche pour chien. Prenez des planches au hasard, un marteau, des clous, assemblez-les, et vous avez une structure qui tient debout. Vous n’avez besoin de savoir que planter un clou.

13:46 Quelqu’un pourrait regarder cette niche et dire : si nous pouvions l’agrandir d’un facteur cent, nous pourrions construire une cathédrale. Une niche de un mètre de haut donnerait un bâtiment de trente étages, ce qui serait impressionnant. On pourrait y accueillir beaucoup de monde.

14:05 Les charpentiers se mettraient au travail pour agrandir cette niche d’un facteur cent. Mais, en tant qu’ingénieurs et scientifiques, nous savons que lorsqu’on agrandit quelque chose d’un facteur cent, sa masse augmente d’un facteur un million, et sa résistance, qui dépend principalement des sections transversales, n’augmente que d’un facteur dix mille. En agrandissant d’un facteur cent, la structure devient environ cent fois plus faible. Cette niche s’effondrerait en un tas de débris.

14:48 À ce moment, il y a deux choix. Le plus populaire est de dire que c’était l’objectif depuis le début, d’ajouter plus de débris, de recouvrir de calcaire et de prétendre qu’on voulait faire des pyramides, pas des cathédrales gothiques. Cela explique, je pense, une grande partie de la structure des systèmes d’exploitation modernes.

15:24 Ou vous pouvez proposer un nouveau concept. Les personnes intéressées par les structures complexes il y a de nombreuses années l’ont fait. Elles ont appelé cela l’architecture, littéralement la conception et la construction d’arches réussies, une interaction non linéaire et non évidente entre des matériaux simples pour obtenir des synergies inattendues et une multiplication des matériaux.

16:07 Il est remarquable que la quantité de matériaux dans la cathédrale de Chartres, une structure physique énorme, soit inférieure à celle utilisée pour le Parthénon. La raison est que Chartres est presque entièrement faite d’air et de verre. Tout est organisé avec ingéniosité dans une structure magnifique pour que l’ensemble ait beaucoup plus d’intégrité que chacune de ses parties.

16:37 C’est une autre voie à suivre. Une partie du message de la programmation orientée objet est que, à mesure que la complexité devient plus importante, l’architecture dominera toujours le matériau. Le triste constat est que les gens ne se sont pas intéressés à l’architecture pour sa beauté. Ils commencent à peine à s’y intéresser maintenant, forcés par Internet. C’est assez pathétique.

17:16 Je vais utiliser une métaphore pour cette conférence, tirée d’un merveilleux livre appelé _L’acte de création_ d’Arthur Koestler. Koestler était un romancier devenu scientifique cognitif à la fin de sa vie. Il a écrit sur ce que pourrait être la créativité. Il a réalisé que l’apprentissage est un acte de création, car quelque chose de nouveau apparaît en vous.

17:59 Il utilisait la métaphore des pensées comme des fourmis rampant sur un plan, ici un plan rose. Sur un plan rose, vous pouvez avoir des objectifs, choisir des directions, avancer, mais vous êtes toujours dans le contexte rose.

18:22 Cela signifie que le progrès dans un contexte fixe est presque toujours une forme d’optimisation. Si vous trouvez quelque chose de nouveau, cela ne faisait pas partie des règles ou du contexte du plan rose. Les actes créatifs sortent généralement du contexte initial.

19:00 Même si vous avez été soigneusement éduqué par vos parents et l’école pendant des années, parfois, sous la douche, en jogging ou dans un moment d’inattention, une idée bleue surgit. Cette chose qui vous intriguait, que vous observiez, apparaît sous un jour complètement différent, comme si c’était autre chose.

19:33 Koestler disait que la réaction émotionnelle à cela prend trois formes : pour une blague, c’est _haha_ ; pour la science, c’est _aha_ ; pour l’art, c’est _ah_. Dans chaque cas, quelque chose de similaire se produit. Une blague vous mène sur un chemin, puis révèle qu’il s’agit d’autre chose, provoquant une explosion agressive. La science procure une sensation similaire, souvent accompagnée de rires, car la réponse était juste sous vos yeux, comme une blague. L’art nous rappelle que, quel que soit le contexte dans lequel nous pensons être, il y en a d’autres. L’art nous sort de notre contexte pour nous rendre conscients d’autres contextes.

20:34 C’est une métaphore simple, voire simpliste, mais elle servira pour cette conférence. Koestler a aussi souligné qu’il faut quelque chose de bleu pour avoir des pensées bleues. Cela échappe souvent à ceux qui se spécialisent à outrance. En se spécialisant, on se met dans un état mental où l’optimisation est à peu près tout ce qu’on peut faire. Il faut apprendre beaucoup de choses différentes pour commencer à entrevoir d’autres contextes.

21:17 Voici quelques déclics que j’ai eus au fil des ans. L’un d’eux, je pense, vous intéressera, car c’est la forme la plus ancienne connue de ce qu’on appelle l’abstraction de données. Cela remonte à avant 1961. J’étais dans l’Armée de l’Air en 1961, et je l’ai vu à ce moment-là, probablement un an plus tôt.

21:47 À l’époque, il n’y avait pas vraiment de systèmes d’exploitation. Le Commandement de l’entraînement aérien devait envoyer des bandes magnétiques avec divers types d’enregistrements d’une base aérienne à une autre. La question était de savoir comment gérer tous ces formats, autrefois des images de cartes, qui devenaient plus complexes avec l’arrivée des bandes.

22:19 Quelqu’un, probablement un engagé, car les officiers ne programmaient pas à l’époque, a eu l’idée suivante : sur la troisième partie de l’enregistrement, on mettra tous les enregistrements de ce type particulier ; sur la partie centrale, toutes les procédures qui savent gérer les formats de cette troisième partie ; et sur la première partie, des pointeurs vers ces procédures. Les dix premiers pointeurs seraient standardisés, comme la lecture, l’écriture des champs et l’impression, avec un vocabulaire standard pour les dix premiers, puis des pointeurs plus spécifiques ensuite.

23:14 Pour lire une bande en 1961, il suffisait de charger la partie avant d’un enregistrement dans la mémoire centrale et de sauter directement via les pointeurs vers les procédures. Comparez cela à ce que vous devez faire avec HTML sur Internet.

23:41 HTML sur Internet est un retour à l’âge des ténèbres, car il présuppose qu’un navigateur doit comprendre ses formats. C’est l’une des pires idées depuis MS-DOS. C’est vraiment honteux. Peut-être est-ce ce qui arrive quand des physiciens jouent avec des ordinateurs, je ne suis pas sûr.

24:13 Nous voyons ce qui arrive à Internet maintenant : il y a deux guerres en cours. Les guerres des navigateurs, qui sont totalement inutiles, sont soit une tentative de démontrer une incompréhension de la construction de systèmes complexes, soit une tentative encore plus grossière de s’approprier du territoire, ce que je suspecte de Microsoft.

24:42 Vous n’avez pas besoin d’un navigateur si vous suivez ce qu’un sergent d’état-major de l’Armée de l’Air savait faire en 1961. Il suffit de lire, tout devrait voyager avec ce dont il a besoin. Vous n’avez besoin de rien de plus complexe que quelque chose comme X Windows, en mieux, mais vous voulez distribuer toute la connaissance de ces choses.

25:15 Internet commence à aller dans cette direction, car les gens découvrent des formats HTML de plus en plus complexes et intraitables. C’est une erreur qui se répète à chaque génération, et ce n’est tout simplement pas la bonne façon de faire.

25:39 Cette programmation était faite avant l’existence des langages de haut niveau dans l’Armée de l’Air. Mais cette approche a été éliminée par COBOL quand ils ont standardisé sur COBOL.

26:01 Le Sketchpad d’Ivan Sutherland était immensément sophistiqué, presque stupéfiant dans sa conception. C’était un système orienté objet avec une notion réelle de classes et de sous-classes, et un polymorphisme encore plus fort que celui du Commandement de l’entraînement aérien.

26:43 J’avais vu cette idée trois ou quatre fois, mais ce n’est qu’en essayant de comprendre Simula que j’ai enfin saisi. Nous pensions que c’était censé être un Algol, mais c’était un amas de bandes, le premier Simula, modifié par Case Western Reserve et les inventeurs de Simula, Nygaard et Dahl, en Norvège, distribué avec une documentation incompréhensible en 1966.

27:19 En essayant de comprendre Simula, peut-être parce qu’une bonne idée étrange vue quatre fois sous différents costumes finit par faire impression, j’ai réalisé quelque chose.

27:41 Quand vous êtes confronté à quelque chose de nouveau, vous pouvez considérer cet avancement technologique comme une meilleure façon de faire ce que vous faites déjà, et l’utiliser pour continuer sur votre chemin, restant dans le plan rose. Ou vous pouvez dire que ce n’est pas une meilleure version de l’ancien, mais presque une nouvelle chose, et vous demander ce que cette nouvelle chose essaie d’être.

28:15 Si vous faites cela, il y a une chance d’obtenir un levier incroyable, plutôt que d’optimiser quelque chose qui ne peut pas l’être beaucoup. Simula venait du monde des structures de données et des procédures, avec cette saveur, si vous vouliez le voir ainsi. Mais il avait une manière de lier les états de votre calcul avec des procédures, ce qui était extrêmement utile et bien meilleur que ce qu’on appelait les variables propres dans Algol 60.

29:02 C’était une façon de le voir. Puis il y avait cette autre question : si c’était presque une nouvelle chose, de quel type de nouvelle chose s’agissait-il ? L’une de mes spécialités universitaires était la biologie moléculaire, avec un intérêt particulier pour la physiologie cellulaire et l’embryologie, aujourd’hui appelée morphogenèse.

29:27 Le livre _Molecular Biology of the Gene_ venait de sortir en 1965, un ouvrage merveilleux, toujours en impression, bien que les seules mots communs entre cette édition et celle d’aujourd’hui soient probablement les articles comme _le_ ou _et_. Même le mot _gène_ y est encore, mais il signifie quelque chose de complètement différent maintenant.

29:58 Dans ce livre, Watson a réalisé le premier essai d’une créature vivante entière, la bactérie E. coli.

30:20 Si vous regardez à l’intérieur, la complexité est stupéfiante. Ces choses en forme de popcorn sont des molécules de protéines avec environ 5000 atomes. En éliminant les petites molécules comme l’eau, les ions calcium et potassium, qui constituent environ 70 % de la masse, il reste 30 % avec environ 120 millions de composants qui interagissent de manière informationnelle.

31:06 Chaque composant porte beaucoup d’informations. Une façon simple de voir cela est que ça fonctionne un peu comme Ops5 : il y a une correspondance de motifs, et des choses se produisent si les motifs sont appariés avec succès.

31:29 L’état impliqué représente environ cent giga-octets. Aujourd’hui, cela équivaut à une centaine d’ordinateurs de bureau, mais c’est toujours impressionnant comme quantité de calcul. Ce qui est peut-être le plus intéressant, c’est que la rapidité de ce calcul rivalise sérieusement avec celle des ordinateurs actuels.

32:04 Particulièrement en considérant que c’est fait en parallèle. Par exemple, l’une de ces choses de la taille d’un popcorn se déplace de sa propre longueur en deux nanosecondes. Si un atome était de la taille d’une balle de tennis, une de ces molécules de protéines serait de la taille d’une Volkswagen, se déplaçant de sa propre longueur en deux nanosecondes, soit environ 2,4 mètres à notre échelle.

32:37 Quelqu’un peut-il calculer quelle fraction de la vitesse de la lumière représente un déplacement de 2,4 mètres en deux nanosecondes ? Oui, quatre fois la vitesse de la lumière à cette échelle.

32:50 Si vous vous demandez pourquoi la chimie fonctionne, c’est à cause de l’agitation thermique incroyablement violente à cette échelle, qu’on ne peut même pas imaginer avec l’aide des ordinateurs. On ne voit rien à l’intérieur de ces choses tant qu’on ne les tue pas, car c’est un flou total d’activité.

33:16 Dans de bonnes conditions, il ne faut qu’environ 15 à 18 minutes pour qu’une de ces bactéries se duplique complètement. Bien plus est connu aujourd’hui. Ces bactéries, un cinq-centième de la taille des cellules de notre corps, qui ont environ 60 milliards de composants informationnels au lieu de 120 millions, montrent l’ampleur.

34:05 Nous avons entre 10^12 et 10^13 cellules dans notre corps, peut-être plus. Pourtant, il ne faut que cinquante divisions cellulaires pendant une grossesse de neuf mois pour faire un bébé.

34:20 En calculant, vous réalisez qu’il n’en faut qu’environ quarante. Les dix puissances supplémentaires sont là car, pendant le processus embryologique, de nombreuses cellules inadaptées à l’organisme sont éliminées. Les choses sont faites par surprolifération, test et élagage selon un plan beaucoup plus vaste.

34:53 Chacun de nous est intégré dans une biomasse énorme. Pour quelqu’un dont le contexte bleu pourrait être la biologie, un ordinateur ne pourrait pas être considéré comme particulièrement complexe, grand ou rapide.

35:17 Lent, petit, stupide : voilà ce que sont les ordinateurs. La question est : comment pouvons-nous les amener à réaliser leur destin ?

35:41 Nous utilisons une forme de technologie que Napoléon utilisait, rappelez-vous les sémaphores à travers la France. Le changement de perspective ici passe de la mécanique à autre chose.

36:01 Si vous prenez des niches pour chiens, elles ne s’agrandissent pas bien d’un facteur cent. Les horloges non plus. Mais les cellules s’agrandissent non pas d’un facteur cent, mais d’un facteur mille milliards. La question est : comment font-elles, et comment pourrions-nous adapter cette idée pour construire des systèmes complexes ?

36:34 C’est simple, mais même C++ n’a pas encore compris. Aucune idée n’est si simple et puissante qu’on ne puisse pas la faire mal comprendre par des millions de personnes.

36:56 Il ne faut absolument pas permettre que l’intérieur de l’un de ces éléments soit un facteur dans le calcul de l’ensemble. Ce n’est qu’une partie de l’histoire. La membrane cellulaire est là autant pour empêcher certaines choses d’entrer que pour retenir certaines choses à l’intérieur.

37:20 Une grande partie de notre confusion avec les objets vient du problème que, dans notre culture occidentale, nous avons un langage avec des noms et des verbes très durs. Nos mots de processus sont médiocres. Il nous est plus facile de penser à un objet.

37:42 Je m’excuse profondément depuis vingt ans d’avoir inventé le terme _orienté objet_, car dès qu’il a été mal appliqué, j’ai réalisé que j’aurais dû utiliser un terme beaucoup plus orienté vers les processus.

38:05 Les Japonais ont un mot intéressant, _ma_, qui désigne l’espace entre ce que nous appelons des objets, ce que nous ne voyons pas parce que nous sommes focalisés sur la _chose_ plutôt que sur le processus. En japonais, il y a une manière plus orientée vers les processus de voir comment les choses se relient.

38:40 On peut le voir à la taille des mots utilisés pour exprimer quelque chose d’important. _Ma_ est très court. Nous devons utiliser des mots comme _interstitiel_ ou pire pour approcher ce dont parlent les Japonais.

39:00 Cette réalisation ne peut être attribuée à une personne en particulier. Elle est dans les germes de Sketchpad, dans le système de fichiers du Commandement de l’entraînement aérien, et dans Simula.

39:18 Une fois que vous avez encapsulé de manière à avoir une interface entre l’intérieur et l’extérieur, il est possible de faire en sorte qu’un objet agisse comme n’importe quoi. La raison est simple : ce que vous avez encapsulé est un ordinateur.

39:40 Vous avez fait quelque chose de puissant en informatique : prendre la chose puissante sur laquelle vous travaillez et ne pas la perdre en partitionnant votre espace de conception. C’est le défaut des langages de données et de procédures.

39:58 Je pense que la chose la plus pernicieuse à propos de langages comme C++ et Java est qu’ils croient aider le programmeur en ressemblant autant que possible à l’ancien paradigme. En réalité, ils nuisent terriblement au programmeur en rendant difficile la compréhension de ce qui est vraiment puissant dans cette nouvelle métaphore.

40:21 Les personnes travaillant sur des systèmes de partage de temps l’avaient déjà compris. La thèse de Butler Lampson en 1965 parlait de donner à chaque personne sur un système de partage de temps ce qu’on appelle maintenant une machine virtuelle, quelque chose d’aussi proche que possible de l’ordinateur physique, mais séparé pour chaque utilisateur.

40:56 UNIX avait cette idée, mais le plus gros problème était qu’un processus UNIX avait une surcharge d’environ deux mille octets juste pour exister. Il était très difficile dans UNIX de laisser un processus UNIX représenter simplement le nombre trois. Vous passiez de trois bits à quelques milliers d’octets, ce qui posait un problème d’échelle.

41:22 Une grande partie du problème est de décider que la métaphore biologique est celle qui prédominera au cours des vingt-cinq prochaines années, puis de s’y engager suffisamment pour qu’elle soit pratique à tous les niveaux d’échelle dont nous avons besoin.

41:48 Nous avons un tour que la biologie ne sait pas faire : nous pouvons extraire l’ADN des cellules. Cela permet de traiter la fibrose kystique beaucoup plus facilement qu’aujourd’hui. Les systèmes ont aussi une sorte de fibrose kystique.

42:07 Pour certains, la fibrose kystique est traitée aujourd’hui en les infectant avec un virus du rhume modifié, provoquant une infection pulmonaire. Le gène défectueux pour la fibrose kystique est dans ce virus, trop faible pour détruire les poumons comme une pneumonie, mais assez fort pour insérer une copie de ce gène dans chaque cellule des poumons.

42:34 C’est une manière très compliquée de reprogrammer l’ADN d’un organisme une fois qu’il est en marche.

42:51 Ce qui m’étonne, c’est que nous n’ayons pas vu plus de progrès. Par exemple, une des choses les plus surprenantes pour moi chez ceux qui travaillent sur Internet est que je ne connais personne – et j’espère que quelqu’un viendra me contredire après – qui ait réalisé qu’au minimum, chaque objet devrait avoir une URL.

43:19 Je crois que chaque objet sur Internet devrait avoir une adresse IP, car cela représente beaucoup mieux les abstractions réelles du matériel physique aux bits.

43:39 C’est une intuition précoce que les objets sont fondamentalement comme des serveurs. La notion de polymorphisme, autrefois appelée procédures génériques, est une façon de penser aux classes de ces serveurs.

44:00 Nous n’y avons pas encore vraiment fait face, mais nous devons construire ces choses, et bientôt il faudra les faire croître. Il est facile de faire grandir un bébé de quinze centimètres, il le fait environ dix fois dans sa vie sans jamais s’arrêter pour maintenance. Mais essayez de faire grandir un Boeing 747, et vous faites face à un problème incroyable, car il est dans un monde mécanique simpliste où le seul objectif était de fabriquer l’artefact, pas de le réparer, de le modifier ou de le faire vivre cent ans.

44:46 Combien de personnes ici utilisent encore un langage qui, dans le système de développement, vous force à développer en dehors du langage, à compiler, recharger et exécuter, même si c’est rapide comme Java Virtual Cafe ? Allez, avouez-le, nous pouvons organiser une réunion sous une tente texane plus tard.

45:23 Si vous y pensez, cela ne peut être qu’une impasse pour construire des systèmes complexes, où une grande partie de la construction consistera à essayer de comprendre les possibilités d’interopérabilité avec ce qui existe déjà.

45:45 J’ai joué un rôle mineur dans la conception de l’ARPANET. J’étais l’un des trente étudiants diplômés qui ont participé à des réunions de conception de systèmes pour formuler des principes de conception pour l’ARPANET il y a environ trente ans.

46:02 L’ARPANET est devenu Internet. Depuis qu’il a commencé à fonctionner autour de 1969 jusqu’à aujourd’hui, il s’est agrandi d’un facteur d’environ cent millions. C’est assez impressionnant, huit ordres de grandeur.

46:31 D’après ce que je sais, après avoir parlé à Larry Roberts récemment, il n’y a pas un seul atome physique dans l’Internet d’aujourd’hui qui était dans l’ARPANET original, ni une seule ligne de code.

46:53 Si nous avions eu des mainframes IBM dans l’ARPANET original, cela n’aurait pas été vrai. C’est un système qui s’est agrandi de cent millions, a changé chaque atome et chaque bit, et n’a jamais eu à s’arrêter.

47:11 C’est la métaphore que nous devons absolument appliquer à ce que nous considérons comme des choses plus petites. C’est pourquoi vos programmes sont si grands, pourquoi ils deviennent des pyramides au lieu de cathédrales gothiques.

47:40 Voici une autre grande source. Avec Simula, Lisp est certainement le plus grand langage des années 1960, avec autant, sinon plus, d’intuitions profondes.

48:05 Sur la page 13 de ce livre publié en 1962, il y a une demi-page de code qui est le modèle réflexif de Lisp écrit en lui-même. Tous les détails importants de la sémantique de Lisp et les directives pour créer un interpréteur Lisp sont dans cette demi-page.

48:29 C’est cet aspect méta-réflexif qui, pour moi, est la chose la plus triste à propos de ce qui arrive à Java. Quand Java est apparu, j’ai pensé qu’il légitimait quelque chose que beaucoup ne croyaient plus depuis longtemps : l’approche des codes intermédiaires multiplateformes, comme nous avions chez Xerox PARC. Ce n’est pas une nouvelle idée, elle remonte aux années 1960.

49:02 Mais en regardant Java, je me suis dit : comment peuvent-ils espérer survivre à tous les changements, modifications, adaptations et exigences d’interopérabilité sans un système méta, sans même pouvoir charger de nouvelles choses pendant l’exécution ?

49:37 Le fait que les gens aient adopté cela comme un grand espoir est probablement la chose la plus désolante pour moi, personnellement, depuis MS-DOS. Cela représente un véritable échec de la compréhension de la vue d’ensemble.

50:00 Cette notion de métaprogrammation peut être vue de différentes manières. Une implémentation particulière fait des choix pragmatiques, qui ne couvriront probablement pas tous les cas avec l’efficacité ou la richesse requise.

50:32 C’est une connaissance standard en programmation orientée objet : nous encapsulons pour cacher nos désordres, pour avoir différentes manières de traiter les mêmes concepts sans distraire le programmeur. Mais, comme les gens de Lisp et nous chez Xerox PARC l’avons découvert, cela s’applique aussi à la construction du langage lui-même.

51:03 Plus le langage peut voir ses propres structures, plus vous êtes libéré de la tyrannie d’une seule implémentation. C’est l’une des choses les plus critiques dont très peu de gens se préoccupent de manière pratique.

51:22 Une des raisons pour lesquelles ces questions méta seront importantes, au point que personne ne pourra les ignorer, est la question de l’interopérabilité sur Internet dans cinq ou dix ans.

51:40 Je ne crois pas que Microsoft pourra capturer Internet. Il est trop grand, trop de gens y apportent des idées, et les gens seront assez sophistiqués pour réaliser qu’une solution de type IBM ou Microsoft n’est ni nécessaire ni possible.

52:08 Cela signifie qu’il y aura des dizaines et des dizaines de systèmes d’objets différents, tous avec des sémantiques très similaires mais des détails pragmatiques très différents.

52:27 Si vous pensez à ce qu’est une URL, un message HTTP, un objet, ou un pointeur orienté objet, il devrait être clair que n’importe quel langage orienté objet peut internaliser ses propres pointeurs locaux vers n’importe quel objet dans le monde, peu importe où il a été créé. C’est tout l’intérêt de ne pas pouvoir voir à l’intérieur.

53:00 Une interopérabilité sémantique est possible presque immédiatement en adoptant simplement cette position. Cela va tout changer. Des choses comme Java Beans et CORBA ne suffiront pas, car à un moment donné, il faudra commencer à découvrir ce que les objets pensent pouvoir faire.

53:20 Cela mènera à un langage d’interface universel, qui n’est pas un langage de programmation en soi, mais plutôt un langage de prototypage permettant un échange profond d’informations sur ce que les objets pensent pouvoir faire, et permettant aux objets de faire des expériences avec d’autres objets de manière sûre pour voir comment ils répondent à divers messages. Ce sera crucial à automatiser dans les dix prochaines années.

53:57 Voici un excellent livre. Combien de personnes l’ont lu ? Quand ils l’ont écrit, je les ai appelés et j’ai dit : c’est le meilleur livre écrit depuis dix ans, mais pourquoi diable l’avoir écrit d’une manière si centrée sur Lisp, si fermée à un club ?

54:20 Ce livre est très difficile à lire si vous ne connaissez pas la culture Lisp ou la manière dont Scilos est fait. Il contient certaines des intuitions les plus profondes et pratiques sur la programmation orientée objet depuis de nombreuses années. Je vous le recommande vivement.

54:49 S’il y a des professeurs d’université ici qui veulent remporter le prochain prix Limoge, je le donnerai à quiconque réécrira ce livre pour que la communauté orientée objet générale puisse le comprendre. Ce serait un grand service à l’humanité.

55:08 Ce qui s’est passé dans la plupart du monde à partir des années 1970, c’est les types de données abstraits, une manière de penser centrée sur l’affectation. Quand j’ai fait cette diapositive, C++ n’était qu’un point à l’horizon. C’était comme MS-DOS : personne ne le prenait au sérieux, car qui tomberait pour une blague pareille ?

55:55 Mon histoire préférée sur C++ est chez Apple. Il y avait cet système d’exploitation, nommé par une coïncidence remarquable _Pink_.

56:06 Ce système avait deux caractéristiques intéressantes. La première, c’est qu’il devait toujours être terminé dans deux ans. Nous connaissons de grands concepteurs de systèmes d’exploitation, et je ne connais aucun bon système d’exploitation réalisé en deux ans, même par des gens dix fois plus intelligents que l’équipe de Pink.

56:35 L’autre chose, c’est qu’il devait être fait en C++ pour l’efficacité. Ne le faisons pas en Smalltalk, c’est trop lent. Eh bien, permettez-moi de vous dire qu’il n’y a rien de plus inefficace que de passer dix ans sur un système d’exploitation qui ne fonctionne jamais.

57:01 \[Applaudissements\]

57:08 Les pires sont ceux qui semblent fonctionner.

57:21 Prenons notre plan rose. Voici ma citation préférée de McLuhan : je ne sais pas qui a découvert l’eau, mais ce n’était pas un poisson. Il nous considérait comme les poissons, et l’eau comme nos structures de croyance, notre contexte.

57:39 Je crois que c’est la cause principale des difficultés dans notre domaine et dans l’humanité en général : adopter un seul point de vue et s’y engager comme à une religion. Cela s’est produit avec Smalltalk.

58:05 Schopenhauer, philosophe allemand du XIXe siècle, a dit que chaque idée passe par trois étapes. D’abord, elle est dénoncée comme l’œuvre de fous, ce que Swift appelait une confédération d’imbéciles. Ensuite, on remarque qu’elle était totalement évidente depuis le début. Enfin, le dénonciateur initial prétend l’avoir inventée. C’est là qu’elle entre dans sa phase religieuse.

58:47 Ce qui m’a le plus attristé avec Smalltalk, lorsqu’il est sorti de Xerox PARC, c’est qu’il a cessé de changer à bien des égards. À Xerox PARC, il y a eu quatre versions majeures, complètement différentes, sur environ dix ans, et des dizaines de versions significatives au sein de ces versions.

59:11 Ce que nous aimions le plus dans Smalltalk, ce n’était pas ce qu’il pouvait faire, mais le fait qu’il était un si bon véhicule pour amorcer la prochaine série d’idées sur la construction de systèmes. Quand Smalltalk est devenu commercial, ce processus s’est pratiquement arrêté.

59:31 Il y avait un livre, le célèbre _Blue Book_ d’Adèle et Dave, qui contenait le code pour créer des interpréteurs Smalltalk et démarrer ce processus soi-même. Presque personne n’en a profité. Presque aucune université, presque aucune entreprise commerciale.

59:58 Ce qu’ils ont manqué, c’est, pour moi, la chose la plus profonde que je voudrais vous transmettre aujourd’hui : nous ne savons pas encore concevoir des systèmes. Ne transformons pas ce que nous ne savons pas en religion, pour l’amour de Dieu.

1:00:05 Ce que nous devons faire, c’est penser, penser et repenser à ce qui est important. Nos systèmes doivent nous permettre d’atteindre les prochains niveaux d’abstraction à mesure que nous les découvrons.

1:00:24 Ce dont je suis le plus fier à propos de Smalltalk, presque la seule chose dont je suis fier de mon point de vue, c’est qu’il a été si efficace pour se débarrasser de ses versions précédentes, jusqu’à ce qu’il sorte dans ce monde.

1:00:38 Une des raisons pour lesquelles nous nous sommes à nouveau impliqués dans Smalltalk, après seize ans sans travailler sur les langages de programmation, est que nous avons lancé il y a quelques années un projet appelé Squeak.

1:00:56 Ce n’est pas une tentative de donner au monde un Smalltalk gratuit, mais un mécanisme d’amorçage pour quelque chose de bien meilleur que Smalltalk. Quand vous jouerez avec Squeak, pensez-y de ce point de vue : détruisez-le en utilisant ses propres mécanismes pour obtenir une version suivante.

1:01:21 Cherchez les pensées bleues. Je cherchais une façon de conclure cette conférence, car je pourrais continuer indéfiniment. Je me suis souvenu d’une histoire. Je suis organiste, et la plupart des organistes ont un héros nommé E. Power Biggs.

1:01:49 Il a ravivé l’intérêt pour l’orgue, surtout tel qu’il était joué aux XVIIe et XVIIIe siècles, et a eu une énorme influence sur nous tous, organistes. Un bon ami à moi était son assistant pendant de nombreuses années dans les années 1940 et 1950. Il a maintenant plus de quatre-vingts ans.

1:02:07 Quand nous l’invitons à dîner, nous le faisons toujours raconter des histoires sur E. Power Biggs. L’orgue que Biggs avait à l’époque pour ses émissions était un petit orgue médiocre, ni poisson ni oiseau, dans un petit musée à Harvard appelé Bush-Reisinger.

1:02:30 Mais toutes sortes de musiques y étaient jouées. Un jour, cet assistant a dû remplacer Biggs. Il lui a demandé quelle pièce devait être jouée. Biggs a répondu qu’il avait programmé la _Pièce héroïque_ de César Franck.

1:02:50 Si vous connaissez cette pièce, elle est faite pour les plus grands orgues jamais construits, les plus puissants, dans les plus grandes cathédrales, car c’est une œuvre symphonique pour orgue du XIXe siècle.

1:03:04 Biggs demandait à mon ami de jouer cela sur ce petit orgue minable. Il a dit : mais comment puis-je jouer ça là-dessus ? Biggs a répondu : joue-le simplement avec grandeur, joue-le avec grandeur.

1:03:26 La façon de rester avec l’avenir à mesure qu’il avance est de toujours jouer vos systèmes avec plus de grandeur qu’ils ne semblent en avoir maintenant. Merci.

Après avoir regardée la vidéo, vous je vous invite à réfléchir aux questions suivantes.

1.  Comment l’analogie entre la programmation orientée objet et l’architecture illustre-t-elle l’importance de concevoir des systèmes logiciels capables de gérer une complexité croissante ?
2.  En quoi la métaphore des « pensées bleues » peut-elle vous inspirer à sortir des paradigmes établis pour innover ?

La programmation orientée objet se diffuse ensuite dans de nombreux langages : C++ (1983) ajoute l’orienté objet au C, Java (1995) en fait un pilier de sa conception, Python, Ruby, C#, et bien d’autres adoptent ou s’inspirent de ces principes. La programmation orientée objet devient le paradigme dominant dans l’industrie logicielle, car on croit qu’elle facilite la modularité, la réutilisation et la maintenance du code.

Aujourd’hui, la programmation orientée objet est enseignée dans la plupart des cursus en informatique et reste au cœur du développement de logiciels complexes, bien qu’elle coexiste avec d’autres paradigmes (fonctionnel, procédural, etc.) dans les langages modernes.

Notre façon de programmer continuer d’évoluer. Aujourd’hui, plusieurs des idées fortes de la méthode orientée objet (comme l’héritage) sont vues comme parfois trop contraignantes. Néanmoins, les langages populaires comme Python, C#, Java, etc. relèvent de l’orienté objet.

_Définition._ La programmation orientée objet est un paradigme de programmation qui organise le code autour d’« objets » représentant des entités du monde réel ou conceptuel. Chaque objet regroupe des données (attributs) et des comportements (méthodes) et interagit avec d’autres objets via des messages ou des appels de méthodes.

Java [#](#java)
---------------

Java a été créé au début des années 1990 par James Gosling et son équipe chez Sun Microsystems. Le projet, initialement nommé « Oak », visait à développer un langage portable pour les appareils électroniques embarqués. En 1995, le langage est officiellement lancé sous le nom de Java, avec la promesse « écrire une fois, exécuter partout » (Write Once, Run Anywhere), grâce à la machine virtuelle Java (JVM) qui permet d’exécuter le même code sur différentes plateformes.

La JVM est un environnement d’exécution logiciel qui agit comme une couche d’abstraction entre le code Java compilé et le matériel ou le système d’exploitation de l’appareil sur lequel il s’exécute. Elle permet au même programme Java de fonctionner sur différentes plateformes (Windows, Linux, macOS, etc.) sans modification, à condition qu’une JVM spécifique à cette plateforme soit installée. Lorsque vous écrivez un programme en Java, il est d’abord compilé par le compilateur Java (javac) en un code intermédiaire appelé bytecode. Ce bytecode n’est pas du code machine directement exécutable par un processeur, mais un format standardisé compris par la JVM. La JVM lit le bytecode et le traduit en instructions spécifiques à la plateforme sur laquelle elle est installée.

Java connaît un succès rapide, d’abord dans le développement d’applets pour le web, puis dans les applications d’entreprise avec la plateforme Java EE. Au fil des années, Java s’impose comme un standard pour le développement de logiciels robustes, portables et sécurisés, aussi bien côté serveur (applications web, systèmes bancaires, etc.) que côté client (applications de bureau, Android).

Le langage évolue régulièrement : Java 5 introduit les génériques et les annotations, Java 8 apporte les expressions lambda et l’API Stream, Java 9 les modules, et les versions récentes (Java 17, 21…) continuent d’ajouter des fonctionnalités modernes (pattern matching, records, virtual threads…).

En 2010, Oracle rachète Sun Microsystems et devient le principal responsable du développement de Java. Aujourd’hui, Java reste l’un des langages les plus utilisés au monde, soutenu par une vaste communauté et de nombreux outils open source. Il est omniprésent dans l’industrie, l’enseignement, le développement mobile (Android), le cloud et l’Internet des objets.

Le langage Java est en pleine évolution. Certaines des techniques enseignées dans notre cours ne fonctionnent pas avec des versions précédentes du Java.

Version

Changement principal

Année de sortie

JDK 1.0

Lancement initial

1996

JDK 1.1

Classes internes

1997

J2SE 1.2

API Swing

1998

J2SE 1.3

Améliorations HotSpot

2000

J2SE 1.4

Assertions

2002

J2SE 5.0

Génériques

2004

Java SE 6

Performance JVM

2006

Java SE 7

Syntaxe try-with-resources

2011

Java SE 8

Expressions lambda

2014

Java SE 9

Système de modules

2017

Java SE 10

Inférence de types

2018

Java SE 11

Client HTTP standard

2018

Java SE 12

Switch expressions

2019

Java SE 13

Blocs de texte

2019

Java SE 14

Records (aperçu)

2020

Java SE 15

Classes scellées

2020

Java SE 16

Records finalisés

2021

Java SE 17

Pattern matching

2021

Java SE 18

API vectorielle (aperçu)

2022

Java SE 19

Threads virtuels

2022

Java SE 20

Structured Concurrency

2023

Java SE 21

Sequenced Collections

2023

Java SE 22

Foreign Function API

2024

Java SE 23

Module import simplifié

2024

Java SE 24

Améliorations Loom

2025

Java SE 25

Finalisation Valhalla

2025

Java SE 26

Optimisations Leyden

2026

Je vous invite à regarder cette vidéo par l’inventeur du Java (activité optionnelle). J’inclus une transcription en français.

Transcription traduite en françaisVoici une conversation avec James Gosling, le fondateur et principal concepteur du langage de programmation Java, qui, selon de nombreux indices, est le langage de programmation le plus populaire au monde, ou du moins toujours parmi les deux ou trois premiers. Nous n’avions qu’un temps limité pour cette conversation, mais je suis sûr que nous discuterons à nouveau à plusieurs reprises dans ce podcast. Résumé rapide des sponsors : Public Goods, BetterHelp et ExpressVPN. Veuillez consulter ces sponsors dans la description pour obtenir une réduction et soutenir ce podcast. En aparté, permettez-moi de dire que Java est le langage avec lequel j’ai appris pour la première fois la programmation orientée objet et, avec elle, l’art et la science de l’ingénierie logicielle. Également, au début de mes études universitaires, j’ai suivi un cours sur la programmation concurrente avec Java. En repensant à cette époque, avant que je ne tombe amoureux des réseaux neuronaux, l’art du calcul parallèle était à la fois algorithmiquement et philosophiquement fascinant pour moi. Avant cela, le concept d’un ordinateur dans mon esprit était quelque chose qui fait une chose à la fois. L’idée que nous puissions créer une abstraction de parallélisme, où l’on pourrait faire plusieurs choses en même temps tout en garantissant stabilité et exactitude, était magnifique. Alors que certains à l’université prenaient des drogues pour élargir leur esprit, moi, je prenais des cours de programmation concurrente. Si vous appréciez ce contenu, abonnez-vous sur YouTube, donnez-lui cinq étoiles sur Apple Podcast, suivez sur Spotify, soutenez sur Patreon ou connectez-vous avec moi sur Twitter à @lexfridman. Comme d’habitude, je vais faire quelques minutes de publicités maintenant, sans publicités au milieu. J’essaie de rendre cela intéressant, mais je vous donne des horodatages, alors n’hésitez pas à passer, mais veuillez consulter les sponsors en cliquant sur les liens dans la description. C’est la meilleure façon de soutenir ce podcast.

Ce programme est sponsorisé par Public Goods, le guichet unique pour des produits ménagers abordables, durables et sains. Je prends leur huile de poisson et utilise leur brosse à dents, par exemple. Leurs produits ont souvent un design minimaliste noir et blanc que je trouve tout simplement magnifique. Certaines personnes demandent pourquoi je porte ce costume noir et cette cravate ; il y a une simplicité qui, pour moi, concentre mon esprit sur les éléments les plus importants de chaque instant de chaque jour, tirant uniquement sur le fil de l’essentiel dans tout ce que la vie a à m’offrir. Ce n’est pas une question de comment je parais, mais de comment je me sens. C’est ce que le design représente pour moi : créer une expérience consciente intérieure, pas un look extérieur. Quoi qu’il en soit, Public Goods plante un arbre pour chaque commande passée, ce qui est plutôt cool. Visitez publicgoods.com/lex ou utilisez le code LEX à la caisse pour obtenir 15 dollars de réduction sur votre première commande.

Ce programme est également sponsorisé par BetterHelp, écrit H-E-L-P. Consultez-le sur betterhelp.com/lex. Ils déterminent ce dont vous avez besoin et vous mettent en relation avec un thérapeute professionnel agréé en moins de 48 heures. J’ai discuté avec une personne là-bas et j’ai apprécié. Bien sûr, je parle aussi régulièrement à David Goggins ces jours-ci, qui n’est définitivement pas un thérapeute professionnel agréé, mais il m’aide à rencontrer ses démons et les miens, et à devenir à l’aise en leur présence. Chacun est différent, mais pour moi, je pense que la souffrance est essentielle à la création, mais on peut souffrir magnifiquement, d’une manière qui ne vous détruit pas. Je pense que la thérapie peut aider, quelle que soit la forme que prend cette thérapie, et je pense que BetterHelp est une option qui vaut la peine d’être essayée. Ils sont faciles, privés, abordables et disponibles dans le monde entier. Vous pouvez communiquer par texte à tout moment et programmer des sessions audio et vidéo hebdomadaires. Consultez-le sur betterhelp.com/lex.

Ce programme est également sponsorisé par ExpressVPN. Vous pouvez l’utiliser pour débloquer des films et des émissions uniquement disponibles dans d’autres pays. Je l’ai fait récemment avec Star Trek Discovery sur Netflix UK, principalement parce que je me demande ce que ça fait de vivre à Londres. Je pense à déménager de Boston vers un endroit où je pourrais construire l’entreprise dont j’ai toujours rêvé. Londres n’est probablement pas dans le top trois, mais dans le top dix, c’est sûr. Le choix numéro un actuellement est Austin, pour de nombreuses raisons dont je parlerai peut-être une autre fois. San Francisco, malheureusement, a chuté de la première place, mais reste dans la course. Si vous avez des conseils, faites-le-moi savoir. Quoi qu’il en soit, consultez ExpressVPN. Il vous permet de changer votre localisation dans près de 100 pays et il est super rapide. Allez sur expressvpn.com/lexpod pour obtenir trois mois supplémentaires d’ExpressVPN gratuitement.

Et maintenant, voici ma conversation avec James Gosling.

### Nombres irrationnels [#](#nombres-irrationnels)

J’ai lu quelque part que la racine carrée de deux est votre nombre irrationnel préféré. Je n’ai aucune idée d’où cela vient. Y a-t-il une part de vérité là-dedans ? Y a-t-il quelque chose en mathématiques ou dans les nombres que vous trouvez beau ?

Oh, eh bien, il y a beaucoup de choses en mathématiques qui sont vraiment belles. Vous savez, je me considérais comme vraiment bon en mathématiques, et ces jours-ci, je me considère comme vraiment mauvais en mathématiques. Je n’ai jamais vraiment eu un faible pour la racine carrée de deux, mais quand j’étais adolescent, il y avait ce livre intitulé _Le dictionnaire des nombres curieux et intéressants_, que pour une raison quelconque, j’ai lu en entier et presque mémorisé. Et j’ai commencé cette étrange habitude, quand je remplissais des chèques ou payais avec des cartes de crédit, de vouloir que le reçu totalise un nombre intéressant. Y a-t-il des nombres qui vous ont marqué, qui vous font vous sentir bien ?

Ils ont tous une histoire, et heureusement, je les ai pour la plupart oubliés. Comme 42 ? Eh bien, oui, celui-là, 42, est assez magique. Et les irrationnels ? Y a-t-il une histoire avec la racine carrée de deux quelque part ? Eh bien, c’est comme le seul nombre qui a détruit une religion. De quelle manière ? Eh bien, les pythagoriciens croyaient que tous les nombres étaient parfaits et que tout pouvait être représenté comme un nombre rationnel. À cette époque, une preuve est apparue montrant qu’il n’existait aucune fraction rationnelle dont la valeur était égale à la racine carrée de deux, et cela signifiait que rien dans ce monde n’est parfait, pas même les mathématiques. Eh bien, cela signifie que votre définition de parfait était imparfaite. Ensuite, il y a les théorèmes d’incomplétude de Gödel au 20e siècle qui ont encore tout ruiné pour tout le monde. Bien que le théorème de Gödel, la leçon que j’en tire, ce n’est pas qu’il y a des choses qu’on ne peut pas savoir, ce qu’il dit fondamentalement, mais que les gens veulent des réponses en noir et blanc, vrai ou faux. Mais si vous autorisez une logique à trois états, vrai, faux ou peut-être, alors la vie est belle. J’ai l’impression qu’il y a un parallèle avec le discours politique moderne quelque part là-dedans.

### Mathématiques et programmation [#](#math%c3%a9matiques-et-programmation)

Avec votre amour précoce ou votre appréciation de la beauté des mathématiques, voyez-vous un parallèle entre ce monde et celui de la programmation ?

La programmation, c’est tout au sujet de la structure logique, de la compréhension des motifs qui émergent du calcul, de la compréhension, je veux dire, c’est souvent comme tracer un chemin à travers le graphe des possibilités pour trouver une route courte, c’est-à-dire trouver un programme court qui fait le travail. Mais sur le sujet des nombres irrationnels, voyez-vous la programmation comme fondamentalement désordonnée, peut-être contrairement aux mathématiques ? Je ne la considère pas comme désordonnée. Vous savez, vous regardez quelqu’un qui est bon en mathématiques faire des mathématiques, et souvent, c’est assez désordonné. Parfois, c’est un peu magique. Quand j’étais étudiant diplômé, l’un des étudiants, Jim Sax, avait cette réputation d’être une sorte de machine humaine de preuve de théorèmes ambulante et parlante. Si vous aviez un problème difficile avec quelque chose, vous pouviez l’aborder dans le couloir et dire « Jim », et il faisait cette chose amusante où il se redressait, ses yeux se déconcentraient un peu, il disait « hum », comme dans les films d’aujourd’hui, puis il se redressait et disait « n log n » et s’en allait. Et vous vous disiez, eh bien, d’accord, donc n log n est la réponse, comment est-il arrivé là ? À ce moment-là, il était déjà au bout du couloir. C’est juste l’oracle, la boîte noire qui vous donne la réponse, et ensuite vous devez trouver le chemin de la question à la réponse.

### Style de codage [#](#style-de-codage)

Dans l’une des vidéos que j’ai vues, vous avez mentionné Don Knuth, du moins en recommandant son livre comme quelque chose que les gens devraient lire. Mais en termes de science informatique théorique, voyez-vous quelque chose de beau là-dedans qui vous a inspiré dans votre travail sur les langages de programmation, dans ce monde des algorithmes et de la complexité, et ces choses plus formelles et mathématiques ? Ou cela ne vous a-t-il pas vraiment marqué dans votre vie de programmeur ?

Cela m’a marqué assez clairement, car l’une des choses qui me tient à cœur, c’est de pouvoir regarder un morceau de code et me prouver à moi-même qu’il fonctionne. Par exemple, je me trouve en désaccord avec beaucoup de gens autour de moi sur des questions comme la manière de structurer un logiciel. Les ingénieurs logiciels deviennent très pointilleux sur la façon dont ils formatent les documents qui sont les programmes, où ils mettent les nouvelles lignes, les accolades, et tout le reste. Moi, j’ai tendance à opter pour un style très dense, pour minimiser l’espace blanc, pour maximiser la quantité que je peux voir d’un coup. J’aime pouvoir voir une fonction entière et comprendre ce qu’elle fait, plutôt que de devoir défiler, défiler, défiler et me souvenir. Je suis d’accord avec vous là-dessus. Mais les gens n’aiment pas ça. J’ai eu plusieurs fois des équipes d’ingénieurs qui ont organisé ce qui était effectivement une intervention. Ils m’invitaient à une réunion, tout le monde arrivait avant moi, et ils me regardaient tous en disant : « James, à propos de ton style de codage. »

Je suis un peu une personne étrange pour programmer, car je ne pense pas très bien verbalement. Je suis naturellement un lecteur lent. Ce que la plupart des gens appelleraient un penseur visuel. Donc, quand vous pensez à un programme, que voyez-vous ? Je vois des images. Quand je regarde un morceau de code sur une feuille de papier, il se transforme très rapidement en une image, presque comme une pièce de machinerie, avec ceci connecté à cela, comme des engrenages. Je les vois plus comme ça que comme la structure verbale ou lexicale des lettres. Donc, quand vous regardez le programme, c’est pourquoi vous voulez tout voir au même endroit, pour pouvoir le mapper à quelque chose de visuel, et ça saute de la page. Quelles sont les entrées, les sorties, que fait ce truc ? Obtenir une vision complète.

### Premier ordinateur [#](#premier-ordinateur)

Pouvons-nous remonter dans vos souvenirs, accéder à votre mémoire à long terme ? Quel est le premier programme que vous ayez jamais écrit ?

Je n’ai aucune idée de ce qu’était le premier. Je sais sur quelle machine j’ai appris à programmer. C’était un PDP-8, à l’Université de Calgary. Vous souvenez-vous des spécifications ? Oh oui, la machine avait 4 Ko de RAM, des mots de 12 bits, la fréquence d’horloge était d’environ un tiers de mégahertz. Donc, on n’atteignait même pas le mégahertz. Aujourd’hui, on est environ 10 000 fois plus rapides. Était-ce une sorte de superordinateur, un ordinateur sérieux ? Non, le PDP-8i était la première chose que les gens appelaient un mini-ordinateur. Ils étaient assez peu coûteux pour qu’un laboratoire universitaire puisse peut-être se permettre d’en acheter un. Y avait-il du partage de temps, tout ça ? Il y avait effectivement un système d’exploitation à partage de temps pour cela, mais il n’était pas vraiment largement utilisé. La machine sur laquelle j’ai appris était cachée dans un coin reculé du centre informatique. Elle avait été achetée dans le cadre d’un projet de mise en réseau informatique, mais elle n’était pas beaucoup utilisée. Elle était juste là, et j’ai remarqué qu’elle était juste là, alors j’ai commencé à jouer avec, et personne ne semblait s’en soucier, alors j’ai continué. J’avais un clavier et un moniteur ? Oh, c’était bien avant que les moniteurs ne soient courants. C’était littéralement une télétype modèle 33, avec un lecteur de bande perforée. L’interface utilisateur n’était pas terrible. C’était le premier ordinateur construit avec des circuits intégrés, mais par circuits intégrés, je veux dire qu’ils avaient environ 10 ou 12 transistors sur une seule puce de silicium, pas les 10 ou 12 milliards que les machines ont aujourd’hui.

Qu’est-ce que ça faisait de travailler là-dessus ? Aviez-vous des intuitions sur la magie de l’amélioration exponentielle, de la loi de Moore, du potentiel de l’avenir qui était à portée de main ? Oh, c’était juste cool, un jouet. J’ai toujours aimé construire des choses, mais le problème avec la construction, c’est qu’il faut des pièces, du bois, des fils, des interrupteurs, des trucs comme ça, et ça coûte de l’argent. Là, vous pouviez construire des choses arbitrairement compliquées sans avoir besoin de matériaux physiques. Ça ne demandait pas d’argent. C’est une bonne manière de décrire la programmation. Si vous aimez construire des choses, c’est complètement accessible, vous n’avez besoin de rien, et n’importe qui, de n’importe où, peut construire quelque chose de vraiment cool. Oui, si vous avez accès à un ordinateur, vous pouvez construire toutes sortes de trucs fous. Et quand vous étiez quelqu’un comme moi, qui n’avait vraiment pas d’argent, je me souviens de convoiter l’achat d’un transistor. Quand je faisais des projets électroniques, ils étaient principalement réalisés en fouillant dans les poubelles pour trouver des déchets. L’un de mes gros butins était des racks de relais abandonnés à l’arrière d’un centre de commutation de la compagnie de téléphone. Oh, sympa, qu’en avez-vous fait ? J’ai construit une machine qui jouait au morpion. Bien sûr, avec des relais. Ce qui était vraiment difficile, c’est que tous les relais nécessitaient une tension spécifique, mais obtenir une alimentation qui fournissait cette tension était assez compliqué. Comme j’avais un tas de téléviseurs jetés, j’ai dû bricoler quelque chose qui n’était pas correct mais qui fonctionnait. Je faisais fonctionner ces relais à 300 volts, et aucune des connexions électriques n’était correctement scellée. Vous avez survécu à cette période de votre vie ? Oh, pour tant de raisons. Vous savez, il est assez courant pour les geeks adolescents de découvrir, oh, le thermite, c’est vraiment facile à faire.

Vous souvenez-vous d’un programme à Calgary que vous avez écrit, quelque chose qui se démarque, et en quel langage ? Eh bien, la plupart des programmes de taille significative étaient en code assembleur. En fait, avant d’apprendre l’assembleur, il y avait ce langage de programmation sur le PDP appelé Focal 5. Focal 5 était une sorte de Fortran très simplifié. Je me souviens d’avoir joué à construire des programmes qui faisaient des choses comme jouer au blackjack, au solitaire, ou pour une raison quelconque, les choses que j’aimais vraiment étaient celles où je traçais des graphiques, comme une fonction ou des données, et ensuite je les traçais. Et ça s’imprimait, pas sur un moniteur, mais sur une télétype, en utilisant quelque chose comme une machine à écrire pour tracer des fonctions.

Quand êtes-vous tombé amoureux de la programmation pour la première fois ? Quel était le premier langage de programmation, peut-être en tant qu’ingénieur logiciel sérieux, où vous avez pensé que c’était une chose magnifique ? Je n’ai jamais vraiment pensé qu’un langage particulier était magnifique, car pour moi, ce n’était jamais vraiment à propos du langage, mais de ce qu’on pouvait faire avec. Même aujourd’hui, les gens essaient de m’entraîner dans des débats sur des formes particulières de syntaxe pour ceci ou cela, et je suis comme, qui s’en soucie ? C’est à propos de ce que vous pouvez faire, pas de comment vous écrivez le mot. À l’époque, j’ai appris des langages comme PL/I, Fortran, Cobol, et au moment où les gens étaient prêts à m’embaucher pour faire des choses, c’était surtout du code assembleur, du code assembleur PDP, du code Fortran, et du code assembleur Control Data pour le CDC 6400, qui était, je suppose, un superordinateur précoce, même si ce superordinateur avait moins de puissance de calcul que mon téléphone, et de loin.

### Lisp [#](#lisp)

Vous avez également montré une appréciation pour le meilleur langage de tous les temps, que tout le monde considère comme étant Lisp. Eh bien, Lisp était définitivement sur ma liste des plus grands langages qui aient existé. Est-ce le numéro un ? Je ne le mettrais pas en numéro un maintenant. Est-ce les parenthèses ? Qu’aimez-vous et qu’aimez-vous moins dans Lisp ?

Eh bien, je suppose que la première chose à ne pas aimer, c’est qu’il y a tellement de parenthèses. Ce que j’aime, c’est que, malgré toutes ces parenthèses, on obtient une structure de langage intéressante. J’ai toujours pensé qu’il y avait une version plus conviviale de Lisp cachée quelque part, mais je n’ai jamais vraiment passé beaucoup de temps à y réfléchir. Plus haut dans la chaîne alimentaire pour moi, après Lisp, il y a Simula, que très peu de gens ont utilisé, mais qui, je pense, a eu une énorme influence. Simula, si je ne me trompe pas, est l’un des premiers langages fonctionnels ? Non, c’était le premier langage de programmation orienté objet. C’est là que les langages orientés objet ont vraiment pris forme. C’était aussi le langage où les coroutines sont apparues pour la première fois comme partie intégrante du langage, permettant un style de programmation que l’on pouvait considérer comme multi-threadé avec beaucoup de parallélisme. Il y avait des idées de parallélisme là-dedans. La première spécification de Simula, Simula 67, date de 1967. Les coroutines étaient presque des threads, mais elles n’avaient pas de véritable concurrence, donc on pouvait s’en sortir sans verrouillage complexe. Mais en termes de style de programmation, on pouvait écrire du code et le penser comme étant multi-threadé. Le modèle mental était très proche d’un modèle multi-threadé, et toutes sortes de problèmes pouvaient être abordées très différemment.

### Écrire une implémentation d’Emacs en C [#](#%c3%a9crire-une-impl%c3%a9mentation-demacs-en-c)

Pour revenir au monde de Lisp un bref instant, à CMU, vous avez écrit une version d’Emacs qui, je pense, a eu un impact significatif sur l’histoire d’Emacs. Quelle était votre motivation à ce moment-là ?

C’était en 85 ou 86. J’utilisais Unix depuis quelques années, et la plupart des éditions se faisaient avec cet outil appelé Eddie, qui était une sorte d’ancêtre de vi. Était-ce un bon éditeur ? Pas un bon éditeur, sauf si votre dispositif d’entrée est une télétype, là c’est plutôt pas mal. C’était certainement plus humain que TECO, qui était courant dans l’univers DEC à l’époque. TECO, c’est le Text Editor and Corrector. L’Emacs original est sorti comme Editor MACroS. TECO avait une manière d’écrire des macros, et l’Emacs original de MIT a commencé comme une collection de macros pour TECO. Mais ensuite, le style Emacs est devenu populaire, d’abord à MIT, puis d’autres implémentations d’Emacs ont vu le jour, avec des bases de code entièrement différentes, mais dans le style philosophique de l’Emacs original.

Quelle était la philosophie d’Emacs, et d’ailleurs, toutes les implémentations étaient-elles toujours en C, et comment Lisp s’intègre-t-il dans l’histoire ? Non, le tout premier Emacs a été écrit comme un ensemble de macros pour l’éditeur de texte TECO. Le langage de macros de TECO était probablement le format le plus ridiculement obscur. Si vous regardiez un programme TECO sur une page, vous penseriez que ce sont juste des caractères aléatoires. Ça ressemble vraiment à du bruit de ligne, bien pire que LaTeX. Mais si vous utilisiez beaucoup TECO, ce que j’ai fait, TECO était complètement optimisé pour la frappe rapide au toucher. Il n’y avait presque pas de commandes à deux caractères, presque toutes étaient à un seul caractère. Chaque caractère sur le clavier était une commande distincte, et en fait, chaque caractère était généralement deux ou trois commandes, car vous aviez shift, control, et tout ça. C’était une manière de coder très densément. Ce qu’Emacs a fait principalement, c’est rendre cela visuel. Une façon de penser à TECO, c’est d’utiliser Emacs avec les yeux fermés, où vous devez maintenir un modèle mental de votre document. Vous devez vous dire, d’accord, le curseur est entre le « a » et le « e », et je veux les échanger, donc je fais ceci. C’est presque exactement l’ensemble de commandes d’Emacs, ou à peu près, mais en utilisant Emacs avec les yeux fermés.

Ce qu’Emacs a ajouté, c’est la capacité de voir visuellement ce que vous éditiez, sous une forme qui correspondait à votre document. Beaucoup de choses ont changé dans l’ensemble des commandes. Comme il était programmable, il était très flexible, vous pouviez ajouter de nouvelles commandes pour toutes sortes de choses. Ensuite, les gens ont réécrit Emacs plusieurs fois en Lisp. Il y en a eu un pour la machine Lisp à MIT, un pour Multics. Un été, j’ai eu un job d’été pour travailler sur le compilateur Pascal pour Multics. C’était la première fois que j’utilisais Emacs, pour écrire les compilateurs. J’ai passé trois mois intensifs à travailler sur ce compilateur Pascal, vivant pratiquement dans Emacs, celui écrit en MacLisp par Bernie Greenberg. J’ai pensé, wow, c’est une manière tellement meilleure d’éditer. Ensuite, je suis retourné à CMU, où nous avions un peu de tout, et comme je travaillais principalement dans l’univers Unix, et qu’Unix n’avait pas d’Emacs, j’ai décidé de régler ce problème.

J’ai donc écrit cette implémentation d’Emacs en C, car à l’époque, C était vraiment le seul langage qui fonctionnait sur Unix. Vous étiez à l’aise avec C aussi ? Oh oui, à ce moment-là, j’avais fait beaucoup de codage en C. C’était en 86. Ça fonctionnait assez bien pour que je puisse l’utiliser pour s’éditer lui-même en un mois ou deux. Ensuite, ça a pris le contrôle de l’université, ça s’est répandu, puis c’est mort. Et puis c’est sorti à l’extérieur, en grande partie parce qu’Unix a pris le contrôle de la communauté de recherche sur l’ARPANET. Emacs était en quelque sorte le meilleur éditeur disponible, il a pris le dessus. Il y a eu une brève période où j’avais des identifiants de connexion sur tous les hôtes non militaires de l’ARPANET, parce que les gens disaient : « Oh, pouvons-nous installer ça ? » et je disais : « Oui, mais vous aurez besoin d’aide. » À l’époque, la sécurité n’était pas une préoccupation, personne ne s’en souciait.

### Les débuts de l’Internet [#](#les-d%c3%a9buts-de-linternet)

Comment étaient les débuts de l’ARPANET et de l’Internet ? Pouviez-vous imaginer que l’Internet ressemblerait à ce qu’il est aujourd’hui ?

Certaines choses sont remarquablement inchangées. L’une des choses que j’ai remarquées très tôt, à Carnegie Mellon, c’est que beaucoup de vie sociale s’est centrée autour de l’ARPANET. Des choses comme organiser un déjeuner ou sortir en rendez-vous, tout était piloté par les médias sociaux. Entre les emails et les messages texte, car les messages texte faisaient partie de l’ARPANET très tôt. Il n’y avait pas de téléphones portables, mais vous étiez assis à un terminal, vous tapiez des trucs, essentiellement des emails ou des messages d’une ligne, comme un chat. Ma vie était devenue telle que je vivais sur les médias sociaux dès le milieu des années 80. Quand cela s’est transformé en Internet et que les médias sociaux ont explosé, je me suis dit : « Quel est le problème ? C’est juste une question d’échelle. » L’échelle est simplement stupéfiante, mais les fondamentaux, d’une certaine manière, ont à peine changé. Les technologies derrière le réseautage ont beaucoup changé, le moment décisif étant le passage de l’ARPANET à l’Internet, puis les gens ont commencé à faire évoluer, évoluer, évoluer. L’expansion qui s’est produite au début des années 90, et la manière dont tant d’intérêts établis ont combattu l’Internet… Qui ? Parce qu’on ne peut pas vraiment contrôler l’Internet. Les compagnies de télévision par câble, les diffuseurs, les compagnies de téléphone, au plus profond de leur être, détestaient l’Internet. C’était souvent drôle, car si vous pensez à une compagnie de câble, la plupart des employés ont pour mission de diffuser des émissions de télévision, des films, à leurs clients. Ils considèrent leur travail comme étant au service de leurs clients. Mais en montant dans la hiérarchie, cette vision change, car le véritable business des compagnies de câble a toujours été de vendre des globes oculaires aux annonceurs.

Cette vision d’une compagnie de câble ne se révélait pas à la plupart des gens qui y travaillaient. J’ai eu divers accrochages avec des compagnies de câble où l’on pouvait voir, dans les couches stratifiées de l’entreprise, cette vision que la raison d’avoir la télévision par câble est de capturer des globes oculaires. Les gens qui travaillaient dans les compagnies de téléphone ou de câble pensaient que leur travail était de fournir du contenu délicieux à leurs clients, et que les clients paieraient pour cela. Plus haut, ils voyaient cela comme une manière d’attirer des globes oculaires, puis de vendre ces globes oculaires collés à leur contenu aux annonceurs. L’Internet était donc une concurrence dans ce sens. Nous avions envoyé une proposition détaillée, à l’époque chez Sun, au début des années 90, qui disait essentiellement : avec les technologies Internet, n’importe qui peut devenir un fournisseur de contenu. Vous pourriez distribuer des films familiaux à vos parents ou cousins, n’importe où. N’importe qui peut devenir éditeur. Vous pensiez déjà à ça ? Oui, c’était au début des années 90. Nous pensions que ce serait génial, des choses comme des films familiaux, des essais d’enfants, des informations de supermarchés ou de restaurants. La réaction des compagnies de câble était : non, car alors nous sommes hors jeu.

Qu’est-ce qui fait que les entreprises ne voyaient pas de chemin vers des revenus ? Il y a une leçon là-dedans pour les grandes entreprises, écouter, anticiper les renégats, les gens qui pensent hors des sentiers battus comme vous, rédigeant des propositions sur ce que cela pourrait être. Si vous êtes dans une position où vous gagnez des tonnes d’argent avec un modèle commercial particulier, l’idée de sauter le fossé, vous savez, vous pouvez voir de nouveaux modèles plus efficaces émerger. Comme les appareils photo numériques par rapport aux appareils à pellicule. Pourquoi faire le saut quand vous gagnez tant d’argent avec la pellicule ? Chez Sun, l’un de nos gros clients était Kodak. J’ai beaucoup interagi avec des gens de Kodak, et ils avaient un gros groupe de recherche et développement sur les appareils photo numériques. Ils savaient que, en regardant les tendances, la qualité des appareils numériques s’améliorait, et les lignes allaient se croiser. Le moment où les lignes se croiseraient serait un effondrement de leur business, et ils le voyaient clairement. Le problème, c’est que jusqu’à ce qu’ils heurtent le mur, ils gagnaient des tonnes d’argent. Quand ils faisaient les calculs, ça n’avait jamais de sens de mener la charge.

### Elon Musk, Steve Jobs, Jeff Bezos [#](#elon-musk-steve-jobs-jeff-bezos)

C’est là que le leadership visionnaire entre en jeu, non ? Quelqu’un doit arriver et dire : faisons le saut. Oui, mais c’est aussi prendre le coup. Vous pouvez dessiner tous les graphiques que vous voulez montrant que si nous sautons d’ici, sur notre trajectoire actuelle, nous allons vers une falaise. Si nous nous forçons à une transition proactive, nous pouvons être sur la prochaine vague, mais il y aura une période où nous serons dans un creux. Presque toujours, il y a un creux quand on traverse le fossé. Mais la manière dont fonctionnent les entreprises publiques, en rendant des comptes tous les trimestres, la seule chose qu’un PDG ne doit jamais faire, c’est prendre un gros coup sur un trimestre. Beaucoup de ces transitions impliquent un gros coup pendant un certain temps, un, deux, trois trimestres. Certaines entreprises, comme Tesla et Amazon, sont de très bons exemples d’entreprises qui prennent d’énormes coups, mais elles ont le luxe de pouvoir ignorer le marché boursier pendant un moment. Ce n’est pas vraiment vrai aujourd’hui, mais au début de ces deux entreprises, elles se fichaient des rapports trimestriels, elles se préoccupaient du nombre de clients satisfaits. Avoir le plus de clients satisfaits possible peut souvent être un ennemi des résultats financiers.

Comment font-elles pour que ça marche ? Amazon a opéré dans le négatif pendant longtemps, c’est comme investir dans l’avenir. Amazon, Google, Tesla, Facebook, beaucoup d’entre elles avaient ce qu’on pourrait appeler de l’argent patient, souvent parce qu’il y avait une figure centrale charismatique avec un gros bloc d’actions, et ils pouvaient simplement le faire. Sur ce sujet, vous avez eu l’occasion de travailler avec de grands leaders. Quelles sont vos pensées sur le leadership d’Elon Musk chez Tesla, de Jeff Bezos chez Amazon, tous ces gens avec de grandes quantités d’actions et une vision dans leur entreprise ? Ce sont des fondateurs, ou des gens arrivés très tôt, et Amazon a pris beaucoup de sauts. À l’époque, les gens critiquaient probablement : qu’est-ce que cette librairie ? Bezos avait une vision et la capacité de la suivre. Beaucoup de gens ont des visions, et la vision moyenne est complètement idiote, et vous vous écrasez et brûlez. Le taux d’échec et d’incendie de la Silicon Valley est assez élevé. Ils ne s’écrasent pas nécessairement parce que les idées étaient stupides, mais souvent, c’est juste une question de timing, de chance. Prenez des entreprises comme Tesla. Le Tesla original, avant Elon, allait à peu près bien, mais il les a conduits avec une vision vraiment forte. Il prenait des décisions qui étaient généralement assez bonnes. Le Model X était un peu une idée farfelue, mais il l’a fait audacieusement. Tant de gens se sont opposés aux portes en ailes de faucon. D’un point de vue technique, ces portes sont ridicules, un véritable désastre, mais elles sont exactement le symbole d’un grand leadership : vous avez une vision, et si vous faites quelque chose de stupide, faites-le vraiment stupide, et allez-y à fond.

Pour revenir un peu en arrière, à Steve Jobs. Il était un personnage similaire, avec une vision forte et très intelligent. Il n’était pas intelligent sur les aspects technologiques, mais sur la relation humaine entre les humains et les objets. Mais c’était un con. Pouvons-nous nous attarder là-dessus un peu ? Les gens disent qu’il était un con. Est-ce une caractéristique ou un défaut ? C’est la question. Prenez quelqu’un comme Steve, qui était vraiment dur avec les gens. Était-il inutilement dur, ou faisait-il simplement en sorte que les gens atteignent sa vision ? On pourrait le voir des deux façons. Les résultats racontent une histoire. Par ses manières de con, il a souvent poussé les gens à faire le meilleur travail de leur vie. J’ai passé plusieurs entretiens avec lui, j’ai eu diverses négociations avec lui. Même si, personnellement, je l’aimais, je n’aurais jamais pu travailler pour lui. Pourquoi ? Pouvez-vous mettre des mots sur la tension que vous pensez serait destructrice plutôt que constructive ? Il criait sur les gens, il les insultait. Vous n’aimez pas ça ? Non, je ne pense pas qu’il soit nécessaire de faire ça. Il y a pousser les gens à exceller, et puis il y a aller trop loin, et je pense qu’il était du mauvais côté de la ligne.

Je n’ai jamais travaillé pour Musk, je connais plusieurs personnes qui l’ont fait. Beaucoup ont dit, et ça apparaît beaucoup dans la presse, que Musk est un peu comme ça. Une des choses que je déteste dans la Silicon Valley ces jours-ci, c’est que beaucoup de succès fulgurants sont dirigés par des gens qui sont de vrais cons. Il semble y avoir cette mythologie, venue de Steve Jobs, que la raison de son succès était qu’il était super dur avec les gens. Dans certains milieux, les gens commencent à se dire : si je veux réussir, je dois être un vrai con. Pour moi, ça ne tient pas. Je connais beaucoup de gens qui réussissent et qui ne sont pas des cons, qui sont des gens parfaitement bien. Ils ont tendance à ne pas être sous les projecteurs. Le grand public, d’une manière ou d’une autre, élève les cons au statut de héros, parce qu’ils font des choses qui les mettent dans la presse.

### Travailler dur et intelligemment [#](#travailler-dur-et-intelligemment)

Sur le côté des cons, il y a aussi, si je devais critiquer ce que j’ai vu dans la Silicon Valley, une résistance à travailler dur. Jobs et Musk poussent les gens à travailler vraiment dur. La question est de savoir s’il est possible de le faire gentiment. Ce qui me dérange, peut-être parce que je romantise la souffrance, c’est que je pense que travailler dur est essentiel pour accomplir quelque chose d’intéressant, vraiment dur. Dans le jargon de la Silicon Valley, c’est probablement trop dur. Cette idée qu’il faut travailler intelligemment, pas dur, me semble souvent dire qu’il faut être paresseux. Bien sûr, vous voulez travailler intelligemment, être le plus efficace possible, mais pour découvrir le chemin efficace, comme nous parlions des programmes courts, eh bien, l’idée de travailler intelligemment et dur, ce n’est pas l’un ou l’autre, c’est les deux. Les gens qui disent qu’il faut travailler intelligemment, pas dur, échouent presque toujours. Merci. C’est juste une recette pour le désastre. Il y a des contre-exemples, mais ce sont plus des gens qui ont bénéficié de la chance et du timing. Vous dites qu’on peut pousser les gens à travailler dur et à faire un travail incroyable sans être méchant. Google est un bon exemple. Le leadership de Google, à travers son histoire, a été un assez bon exemple de ne pas être méchant. Les jumeaux, Larry et Sergey, sont tous deux assez gentils. Sundar Pichai est très gentil. C’est une culture de gens qui travaillent vraiment, vraiment dur.

### Open source [#](#open-source)

Une question un peu tendue. Nous parlons d’Emacs, il semble que vous ayez fait un travail incroyable, mais en dehors de Java, certaines de vos réalisations n’ont pas été aussi populaires qu’elles auraient pu l’être à cause de problèmes de licences et d’open source. Quelles sont vos pensées sur tout ce désordre, sur l’open source maintenant, avec le recul ? Sur les licences, l’open source, pensez-vous que l’open source est une bonne chose, une mauvaise chose ? Avez-vous des regrets ? Avez-vous tiré des leçons de cette expérience ?

En général, je suis un grand fan de l’open source, de la manière dont il peut être utilisé pour construire des communautés, promouvoir le développement des choses, favoriser la collaboration. Tout cela est vraiment formidable. Quand l’open source devient une religion qui dit que tout doit être open source, je deviens un peu bizarre à ce sujet, car c’est un peu comme dire que tous les ingénieurs logiciels doivent faire vœu de pauvreté, comme si c’était contraire à l’éthique d’avoir de l’argent, de construire une entreprise. Une partie de moi y adhère un peu, parce que les gens qui gagnent des milliards de dollars grâce à un brevet qui est venu d’une idée fulgurante alors qu’ils étaient à moitié éveillés dans leur lit, c’est de la chance, bravo pour eux. Mais la manière dont cela explose parfois en quelque chose qui ressemble beaucoup à de l’exploitation, on voit beaucoup ça dans l’industrie pharmaceutique, avec des médicaments qui coûtent 100 dollars par jour. Ce qui me dérange avec l’open source, c’est quand quelque chose n’est pas open source et que, à cause de ça, c’est un produit moins bon. Par exemple, votre implémentation d’Emacs aurait pu être l’implémentation dominante. J’utilise Emacs, c’est mon IDE principal, je m’excuse auprès du monde, mais je l’aime toujours. J’aurais pu utiliser votre implémentation d’Emacs. Pourquoi ne le fais-je pas ? Vous utilisez GNU Emacs ? Je suppose que c’est celui par défaut sur Linux. Et à travers un étrange passage, il a commencé comme celui que j’ai écrit. Une partie de cela était parce que, dans les deux dernières années de mon doctorat, il est devenu clair pour moi que j’allais soit être M. Emacs pour toujours, soit obtenir mon diplôme. Je ne pouvais pas faire les deux.

Était-ce une décision difficile ? C’est fascinant de penser à vous comme à une figure publique, une trajectoire différente aurait pu se produire. Peut-être que j’aurais pu être fabuleusement riche aujourd’hui si j’étais devenu M. Emacs et qu’Emacs s’était transformé en une série d’applications de traitement de texte et toutes sortes de choses. J’ai une longue histoire de décisions financièrement sous-optimales parce que je ne voulais pas de cette vie. Je suis allé à l’école doctorale parce que je voulais obtenir mon diplôme. Être M. Emacs pendant un moment était amusant, puis ça a cessé de l’être. Quand ce n’était plus amusant, et que je ne pouvais pas payer mon loyer, j’ai décidé de choisir. J’ai contacté toutes les personnes que je connaissais sur l’ARPANET qui pourraient prendre en charge Emacs, et presque tout le monde a dit : j’ai un boulot à temps plein. J’ai finalement trouvé deux personnes dans un garage dans le New Jersey, avec un chien, qui étaient prêtes à prendre le relais, mais elles allaient devoir faire payer. Mon accord avec elles était qu’elles le rendraient gratuit pour les universités et les écoles, et elles ont dit d’accord. Ça a contrarié certaines personnes.

Il y a une tension avec M. Richard Stallman, sur cette question de logiciel libre, une sorte de focalisation dogmatique sur le fait que toute information doit être libre. Quelle est une manière intéressante de décrire le désaccord que vous avez eu avec Richard au fil des années ? Mon opposition de base est que, quand vous dites que l’information doit être libre, sous une forme vraiment extrême, cela se transforme en dire que toutes les personnes dont le travail est la production de tout, des films au logiciel, doivent faire vœu de pauvreté. Ça ne marche pas pour moi. Je ne veux pas être follement riche, je ne le suis pas, je m’en sors bien, je peux nourrir mes enfants. Je suis tout à fait d’accord avec vous. Ça me rend triste que parfois, la fermeture du code source, pour une raison ou une autre, entraîne la construction d’une bureaucratie, et parfois ça nuit au produit. Absolument, c’est toujours triste. Il y a un équilibre là-dedans, ce n’est pas du capitalisme rapace d’un côté, ni l’extrême opposé. Beaucoup du mouvement open source a été magique pour trouver un chemin pour gagner de l’argent, comme le service et le support. Il y a des manières un peu perverses, comme avec la loi Sarbanes-Oxley et diverses interprétations des principes comptables. Si une entreprise dépend d’un logiciel, souvent, les normes comptables disent que si vous n’avez pas de contrat de support, c’est mauvais. Donc, si vous avez une base de données, vous devez payer pour le support. Mais il y a une différence entre les contrats de support que les producteurs de bases de données open source facturent et ce que quelqu’un de véritablement rapace comme Oracle facture. C’est un équilibre.

### Java [#](#java-1)

Vous avez créé l’un des langages de programmation les plus populaires au monde, le langage avec lequel j’ai appris la programmation orientée objet. C’est un langage que beaucoup de gens utilisent dans de nombreux endroits et sur des millions d’appareils aujourd’hui, Java. La question absurde, mais pouvez-vous raconter l’histoire de l’origine de Java ?

Il y a longtemps, chez Sun, vers 1990, un groupe d’entre nous s’inquiétait du fait qu’il se passait des choses dans l’univers de l’informatique que l’industrie informatique ratait. Quelques-uns d’entre nous ont lancé ce projet chez Sun, qui a vraiment démarré en 1991. Il s’agissait de ce qui se passait en termes de matériel informatique, de processeurs, de réseautage, tout ça, en dehors de l’industrie informatique. Cela allait des premières lueurs des téléphones portables à l’époque, aux ascenseurs, locomotives, systèmes de contrôle de processus dans les usines, équipements audio et vidéo. Ils avaient tous des processeurs, et ils faisaient des choses avec. On avait l’impression qu’il se passait quelque chose là-dedans qu’on devait comprendre. C, C++ étaient déjà dans l’air. Oh non, C et C++ dominaient complètement l’univers à ce moment-là, tout était écrit en C et C++. Alors, d’où venait l’intuition qu’il y avait besoin d’une révolution ? Le besoin d’une révolution ne concernait pas un langage, c’était juste aussi simple et vague qu’il se passait des choses là dehors, et nous devons les comprendre.

Quelques-uns d’entre nous sont partis pour plusieurs voyages épiques, littéralement des voyages. On prenait l’avion, on allait au Japon, on visitait Toshiba, Sharp, Mitsubishi, Sony, et comme nous travaillions pour Sun, nous avions des gens prêts à nous présenter. Nous avons visité Samsung, un tas d’entreprises coréennes, nous sommes allés partout en Europe, chez Philips, Siemens, Thompson. Qu’avez-vous vu là-bas ? Pour moi, ce qui m’a marqué, c’est qu’ils faisaient toutes les choses informatiques habituelles que les gens faisaient 20 ans auparavant. Ce qui m’a vraiment sauté aux yeux, c’est qu’ils réinventaient le réseautage informatique, et ils faisaient toutes les erreurs que l’industrie informatique avait faites. Comme j’avais beaucoup travaillé dans le domaine du réseautage, on visitait une entreprise X, ils décrivaient leur truc de réseautage, et sans réfléchir, je pouvais leur dire les 25 choses qui allaient être des catastrophes complètes avec ce qu’ils faisaient. Je ne sais pas si ça a eu un impact sur eux, mais cette histoire de répéter les désastres de l’industrie informatique était là. On pensait qu’on pourrait peut-être faire quelque chose d’utile en les faisant avancer un peu, mais en même temps, nous avons appris beaucoup de ces entreprises d’électronique grand public.

En haut de la liste, il y avait leur vision de la relation avec le client comme sacrée. Ils n’étaient jamais prêts à faire des compromis sur la sécurité. Une chose qui m’a toujours rendu nerveux dans l’industrie informatique, c’est que les gens étaient prêts à faire des compromis sur la fiabilité pour obtenir des performances. Ils voulaient plus rapide, même si ça casse un peu plus souvent, ou peut-être qu’on le fait fonctionner un peu plus chaud que nécessaire. Ce qui me soufflait toujours, c’était la manière dont les gens chez Cray Supercomputers rendaient leur division super rapide en utilisant des approximations de Newton-Raphson, donc les bits les plus bas de a sur b étaient essentiellement des nombres aléatoires. Qu’est-ce qui pourrait mal tourner ? Juste comprendre comment clouer le dernier bit, s’assurer que si vous mettez une tranche de pain dans un grille-pain, ça ne va pas tuer le client ou mettre le feu à la maison.

Ce sont les principes qui inspiraient, mais comment, des jours où Java s’appelait Oak à cause d’un arbre devant la fenêtre, est-il devenu ce langage incroyablement puissant ? C’était un ensemble de choses. Après tout ça, nous avons décidé que la meilleure manière de comprendre les choses était de construire une démo, un prototype de quelque chose. Parce que c’était facile et amusant, nous avons décidé de construire un système de contrôle pour des appareils électroniques domestiques, TV, magnétoscope, ce genre de choses. En le construisant, nous avons découvert que certaines pratiques standard en programmation C nous gênaient vraiment. Ce n’était pas qu’on ne pouvait pas écrire le code pour faire ce qu’il fallait, mais dans le groupe, nous avions un gars dont le travail de haut niveau était d’être un homme d’affaires, un type de MBA, qui pensait aux plans d’affaires. Nous parlions des choses qui allaient mal ou bien, et en pensant aux exigences de sécurité, certains détails de bas niveau en C, comme les pointeurs nus. Au début des années 90, il était bien compris que la source numéro un des vulnérabilités de sécurité était les pointeurs, les bugs. Environ 50, 60, 70 % de toutes les vulnérabilités de sécurité étaient des bugs, et la grande majorité étaient des dépassements de tampon. On s’est dit : il faut réparer ça, il faut s’assurer que ça ne puisse pas arriver.

C’était le point de départ pour moi : ça ne peut pas continuer. Cette année, j’ai trouvé amusant un article, je ne sais plus quel magazine l’a publié, qui examinait toutes les vulnérabilités de sécurité dans Chrome, un énorme morceau de code C++. 60 ou 70 % de toutes les vulnérabilités de sécurité étaient des trucs stupides avec les pointeurs. J’ai pensé : 30 ans plus tard, on est encore là, et on veut juste pleurer. Attribueriez-vous la création de Java aux problèmes évidents de C ? C’était l’un des points déclencheurs. La concurrence était un gros problème. Quand vous interagissez avec des gens, la dernière chose que vous voulez voir, c’est que ça attend. Les problèmes liés au processus de développement logiciel, quand des erreurs se produisent, pouvez-vous récupérer ? Que pouvez-vous faire pour faciliter la création et l’élimination de structures de données complexes ? Que pouvez-vous faire pour résoudre l’un des problèmes les plus courants en C, les fuites de mémoire, et son jumeau maléfique, la mémoire libérée mais encore utilisée ? Quand j’y pensais au départ, je pensais en termes de problèmes de sécurité, mais j’ai fini par comprendre que ce n’était pas seulement une question de sécurité, mais de vélocité des développeurs.

Je suis devenu très religieux à ce sujet, car à ce moment-là, j’avais passé un temps fou à chasser des bugs mystérieux de pointeurs. Environ les deux tiers de mon temps en tant que développeur logiciel étaient consacrés à ça, car les bugs de pointeurs mystérieux sont les plus difficiles à trouver, car ils sont très statistiques. Ceux qui font mal, c’est une chance sur un million, mais ça crée une souffrance infinie, car quand vous faites un milliard d’opérations par seconde, une chance sur un million signifie que ça va arriver. Je suis devenu très religieux sur le fait de s’assurer que si quelque chose échoue, ça échoue immédiatement et visiblement. Une des choses qui a vraiment attiré beaucoup d’équipes de développement vers Java, c’était qu’on faisait fonctionner notre code deux fois plus vite. Vous parlez de l’ensemble du processus de développement, le débogage, tout ça ? Oui, si vous mesurez le temps depuis le moment où vous touchez le clavier jusqu’à ce que vous obteniez votre première démo, pas beaucoup de différence. Mais si vous regardez depuis le moment où vous touchez le clavier jusqu’à un logiciel solide que vous pouvez mettre en production, c’était beaucoup plus rapide. Ce que les gens ne réalisent pas souvent, c’est que les bugs difficiles à attraper ralentissent vraiment les choses. Mais aussi, une des choses que vous obtenez de la programmation orientée objet, c’est une méthodologie stricte sur ce que sont les interfaces entre les choses, et être vraiment clair sur la manière dont les parties se relient les unes aux autres.

Cela aide, car souvent, les gens contournent les côtés. Si vous avez construit quelque chose et que les gens l’utilisent, vous dites : je l’ai construit, vous l’utilisez comme ça. Ensuite, vous le changez d’une manière qui fait toujours ce que vous avez dit, mais différemment. Puis vous découvrez que quelqu’un là dehors contournait par un chemin détourné, et son code s’est cassé. Normalement, l’attitude est : idiot. Mais souvent, vous ne pouvez pas simplement leur taper sur la main et leur dire de ne pas faire ça, car c’est peut-être le système de réconciliation des comptes d’une banque, où un développeur a décidé : je suis paresseux, je vais passer par la porte dérobée, parce que le langage le permet. Vous ne pouvez même pas être en colère contre eux. Une des choses que j’ai faites, qui a contrarié beaucoup de gens, c’est que j’ai rendu impossible de passer par les portes dérobées. Le but était de dire : si l’interface ici n’est pas correcte, la mauvaise manière de gérer ça, c’est de passer par une porte dérobée. La bonne manière, c’est d’aller voir le développeur de ce truc et de dire : change l’interface, corrige-la. C’était une sorte d’ingénierie sociale, et les gens ont fini par découvrir que ça faisait vraiment une différence, surtout quand vous construisez des logiciels plus grands et complexes, avec beaucoup de gens qui travaillent dessus, et surtout quand ils couvrent plusieurs organisations. Avoir une clarté sur la manière dont ces choses sont structurées vous sauve la vie. Surtout, il y a tellement de logiciels qui sont fondamentalement intestables. Mieux vaut écrire du bon code dès le départ, plutôt que d’écrire du code médiocre et essayer de le réparer en cherchant les bugs par des tests.

### Machine virtuelle Java [#](#machine-virtuelle-java)

L’une des idées les plus belles, philosophiquement et techniquement, est celle d’une machine virtuelle, la machine virtuelle Java (JVM). Comment l’idée de la JVM est-elle née ? Était-ce une idée radicale ? Cela me semble être une idée vraiment intéressante dans l’histoire de la programmation. Qu’est-ce que c’est ?

La machine virtuelle Java, on peut la voir de différentes manières, car elle a été soigneusement conçue pour être vue de différentes façons. Une vision, que la plupart des gens ne réalisent pas vraiment, est qu’on peut la voir comme une sorte d’encodage de l’arbre de syntaxe abstraite en notation polonaise inversée. Je ne sais pas si ça a du sens. Je pourrais l’expliquer, mais ça prendrait tout notre temps. Une autre manière de la penser, et celle qui est généralement expliquée, est que c’est comme l’ensemble d’instructions d’une machine abstraite conçue de telle sorte qu’on peut traduire cette machine abstraite vers une machine physique. La raison pour laquelle c’est important, c’est que, si vous remontez au début des années 90, quand nous parlions à toutes ces entreprises d’électronique grand public, les discussions avec les acheteurs étaient intéressantes. Si vous regardez comment ces appareils sont assemblés, ce sont de la tôle, des engrenages, des circuits imprimés, des condensateurs, des résistances, et tout ce que vous achetez a plusieurs sources. Vous pouvez acheter un condensateur ici ou là, et vous avez un marché, donc vous pouvez obtenir un prix décent. Mais les CPU, particulièrement au début des années 90, étaient tous différents et tous propriétaires. Si vous utilisiez une puce d’Intel, vous deviez être client d’Intel jusqu’à la fin des temps, car si vous écriviez un logiciel, il était lié à cette machine particulière. Cela rendait les acheteurs absolument fous, qu’ils soient soudés à cette décision, et qu’ils doivent la prendre avant que la première ligne de logiciel ne soit écrite.

C’est drôle que vous parliez des acheteurs, c’est une perspective. Il y a probablement beaucoup d’autres perspectives qui détestaient cette idée. Mais d’un point de vue technique, créer une couche d’abstraction agnostique de la machine sous-jacente, du point de vue du développeur, c’est brillant, non ? Oui, et en plus, il y a la question du temps. D’une génération à la prochaine, elles étaient toutes différentes, et il fallait souvent réécrire votre logiciel. Une des choses qui m’a vraiment pris un an de ma vie, c’est quand Sun est passé du processeur Motorola 68010 au 68020. Ils avaient plusieurs différences, et l’une d’elles nous a durement touchés. J’ai fini par être le gars en pointe sur le pire cas où l’architecture du nouveau cache d’instructions nous a fait mal.

Vous articulez un problème fondamental dans toute l’informatique, mais d’où tirez-vous le courage de penser qu’on peut vraiment résoudre ça ? Dans nos conversations avec tous ces vendeurs, ces problèmes ont commencé à apparaître. J’ai eu une sorte d’épiphanie, car ça me rappelait un job d’été que j’avais eu en école doctorale. À l’époque, j’avais deux directeurs de thèse, pour des raisons bizarres, Raj Reddy et Bob Sproul. Le département avait acheté un tas de stations de travail précoces d’une entreprise appelée Three Rivers Computer Company. Cette entreprise était composée d’ingénieurs électriciens qui voulaient faire le moins de logiciels possible. Ils savaient qu’ils auraient besoin de compilateurs, d’OS, et tout ça, mais ils ne voulaient pas le faire, et pour presque rien. Ils ont construit une machine dont l’ensemble d’instructions était littéralement le bytecode pour UCSD Pascal, le P-code. Nous avions un tas de logiciels écrits pour cette machine, et pour diverses raisons, l’entreprise ne se portait pas très bien. Nous voulions que ces logiciels tournent sur d’autres machines, principalement des VAX. Raj m’a demandé si je pouvais trouver un moyen de porter tout ce logiciel, de traduire des machines Perq vers les VAX. Je pense qu’il avait en tête quelque chose qui traduirait du Pascal vers du C. À l’époque, vous pouviez traduire en C, et si vous n’aimiez pas traduire en C, eh bien, vous traduisiez en C. C’était comme Henry Ford : n’importe quelle couleur, tant que c’est noir.

J’ai pensé que c’était vraiment difficile. En regardant les choses, je me suis dit : je parie que je pourrais réécrire le P-code en code assembleur VAX. J’ai commencé à réaliser que certaines propriétés du P-code rendaient ça vraiment facile, d’autres vraiment difficile. J’ai fini par écrire ce truc qui traduisait du P-code des Perq Three Rivers en code assembleur sur les VAX, et j’ai obtenu un code de meilleure qualité que le compilateur C. Tout est devenu vraiment rapide, vraiment facile. J’ai pensé que c’était un hack minable parce que j’étais paresseux, mais en fait, ça fonctionnait vraiment bien. J’ai essayé de convaincre les gens que c’était peut-être un bon sujet de thèse, mais personne n’était convaincu. Avancez de quelques années, et nous devions permettre de passer d’un microprocesseur bizarre à un autre totalement différent. Je me suis dit, peut-être en faisant quelque chose dans l’espace du P-code Pascal, je pourrais faire plusieurs traducteurs. J’ai passé du temps à réfléchir à ce qui avait fonctionné et ce qui n’avait pas fonctionné quand j’ai fait le traducteur P-code vers VAX. J’ai parlé à des gens impliqués dans Smalltalk, car Smalltalk utilisait aussi du bytecode. Puis je me suis dit : oui, je veux faire ça. Ça avait l’avantage qu’on pouvait soit l’interpréter, soit le compiler. Les interpréteurs sont généralement plus faciles à faire, mais pas aussi rapides qu’un compilateur. J’ai pensé : super, je peux encore être paresseux. Parfois, je pense que la plupart de mes bonnes idées sont motivées par la paresse. Elles sont souvent le résultat de la souffrance, mais d’une manière ou d’une autre, elles finissent par être de bonnes idées.

C’est ainsi que ça s’est fait. Ça s’est transformé en une position presque religieuse de ma part, ce qui m’a valu plusieurs autres conflits. Par exemple, la manière dont l’arithmétique fonctionnait. Il fut un temps où ce n’était pas toujours l’arithmétique en complément à deux. Certaines machines avaient une arithmétique en complément à un, comme presque tout ce qui était construit par CDC. Occasionnellement, il y avait des machines avec une arithmétique décimale. J’ai pensé : c’est fou. L’arithmétique entière en complément à deux a gagné, alors faisons juste ça. Un autre endroit où il y avait beaucoup de variabilité, c’était dans la manière dont les nombres à virgule flottante se comportaient, ce qui causait beaucoup de douleur dans l’industrie du logiciel. Vous ne pouviez pas faire une bibliothèque de calcul numérique qui fonctionnait sur CDC, puis sur une machine IBM, puis sur une machine DEC. À travers cette lutte, il y avait eu tout un travail sur les normes de virgule flottante, et cette chose appelée IEEE 754 est apparue, la norme de virgule flottante qui a pratiquement pris le contrôle de tout l’univers. À l’époque où je faisais Java, elle avait presque fini de conquérir l’univers, il restait quelques poches de résistants. J’ai pensé : il est important de pouvoir dire ce que deux plus deux signifie. J’ai eu des conflits avec des gens, car quelques machines n’implémentaient pas correctement IEEE 754. Bien sûr, ce sont des combats à court terme, je pense qu’à long terme, cette vision a triomphé. Les plus gros combats étaient avec Intel, car ils avaient fait des choses étranges avec l’arrondi, des choses étranges avec leurs fonctions transcendantales, ce qui pouvait devenir une explosion de bizarreries au nom de l’optimisation. Leurs problèmes avec les fonctions transcendantales étaient juste stupides, ils faisaient une réduction de plage pour le sinus et le cosinus en utilisant une valeur légèrement fausse pour pi.

### Android [#](#android)

Dans l’intérêt du temps, deux questions, une sur Android et une sur la vie. On pourrait parler pendant des heures, j’espère qu’on pourra reparler un jour, mais je dois vous poser une question sur Android et l’utilisation de Java là-dedans, car c’est l’un des nombreux endroits où Java a un impact énorme sur ce monde. De votre point de vue, y a-t-il des choses qui vous rendent heureux concernant la manière dont Java est utilisé dans le monde Android, et y a-t-il des choses que vous souhaiteriez différentes ?

Je ne sais pas comment faire une réponse courte à ça, mais je dois faire une réponse courte. Je suis heureux qu’ils l’aient fait. Java tournait sur les téléphones portables depuis plusieurs années à ce moment-là, et ça fonctionnait vraiment bien. Il y avait des choses dans la manière dont ils l’ont fait, en particulier diverses façons dont ils ont violé toutes sortes de contrats. Le gars qui a dirigé ça, Andy Rubin, a franchi beaucoup de lignes. Certaines lignes ont été franchies, ce qui a depuis explosé en d’énormes affaires judiciaires. Ils n’avaient pas besoin de faire ça, et en fait, ça aurait été tellement moins cher pour eux de ne pas franchir les lignes. Je suppose qu’ils n’anticipaient pas le succès de toute cette entreprise, ou pensez-vous qu’à ce moment-là, il était déjà clair que ça allait exploser ? J’ai fini par croire que peu importe ce qu’Andy faisait, ça allait exploser. Je commençais à le voir comme un fabricant de bombes. Certaines des meilleures choses dans ce monde viennent d’un peu d’explosion, et certaines des pires. Ça vous rend fier que Java soit dans des millions, peut-être des milliards d’appareils ? Eh bien, il était dans des milliards de téléphones avant qu’Android n’arrive. Je suis tout aussi fier de la manière dont les normes de cartes à puce ont adopté Java. Tout le monde impliqué là-dedans a fait un très bon travail, et c’est des milliards et des milliards. Les cartes SIM dans votre poche. J’ai été hors de ce monde pendant une décennie, donc je ne sais pas comment ça a évolué, mais c’est juste fou.

### Conseils [#](#conseils)

Sur ce sujet, encore une fois, il y a un million de choses techniques dont nous pourrions parler, mais permettez-moi de poser la vieille question philosophique absurde sur la vie. Quand vous regarderez en arrière sur votre vie, et que les gens parleront de vous dans 500 ans, quel héritage espérez-vous laisser ?

Que les gens n’aient pas peur de faire un saut dans l’inconnu. J’ai cette histoire bizarre de faire des trucs bizarres, et ça a plutôt bien marché. Je pense que certaines des choses les plus étranges que j’ai faites ont été les plus cool. Certaines se sont écrasées et ont brûlé, plus de la moitié de ce que j’ai fait s’est écrasé et a brûlé, ce qui a parfois été vraiment ennuyeux, mais vous avez continué. Même quand les choses s’écrasent et brûlent, vous apprenez au moins quelque chose. En guise de conseil, pour les développeurs, ingénieurs, scientifiques, ou simplement les jeunes qui vous admirent, quel conseil leur donneriez-vous sur la manière d’aborder leur vie ?

N’ayez pas peur du risque. C’est okay de faire des choses stupides une fois, peut-être même deux fois. Vous avez un passe pour la première ou la deuxième fois que vous faites quelque chose de stupide. La troisième ou quatrième fois, pas tellement. Très tôt, j’ai commencé à penser aux choix éthiques dans ma vie. Étant un grand fan de science-fiction, j’ai commencé à penser à presque chaque décision technique que je prends en termes de : est-ce que vous construisez Blade Runner ou Star Trek ? Quel futur préféreriez-vous vivre ? Eh bien, je préférerais certainement vivre dans l’univers de Star Trek. Ça ouvre tout un sujet sur l’IA, mais c’est une idée vraiment intéressante. Votre système d’IA préféré serait Data de Star Trek, et le moins préféré serait facilement Skynet.

Magnifiquement dit, je ne pense pas qu’il y ait une meilleure manière de conclure. James, je ne peux pas exprimer à quel point c’est un honneur de vous rencontrer, de vous parler. Merci beaucoup d’avoir perdu votre temps avec moi aujourd’hui. Pas une perte du tout, merci James.

Merci d’avoir écouté cette conversation avec James Gosling, et merci à nos sponsors Public Goods, BetterHelp et ExpressVPN. Veuillez consulter ces sponsors dans la description pour obtenir une réduction et soutenir ce podcast. Si vous appréciez ce contenu, abonnez-vous sur YouTube, donnez-lui cinq étoiles sur Apple Podcast, suivez sur Spotify, soutenez sur Patreon, ou connectez-vous avec moi sur Twitter à @lexfridman.

Et maintenant, permettez-moi de vous laisser avec quelques mots de James Gosling : l’une des choses les plus difficiles dans la vie, c’est de faire des choix. Merci d’avoir écouté et à la prochaine fois.

Après avoir regardé la vidéo, essayez de répondre aux questions suivantes.

1.  Quelles étaient les motivations principales de James Gosling pour créer le langage Java, et comment les problèmes des langages comme C et C++ ont-ils influencé son développement ?
2.  Comment Gosling explique-t-il l’importance de la machine virtuelle Java (JVM) pour résoudre les problèmes rencontrés par les entreprises d’électronique grand public dans les années 1990 ?

Résumé de l’architecture des ordinateurs et de l’abstraction des langages [#](#r%c3%a9sum%c3%a9-de-larchitecture-des-ordinateurs-et-de-labstraction-des-langages)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Tous ces langages partagent un objectif commun : permettre aux programmeurs de décrire des solutions à des problèmes en s’éloignant progressivement des contraintes du matériel. Pour comprendre leur rôle, il est essentiel de se pencher sur le fonctionnement des ordinateurs.

Les ordinateurs modernes s’appuient sur deux concepts fondamentaux : la machine de Turing, théorisée par Alan Turing, qui définit une machine capable d’exécuter n’importe quel algorithme, et l’architecture de von Neumann, qui structure les ordinateurs autour de quatre composantes principales. Premièrement, la mémoire stocke à la fois les données et les programmes, une innovation clé par rapport aux machines antérieures où les instructions étaient fixes. Deuxièmement, l’unité de contrôle orchestre l’exécution des instructions en suivant un séquençage précis. Troisièmement, l’unité arithmétique et logique effectue les calculs de base, comme les additions ou les comparaisons. Enfin, les interfaces d’entrée/sortie permettent d’interagir avec l’utilisateur ou d’autres systèmes, via des périphériques comme les claviers, écrans ou réseaux.

Un ordinateur contemporain se compose de processeurs (CPU), de mémoire vive (RAM) pour les calculs temporaires, de stockage à long terme (disques durs ou SSD), de processeurs graphiques (GPU) pour le rendu visuel, et de cartes d’entrée/sortie pour la connectivité. La carte mère agit comme un chef d’orchestre, coordonnant les échanges entre ces éléments. Par exemple, lorsqu’un programme s’exécute, le CPU lit les instructions depuis la RAM, effectue les calculs nécessaires, et envoie les résultats vers la mémoire ou un périphérique de sortie, comme un écran.

Les processeurs se déclinent en plusieurs architectures. Dans les ordinateurs personnels, les puces x64 (ou x86-64), produites par Intel et AMD, dominent grâce à leur puissance et leur compatibilité. Dans les appareils mobiles, comme les smartphones, les processeurs ARM, plus économes en énergie, sont privilégiés. La mémoire vive repose sur la technologie DRAM, rapide mais volatile, tandis que le stockage à long terme utilise majoritairement la mémoire flash, comme dans les SSD, pour sa rapidité et sa fiabilité.

Les langages de programmation jouent un rôle crucial en traduisant des instructions humaines en commandes compréhensibles par ces composants matériels. Leur niveau d’abstraction varie : les langages de bas niveau, comme l’assembleur, sont proches du matériel et offrent un contrôle précis mais exigent une expertise technique. À l’opposé, les langages de haut niveau, comme Python ou Java, simplifient le développement en masquant les détails matériels, ce qui les rend plus accessibles et adaptés à des applications complexes, comme le développement web ou l’intelligence artificielle.

Dans ce cours, nous explorerons le langage Java, largement adopté dans l’industrie pour sa portabilité, sa robustesse et sa polyvalence. Utilisé dans des domaines variés, des applications mobiles Android aux systèmes d’entreprise, Java illustre parfaitement comment un langage de haut niveau peut répondre à des besoins modernes tout en s’appuyant sur les principes fondamentaux de l’informatique.

Langage machine [#](#langage-machine)
-------------------------------------

Votre ordinateur ne connaît pas le language Java. L’ordinateur contient un microprocesseur (CPU) qui traite des suites de bits. Ces bits sont regroupés en paquets de taille fixe (par ex. 32, 64 ou 128 bits) et peuvent représenter soit une valeur, soit une instruction. Le flot de bits exposé au CPU (en mémoire ou sur un support) est un programme. Le CPU exécute ce programme séquentiellement : lire un mot, l’interpréter, exécuter son action, passer au mot suivant. Des ingénieurs permettent à votre ordinateur de faire fonctionner un langage Java en transformant le code Java en instructions que la machine peut comprendre. L’ordinateur stocke ses données dans un petit nombre de registres (très rapides) ou en mémoire (un peu plus lent).

Les instructions exactes que votre ordinateur peut exécuter dépendent de son architecture. À titre d’illustration, voici quelques instructions fictives qu’un ordinateur pourrait comprendre.

*   `SETA` : stocke la valeur qui suit dans le registre A
*   `SETB` : stocke la valeur qui suit dans le registre B
*   `ADD A→B` : ajoute la valeur du registre A au registre B et stocke le résultat dans le register B
*   `DEC A` : diminue la valeur contenu dans le registre A par 1
*   `JNZ` : si le registre A contient une valeur non-nulle, déplace toi à l’instruction indiquée (00: première instructions, 01: deuxième instruction, 03: troisième instruction, etc.)
*   `HTL` : met fin au programme

Avec ces instructions, nous pouvons créer un programme en langage machine capable de faire la somme des entiers de 0 à \\( N \\). Par exemple, pour \\( N=10 \\), nous avons que \\( 1+2+3+\\cdots+10 = N(N + 1)/2 = 55 \\).

Vous pouvez tester le programme avec la petite application suivante. Exécutez le programme pas à pas. Essayez de comprendre comment le programme arrive à calculer la somme. Il n’est pas nécessaire à ce point-ci dans le cours que vous compreniez le fonctionnement du programme.

Bien que le mécanisme puisse semble mécanique et limité, c’est ainsi que nos ordinateurs fonctionnent. Naturellement, la programmation avec des instructions spécifiques à un processeur a des inconvénients. Elle ne fonctionnera que sur un processeur du même type. C’est une des raisons pour préférer la programmation dans un langage comme Java: un programme Java ne dépend pas de l’architecture de votre processeur.

Entrez N : 

Registre **A** (compteur) : –

Registre **B** (somme) : –

Pas à pas Réinitialiser

(function(){const l=document.getElementById("program"),r=document.getElementById("userN"),m=document.getElementById("regA"),h=document.getElementById("regB"),s=document.getElementById("stepBtn"),f=document.getElementById("resetBtn");let t=\[\],e=0,n=0,o=0,a=!1;function c(){const e=Math.max(1,parseInt(r.value)||1),n=\[\`SETA ${e.toString().padStart(4,"0")} ; A ← N (compteur décroissant)\`,\`SETB 0000 ; B ← 0 (somme)\`,\`ADD A→B ; B ← B + A\`,\`DEC A ; A ← A - 1\`,\`JNZ 02 ; si A ≠ 0, revenir à l'instruction 2\`,\`HLT ; fin du programme – B = somme de 1 à N\`\];l.innerHTML="",t=\[\],n.forEach((e)=>{const s=document.createElement("li"),\[o,r\]=e.split(";"),\[i,a\]=o.trim().split(/\\s+/);s.textContent=e.trim(),s.style.padding="0.5rem 0.9rem",s.style.border="1px solid #ddd",s.style.borderRadius="8px",s.style.marginBottom="0.5rem",s.style.background="#f8f8f8",s.style.fontFamily="Courier New, monospace",s.dataset.op=i,s.dataset.arg=a||"",l.appendChild(s),t.push(s)}),d()}function p(){t.forEach((t,n)=>{n===e?(t.style.background="rgba(33,150,243,0.25)",t.style.borderColor="#2196f3",t.style.fontWeight="bold"):(t.style.background="#f8f8f8",t.style.borderColor="#ddd",t.style.fontWeight="normal")})}function i(){m.textContent=n,h.textContent=o,p();const i=e>=t.length;s.disabled=i,s.style.opacity=i?"0.4":"1",s.style.cursor=i?"not-allowed":"pointer"}function d(){e=0,n=0,o=0,a=!1,i()}function u(){if(e>=t.length)return!1;const i=t\[e\],r=i.dataset.op,s=i.dataset.arg;switch(r){case"SETA":n=parseInt(s,10);break;case"SETB":o=parseInt(s,10);break;case"ADD":s==="A→B"&&(o+=n);break;case"DEC":s==="A"&&(n--,a=n===0);break;case"JNZ":a||(e=parseInt(s,10)-1);break;case"HLT":return!1}return e++,!0}function g(){u(),i()}function v(){const e=setInterval(()=>{u()||clearInterval(e),i()},400)}r.addEventListener("input",c),s.addEventListener("click",g),f.addEventListener("click",d),c()})()

API [#](#api)
-------------

Le terme **API** signifie « Application Programming Interface » (interface de programmation d’application). Une API est un ensemble organisé de classes, de méthodes et de conventions qui permet à des développeurs d’utiliser facilement des fonctionnalités sans avoir à connaître les détails internes de leur implémentation. En Java, on parle souvent de l’API standard (Java Standard Library), qui regroupe des milliers de classes prêtes à l’emploi pour manipuler des chaînes de caractères, des fichiers, des collections, des dates, des flux de données, etc.

Par exemple, l’**API Stream** introduite en Java 8 fournit des outils puissants pour traiter des collections de données de façon déclarative et fonctionnelle (filtrer, transformer, trier, agréger…). L’API Swing permet de créer des interfaces graphiques, l’API JDBC permet d’accéder à des bases de données, etc. Chaque API définit un « contrat » : si vous respectez la façon d’utiliser ses classes et méthodes, vous pouvez profiter de fonctionnalités avancées sans réinventer la roue.

En résumé, une API est une boîte à outils logicielle, conçue pour être utilisée par d’autres développeurs, qui facilite l’accès à des fonctionnalités complexes (réseau, interface graphique, traitement de données, etc.) tout en masquant les détails techniques.

Taille des processeurs et des transistors [#](#taille-des-processeurs-et-des-transistors)
-----------------------------------------------------------------------------------------

Les processeurs modernes sont construits à l’aide de milliards de transistors. Le transistor est l’unité de base des circuits informatiques et il permet de réaliser les différentes opérations de calcul. Nos processeurs modernes sont relativement petits, la plupart pouvant tenir sur le bout d’un doigt. Les transistors sont très petits. Cliquez sur le bouton _Zoomer_ pour vous faire une idée.

Zoom ×1

Zoomer

1.  Processeur Intel (45 mm × 37,5 mm)
2.  Grain de sel (~1 mm)
3.  Cellule de peau (~35 µm)
4.  Globule rouge (~7,5 µm)
5.  Mitochondrie (~2 µm)
6.  Transistor moderne (~2,5 nm)

const info=document.getElementById("info"),hint=document.getElementById("hint"),svg=document.getElementById("mysvg");let zoom=1;const zoomMax=1e6,zoomInterval=50;let zoomTimer=null;const levels=\[{name:"processeur Intel",width:.045,height:.0375,color:"#888",label:"Processeur Intel (45 mm × 37,5 mm)",type:"rect"},{name:"grain de sel",size:.001,color:"#ccc",label:"Grain de sel (~1 mm)",type:"circle"},{name:"cellule de peau",size:35e-6,color:"#8cf",label:"Cellule de peau (~35 µm)",type:"circle"},{name:"globule rouge",size:75e-7,color:"#f44",label:"Globule rouge (~7,5 µm)",type:"circle"},{name:"mitochondrie",size:2e-6,color:"#F6BE00",label:"Mitochondrie (~2 µm)",type:"circle"},{name:"transistor",size:.25e-8,color:"#0f0",label:"Transistor moderne (~2,5 nm)",type:"transistor"}\];function drawSVG(){for(;svg.firstChild;)svg.removeChild(svg.firstChild);let e=500,t=500;levels.forEach(n=>{if(n.type==="rect"){let o=n.width\*zoom\*1e4,i=n.height\*zoom\*1e4,s=document.createElementNS("http://www.w3.org/2000/svg","rect");s.setAttribute("x",e-o/2),s.setAttribute("y",t-i/2),s.setAttribute("width",o),s.setAttribute("height",i),s.setAttribute("fill",n.color),s.setAttribute("stroke","#fff"),svg.appendChild(s)}else if(n.type==="circle"){let o=n.size\*zoom\*1e4,s=document.createElementNS("http://www.w3.org/2000/svg","circle");s.setAttribute("cx",e),s.setAttribute("cy",t),s.setAttribute("r",o/2),s.setAttribute("fill",n.color),s.setAttribute("stroke","#fff"),s.setAttribute("stroke-width",4),svg.appendChild(s)}else if(n.type==="transistor"){let s=n.size\*zoom\*1e4,o=document.createElementNS("http://www.w3.org/2000/svg","rect");o.setAttribute("x",e-s\*3),o.setAttribute("y",t-s\*2),o.setAttribute("width",s\*6),o.setAttribute("height",s\*4),o.setAttribute("fill",n.color),o.setAttribute("stroke","#fff"),svg.appendChild(o);let i=document.createElementNS("http://www.w3.org/2000/svg","line");i.setAttribute("x1",e-s\*2),i.setAttribute("y1",t),i.setAttribute("x2",e+s\*2),i.setAttribute("y2",t),i.setAttribute("stroke","#fff"),i.setAttribute("stroke-width",s\*.8),svg.appendChild(i)}}),document.getElementById("zoomval").textContent=Math.round(zoom);var n=document.getElementById("hint");n&&(n.textContent="")}function startZoomTimer(){zoomTimer&&clearInterval(zoomTimer),zoom=1,drawSVG(),zoomTimer=setInterval(()=>{zoom<zoomMax?(zoom=Math.min(zoom\*1.1,zoomMax),drawSVG()):clearInterval(zoomTimer)},zoomInterval)}document.getElementById("zoombtn").addEventListener("click",startZoomTimer),window.addEventListener("DOMContentLoaded",drawSVG)

Unités de mesures [#](#unit%c3%a9s-de-mesures)
----------------------------------------------

Les ordinateurs et leurs composants sont caractérisés par différentes unités de mesure :

### Fréquence (vitesse du processeur) [#](#fr%c3%a9quence-vitesse-du-processeur)

*   _Hertz (Hz)_ : unité de fréquence, correspond à un cycle par seconde.
*   _Kilohertz (kHz)_ : 1 000 Hz.
*   _Mégahertz (MHz)_ : 1 000 000 Hz (un million de cycles/seconde).
*   _Gigahertz (GHz)_ : 1 000 000 000 Hz (un milliard de cycles/seconde).

La fréquence d’un processeur (ex : 3,2 GHz) indique combien d’opérations il peut effectuer par seconde.

### Temps [#](#temps)

*   _Seconde (s)_ : unité de base du temps.
*   _Milliseconde (ms)_ : 1/1 000 de seconde (\\(10^{-3}\\) s).
*   _Microseconde (µs)_ : 1/1 000 000 de seconde (\\(10^{-6}\\) s).
*   _Nanoseconde (ns)_ : 1/1 000 000 000 de seconde (\\(10^{-9}\\) s).

Les temps d’accès à la mémoire ou d’exécution d’instructions sont souvent mesurés en nanosecondes ou microsecondes.

### Stockage et mémoire [#](#stockage-et-m%c3%a9moire)

*   _Octet (B)_ : unité de base, correspond à 8 bits.
*   _Kilooctet (ko)_ : 1 000 octets (notation décimale, SI).
*   _Mégaoctet (Mo)_ : 1 000 000 octets.
*   _Gigaoctet (Go)_ : 1 000 000 000 octets.
*   _Téraoctet (To)_ : 1 000 000 000 000 octets.
*   _Kibioctet (Kio)_ : 1 024 octets (\\(2^{10}\\)).
*   _Mebioctet (Mio)_ : 1 048 576 octets (\\(2^{20}\\)).
*   _Gibioctet (Gio)_ : 1 073 741 824 octets (\\(2^{30}\\)).

> _Remarque :_ Les systèmes d’exploitation et les fabricants utilisent parfois les préfixes kilo, méga, giga pour désigner soit des puissances de 10 (décimal), soit des puissances de 2 (binaire). Par exemple, 1 Go peut désigner 1 000 000 000 octets (décimal) ou 1 073 741 824 octets (binaire). Les préfixes Kio, Mio, Gio sont utilisés pour lever cette ambiguïté.

Ces unités sont essentielles pour comprendre les performances, la capacité de stockage et la rapidité des ordinateurs modernes.

La vitesse de la lumière dans le vide est d’environ 299 792 458 mètres par seconde (environ 300 000 km/s). C’est la vitesse maximale à laquelle l’information ou l’énergie peut se déplacer dans l’univers selon la physique moderne. La lumière parcourt environ 29,98 centimètres (soit presque 30 cm) en une nanoseconde dans le vide. Autrement dit, en une nanoseconde (1 ns = 10⁻⁹ seconde), la lumière se déplace d’environ 30 cm.

### Binaire [#](#binaire)

Les ordinateurs fonctionnent en binaire, c’est-à-dire qu’ils ne manipulent que deux états possibles : 0 et 1. Cette représentation repose sur le système de numération binaire, où chaque chiffre (bit) correspond à une puissance de 2. Un bit (binary digit) est l’unité d’information la plus petite : il peut valoir 0 ou 1.

Un groupe de 8 bits forme un octet (byte), qui permet de représenter 256 valeurs différentes (de 0 à 255). Les ordinateurs stockent et traitent toutes les données (nombres, texte, images, sons) sous forme de suites de bits. Par exemple, le nombre décimal 5 s’écrit 101 en binaire :

*   1 × 2² + 0 × 2¹ + 1 × 2⁰ = 4 + 0 + 1 = 5

Voici quelques exemples de conversion :

Décimal

Binaire

0

0000

1

0001

2

0010

3

0011

4

0100

5

0101

6

0110

7

0111

8

1000

9

1001

Chaque bit supplémentaire double le nombre de valeurs possibles. Ainsi, avec n bits, on peut représenter 2ⁿ valeurs différentes.

Utilisez l’application suivante pour explorer la représentation binaire. Observez comment, par convention, le bit le plus à gauche est le plus significatif. Que remarquez-vous au sujet des puissances de deux comme 2, 4, 8 ?

Manipulateur de 8 bits
----------------------

Valeur binaire: 00000000

Valeur décimale: 0

(function(){const t=document.getElementById("bitApp");if(!t)return;const n=t.querySelector("#bitContainer");if(!n)return;const o=t.querySelector("#binaryValue"),i=t.querySelector("#decimalValue"),e=Array(8).fill(0);for(let t=0;t<8;t++){const e=document.createElement("button");e.textContent="0",e.setAttribute("aria-label",\`Bit ${7-t}\`),e.style.cssText=\` width: 40px; height: 40px; font-size: 18px; font-family: monospace; background-color: #f0f0f0; border: 1px solid #999; border-radius: 4px; cursor: pointer; transition: background-color 0.2s; \`,e.addEventListener("click",()=>a(7-t)),n.appendChild(e)}function a(t){e\[t\]=e\[t\]?0:1,s()}function s(){const s=n.querySelectorAll("button");let t="";for(let n=0;n<8;n++)s\[7-n\].textContent=e\[n\],s\[7-n\].style.backgroundColor=e\[n\]?"#4caf50":"#f0f0f0",t=e\[n\]+t;o.textContent=t,i.textContent=parseInt(t,2)||0}s()})()

#### Pourquoi le binaire ? [#](#pourquoi-le-binaire)

Le choix du binaire s’explique par la simplicité de la technologie électronique : il est facile de concevoir des circuits qui distinguent deux états (tension présente ou absente, aimantation positive ou négative, etc.). Cela rend les ordinateurs plus fiables et moins sensibles au bruit que s’ils utilisaient plus de deux états.

Les ordinateurs effectuent des opérations logiques (ET, OU, NON, OU exclusif) directement sur les bits. Ces opérations sont à la base de tous les calculs et traitements informatiques.

 [![Previous](/inf1220-hugo/svg/backward.svg "Java pas à pas") Java pas à pas](/inf1220-hugo/docs/modules/module1/pasapas/) [Les algorithmes ![Next](/inf1220-hugo/svg/forward.svg "Les algorithmes")](/inf1220-hugo/docs/modules/module1/algorithmes/) 


*   [Programmation orientée objet](#programmation-orientée-objet)
*   [Java](#java)
    *   [Nombres irrationnels](#nombres-irrationnels)
    *   [Mathématiques et programmation](#mathématiques-et-programmation)
    *   [Style de codage](#style-de-codage)
    *   [Premier ordinateur](#premier-ordinateur)
    *   [Lisp](#lisp)
    *   [Écrire une implémentation d’Emacs en C](#écrire-une-implémentation-demacs-en-c)
    *   [Les débuts de l’Internet](#les-débuts-de-linternet)
    *   [Elon Musk, Steve Jobs, Jeff Bezos](#elon-musk-steve-jobs-jeff-bezos)
    *   [Travailler dur et intelligemment](#travailler-dur-et-intelligemment)
    *   [Open source](#open-source)
    *   [Java](#java-1)
    *   [Machine virtuelle Java](#machine-virtuelle-java)
    *   [Android](#android)
    *   [Conseils](#conseils)
*   [Résumé de l’architecture des ordinateurs et de l’abstraction des langages](#résumé-de-larchitecture-des-ordinateurs-et-de-labstraction-des-langages)
*   [Langage machine](#langage-machine)
*   [API](#api)
*   [Taille des processeurs et des transistors](#taille-des-processeurs-et-des-transistors)
*   [Unités de mesures](#unités-de-mesures)
    *   [Fréquence (vitesse du processeur)](#fréquence-vitesse-du-processeur)
    *   [Temps](#temps)
    *   [Stockage et mémoire](#stockage-et-mémoire)
    *   [Binaire](#binaire)

## Les algorithmes


*   [Préalables](#préalables)
*   [Introduction](#introduction)
    *   [Qu’est-ce qu’un algorithme ?](#quest-ce-quun-algorithme-)
    *   [Qu’est-ce que le pseudo-code ?](#quest-ce-que-le-pseudo-code-)
    *   [Variables et valeurs](#variables-et-valeurs)
    *   [Logique booléenne](#logique-booléenne)
    *   [Notation des programmeurs](#notation-des-programmeurs)
*   [La boucle](#la-boucle)
*   [Tableau](#tableau)
*   [Exemple : Calcul de la moyenne](#exemple--calcul-de-la-moyenne)

Les algorithmes [#](#les-algorithmes)
=====================================

> _The etymology of program is pro ‘before’ + graphein ‘write’. I think of programming as making a plan that will be executed in the future, something that every human does from time to time. The hard part is that a computer has to execute the plan, and computers are incredibly stupid. Dealing with such stupidity requires more patience and determination than many people have._ (Peter Turney)

> Préalables [#](#pr%c3%a9alables)
> --------------------------------
> 
> Dans ce cours, nous présentons les notions de manière exhaustive, avec beaucoup d’exemples et des activités d’approfondissement. Néanmoins, nous supposons dans ce cours que vous avez complété les mathématiques du collégial et que vous avez de bonnes aptitudes en ce qui a trait aux raisonnements formels. Dans ce premier module, vous aurez à exprimer la solution de certains problèmes en terme de variables, de boucles et d’embranchement. Il ne s’agit pas de notions avancées : vous devriez être familier avec ces notions. Les boucles font partie implicitement du calcul d’une somme ou d’un produit scalaire. Les variables en informatique sont une notion voisine des variables en algèbre. Les embranchements sont des notions de base en logique élémentaire. Nous supposons une familiarité avec ces notions. Vous êtes responsables de vous assurez que vous avez la préparation nécessaire pour suivre le cours INF 1220.

Introduction [#](#introduction)
-------------------------------

Le processus systématique de résolution d’un problème donné s’appelle algorithme. La notion d’algorithme formel est vue dans le cadre des cours de mathématiques du secondaire, notamment dans le contexte de [la théorie des graphes](https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-chaine-de-poids-minimal-m1010) et des algorithmes d’optimisation. Comme point de départ dans le cours INF 1220, nous revisitons et approfondissons brièvement cette notion fondamentale.

Un algorithme est donc une suite d’actions pour répondre à un problème de traitement de l’information. Ces actions peuvent être mathématiques (ex. somme = a + b), de contrôles (ex. SI a > b ALORS) ou d’itérations (ex. TANT QUE a > b FAIRE). Pour décrire ces algorithmes, il existe également plusieurs formalismes, certains utiliseront des formalismes mathématiques alors que d’autres utiliseront des pseudo-codes. Encore là dans plusieurs formats pour représenter un pseudo-code, il n’existe pas de normes uniques!

En cuisine, une recette est un exemple d’algorithme si celle-ci comporte une séquence d’instructions précises. Pouvoir rédiger de manière précise une recette afin que d’autres cuisiniers puissent reproduire la même séquence d’opération est de facto de la programmation informatique. Si vous avez fait l’expérience du manuel de recette de quelqu’un d’autre (par ex., votre grand-mère), vous avez peut-être découvert qu’il peut être difficile de suivre des consignes de quelqu’un d’autre surtout quand celles-ci ne sont pas suffisamment précises. Une recette de cuisine est du pseudo-code.

Avant l’invention du GPS, il était commun d’expliquer à des amis ou des parents comment se rendre à un lieu donné en suivant une série d’instructions. Il arrivait souvent, malheureusement, que ces instructions n’étaient pas assez précises et que les gens se perdent. Expliquer à quelqu’un comment se rendre à un lieu donné est un exemple de programmation informatique. Votre explication est du pseudo-code.

Il est essentiel de comprendre ce qu’est le pseudo-code: il s’agit d’une façon de décrire un algorithme afin que d’autres êtres humains puissent vous comprendre. Il faut donc interpréter le pseudo-code en utilisant son jugement humain de la même façon que vous interprétez tout autre texte ou discours. Pouvoir lire un algorithme, décrit en pseudo-code, est une compétence essentielle en informatique. Il faut être capable de comprendre d’autres informaticiens sans nécessairement exiger que ceux-ci utilisent du code informatique dans un langage particulier (par ex., Java). Programmer et faire de l’informatique exige de pouvoir bien communiquer avec les autres informaticiens indépendamment de langages de programmation spécifiques.

Pour un programmeur d’expérience, s’exprimer à l’aide d’un pseudo-code est chose aisée. Pour le commun des mortels, c’est un peu plus difficile. La blague suivante illustre le problème.

> Une femme demande à son programmeur de mari : « Va au supermarché acheter une bouteille de lait. Et si ils ont des œufs, prends en 6 ». Le mari revient avec six bouteilles de lait. Sa femme lui demande pourquoi il a pris six bouteilles. « Parce qu’ils avaient des oeufs » répond-il.

Quand on rédige un pseudo-code, il faut tout spécifier, comme si on s’adressait à quelqu’un qui prend tout littéralement, sans aucun jugement. Pour devenir un programmeur, pour penser comme un programmeur, il faut s’habituer à rédiger des séquences d’instructions précises. La lecture et la rédaction de pseudo-codes relativement simples peut être une bonne pratique.

Le pseudocode est destiné à être lu par l’humain, et il peut être écrit de diverses manières tant que l’humain le comprend. Le cours ne vise pas à vous permettre de comprendre une syntaxe particulière de pseudocode, mais bien le pseudocode en général.

### Qu’est-ce qu’un algorithme ? [#](#quest-ce-quun-algorithme-)

Un _algorithme_ est une suite finie et ordonnée d’instructions permettant de résoudre un problème ou d’accomplir une tâche spécifique. Il s’agit d’une méthode systématique, exprimée de manière précise, qui garantit un résultat correct lorsqu’elle est exécutée. Les algorithmes sont au cœur de l’informatique, car ils décrivent comment un programme doit fonctionner pour atteindre un objectif.

Exemples d’algorithmes dans la vie quotidienne :

*   Une recette de cuisine (série d’étapes pour préparer un plat).
*   Les instructions pour assembler un meuble.

En informatique, un algorithme peut, par exemple, trier une liste de nombres ou calculer le chemin le plus court entre deux points.

### Qu’est-ce que le pseudo-code ? [#](#quest-ce-que-le-pseudo-code-)

Le _pseudo-code_ est une manière d’écrire un algorithme en utilisant un langage simplifié, proche du langage naturel, mais structuré comme un programme informatique. Il n’est pas destiné à être exécuté directement par un ordinateur, mais sert à décrire la logique d’un algorithme de manière claire et compréhensible, indépendamment d’un langage de programmation spécifique.

Le pseudo-code utilise des conventions comme :

*   `SI`, `ALORS`, `SINON` pour les conditions.
*   `POUR`, `TANT QUE` pour les boucles.
*   Des instructions comme `écrire` ou `lire` pour les entrées/sorties.

Exemple de pseudo-code pour calculer la somme de deux nombres :

    lire nombre1
    lire nombre2
    somme ← nombre1 + nombre2
    écrire somme
    

Le pseudo-code permet aux programmeurs de planifier la logique avant de la traduire dans un langage comme Python, C++ ou Java.

En résumé, un algorithme est une méthode pour résoudre un problème, tandis que le pseudo-code est un outil pour exprimer cet algorithme de manière claire et universelle. Ces deux concepts sont essentiels pour concevoir des solutions informatiques efficaces.

### Variables et valeurs [#](#variables-et-valeurs)

Une _variable_ en informatique est un espace de stockage nommé qui contient une valeur. Elle peut être vue comme une boîte étiquetée dans laquelle on place une donnée, et cette donnée peut changer au cours de l’exécution d’un algorithme. Les variables permettent de manipuler des informations de manière dynamique, en les stockant temporairement pour les utiliser ou les modifier plus tard.

Les variables peuvent contenir différents types de données, selon leur nature et leur usage. Les types courants incluent :

*   **Entier** : un nombre sans partie décimale, comme 5, -12 ou 0.
*   **Réel** : un nombre avec une partie décimale, comme 3.14, -0.001 ou 10.4.
*   **Booléen** : une valeur logique qui peut être soit vrai, soit faux.
*   **Chaîne de caractères** : une séquence de caractères, comme “bonjour” ou “INF1220”.

Dans le pseudo-code, le type de la variable est souvent implicite, mais il est essentiel de comprendre quel type de donnée une variable contient pour éviter des erreurs lors de la manipulation. Une variable doit être _nommée_ de manière claire et descriptive (par exemple, `age`, `somme`, `notes`). On lui attribue une valeur à l’aide de l’opérateur d’affectation, souvent représenté par `←` ou `=`. Par exemple :

    age ← 18
    somme ← 0
    

Ici, la variable `age` reçoit la valeur entière 18, et `somme` reçoit la valeur entière 0.

Considérons un algorithme simple qui calcule le carré d’un nombre entré par l’utilisateur :

    lire nombre
    carre ← nombre * nombre
    écrire carre
    

Dans cet exemple :

*   `nombre` est une variable qui stocke la valeur entrée (par exemple, un réel comme 4.5).
*   `carre` est une variable qui stocke le résultat de l’opération `nombre * nombre` (par exemple, 20.25 si `nombre` vaut 4.5).
*   L’instruction `écrire carre` affiche la valeur de la variable `carre`.

Chaque variable doit avoir un nom distinct dans un algorithme pour éviter toute confusion. Il est recommandé d’initialiser une variable (lui donner une valeur de départ) avant de l’utiliser, pour éviter des comportements imprévisibles. Par exemple, avant d’additionner des nombres dans une variable `somme`, on écrit souvent `somme ← 0`. Certaines variables ont une une portée et elles ne sont accessibles que dans la partie de l’algorithme où elles sont définies. Par exemple, nous nous pouvons utiliser la valeur de la variable `somme` avant de lui avoir assigné une valeur (`somme ← 0`).

Les variables sont essentielles pour écrire des algorithmes flexibles et réutilisables. Elles permettent de travailler avec des données qui varient, comme des entrées utilisateur ou des résultats intermédiaires, et de suivre l’état d’un algorithme tout au long de son exécution. En pseudo-code, les variables servent à rendre les instructions claires et compréhensibles, tout en préparant la transition vers un langage de programmation réel.

Pour illustrer simplement la déclaration et l’affectation d’une variable, voici comment on déclare une variable nommée `age` et on lui assigne la valeur 18 dans différents langages.

En Java, la déclaration exige de préciser le type :

    int age = 18;  // déclaration et affectation en une seule ligne
    

En JavaScript, le type est inféré automatiquement :

    let age = 18;  // déclaration et affectation
    

En Go, on peut utiliser la déclaration courte quand le type est évident :

    age := 18  // déclaration et affectation, type int inféré
    

Ou de manière plus explicite :

    var age int = 18
    

En C++, le type doit aussi être indiqué explicitement :

    int age = 18;  // déclaration et affectation
    

Ces lignes montrent la forme la plus basique de création et d’initialisation d’une variable, équivalente à l’instruction `age ← 18` du pseudo-code. La syntaxe varie légèrement selon le langage, mais le principe reste identique : nommer un espace mémoire et y placer une valeur.

### Logique booléenne [#](#logique-bool%c3%a9enne)

Un des fondements des algorithmes est la logique booléenne. Elle permet de manipuler des valeurs logiques, appelées booléennes, qui ne peuvent prendre que deux états : vrai ou faux. Ces valeurs sont utilisées pour prendre des décisions, contrôler le flux d’un algorithme ou évaluer des conditions dans des structures comme les boucles et les embranchements.

Les principaux opérateurs booléens sont décrits ci-dessous, accompagnés de leur table de vérité, qui montre le résultat de chaque opération pour toutes les combinaisons possibles des entrées A et B.

A

B

NON A

A ET B

A OU B

vrai

vrai

faux

vrai

vrai

vrai

faux

faux

faux

vrai

faux

vrai

vrai

faux

vrai

faux

faux

vrai

faux

faux

*   **NON A** : l’inverse de A (négation)
*   **A ET B** : vrai seulement si A et B sont vrais
*   **A OU B** : vrai si au moins un des deux est vrai

En informatique, nous utilisons le plus souvent l’anglais.

*   **NON A** : **NOT A**
*   **A ET B** : **A AND B**
*   **A OU B** : **A OR B**

#### Exemple 1 : Contrôle d’accès selon l’âge [#](#exemple-1--contr%c3%b4le-dacc%c3%a8s-selon-l%c3%a2ge)

    lire age
    SI age >= 18 ALORS
        écrire "Accès autorisé"
    SINON
        écrire "Accès refusé"
    FIN SI
    

Ce pseudocode décrit un algorithme simple de contrôle d’accès basé sur l’âge d’une personne. L’instruction lire age récupère une valeur (l’âge) entrée par l’utilisateur ou une source externe, stockée dans la variable age. Une structure conditionnelle (SI … ALORS … SINON) vérifie si age est supérieur ou égal à 18. Si la condition est vraie (age >= 18), l’algorithme affiche le message “Accès autorisé”, indiquant que la personne est majeure et peut accéder à une ressource ou un lieu. Sinon, si age est inférieur à 18, il affiche “Accès refusé”, signalant que l’accès est interdit. L’algorithme se termine après l’affichage.

La logique booléenne est essentielle pour écrire des conditions dans les algorithmes. Par exemple, dans une structure conditionnelle ou une boucle, les opérateurs booléens permettent de combiner plusieurs critères. Voici un exemple en pseudo-code pour vérifier si une personne peut voter :

    lire age
    lire est_citoyen
    SI age >= 19 ET est_citoyen = vrai ALORS
        écrire "Vous pouvez voter"
    SINON
        écrire "Vous ne pouvez pas voter"
    FIN SI
    

Ici, la condition `age >= 19 ET est_citoyen = vrai` utilise l’opérateur ET pour vérifier que deux critères sont remplis avant d’autoriser le vote.

Lorsqu’on combine plusieurs opérateurs booléens, il est important de connaître leur ordre de priorité :

1.  **NON** (évalué en premier).
2.  **ET**.
3.  **OU** (évalué en dernier). Pour éviter toute ambiguïté, on utilise des parenthèses pour préciser l’ordre des opérations. Par exemple :

    vrai ET faux OU vrai
    

Sans parenthèses, ET est évalué avant OU, donc cela donne `(vrai ET faux) OU vrai`, qui vaut `faux OU vrai`, soit `vrai`. Avec des parenthèses, on peut changer le résultat : `vrai ET (faux OU vrai)` donne `vrai ET vrai`, soit `vrai`.

Pour renforcer votre compréhension, utilisez l’application suivante.

Points : 0 | Vies : 5

Expression : TRUE AND FALSE

Démarrer le jeu Gauche Droite Tirer

(function(){const n="logicalGame\_",s=document.getElementById(\`${n}gameCanvas\`),t=s.getContext("2d"),C=document.getElementById(\`${n}score\`),\_=document.getElementById(\`${n}lives\`),N=document.getElementById(\`${n}expression\`),m=document.getElementById(\`${n}startButton\`),D=document.getElementById(\`${n}leftButton\`),T=document.getElementById(\`${n}rightButton\`),k=document.getElementById(\`${n}shootButton\`),a=document.getElementById(\`${n}feedbackMessage\`),u=document.getElementById(\`${n}gameOver\`),g=document.getElementById(\`${n}shootSound\`),p=document.getElementById(\`${n}correctSound\`),y=document.getElementById(\`${n}incorrectSound\`);let r=0,l=5,h=!1,e={x:s.width/2-25,y:550,width:50,height:30,speed:5},o=\[\],i=\[\],c=\[\],w={p:!0,q:!1,result:!1,text:"TRUE AND FALSE"},O=0,x=0;const F=200;function E(e,t){a.textContent=e,a.style.display="block",a.style.backgroundColor=t?"rgba(144, 238, 144, 0.9)":"rgba(255, 99, 71, 0.9)",a.style.color=t?"#006400":"#8B0000";const n=s.getBoundingClientRect(),o=s.parentElement.getBoundingClientRect();a.style.left=\`${n.left-o.left+n.width/2}px\`,a.style.top=\`${n.top-o.top+n.height/2}px\`,setTimeout(()=>{a.style.display="none"},1500)}function S(e,t){c.push({x:e,y:t,radius:5,maxRadius:40,opacity:1,color:"orange"})}function A(){for(let n=c.length-1;n>=0;n--){let e=c\[n\];t.beginPath(),t.arc(e.x,e.y,e.radius,0,Math.PI\*2),t.fillStyle=\`rgba(255, 165, 0, ${e.opacity})\`,t.fill(),e.radius+=3,e.opacity-=.07,e.opacity<=0&&c.splice(n,1)}}function j(){const o=\["AND","OR","XOR"\],e=Math.random()>.5,t=Math.random()>.5,s=o\[Math.floor(Math.random()\*o.length)\];let n,i=\`${String(e).toUpperCase()} ${s} ${String(t).toUpperCase()}\`;s==="AND"?n=e&&t:s==="OR"?n=e||t:n=(e||t)&&!(e&&t),w={p:e,q:t,result:n,text:i},N.textContent=\`Expression : ${i}\`}function M(){const e=Math.random()>.5,t=Math.random()\*(s.width-50);o.push({x:t,y:0,width:50,height:40,value:e,speed:2})}function d(t){t==="left"&&e.x>0&&(e.x-=e.speed),t==="right"&&e.x<s.width-e.width&&(e.x+=e.speed)}function v(){const t=Date.now();t-x>F&&(i.push({x:e.x+e.width/2-2.5,y:e.y,width:5,height:10,speed:7}),g.currentTime=0,g.play(),x=t)}function z(e,t){return e.x<t.x+t.width&&e.x+e.width>t.x&&e.y<t.y+t.height&&e.y+e.height>t.y}function b(){if(!h)return;t.clearRect(0,0,s.width,s.height),t.fillStyle="blue",t.fillRect(e.x,e.y,e.width,e.height),Date.now()-O>1e3&&(M(),O=Date.now()),o=o.filter(e=>e.y<s.height),o.forEach(e=>{e.y+=e.speed,t.fillStyle=e.value?"green":"red",t.fillRect(e.x,e.y,e.width,e.height),t.fillStyle="white",t.font="16px Arial",t.textAlign="center",t.fillText(String(e.value).toUpperCase(),e.x+e.width/2,e.y+e.height/2+5)}),i=i.filter(e=>e.y>0),i.forEach(e=>{e.y-=e.speed,t.fillStyle="black",t.fillRect(e.x,e.y,e.width,e.height)});for(let e=i.length-1;e>=0;e--){const t=i\[e\];for(let s=o.length-1;s>=0;s--){const n=o\[s\];if(z(t,n)){S(n.x+n.width/2,n.y+n.height/2),i.splice(e,1),o.splice(s,1),n.value===w.result?(r+=10,C.textContent=r,p.currentTime=0,p.play(),E("Bonne réponse !",!0),j()):(l-=1,\_.textContent=l,y.currentTime=0,y.play(),E("Mauvaise réponse !",!1),l<=0&&(h=!1,u.textContent=\`Partie terminée ! Points : ${r} Cliquez pour recommencer\`,u.style.display="block",u.onclick=f));break}}}A(),requestAnimationFrame(b)}function f(){h=!0,r=0,l=5,o=\[\],i=\[\],c=\[\],e.x=s.width/2-e.width/2,C.textContent=r,\_.textContent=l,j(),m.textContent="Jeu en cours",u.style.display="none",b()}m.addEventListener("click",f),D.addEventListener("click",()=>d("left")),T.addEventListener("click",()=>d("right")),k.addEventListener("click",v),document.addEventListener("keydown",e=>{e.key==="ArrowLeft"&&d("left"),e.key==="ArrowRight"&&d("right"),e.key===" "&&v()})})()

En maîtrisant la logique booléenne, vous serez mieux équipé pour concevoir des algorithmes clairs et efficaces, en particulier lorsqu’il s’agit de prendre des décisions complexes basées sur plusieurs conditions.

#### Exemple 2 : Vérifier si un nombre est dans un intervalle [#](#exemple-2--v%c3%a9rifier-si-un-nombre-est-dans-un-intervalle)

    lire x
    SI x >= 10 ET x <= 20 ALORS
        écrire "x est dans l'intervalle [10, 20]"
    SINON
        écrire "x n'est pas dans l'intervalle"
    FIN SI
    

Ce pseudocode décrit un algorithme qui vérifie si une valeur entrée se situe dans l’intervalle fermé \[10, 20\]. L’instruction lire x récupère une valeur (un nombre, supposé réel ou entier) entrée par l’utilisateur, stockée dans la variable x. Une structure conditionnelle (SI … ALORS … SINON) évalue si x satisfait deux conditions combinées par l’opérateur ET : x >= 10 (x est supérieur ou égal à 10) et x <= 20 (x est inférieur ou égal à 20). Si les deux conditions sont vraies, c’est-à-dire si x est dans l’intervalle \[10, 20\], l’algorithme affiche “x est dans l’intervalle \[10, 20\]”. Sinon, si x est inférieur à 10 ou supérieur à 20, il affiche “x n’est pas dans l’intervalle”. L’algorithme se termine après l’affichage.

mermaid.initialize({flowchart:{useMaxWidth:!0},theme:"default"})

graph TD
    A\[Lire x\] --> B{x >= 10 ET x <= 20 ?}
    B -- Vrai --> C\["x est dans l'intervalle"\]
    B -- Faux --> D\["x n'est pas dans l'intervalle"\]
    C --> E\[Fin\]
    D --> E
  

### Notation des programmeurs [#](#notation-des-programmeurs)

Pour des raisons historiques, les programmeurs remplacent souvent ET par `&&`, OU par `||` et NON par `!`. C’est le cas notamment en Java.

Utilisez l’application suivante pour tester votre compréhension.

Calculateur d'expressions booléennes
====================================

Sélectionner ou entrer une expression Choisir un exemple...!A || AA && BA || B!A && BA || !B!(A && B)(A || B) && !A

Générer la table de vérité

(function(){const e={operators:{"!":{precedence:3,type:"unary"},"&&":{precedence:2,type:"binary"},"||":{precedence:1,type:"binary"}},tokenizeExpression(e){const n=\[\],s=/(!|&&|\\|\\||\\(|\\))|(\[AB\])/g;let t;for(;(t=s.exec(e))!==null;)t\[1\]?n.push(t\[1\]):t\[2\]&&n.push(t\[2\]);return n},toRPN(e){if(!e||typeof e!="string")return\[\];const s=this.tokenizeExpression(e.replace(/\\s+/g,"")),n=\[\],t=\[\];for(const e of s)if(e==="A"||e==="B")n.push(e);else if(e==="(")t.push(e);else if(e===")"){for(;t.length>0&&t\[t.length-1\]!=="(";)n.push(t.pop());if(t.length===0||t\[t.length-1\]!=="(")throw new Error("Parenthèses mal assorties.");t.pop()}else if(this.operators\[e\]){for(;t.length>0&&t\[t.length-1\]!=="("&&this.operators\[t\[t.length-1\]\]&&this.operators\[t\[t.length-1\]\].precedence>=this.operators\[e\].precedence;)n.push(t.pop());t.push(e)}for(;t.length>0;){const e=t.pop();if(e==="("||e===")")throw new Error("Parenthèses mal assorties.");n.push(e)}return n},evaluateRPN(e,t){const n=\[\];for(const s of e)if(s==="A")n.push(t.A);else if(s==="B")n.push(t.B);else if(this.operators\[s\])if(this.operators\[s\].type==="unary"){if(n.length<1)throw new Error(\`Opérandes insuffisants pour l'opérateur '${s}'.\`);const e=n.pop();s==="!"&&n.push(!e)}else{if(n.length<2)throw new Error(\`Opérandes insuffisants pour l'opérateur '${s}'.\`);const e=n.pop(),t=n.pop();s==="&&"?n.push(t&&e):s==="||"&&n.push(t||e)}if(n.length!==1)throw new Error("Expression mal formée.");return n\[0\]},generateTruthTable(e){if(!e||!e.trim())return'<div style="color: #dc2626;">Erreur : veuillez entrer une expression valide.</div>';let n;try{n=this.toRPN(e)}catch(e){return\`<div style="color: #dc2626;">Erreur de l'expression : ${e.message}</div>\`}const s=\[{A:!0,B:!0},{A:!0,B:!1},{A:!1,B:!0},{A:!1,B:!1}\];let t='<h2 style="font-size: 20px; font-weight: bold; margin-bottom: 12px;">Tableau de vérité pour : '+e+"</h2>";return t+='<table style="width: 100%; border-collapse: collapse; margin-top: 8px;">',t+="<thead>",t+='<tr style="background-color: #e5e7eb;">',t+='<th style="border: 1px solid #d1d5db; padding: 8px; text-align: center;">A</th>',t+='<th style="border: 1px solid #d1d5db; padding: 8px; text-align: center;">B</th>',t+='<th style="border: 1px solid #d1d5db; padding: 8px; text-align: center;">Résultat</th>',t+="</tr>",t+="</thead>",t+="<tbody>",s.forEach((e,s)=>{let o;try{o=this.evaluateRPN(n,e)}catch(e){return\`<div style="color: #dc2626;">Erreur d'évaluation : ${e.message}</div>\`}t+=\`<tr id="boolcalc-row-${s}" style="opacity: 0; transition: opacity 0.5s ease, background-color 0.5s ease;">\`,t+=\`<td style="border: 1px solid #d1d5db; padding: 8px; text-align: center;">${e.A?"vrai":"faux"}</td>\`,t+=\`<td style="border: 1px solid #d1d5db; padding: 8px; text-align: center;">${e.B?"vrai":"faux"}</td>\`,t+=\`<td style="border: 1px solid #d1d5db; padding: 8px; text-align: center;">${o?"vrai":"faux"}</td>\`,t+="</tr>"}),t+="</tbody>",t+="</table>",{html:t,rowCount:s.length}},animateRows(e){for(let t=0;t<e;t++)setTimeout(()=>{const e=document.getElementById(\`boolcalc-row-${t}\`);e&&(e.style.opacity="1",e.style.backgroundColor="#bfdbfe",setTimeout(()=>{e.style.backgroundColor="transparent"},1e3))},t\*1e3)},init(){const e=document.getElementById("expression"),n=document.getElementById("customExpression"),s=document.getElementById("calculate"),t=document.getElementById("result");if(!e||!n||!s||!t){console.error("Erreur : un ou plusieurs éléments DOM sont manquants."),t.innerHTML=\`<div style="color: #dc2626;">Erreur : échec de l'initialisation de l'application.</div>\`;return}e.addEventListener("change",()=>{n.value=e.value,t.innerHTML=""}),s.addEventListener("click",()=>{const o=n.value.trim()||e.value.trim(),s=this.generateTruthTable(o);typeof s=="string"?t.innerHTML=s:(t.innerHTML=s.html,this.animateRows(s.rowCount))}),e.value&&(n.value=e.value)}};document.readyState==="loading"?document.addEventListener("DOMContentLoaded",()=>e.init()):e.init()})()

La boucle [#](#la-boucle)
-------------------------

Un algorithme prend habituellement des données et produit un résultat. Par exemple, un algorithme cherchant à déterminer si un nombre est pair, pourra recevoir un nombre en paramètre et il pourra produire comme réponse une valeur booléenne (vrai ou faux). Un même algorithme va donc généralement pouvoir être exécuté sur différentes données et pouvoir fournir des réponses différentes. En ce sens, une fonction (au sens mathématique) comme f(x) = a x + b peut être décrite comme étant un algorithme. Une fonction doit toujours produire la même valeur étant donnée les mêmes données. Un algorithme n’est pas limité de cette manière. Par exemple, un algorithme pourrait servir à choisir un nom aléatoirement au sein d’une liste. D’une exécution à l’autre, l’algorithme pourrait produire des valeurs différentes avec les mêmes données.

La plupart des algorithmes en pratique sont itératifs. Une itération est la répétition d’un processus. Si vous devez teindre une clôture, vous allez peut-être teindre chaque planche une à une. Nous dirons alors que vous itérez sur les planches. Mais comment saurez-vous où vous êtes rendu si vous prenez une pause? Peut-être pourrez-vous poser un petit drapeau sur la planche que vous êtes en train de teindre. On dira alors que le drapeau est un itérateur, c’est-à-dire un indicateur de votre progrès dans votre itération. À chaque étape où vous déplacez le drapeau d’une planche à l’autre, nous pourrons dire que vous incrémentez la position du drapeau. Si jamais vous deviez faire un retour à la planche précédente, nous dirons que vous décrémentez le drapeau. En informatique, nous n’utilisons pas de drapeaux physiques. Pour savoir où on est rendu, on utilise des compteurs, le plus souvent des valeurs entières. Quand on dit qu’on incrémente un entier, on veut généralement dire qu’on ajoute “1” à sa valeur.

Nous obtenons alors la notion de boucle: nous effectuons une tâche donnée tant qu’une condition n’est pas satisfaite. Cette vidéo présente le concept de boucle.

En informatique, on fait souvent référence à la notion d’impression à l’écran. Le plus souvent cela fait référence à l’affichage à l’écran d’un message ou d’un texte.

Pour illustrer concrètement ces concepts, considérons un exemple simple : afficher les nombres de 1 à 10 à l’écran, en utilisant une boucle qui incrémente un compteur à chaque itération. Cela montre comment un compteur agit comme un itérateur et comment la boucle répète l’impression jusqu’à ce que la condition soit satisfaite.

En Java, une boucle for classique s’écrit ainsi :

    for (int i = 1; i <= 10; i++) {
        System.out.println(i);
    }
    

Ici, i est initialisé à 1, la boucle continue tant que i est inférieur ou égal à 10, et i est incrémenté de 1 à chaque tour.

En JavaScript, la syntaxe est très similaire :

    for (let i = 1; i <= 10; i++) {
        console.log(i);
    }
    

La différence principale réside dans l’utilisation de let pour déclarer la variable i, ce qui limite sa portée à la boucle.

En Go, on utilise également une boucle for (la seule structure de boucle disponible dans le langage) :

    for i := 1; i <= 10; i++ {
        fmt.Println(i)
    }
    

L’initialisation, la condition et l’incrémentation sont regroupées dans l’en-tête de la boucle, comme dans les langages précédents.

En C++, la boucle for prend une forme proche de celle de Java :

    #include <iostream>
    
    for (int i = 1; i <= 10; i++) {
        std::cout << i << std::endl;
    }
    

Ces exemples montrent à quel point le concept de boucle avec compteur est universel dans les langages impératifs, même si les syntaxes varient légèrement. Dans tous les cas, l’impression à l’écran (via println, console.log, fmt.Println ou cout) est répétée 10 fois, en incrémentant l’itérateur à chaque passage. Cet usage évite d’écrire manuellement dix instructions d’impression identiques, rendant le code plus concis et plus facile à modifier (par exemple, pour changer la borne supérieure).

Tableau [#](#tableau)
---------------------

Un tableau est une structure de données qui permet de stocker plusieurs éléments, comme des nombres ou des chaînes de caractères, dans une seule variable. Ces éléments sont organisés séquentiellement et accessibles via un indice, un nombre entier qui indique leur position. Par exemple, dans un tableau nommé tableau, l’élément à la position 1 est noté `tableau[1]`, celui à la position 2 est `tableau[2]`, et ainsi de suite. La taille du tableau est normalement fixée et connue.

La numérotation des indices varie selon les langages de programmation ou les contextes. Dans de nombreux langages comme C, Java ou Python, les indices commencent à 0 : le premier élément est `tableau[0]`, le deuxième `tableau[1]`, etc. Cette convention, dite « base 0 », est courante en informatique pour des raisons techniques liées à la gestion de la mémoire. Dans d’autres contextes, comme certaines notations mathématiques ou langages comme Lua, les indices débutent à 1, ce qui peut être plus intuitif pour des utilisateurs non techniques. Le choix de l’index de départ dépend donc du système utilisé, et il est crucial de connaître cette convention pour manipuler correctement les éléments d’un tableau. La convention utilisée est souvent claire selon le contexte.

Tous les langages de programmation supportent les tableaux.

En Java, nous pouvons créer un tableau d’entiers comprenant 5 éléments comme suit.

    int [] tableau = new int[5];
    

Dans ce cas, le tableau comprendra la valeur 0 répétée 5 fois. Nous pouvons aussi initialiser un tableau avec les entiers `1,2,3` comme suit.

    int [] tableau = [1,2,3];
    

En JavaScript, la syntaxe équivalente est celle-ci.

    let tableau = Array(5).fill(0);
    let tableau = [1, 2, 3];
    

En Go, nous utiliserions la syntaxe suivante.

    tableau := make([]int, 5)
    tableau := []int{1, 2, 3}
    

En C++, nous pourrions faire l’équivalent.

    int tableau[5]{};
    int tableau[]{1, 2, 3};
    

Dans tous ces langages, l’expression `tableau[0]` fait référence au premier élément du tableau.

Exemple : Calcul de la moyenne [#](#exemple--calcul-de-la-moyenne)
------------------------------------------------------------------

Pour illustrer la notion de pseudo-code, commençons par un exemple relativement simple. Supposons que nous avons un tableau de notes (par ex., les notes 10.4, 12.6, 18.7, 5.0) et que nous désirons calculer la moyenne. On utilise le convention que si le tableau se nomme ’notes’, alors la première note (par ex., 10.4) est notes\[0\], la seconde note est notes\[1\]… et ainsi de suite jusqu’à notes\[3\]. Évidemment, dans ce cas, on sait qu’il y’a 4 notes, mais il plus pratique d’écrire le pseudo-code de manière générale. On fera donc référence à la longueur du tableau (au nombre d’éléments qu’il contient) comme étant un paramètre. Pour visiter tous les éléments, on peut initialiser une valeur entière à 0, et l’incrémenter de 1 tant qu’elle demeure plus petite que la longueur du tableau.

graph TD
    A\[Début\] --> B\[Initialiser iterateur = 0, moyenne = 0\]
    B --> C{iterateur < longueur de notes ?}
    C -- Vrai --> D\["moyenne = moyenne + notes\[iterateur\]"\]
    D --> E\[iterateur = iterateur + 1\]
    E --> C
    C -- Faux --> F\[moyenne = moyenne / longueur de notes\]
    F --> G\[Afficher moyenne\]
    G --> H\[Fin\]

Utilisez l’application suivante pour explorer l’exécution de l’algorithme. Ce pseudocode calcule la moyenne de quatre nombres rationnels stockés dans un tableau notes. Une variable iterateur est initialisée à 0 pour parcourir le tableau, et une variable moyenne est initialisée à 0 pour accumuler la somme des éléments. La boucle (TANT QUE iterateur < la longueur de notes FAIRE) itère tant que iterateur est inférieur à la longueur du tableau (ici, 4). À chaque itération, l’élément `notes[iterateur]` est ajouté à moyenne, et iterateur est incrémenté de 1. Une fois la boucle terminée, la somme totale des éléments est stockée dans moyenne. Enfin, moyenne est divisée par la longueur du tableau (moyenne = moyenne / la longueur de notes) pour obtenir la moyenne arithmétique. Le résultat, un nombre rationnel, est la sortie.

Calcul de la moyenne
====================

Entrez un tableau de nombres rationnels séparés par des virgules et exécutez le pseudocode pour calculer la moyenne.

Pseudocode

Tableau de quatre nombres rationnels : notes
Variables :
  Nombre entier : iterateur = 0
  Nombre rationnel : moyenne = 0
Sorties :
  Nombre rationnel : moyenne
TANT QUE iterateur < la longueur de notes FAIRE
    moyenne = moyenne + notes\[iterateur\]
    iterateur = iterateur + 1
FIN TANT QUE
moyenne = moyenne / la longueur de notes
                

État

Tableau : \[\]

Itérateur : 0

Moyenne : 0

Prochaine étape Réinitialiser

let moyenneNotes=\[10.4,12.6,18.7,5\],moyenneIterator=0,moyenneAverage=0,moyenneStep=0,moyenneIsRunning=!1;const moyennePseudocodeLines=\["Tableau de quatre nombres rationnels : notes","Variables :"," Nombre entier : iterateur = 0"," Nombre rationnel : moyenne = 0","Sorties :"," Nombre rationnel : moyenne","TANT QUE iterateur < la longueur de notes FAIRE"," moyenne = moyenne + notes\[iterateur\]"," iterateur = iterateur + 1","FIN TANT QUE","moyenne = moyenne / la longueur de notes"\];function moyenneUpdateDisplay(){document.getElementById("moyenneArray").textContent=\`\[${moyenneNotes.join(", ")}\]\`,document.getElementById("moyenneIterator").textContent=moyenneIterator,document.getElementById("moyenneAverage").textContent=moyenneAverage.toFixed(2);const e=document.getElementById("moyennePseudocode");e.innerHTML=moyennePseudocodeLines.map((e,t)=>\`<span style="display: block; ${t===moyenneStep?"background: #e6f4ea; color: #15803d;":""}">${e}</span>\`).join(""),document.getElementById("moyenneStepButton").style.cssText=moyenneIsRunning||moyenneStep>=moyennePseudocodeLines.length?"background: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: not-allowed; font-size: 16px;":"background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px;"}function moyenneLog(e){const n=document.getElementById("moyenneLog"),t=document.createElement("div");t.textContent=e,t.style.cssText="opacity: 0; transition: opacity 0.5s ease;",n.appendChild(t),setTimeout(()=>{t.style.opacity="1"},10),n.scrollTop=n.scrollHeight}function moyenneValidateInput(e){const t=e.split(",").map(e=>e.trim());return t.every(e=>!isNaN(e)&&e!==""&&Number.isFinite(Number(e)))}function moyenneUpdateArray(){const e=document.getElementById("moyenneArrayInput").value;return moyenneValidateInput(e)?(moyenneNotes=e.split(",").map(e=>Number(e.trim())),moyenneReset(),!0):(alert("Veuillez entrer des nombres rationnels valides séparés par des virgules."),document.getElementById("moyenneArrayInput").value=moyenneNotes.join(", "),!1)}async function moyenneRunStep(){if(moyenneIsRunning||moyenneStep>=moyennePseudocodeLines.length)return;if(moyenneIsRunning=!0,document.getElementById("moyenneStepButton").style.cssText="background: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: not-allowed; font-size: 16px;",moyenneStep===2)moyenneIterator=0,moyenneLog("Initialisation : itérateur = 0");else if(moyenneStep===3)moyenneAverage=0,moyenneLog("Initialisation : moyenne = 0");else if(moyenneStep===6)moyenneIterator<moyenneNotes.length?moyenneLog(\`Vérification : itérateur (${moyenneIterator}) < longueur de notes (${moyenneNotes.length})\`):(moyenneLog(\`Vérification : itérateur (${moyenneIterator}) >= longueur de notes (${moyenneNotes.length}), sortie de la boucle\`),moyenneStep=9);else if(moyenneStep===7){const e=moyenneAverage;moyenneAverage+=moyenneNotes\[moyenneIterator\],moyenneLog(\`Moyenne = ${e.toFixed(2)} + notes\[${moyenneIterator}\] = ${moyenneAverage.toFixed(2)}\`)}else if(moyenneStep===8)moyenneIterator++,moyenneLog(\`Itérateur = ${moyenneIterator-1} + 1 = ${moyenneIterator}\`),moyenneStep=5;else if(moyenneStep===10){const e=moyenneAverage;moyenneAverage/=moyenneNotes.length,moyenneLog(\`Moyenne = ${e.toFixed(2)} / ${moyenneNotes.length} = ${moyenneAverage.toFixed(2)}\`)}moyenneStep++,moyenneUpdateDisplay(),await new Promise(e=>setTimeout(e,500)),moyenneIsRunning=!1,moyenneUpdateDisplay()}function moyenneReset(){moyenneIterator=0,moyenneAverage=0,moyenneStep=0,document.getElementById("moyenneLog").innerHTML="",moyenneUpdateDisplay()}document.getElementById("moyenneArrayInput").addEventListener("change",moyenneUpdateArray),document.getElementById("moyenneStepButton").addEventListener("click",moyenneRunStep),document.getElementById("moyenneResetButton").addEventListener("click",()=>{moyenneUpdateArray()&&moyenneReset()}),moyenneUpdateDisplay()

Observez comment on termine la boucle “TANT QUE” avec une ligne “FIN TANT QUE”. Ce n’est pas nécessaire, mais vous devez être clair et précis quant au début et à la fin de vos opérations. On peut aussi indiquer le début et la fin d’une boucle avec l’indentation, ou tout autre moyen compris par les êtres humains. L’expression “TANT QUE” est associée à une condition qui peut être vraie ou fausse. L’exécution se poursuit tant que l’expression est vraie, et elle se termine lorsque l’expression est fausse.

Pour montrer comment ce pseudo-code se traduit dans des langages réels, considérons un tableau contenant les notes {10.4, 12.6, 18.7, 5.0} et calculons sa moyenne en utilisant une boucle qui parcourt les indices.

En Java, on utilise un tableau ou un ArrayList, mais ici avec un tableau fixe :

    double[] notes = {10.4, 12.6, 18.7, 5.0};
    double somme = 0;
    for (int i = 0; i < notes.length; i++) {
        somme += notes[i];
    }
    double moyenne = somme / notes.length;
    System.out.println(moyenne);
    

En JavaScript, les tableaux sont dynamiques et la propriété length donne directement la taille :

    let notes = [10.4, 12.6, 18.7, 5.0];
    let somme = 0;
    for (let i = 0; i < notes.length; i++) {
        somme += notes[i];
    }
    let moyenne = somme / notes.length;
    console.log(moyenne);
    

En Go, on utilise un slice et la fonction len pour obtenir la longueur :

    notes := []float64{10.4, 12.6, 18.7, 5.0}
    somme := 0.0
    for i := 0; i < len(notes); i++ {
        somme += notes[i]
    }
    moyenne := somme / float64(len(notes))
    fmt.Println(moyenne)
    

En C++, on peut utiliser un std::vector ou un tableau classique ; ici avec un initializer list et un vector :

    #include <iostream>
    #include <vector>
    
    std::vector<double> notes = {10.4, 12.6, 18.7, 5.0};
    double somme = 0;
    for (size_t i = 0; i < notes.size(); i++) {
        somme += notes[i];
    }
    double moyenne = somme / notes.size();
    std::cout << moyenne << std::endl;
    

Dans chaque cas, la structure reste fidèle au pseudo-code : initialisation d’une somme à zéro, parcours des indices de 0 à longueur-1 avec incrémentation, accumulation des valeurs, puis division finale par le nombre d’éléments. Cette approche rend l’algorithme indépendant de la taille exacte du tableau, exactement comme souhaité dans la version générale en pseudo-code.

 [![Previous](/inf1220-hugo/svg/backward.svg "Les ordinateurs et leurs langages") Les ordinateurs et leurs langages](/inf1220-hugo/docs/modules/module1/ordinateurs/) [Les algorithmes : conception et syntaxe ![Next](/inf1220-hugo/svg/forward.svg "Les algorithmes : conception et syntaxe")](/inf1220-hugo/docs/modules/module1/algorithmes2/) 


*   [Préalables](#préalables)
*   [Introduction](#introduction)
    *   [Qu’est-ce qu’un algorithme ?](#quest-ce-quun-algorithme-)
    *   [Qu’est-ce que le pseudo-code ?](#quest-ce-que-le-pseudo-code-)
    *   [Variables et valeurs](#variables-et-valeurs)
    *   [Logique booléenne](#logique-booléenne)
    *   [Notation des programmeurs](#notation-des-programmeurs)
*   [La boucle](#la-boucle)
*   [Tableau](#tableau)
*   [Exemple : Calcul de la moyenne](#exemple--calcul-de-la-moyenne)

## Les algorithmes : conception et syntaxe


*   [Concevoir un algorithme](#concevoir-un-algorithme)
*   [Syntaxe d’un algorithme](#syntaxe-dun-algorithme)
    *   [Les entrées, variables et sorties](#les-entrées-variables-et-sorties)
    *   [Les opérations](#les-opérations)
*   [Compter le nombre de voyelles d’un mot entrées au clavier](#compter-le-nombre-de-voyelles-dun-mot-entrées-au-clavier)

Les algorithmes : conception et syntaxe [#](#les-algorithmes--conception-et-syntaxe)
====================================================================================

Un algorithme est une méthode structurée pour résoudre un problème de manière systématique et efficace. Comparable à une recette culinaire, il fournit des instructions précises, exécutables pas à pas, pour transformer des données d’entrée en résultats attendus. Comprendre la conception et la syntaxe des algorithmes est essentiel pour tout programmeur souhaitant traduire une solution abstraite en code fonctionnel, quel que soit le langage utilisé.

Concevoir un algorithme [#](#concevoir-un-algorithme)
-----------------------------------------------------

Pour concevoir un algorithme, il convient d’analyser minutieusement le problème en identifiant les entrées, les sorties et les étapes de traitement nécessaires pour obtenir les résultats souhaités. Un algorithme se présente comme une suite logique d’instructions qu’un programmeur peut adapter à un langage comme Java, C++ ou Python. La démarche de conception suit généralement ces étapes :

Étape 1 : lire et comprendre l’énoncé du problème à résoudre.  
Étape 2 : définir les sorties (résultats attendus), les entrées (données initiales) et le traitement (relations permettant de passer des entrées aux sorties).  
Étape 3 : rédiger l’algorithme en pseudo-code, en respectant une structure claire et compréhensible.

Syntaxe d’un algorithme [#](#syntaxe-dun-algorithme)
----------------------------------------------------

La syntaxe d’un algorithme repose sur des conventions souples, contrairement aux langages de programmation qui imposent des règles strictes. Le pseudo-code privilégie la clarté et la précision des instructions, en s’appuyant sur des structures standardisées. Si une étape semble ambiguë ou trop complexe, il est souvent préférable de la décomposer en sous-étapes pour en faciliter la compréhension.

### Les entrées, variables et sorties [#](#les-entr%c3%a9es-variables-et-sorties)

Un algorithme débute par la déclaration des entrées, c’est-à-dire les données fournies directement (comme un texte à analyser ou des données financières) ou saisies par un utilisateur (via un clavier, une souris, etc.). Viennent ensuite les variables, qui portent un nom et une valeur, comme une variable `x` valant 1. Ces valeurs peuvent évoluer au fil du traitement. Les variables, utilisées pour stocker des informations intermédiaires, se déclinent en divers types : chaînes de caractères, entiers, nombres décimaux, etc. Enfin, les sorties correspondent aux résultats finaux du traitement, transmis à l’utilisateur ou à d’autres algorithmes. Un problème complexe peut en effet être résolu par plusieurs algorithmes interconnectés, un concept que nous relierons plus tard aux fonctions dans les langages de programmation.

### Les opérations [#](#les-op%c3%a9rations)

Un algorithme se décrit comme une séquence d’opérations, par exemple additionner deux nombres ou incrémenter une variable. Les opérations disponibles dépendent du modèle de calcul adopté, mais on presume généralement que les opérations mathématiques de base (addition, soustraction, multiplication, comparaison) sont prises en charge.

Les notations varient selon les conventions. Une multiplication peut s’écrire `x * y`, `x × y` ou simplement `x y`. De même, pour assigner la valeur 1 à une variable `x`, on peut utiliser `x ← 1` ou `x = 1`. Cependant, dans certains contextes, `x = 1` pourrait indiquer une comparaison (« x vaut-il 1 ? »). Pour lever l’ambiguïté, une notation comme `x == 1` est parfois préférée pour les comparaisons, en s’inspirant de langages de programmation. L’essentiel reste que chaque opération soit exprimée de manière claire et sans équivoque pour le lecteur.

Compter le nombre de voyelles d’un mot entrées au clavier [#](#compter-le-nombre-de-voyelles-dun-mot-entr%c3%a9es-au-clavier)
-----------------------------------------------------------------------------------------------------------------------------

L’algorithme suivant compte le nombre de voyelles saisies :

    Entrées :
      Chaîne de caractères : chaine = ""
    Sorties :
      Entier : nbVoyelle = 0
    Imprimer à l'écran "Veuillez entrer un mot au clavier suivi de la touche entrée"
    Saisir le mot au clavier et assigner à la variable chaine
    POUR TOUT caractère c dans chaine FAIRE
        SI c == 'a' OU c == 'e' OU c == 'i' OU c == 'o' OU c == 'u' OU c == 'y' ALORS
            nbVoyelle = nbVoyelle + 1
        FIN SI
    FIN POUR
    

Initialement, une variable chaine est définie comme une chaîne vide, et une variable nbVoyelle est initialisée à 0 pour compter les voyelles. L’algorithme affiche un message invitant l’utilisateur à entrer un mot suivi de la touche Entrée, puis stocke l’entrée dans chaine. Une boucle (POUR TOUT caractère c dans chaine FAIRE) parcourt chaque caractère c de la chaîne. Pour chaque caractère, une condition vérifie si c est une voyelle (a, e, i, o, u ou y) en utilisant une série de comparaisons avec l’opérateur OU. Si le caractère est une voyelle, nbVoyelle est incrémenté de 1. À la fin de la boucle, nbVoyelle contient le nombre total de voyelles dans la chaîne.

Le compteur de voyelles est un outil interactif conçu pour t’aider à comprendre comment un algorithme traite une chaîne de caractères pour compter ses voyelles. Commence par saisir un mot ou une phrase dans le champ de texte, par exemple « bonjour ». Clique sur le bouton « Prochaine étape » pour exécuter l’algorithme pas à pas. À chaque clic, une ligne du pseudocode s’illumine, et une explication apparaît dans la zone de journalisation en bas. Tu verras aussi l’état actuel : la chaîne saisie, le caractère en cours d’analyse et le nombre de voyelles comptées. Si tu veux recommencer, clique sur « Réinitialiser » pour effacer les résultats et repartir de zéro. Assure-toi que ta saisie n’est pas vide, sinon un message te demandera de corriger.

Cet outil vous permet de suivre la logique de l’algorithme de manière visuelle. Le pseudocode, affiché à gauche, détaille chaque étape : initialisation des variables (comme la chaîne et le compteur de voyelles), lecture de la saisie, parcours de chaque caractère et vérification s’il s’agit d’une voyelle (a, e, i, o, u, y). En avançant étape par étape, tu peux observer comment l’algorithme « pense » pour résoudre le problème. Prenez le temps de lire les messages du journal pour comprendre ce qui se passe à chaque moment. Cet exercice est parfait pour t’entraîner à traduire un problème en une série d’instructions claires, une compétence essentielle en programmation.

Compteur de voyelles
====================

Entrez une chaîne de caractères et exécutez le pseudocode pour compter les voyelles.

Pseudocode

Entrées :
  Chaîne de caractères : chaine = ""
Sorties :
  Entier : nbVoyelle = 0
Imprimer à l'écran "Veuillez entrer un mot au clavier suivi de la touche entrée"
Saisir le mot au clavier et assigner à la variable chaine
POUR TOUT caractère c dans chaine FAIRE
    SI c == 'a' OU c == 'e' OU c == 'i' OU c == 'o' OU c == 'u' OU c == 'y' ALORS
        nbVoyelle = nbVoyelle + 1
    FIN SI
FIN POUR
            

Prochaine étape Réinitialiser

État

Chaîne : ""

Caractère courant : \-

Nombre de voyelles : 0

let voyelChaine="bonjour",voyelNbVoyelle=0,voyelCurrentChar="-",voyelIndex=0,voyelStep=0,voyelIsRunning=!1;const voyelPseudocodeLines=\["Entrées :",' Chaîne de caractères : chaine = ""',"Sorties :"," Entier : nbVoyelle = 0",\`Imprimer à l'écran "Veuillez entrer un mot au clavier suivi de la touche entrée"\`,"Saisir le mot au clavier et assigner à la variable chaine","POUR TOUT caractère c dans chaine FAIRE"," SI c == 'a' OU c == 'e' OU c == 'i' OU c == 'o' OU c == 'u' OU c == 'y' ALORS"," nbVoyelle = nbVoyelle + 1"," FIN SI","FIN POUR"\];function voyelUpdateDisplay(){document.getElementById("voyelString").textContent=\`"${voyelChaine}"\`,document.getElementById("voyelCurrentChar").textContent=voyelCurrentChar==="-"?"-":\`'${voyelCurrentChar}'\`,document.getElementById("voyelVowelCount").textContent=voyelNbVoyelle;const e=document.getElementById("voyelPseudocode");e.innerHTML=voyelPseudocodeLines.map((e,t)=>\`<span style="display: block; ${t===voyelStep?"background: #e6f4ea; color: #15803d;":""}">${e}</span>\`).join(""),document.getElementById("voyelStepButton").style.cssText=voyelIsRunning||voyelStep>=voyelPseudocodeLines.length?"background: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: not-allowed; font-size: 16px;":"background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px;"}function voyelLog(e){const n=document.getElementById("voyelLog"),t=document.createElement("div");t.textContent=e,t.style.cssText="opacity: 0; transition: opacity 0.5s ease;",n.appendChild(t),setTimeout(()=>{t.style.opacity="1"},10),n.scrollTop=n.scrollHeight}function voyelValidateInput(e){return e.trim()!==""}function voyelUpdateString(){const e=document.getElementById("voyelStringInput").value;return voyelValidateInput(e)?(voyelChaine=e.trim(),voyelReset(),!0):(alert("Veuillez entrer une chaîne de caractères non vide."),document.getElementById("voyelStringInput").value=voyelChaine,!1)}async function voyelRunStep(){if(voyelIsRunning||voyelStep>=voyelPseudocodeLines.length)return;if(voyelIsRunning=!0,document.getElementById("voyelStepButton").style.cssText="background: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: not-allowed; font-size: 16px;",voyelStep===1)voyelChaine="",voyelLog('Initialisation : chaine = ""'),voyelStep++;else if(voyelStep===3)voyelNbVoyelle=0,voyelLog("Initialisation : nbVoyelle = 0"),voyelStep++;else if(voyelStep===4)voyelLog('Affichage : "Veuillez entrer un mot au clavier suivi de la touche entrée"'),voyelStep++;else if(voyelStep===5)voyelChaine=document.getElementById("voyelStringInput").value.trim(),voyelLog(\`Saisie : chaine = "${voyelChaine}"\`),voyelStep++;else if(voyelStep===6)voyelIndex<voyelChaine.length?(voyelCurrentChar=voyelChaine\[voyelIndex\],voyelLog(\`Début de boucle : traitement du caractère '${voyelCurrentChar}' à l’index ${voyelIndex}\`),voyelStep++):(voyelLog("Fin de la boucle : tous les caractères ont été traités"),voyelCurrentChar="-",voyelStep=10);else if(voyelStep===7){const e=\["a","e","i","o","u","y"\].includes(voyelCurrentChar.toLowerCase());voyelLog(\`Condition : '${voyelCurrentChar}' ${e?"est":"n’est pas"} une voyelle\`),e?voyelStep=8:voyelStep=9}else voyelStep===8?(voyelNbVoyelle++,voyelLog(\`Incrémentation : nbVoyelle = ${voyelNbVoyelle-1} + 1 = ${voyelNbVoyelle}\`),voyelStep=9):voyelStep===9?(voyelIndex++,voyelLog(\`Retour à la boucle : passage au caractère suivant\`),voyelStep=6):voyelStep===10?(voyelLog(\`Résultat final : nbVoyelle = ${voyelNbVoyelle}\`),voyelStep++):voyelStep++;voyelUpdateDisplay(),await new Promise(e=>setTimeout(e,500)),voyelIsRunning=!1,voyelUpdateDisplay()}function voyelReset(){voyelChaine=document.getElementById("voyelStringInput").value.trim(),voyelNbVoyelle=0,voyelCurrentChar="-",voyelIndex=0,voyelStep=0,document.getElementById("voyelLog").innerHTML="",voyelUpdateDisplay()}document.getElementById("voyelStringInput").addEventListener("change",voyelUpdateString),document.getElementById("voyelStepButton").addEventListener("click",voyelRunStep),document.getElementById("voyelResetButton").addEventListener("click",()=>{voyelUpdateString()&&voyelReset()}),voyelUpdateDisplay()

Maintenant que tu as exploré le compteur de voyelles, réfléchis à la manière dont cet algorithme pourrait être adapté ou amélioré. Par exemple, que se passerait-il si tu voulais compter uniquement certaines voyelles, comme « a » et « e », ou inclure les voyelles accentuées (é, è, ô) ? Comment modifierais-tu le pseudocode pour gérer ces cas ? Pense aussi à la structure de l’algorithme : quelles étapes pourraient être simplifiées ou rendues plus efficaces ? En te posant ces questions, tu commenceras à voir les algorithmes non pas comme des recettes figées, mais comme des solutions flexibles que tu peux ajuster pour répondre à différents besoins.

 [![Previous](/inf1220-hugo/svg/backward.svg "Les algorithmes") Les algorithmes](/inf1220-hugo/docs/modules/module1/algorithmes/) [Les algorithmes: les structures de contrôle ![Next](/inf1220-hugo/svg/forward.svg "Les algorithmes: les structures de contrôle")](/inf1220-hugo/docs/modules/module1/algorithmes3/) 


*   [Concevoir un algorithme](#concevoir-un-algorithme)
*   [Syntaxe d’un algorithme](#syntaxe-dun-algorithme)
    *   [Les entrées, variables et sorties](#les-entrées-variables-et-sorties)
    *   [Les opérations](#les-opérations)
*   [Compter le nombre de voyelles d’un mot entrées au clavier](#compter-le-nombre-de-voyelles-dun-mot-entrées-au-clavier)

## Les algorithmes: les structures de contrôle


*   [Le saut](#le-saut)
*   [L’embranchement comme structure de contrôle](#lembranchement-comme-structure-de-contrôle)
*   [La boucle comme structure de contrôle](#la-boucle-comme-structure-de-contrôle)
*   [Composition](#composition)
*   [La fin d’un algorithme](#la-fin-dun-algorithme)
*   [Exécution d’un pseudo-code](#exécution-dun-pseudo-code)
*   [Vidéo suggérée](#vidéo-suggérée)

Les structures de contrôle [#](#les-structures-de-contr%c3%b4le)
================================================================

Nous avons déjà présenté les notions d’embranchement et de boucle. C’est ce que nous appelons des structures de contrôle. Il est essentiel d’en comprendre la fonction.

On peut concevoir un algorithme qui ne comprend qu’une liste d’opérations simples (addition, soustraction, etc.). Cependant sans structures de contrôle, nous auront du mal à gérer les données dynamiques, par exemple un tableau qui peut contenir un nombre variable d’éléments, et on risque de devoir répéter beaucoup d’opérations. Les structures de contrôle permettent à l’algorithme de faire des choix de traitement en fonction de conditions. Une structure de contrôle correspond à l’action de tester des variables de contrôle et selon les résultats d’effectuer des opérations ou non.

Le saut [#](#le-saut)
---------------------

Le saut est une structure de contrôle fondamentale en informatique qui permet de modifier le flux d’exécution d’un algorithme en redirigeant l’exécution vers une autre partie du programme. Contrairement aux structures comme les embranchements (qui choisissent entre plusieurs chemins selon une condition) ou les boucles (qui répètent un bloc d’instructions), le saut est une instruction explicite qui transfère immédiatement le contrôle à une position spécifique dans le code, souvent marquée par une étiquette ou une adresse. Un saut peut être inconditionnel, où l’exécution est toujours redirigée vers une nouvelle position, ou conditionnel, où le saut dépend d’une condition booléenne.

Un saut inconditionnel redirige l’exécution vers une étiquette ou une ligne spécifique sans vérifier de condition. En pseudo-code, cela peut être représenté ainsi :

    ÉTIQUETTE debut
    écrire "Bonjour"
    SAUTER À debut
    

Dans cet exemple, l’algorithme affiche “Bonjour” et saute immédiatement à l’étiquette debut, créant une boucle infinie. Bien que rarement utilisé seul en pseudo-code, ce type de saut est courant dans les langages de bas niveau pour organiser le flux du programme

L’embranchement comme structure de contrôle [#](#lembranchement-comme-structure-de-contr%c3%b4le)
-------------------------------------------------------------------------------------------------

Un saut conditionnel (ou embranchement) dépend d’une condition booléenne. Si la condition est vraie, l’exécution saute à une étiquette donnée ; sinon, elle continue séquentiellement. Voici un exemple en pseudo-code :

    lire nombre
    SI nombre < 0 ALORS
        SAUTER À negatif
    FIN SI
    écrire "Le nombre est positif ou nul"
    SAUTER À fin
    ÉTIQUETTE negatif
    écrire "Le nombre est négatif"
    ÉTIQUETTE fin
    

En pratique, ces structures correspondent à poser des questions avec la syntaxe suivante : SI conditions ALORS opérations FIN SI. Il peut y avoir plusieurs conditions dans une structure de contrôle et la logique booléenne est utilisée pour les construire. Par exemple, SI a est égal 0 ET b est égal 1 ALORS faire c FIN SI.

Dans la notion de pseudo-code, il est également possible de faire une suite de structures de contrôle avec la syntaxe suivante : SI conditionA ALORS opérations SINON SI conditionB ALORS opérations SINON SI conditionC ALORS \[et ainsi de suite\] FIN SI.

Voici un exemple en pseudo-code illustrant une suite de structures de contrôle avec plusieurs conditions pour classer un score obtenu à un examen :

    lire score
    SI score ≥ 90 ALORS
        écrire "Note : A"
    SINON SI score ≥ 80 ALORS
        écrire "Note : B"
    SINON SI score ≥ 70 ALORS
        écrire "Note : C"
    SINON SI score ≥ 60 ALORS
        écrire "Note : D"
    SINON
        écrire "Note : F"
    FIN SI
    

Dans cet exemple, l’algorithme lit une variable score (un nombre entier représentant un score d’examen). Il utilise une série de conditions pour déterminer la note correspondante :

*   Si score est supérieur ou égal à 90, la note est “A”.
*   Sinon, si score est supérieur ou égal à 80, la note est “B”.
*   Sinon, si score est supérieur ou égal à 70, la note est “C”.
*   Sinon, si score est supérieur ou égal à 60, la note est “D”.
*   Sinon (pour tout score inférieur à 60), la note est “F”.

Chaque condition est évaluée séquentiellement, et dès qu’une condition est vraie, l’algorithme exécute l’opération associée (afficher la note) et sort de la structure avec FIN SI. Si aucune condition n’est vraie, l’opération par défaut (afficher “Note : F”) est exécutée.

Considérons l’exemple suivant. Il s’agit d’un outil interactif qui t’aide à comprendre comment un algorithme utilise des conditions pour classer une personne selon son âge. Pour commencer, saisis un âge entier positif dans le champ prévu, par exemple « 25 ». Ensuite, clique sur « Prochaine étape » pour exécuter l’algorithme étape par étape. À chaque clic, une ligne du pseudocode s’illumine, et un message explicatif apparaît dans la zone de journalisation en bas. Tu verras également l’état mis à jour : l’âge saisi et la catégorie déterminée (comme « Vous êtes un adulte »). Si tu veux recommencer, clique sur « Réinitialiser » pour effacer les résultats. Attention, l’âge doit être un nombre entier positif, sinon un message te demandera de corriger.

Cet outil vous permet de suivre le raisonnement de l’algorithme de manière claire. Le pseudocode, affiché à gauche, utilise une structure conditionnelle (SI, SINON SI, SINON) pour évaluer l’âge et assigner une catégorie : enfant (≤ 10 ans), adolescent (> 10 et < 18 ans), adulte (≥ 18 et < 65 ans) ou personne âgée (≥ 65 ans). En progressant dans les étapes, observe comment l’algorithme teste chaque condition et choisit la bonne catégorie. Lisez attentivement les messages du journal pour comprendre les décisions prises.

Catégorie d'âge
===============

Entrez un âge et exécutez le pseudocode pour déterminer la catégorie d'âge.

Pseudocode

État

Âge : 0

Sortie : \-

Prochaine étape Réinitialiser

(function(){for(var t=document.currentScript.previousElementSibling;t&&!t.classList.contains("age-app");)t=t.previousElementSibling;if(!t)return;let n=0,o="-",e=0,i=!1;const r=\["SI age <= 10 ALORS",\` Imprimer à l'écran "Vous êtes un enfant"\`,"SINON SI age > 10 ET age < 18 ALORS",\` Imprimer à l'écran "Vous êtes un adolescent"\`,"SINON SI age >= 18 ET age < 65 ALORS",\` Imprimer à l'écran "Vous êtes un adulte"\`,"SINON",\` Imprimer à l'écran "Vous êtes une personne âgée"\`,"FIN SI"\];function a(){t.querySelector(".ageAge").textContent=n,t.querySelector(".ageOutput").textContent=o;const s=t.querySelector(".agePseudocode");s.innerHTML=r.map((t,n)=>\`<span style="display: block; ${n===e?"background: #e6f4ea; color: #15803d;":""}">${t}</span>\`).join(""),t.querySelector(".ageStepButton").style.cssText=i||e>=r.length?"background: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: not-allowed; font-size: 16px;":"background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px;"}function s(e){const s=t.querySelector(".ageLog"),n=document.createElement("div");n.textContent=e,n.style.cssText="opacity: 0; transition: opacity 0.5s ease;",s.appendChild(n),setTimeout(()=>{n.style.opacity="1"},10),s.scrollTop=s.scrollHeight}function d(e){const t=Number(e);return!isNaN(t)&&Number.isInteger(t)&&t>=0}function c(){const e=t.querySelector(".ageAgeInput").value;return d(e)?(n=Number(e),l(),!0):(alert("Veuillez entrer un âge entier positif."),t.querySelector(".ageAgeInput").value=n||25,!1)}async function u(){if(i||e>=r.length)return;i=!0,t.querySelector(".ageStepButton").style.cssText="background: #95a5a6; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: not-allowed; font-size: 16px;",e===0?(n=Number(t.querySelector(".ageAgeInput").value),s(\`Vérification : age = ${n} <= 10\`),n<=10?e=1:e=2):e===1?(o="Vous êtes un enfant",s('Affichage : "Vous êtes un enfant"'),e=8):e===2?(s(\`Vérification : age = ${n} > 10 et age < 18\`),n>10&&n<18?e=3:e=4):e===3?(o="Vous êtes un adolescent",s('Affichage : "Vous êtes un adolescent"'),e=8):e===4?(s(\`Vérification : age = ${n} >= 18 et age < 65\`),n>=18&&n<65?e=5:e=6):e===5?(o="Vous êtes un adulte",s('Affichage : "Vous êtes un adulte"'),e=8):e===6?(s(\`Condition : SINON (aucune condition précédente n’est vraie)\`),e=7):e===7?(o="Vous êtes une personne âgée",s('Affichage : "Vous êtes une personne âgée"'),e=8):e===8&&(s(\`Fin de l’exécution : résultat = "${o}"\`),e++),a(),await new Promise(e=>setTimeout(e,500)),i=!1,a()}function l(){n=Number(t.querySelector(".ageAgeInput").value)||25,o="-",e=0,t.querySelector(".ageLog").innerHTML="",a()}t.querySelector(".ageAgeInput").addEventListener("change",c),t.querySelector(".ageStepButton").addEventListener("click",u),t.querySelector(".ageResetButton").addEventListener("click",function(){c()&&l()}),a()})()

Après avoir utilisé l’outil, prenez un moment pour réfléchir à la flexibilité de cet algorithme. Comment pourriez-vous le modifier pour ajouter de nouvelles catégories, comme « bébé » pour les âges de 0 à 2 ans, ou pour inclure des critères supplémentaires, comme une distinction entre « jeune adulte » et « adulte senior » ? Que se passerait-il si l’âge pouvait être négatif ou non entier ? Comment adapteriez-vous le pseudocode pour gérer ces cas ?

La boucle comme structure de contrôle [#](#la-boucle-comme-structure-de-contr%c3%b4le)
--------------------------------------------------------------------------------------

Il arrive régulièrement dans la résolution d’un problème qu’il est nécessaire de réaliser à plusieurs reprises une ou des opérations sur un ensemble de données. Par exemple, supposons qu’il est nécessaire de trouver le plus petit nombre dans un tableau d’entiers. Il sera forcément nécessaire d’itérer dans le tableau, une ligne à la fois, et de comparer les nombres entre eux. Pour ce faire, nous utiliserons deux éléments de syntaxe, soit le TANT QUE \_ FAIRE ou bien le POUR TOUT \_ FAIRE. Voici deux exemples de l’utilisation de ces deux approches :

Pseudocode 1 : Boucle POUR TOUT

    Entrées :
    Tableau d'entiers : tableau[100]
    
    Sorties :
    Entier minimum
    
    minimum = tableau[0]
    POUR TOUT Entier e de tableau FAIRE
        SI e < minimum ALORS
            minimum = e;
        FIN SI
    FIN POUR TOUT
    

Ce pseudocode décrit un algorithme pour trouver la valeur minimale dans un tableau d’entiers de taille 100. L’algorithme commence par initialiser la variable minimum à la première valeur du tableau (tableau\[0\]), en supposant que le tableau n’est pas vide. Ensuite, une boucle (POUR TOUT Entier e de tableau FAIRE) parcourt chaque élément e du tableau. À chaque itération, si l’élément e est inférieur à la valeur actuelle de minimum, alors minimum est mis à jour avec la valeur de e (minimum = e). À la fin de la boucle, minimum contient la plus petite valeur du tableau, qui est retournée comme résultat.

Pseudocode 2 : Boucle TANT QUE

    Entrées :
    Tableau d'entiers : tableau[100]
    
    Sorties :
    Entier minimum
    
    minimum = tableau[0]
    Entier iterateur = 0;
    TANT QUE iterateur < 100 FAIRE
        SI tableau[iterateur] < minimum ALORS
            minimum = tableau[iterateur];
        FIN SI
        iterateur = iterateur + 1;
    FIN TANT QUE
    

Ce pseudocode décrit un algorithme pour trouver la valeur minimale dans un tableau d’entiers de taille 100. Une variable minimum est initialisée avec la première valeur du tableau (tableau\[0\]), supposant que le tableau n’est pas vide. Une variable iterateur est initialisée à 0 pour suivre la position dans le tableau. La boucle (TANT QUE iterateur < 100 FAIRE) parcourt le tableau tant que iterateur est inférieur à 100. À chaque itération, si l’élément à l’indice iterateur (tableau\[iterateur\]) est inférieur à minimum, alors minimum est mis à jour avec cette valeur. Ensuite, iterateur est incrémenté de 1 (iterateur = iterateur + 1) pour passer à l’élément suivant. À la fin de la boucle, minimum contient la plus petite valeur du tableau, qui est retournée.

Au niveau fondamental, une boucle peut être vue comme un saut conditionnel dans le flux d’exécution d’un algorithme. Un saut conditionnel est une instruction qui, en fonction d’une condition, redirige l’exécution vers une autre partie du programme. Dans le cas d’une boucle, ce saut ramène l’exécution au début du bloc d’instructions tant que la condition associée à la boucle reste vraie.

Prenons l’exemple de la boucle TANT QUE. La condition iterateur < 100 est évaluée à chaque itération. Si elle est vraie, l’algorithme exécute le corps de la boucle (comparaison et mise à jour de minimum, incrémentation de iterateur), puis retourne au début de la boucle pour réévaluer la condition. Ce retour au début est un saut conditionnel : l’algorithme “saute” en arrière dans le code pour répéter le processus. Lorsque la condition devient fausse (quand iterateur atteint 100), le saut n’a plus lieu, et l’exécution continue après la boucle.

De même, dans la boucle POUR TOUT du Pseudocode 1, bien que la syntaxe soit plus abstraite, le mécanisme sous-jacent est similaire. La boucle parcourt chaque élément du tableau, ce qui peut être traduit en une série de sauts conditionnels gérés implicitement : après avoir traité un élément, l’algorithme “saute” à l’élément suivant tant qu’il reste des éléments à traiter.

Composition [#](#composition)
-----------------------------

Dans la pratique, un algorithme peut comporter plusieurs structures de contrôle itératives, plusieurs structures de contrôle alternatives et plusieurs opérations. On peut les combiner de diverses manières. Il est possible, par exemple, d’avoir une boucle TANT QUE au sein d’une autre boucle TANT QUE.

    TANT QUE x > 0 FAIRE
      TANT QUE x > 10 FAIRE
         x = x - 1
      FIN TANT QUE
    FIN TANT QUE
    

Ce pseudocode décrit une structure de boucles imbriquées qui modifie la valeur de la variable x jusqu’à ce qu’elle devienne inférieure ou égale à 0. La boucle externe (TANT QUE x > 0 FAIRE) continue tant que x est strictement positif. À l’intérieur, la boucle interne (TANT QUE x > 10 FAIRE) s’exécute uniquement si x est supérieur à 10, et dans ce cas, elle décrémente x de 1 à chaque itération (x = x - 1). Une fois que x devient inférieur ou égal à 10, la boucle interne s’arrête, mais la boucle externe ne se termine pas immédiatement, car elle vérifie seulement si x > 0. Cependant, comme il n’y a aucune instruction dans la boucle externe pour modifier x lorsque x ≤ 10, le programme entre dans une boucle infinie si x est compris entre 1 et 10 inclus. Si x est initialement supérieur à 10, il sera décrémenté jusqu’à atteindre 10, puis le programme se bloquera. Si x est initialement inférieur ou égal à 0, aucune des boucles ne s’exécute.

La fin d’un algorithme [#](#la-fin-dun-algorithme)
--------------------------------------------------

Un algorithme continue à s’exécuter tant qu’il reste des operations à faire. L’algorithme prend fin lorsque nous rencontrons la fin du pseudo-code ou lorsque le programmeur invoque la fin spécifiquement. Dans l’exemple suivant, le programmeur demande à ce que l’on cesse l’exécution dès que la valeur 5 est rencontrée.

    x = 0
    TANT QUE x < 10 ALORS
       ajoute un à x
       SI x == 5 ALORS TERMINE
    FIN TANT QUE
    AFFICHE x
    

La valeur x ne sera donc jamais affichée.

Il arrive aussi qu’un pseudo-code doit retourner une valeur. Par convention, dès que la valeur attendue est retournée, l’algorithme prend fin. Ainsi donc, dans le cas suivant, la valeur 5 sera retournée.

    x = 0
    TANT QUE x < 10 ALORS
       ajoute un à x
       SI x == 5 ALORS RETOURNE x
    FIN TANT QUE
    RETOURNE x
    

Exécution d’un pseudo-code [#](#ex%c3%a9cution-dun-pseudo-code)
---------------------------------------------------------------

Pour comprendre un pseudo-code que vous venez de recevoir, ou pour tester un pseudo-code que vous venez de créer, il est essentiel de l’exécuter. Quand on exécute un pseudo-code, on se contente de lire les consignes logiques.

Prenons un exemple:

    Variable test = 0
    
    TANT QUE test < 100
      test = test + 22
    FIN TANT QUE
    
    retourne test
    

mermaid.initialize({flowchart:{useMaxWidth:!0},theme:"default"})

graph TD
    A\[Début\] --> B\[Initialiser test = 0\]
    B --> C{test < 100 ?}
    C -- Vrai --> D\[test = test + 22\]
    D --> C
    C -- Faux --> E\[Retourner test\]
    E --> F\[Fin\]

1.  Je débute le pseudo-code avec la valeur 0 stockée dans la variable test.
2.  J’entre dans la boucle TANT QUE.
3.  J’ajoute 22 à la variable test, le résultat est 22.
4.  J’entre dans la boucle TANT QUE.
5.  J’ajoute 22 à la variable test, le résultat est 44.
6.  J’entre dans la boucle TANT QUE.
7.  J’ajoute 22 à la variable test, le résultat est 66.
8.  J’entre dans la boucle TANT QUE.
9.  J’ajoute 22 à la variable test, le résultat est 88.
10.  J’entre dans la boucle TANT QUE.
11.  J’ajoute 22 à la variable test, le résultat est 110.
12.  Je quitte la boucle TANT QUE.
13.  Je retourne la valeur stockée dans la variable test, soit 110.

Vous devez absolument être capable de faire de telles exécutions. Dans certains cas, votre pseudo-code va dépendre de paramètres: il faut alors exécuter le pseudo-code plus d’une fois, sur plusieurs cas de test. Dans certains cas, le pseudo-code peut prendre trop d’étapes pour qu’un humain puisse l’exécuter entièrement : vous devriez au moins en faire une partie.

Vidéo suggérée [#](#vid%c3%a9o-sugg%c3%a9r%c3%a9e)
--------------------------------------------------

 [![Previous](/inf1220-hugo/svg/backward.svg "Les algorithmes : conception et syntaxe") Les algorithmes : conception et syntaxe](/inf1220-hugo/docs/modules/module1/algorithmes2/) [Les problèmes difficiles ![Next](/inf1220-hugo/svg/forward.svg "Les problèmes difficiles")](/inf1220-hugo/docs/modules/module1/difficile/) 


*   [Le saut](#le-saut)
*   [L’embranchement comme structure de contrôle](#lembranchement-comme-structure-de-contrôle)
*   [La boucle comme structure de contrôle](#la-boucle-comme-structure-de-contrôle)
*   [Composition](#composition)
*   [La fin d’un algorithme](#la-fin-dun-algorithme)
*   [Exécution d’un pseudo-code](#exécution-dun-pseudo-code)
*   [Vidéo suggérée](#vidéo-suggérée)

## Les problèmes difficiles


Les problèmes difficiles [#](#les-probl%c3%a8mes-difficiles)
============================================================

> Dans ce cours, vous n’avez pas à maîtriser la notion de problème difficile, mais vous devriez être familier avec le concept.

Dans un cours d’introduction à la programmation, la plupart des exercices se concentrent sur des problèmes dont les algorithmes sont relativement simples à concevoir, surtout si vous maîtrisez les bases de la programmation et des mathématiques. Ces problèmes, comme calculer une moyenne ou trier une liste, demandent souvent une compréhension des structures de contrôle (conditions et boucles) et une application directe de concepts logiques. Cependant, dans des contextes plus avancés, certains problèmes se révèlent bien plus complexes, non pas à cause de la programmation elle-même, mais en raison de la difficulté à trouver un algorithme efficace. Ces défis, qualifiés de « problèmes difficiles », nécessitent des approches créatives et parfois des compromis, car leurs solutions idéales peuvent être hors de portée avec les ressources informatiques actuelles.

Les problèmes difficiles se rencontrent fréquemment dans des domaines comme l’intelligence artificielle, l’optimisation ou la cryptographie. Par exemple, développer une intelligence artificielle capable de rivaliser avec un grand maître aux échecs exige non seulement de programmer des règles du jeu, mais aussi de concevoir un algorithme capable d’évaluer des millions de positions possibles en un temps raisonnable. Ce type de problème est complexe, car il combine une exploration stratégique (choisir les meilleurs coups) avec des contraintes de performance (limiter le temps de calcul). De même, des problèmes d’optimisation, comme déterminer le chemin le plus court pour un livreur effectuant plusieurs arrêts, peuvent sembler simples en théorie, mais deviennent rapidement ingérables à mesure que le nombre de destinations augmente, en raison du nombre exponentiel de combinaisons possibles.

Un exemple classique de problème difficile est le problème du voyageur de commerce (TSP, pour Traveling Salesman Problem). Ce problème consiste à trouver le chemin le plus court permettant à un voyageur de visiter une liste de villes exactement une fois avant de revenir à son point de départ. Pour un petit nombre de villes, il est possible d’énumérer toutes les permutations et de calculer la distance totale de chaque trajet. Cependant, avec seulement 20 villes, le nombre de trajets possibles dépasse les milliards, rendant une approche par force brute (tester toutes les combinaisons) impraticable, même sur des ordinateurs puissants. Ce problème est dit « NP-difficile », un terme technique que les informaticiens utilisent pour désigner un problème qu’il est difficile de résoudre rapidement en général.

Pour aborder le problème du voyageur de commerce, des algorithmes approchés, comme l’algorithme du plus proche voisin, sont souvent utilisés. Cet algorithme commence par une ville arbitraire, puis choisit à chaque étape la ville la plus proche non visitée, jusqu’à ce que toutes les villes soient incluses, avant de revenir à la ville de départ. Bien que cette méthode ne garantisse pas toujours le chemin le plus court, elle produit une solution acceptable dans un temps de calcul bien plus court que l’énumération complète. Voici un pseudocode pour cet algorithme :

    Entrées :
      Liste de villes : villes[n]
      Matrice des distances : distances[n][n]
    
    Sorties :
      Liste ordonnée des villes : trajet
    
    Initialiser trajet comme une liste vide
    Choisir une ville de départ (par exemple, villes[0]) et l’ajouter à trajet
    Marquer la ville de départ comme visitée
    TANT QUE toutes les villes ne sont pas visitées FAIRE
        Trouver la ville non visitée la plus proche de la dernière ville dans trajet
        Ajouter cette ville à trajet
        Marquer cette ville comme visitée
    FIN TANT QUE
    Ajouter la ville de départ à la fin de trajet pour boucler
    RETOURNER trajet
    

Ce pseudocode décrit une solution gloutonne au problème du voyageur de commerce (TSP), qui cherche un circuit visitant chaque ville d’une liste exactement une fois et revenant à la ville de départ, en minimisant la distance totale. Les entrées sont une liste de n villes (`villes[n]`) et une matrice `distances[n][n]` indiquant les distances entre chaque paire de villes. Une liste trajet est initialisée vide pour stocker l’ordre des villes. L’algorithme commence par choisir une ville de départ (par exemple, `villes[0]`), l’ajoute à trajet, et la marque comme visitée. Une boucle (TANT QUE toutes les villes ne sont pas visitées FAIRE) sélectionne à chaque étape la ville non visitée la plus proche de la dernière ville ajoutée à trajet, en consultant la matrice distances. Cette ville est ajoutée à trajet et marquée comme visitée. Une fois toutes les villes visitées, la ville de départ est ajoutée à la fin de trajet pour former un circuit fermé. La liste trajet est retournée comme résultat.

Considérons une table (fictive) des distances entre certains villes du Québec.

Ville

Montréal

Québec

Laval

Gatineau

Longueuil

Montréal

\-

250

20

200

15

Québec

250

\-

240

450

245

Laval

20

240

\-

210

30

Gatineau

200

450

210

\-

210

Longueuil

15

245

30

210

\-

Vous pouvez vérifier que le trajet suivant représente 910 km.

Montréal -> Gatineau -> Laval -> Québec -> Longueuil -> Montréal

Maintenant, exécutez l’algorithme du plus proche voisin avec l’application suivante :

Problème du voyageur de commerce (TSP)
--------------------------------------

### Pseudocode (Approche du plus proche voisin)

Entrées :
  Liste de villes : villes\[n\]
  Matrice des distances : distances\[n\]\[n\]

Sorties :
  Liste ordonnée des villes : trajet

Initialiser trajet comme une liste vide
Choisir une ville de départ aléatoire et l’ajouter à trajet
Marquer la ville de départ comme visitée
TANT QUE toutes les villes ne sont pas visitées FAIRE
    Trouver la ville non visitée la plus proche de la dernière ville dans trajet
    Ajouter cette ville à trajet
    Marquer cette ville comme visitée
FIN TANT QUE
Ajouter la ville de départ à la fin de trajet pour boucler
RETOURNER trajet, Distance totale
            

### Tableau des distances (km)

Ville

Montréal

Québec

Laval

Gatineau

Longueuil

Montréal

\-

250

20

200

15

Québec

250

\-

240

450

245

Laval

20

240

\-

210

30

Gatineau

200

450

210

\-

210

Longueuil

15

245

30

210

\-

Commencer Réinitialiser

### État actuel

Cliquez sur 'Commencer' pour commencer l'initialisation.

Étape : 0

Trajet actuel :

Distance totale parcourue : 0 km

const TSPApp=function(){const t=\["Montréal","Québec","Laval","Gatineau","Longueuil"\],h=\[\[0,250,20,200,15\],\[250,0,240,450,245\],\[20,240,0,210,30\],\[200,450,210,0,210\],\[15,245,30,210,0\]\];let i=\[\],l=new Array(t.length).fill(!1),e=-1,a=-1,r=0,s=0,c=!1;const \_=\["Entrées :"," Liste de villes : villes\[n\]"," Matrice des distances : distances\[n\]\[n\]","","Sorties :"," Liste ordonnée des villes : trajet","","Initialiser trajet comme une liste vide","Choisir une ville de départ aléatoire et l’ajouter à trajet","Marquer la ville de départ comme visitée","TANT QUE toutes les villes ne sont pas visitées FAIRE"," Trouver la ville non visitée la plus proche de la dernière ville dans trajet"," Ajouter cette ville à trajet"," Marquer cette ville comme visitée","FIN TANT QUE","Ajouter la ville de départ à la fin de trajet pour boucler","RETOURNER trajet, Distance totale"\],o=document.getElementById("tsp-next-btn"),j=document.getElementById("tsp-reset-btn"),n=document.getElementById("tsp-message"),u=document.getElementById("tsp-step"),m=document.getElementById("tsp-trajet"),f=document.getElementById("tsp-distance"),y=document.getElementById("tsp-pseudocode"),p=document.getElementById("tsp-distance-table");function g(){const e={0:7,1:8,2:9,3:10,4:11,5:12,6:13,7:15,8:16},t=e\[s\]||-1;y.innerHTML=\_.map((e,n)=>n+1===t?\`<span style="background-color: #fefcbf; padding: 2px 4px; border-radius: 4px;">${e}</span>\`:e).join(\` \`)}function v(){const t=p.querySelectorAll("tbody tr"),n=p.querySelectorAll("thead th");if(e===-1){t.forEach(e=>{e.querySelectorAll("td").forEach(e=>{e.style.backgroundColor=""})}),n.forEach(e=>{e.style.backgroundColor="#2b6cb0"});return}e!==-1&&!c&&(n\[e+1\]&&(n\[e+1\].style.backgroundColor="#9ae6b4"),t\[e\]&&t\[e\].querySelectorAll("td").forEach((e)=>{e.style.backgroundColor="#fefcbf"}),t.forEach((t)=>{const s=t.querySelectorAll("td")\[e+1\];s&&(s.style.backgroundColor="#fefcbf")}))}function d(){i=\[\],l=new Array(t.length).fill(!1),e=-1,a=-1,r=0,s=0,c=!1,n.textContent="Cliquez sur 'Commencer' pour commencer l'initialisation.",u.textContent=\`Étape : 0\`,m.textContent=\`Trajet actuel : \`,f.textContent=\`Distance totale parcourue : 0 km\`,o.textContent="Commencer",o.disabled=!1,v(),g()}function b(){if(c){n.textContent=\`Algorithme terminé. Trajet final : ${i.join(" → ")}. Distance totale : ${r} km. Cliquez sur 'Réinitialiser' pour recommencer.\`,o.disabled=!0;return}switch(s){case 0:i=\[\],l=new Array(t.length).fill(!1),n.textContent="Le trajet est initialisé. Prêt à choisir une ville de départ.",s=1,o.textContent="Suivant";break;case 1:a=Math.floor(Math.random()\*t.length),i.push(t\[a\]),e=a,n.textContent=\`Ville de départ choisie aléatoirement : ${t\[a\]}.\`,s=2;break;case 2:l\[e\]=!0,n.textContent=\`Ville de départ (${t\[e\]}) marquée comme visitée.\`,s=3;break;case 3:i.length===t.length?(n.textContent="Toutes les villes ont été visitées. Ajout de la ville de départ pour boucler le trajet.",s=7):(n.textContent="Toutes les villes ne sont pas encore visitées. Recherche de la ville la plus proche.",s=4);break;case 4:let u=1/0,m=-1;for(let n=0;n<t.length;n++)if(!l\[n\]){const t=h\[e\]\[n\];t<u&&(u=t,m=n)}if(m===-1){n.textContent="Erreur: Aucune ville non visitée trouvée. L'algorithme est bloqué. Réinitialisez.",c=!0,o.textContent="Terminé",o.disabled=!0;break}o.dataset.nextCityIdx=m,o.dataset.minD=u,n.textContent=\`La ville la plus proche de ${t\[e\]} est ${t\[m\]} (distance ${u} km).\`,s=5;break;case 5:const f=parseInt(o.dataset.nextCityIdx),g=parseInt(o.dataset.minD);i.push(t\[f\]),r+=g,e=f,n.textContent=\`Ajout de ${t\[f\]} au trajet. Distance cumulée : ${r} km.\`,s=6;break;case 6:l\[e\]=!0,n.textContent=\`Ville ${t\[e\]} marquée comme visitée.\`,s=3;break;case 7:const p=h\[e\]\[a\];i.push(t\[a\]),r+=p,n.textContent=\`Retour à la ville de départ (${t\[a\]}) pour boucler (distance ${p} km).\`,s=8;break;case 8:c=!0,n.textContent=\`Algorithme terminé. Trajet final : ${i.join(" → ")}. Distance totale : ${r} km.\`,o.textContent="Terminé",o.disabled=!0;break;default:n.textContent="État inconnu. Réinitialisation.",d();break}u.textContent=\`Étape : ${s}\`,m.textContent=\`Trajet actuel : ${i.join(" → ")}\`,f.textContent=\`Distance totale parcourue : ${r} km\`,v(),g()}return o.addEventListener("click",b),j.addEventListener("click",d),d(),{initialize:d,nextStep:b}}()

Pouvez-vous obtenir une distance aussi courte que 910 km ;? Comment pourriez-vous modifier le pseudocode pour obtenir toujours la distance la plus courte ? C’est une question difficile.

Cet exemple d’algorithme est un algorithme glouton. Un algorithme glouton est une méthode algorithmique qui résout un problème en faisant à chaque étape le choix localement optimal, dans l’espoir que ces choix mènent à une solution globale optimale. Il privilégie la simplicité et la rapidité, mais ne garantit pas toujours la meilleure solution pour tous les problèmes, car il ne revient jamais en arrière pour réévaluer les décisions prises. Ce type d’algorithme est souvent utilisé pour des problèmes d’optimisation où une solution approximative est acceptable ou lorsque le problème possède une structure particulière, comme la propriété de sous-structure optimale ou la propriété gloutonne.

Considérons d’autres exemples de l’approche gloutonne.

*   Suppose que nous disposions d’un sac à dos de capacité limitée et d’objets ayant chacun un poids et une valeur. L’objectif est de maximiser la valeur totale des objets dans le sac, en autorisant des fractions d’objets. L’approche gloutonne dans ce cas consiste à d’abord trier les objets par rapport décroissant de leur rapport valeur/poids. Ensuite, il faut remplir le sac en prenant autant que possible de chaque objet dans cet ordre jusqu’à atteindre la capacité.
*   Suppose que nous disposions d’un ensemble d’activités avec des heures de début et de fin, et l’objectif est de sélectionner le plus grand nombre d’activités compatibles (qui ne se chevauchent pas). Une approche gloutonne consiste à trier les activités par heure de fin croissante. Sélectionner la première activité, puis la prochaine activité compatible, et ainsi de suite.

Les approches gloutonnes donnent généralement une solution qui n’est pas optimale.

Dans le cadre de ce cours, vous ne serez pas confronté à des problèmes aussi complexes que le voyageur de commerce. Les exercices proposés viseront à renforcer votre compréhension des bases algorithmiques, comme les boucles, les conditions et la manipulation de données simples. Cependant, il est utile de connaître l’existence de ces problèmes difficiles pour apprécier la profondeur de l’informatique. Ils illustrent l’importance de l’efficacité algorithmique et des compromis dans la conception de solutions. En explorant des cas plus simples, vous poserez les fondations nécessaires pour, un jour, peut-être, relever ces défis plus ardus.

 [![Previous](/inf1220-hugo/svg/backward.svg "Les algorithmes: les structures de contrôle") Les algorithmes: les structures de contrôle](/inf1220-hugo/docs/modules/module1/algorithmes3/) [Complexité algorithmique ![Next](/inf1220-hugo/svg/forward.svg "Complexité algorithmique")](/inf1220-hugo/docs/modules/module1/complex/)

## Complexité algorithmique


*   *   [Notation grand-O](#notation-grand-o)
    *   [Notation grand-O](#notation-grand-o-1)
    *   [Exemples d’algorithmes en](#exemples-dalgorithmes-en)
    *   [Exemples d’algorithmes en](#exemples-dalgorithmes-en-1)
    *   [Recherche dans un tableau trié](#recherche-dans-un-tableau-trié)
    *   [Tri](#tri)
    *   [Table de hachage](#table-de-hachage)
    *   [Un problème résoluble en ou en](#un-problème-résoluble-en--ou-en)
    *   [Les arbres en informatique](#les-arbres-en-informatique)
*   [Analyse amortie](#analyse-amortie)
*   [Vidéo optionnelle](#vidéo-optionnelle)

Complexité algorithmique [#](#complexit%c3%a9-algorithmique)
============================================================

La plupart des problèmes ne sont pas fondamentalement difficiles, mais toutes les solutions ne sont pas également efficaces. La complexité algorithmique fournit une mesure de cette efficacité.

La complexité algorithmique mesure le temps ou la mémoire qu’un algorithme nécessite en fonction de la taille de l’entrée (souvent notée \\( n \\)). Pour comparer les algorithmes, on utilise la notation grand-O (ou O-grande), qui donne un ordre de grandeur du nombre d’opérations à effectuer lorsque la taille des données augmente.

Comprendre la complexité algorithmique permet de choisir ou d’inventer des solutions efficaces, surtout pour de grandes quantités de données. Il est souvent utile de commencer par une solution simple (même lente), puis de chercher à l’optimiser en utilisant des structures de données ou des propriétés mathématiques adaptées.

> Dans ce cours, vous n’avez pas à maîtriser la notation grand-O et la complexité algorithmique. Néanmoins, il est utile d’être familier avec les principales notions.

### Notation grand-O [#](#notation-grand-o)

La notation \\( O(f(n)) \\) signifie que, pour des entrées de taille \\( n \\), l’algorithme effectue au plus un nombre d’opérations proportionnel à \\( f(n) \\) (à une constante près). On ne s’intéresse qu’au comportement pour de grandes valeurs de \\( n \\), et on ignore les détails d’implémentation ou les constantes cachées.

On considère souvent que l’accès à un élément d’un tableau par son index a une complexité \\( O(1) \\) puisqu’il s’agit d’une seule opération. Les operations arithmétique (+, -, etc.) ont aussi une complexité \\( O(1) \\).

### Notation grand-O [#](#notation-grand-o-1)

La notation \\( O(f(n)) \\) signifie que, pour des entrées de taille \\( n \\), l’algorithme effectue au plus un nombre d’opérations proportionnel à \\( f(n) \\) (à une constante près). On ne s’intéresse qu’au comportement pour de grandes valeurs de \\( n \\), et on ignore les détails d’implémentation ou les constantes cachées.

On considère souvent que l’accès à un élément d’un tableau par son index a une complexité \\( O(1) \\) puisqu’il s’agit d’une seule opération. Les opérations arithmétiques (+, -, etc.) ont aussi une complexité \\( O(1) \\).

Cette notation permet également de comparer différentes classes de complexité. Une hiérarchie courante observe que les algorithmes en complexité constante sont les plus efficaces pour de grandes entrées, suivis de ceux en complexité logarithmique (\\(O(\\log n)\\)), puis linéaire (\\(O(n)\\)), linéarithmique (\\(O(n\\log n)\\)), et enfin quadratique (\\(O(n^2\\)). Formellement, cela se traduit par des inclusions entre les classes : \\( O(1) \\subseteq O(\\log n) \\subseteq O(n) \\subseteq O(n \\log n) \\subseteq O(n^2) \\), où le logarithme est pris en base quelconque supérieure à 1 (la base n’affecte la définition qu’à une constante multiplicative près).

Pour établir ces inclusions, rappelons la définition : une fonction \\( g(n) \\) appartient à \\( O(f(n)) \\) s’il existe une constante positive \\( c \\) et un entier \\( n\_0 \\) tels que, pour tout \\( n \\geq n\_0 \\), \\( g(n) \\leq c \\cdot f(n) \\) (en considérant des fonctions positives pour \\( n \\) grand).

Considérons le logarithme en base 2 pour les preuves explicites, sans perte de généralité.

Pour \\( O(1) \\subseteq O(\\log n) \\) : toute fonction constante, disons \\( g(n) = k \\), satisfait l’inclusion. Comme \\( \\log\_2 n \\to \\infty \\) lorsque \\( n \\to \\infty \\), il existe \\( n\_0 \\) tel que \\( \\log\_2 n \\geq k \\) pour \\( n \\geq n\_0 \\). Ainsi, avec \\( c = 1 \\), \\( k \\leq \\log\_2 n \\) pour \\( n \\geq n\_0 \\).

Pour \\( O(\\log n) \\subseteq O(n) \\) : prenons \\( g(n) = \\log\_2 n \\). Il est clair que \\( \\log\_2 n \\leq n \\) pour tout \\( n \\geq 1 \\) (vérifiable pour petits \\( n \\), et évident asymptotiquement puisque la fonction exponentielle croît plus vite). Plus précisément, le limite \\( \\frac{\\log\_2 n}{n} \\to 0 \\) quand \\( n \\to \\infty \\) implique l’existence de \\( c = 1 \\) et \\( n\_0 = 1 \\) tels que \\( \\log\_2 n \\leq n \\).

Pour \\( O(n) \\subseteq O(n \\log n) \\) : pour \\( g(n) = n \\), observons que \\( \\log\_2 n \\geq 1 \\) pour \\( n \\geq 2 \\). Donc \\( n \\leq n \\cdot \\log\_2 n \\) pour \\( n \\geq 2 \\), avec \\( c = 1 \\) et \\( n\_0 = 2 \\).

Pour \\( O(n \\log n) \\subseteq O(n^2) \\) : pour \\( g(n) = n \\log\_2 n \\), notons que \\( \\log\_2 n \\leq n \\) pour \\( n \\geq 1 \\) (comme ci-dessus). Il suit que \\( n \\log\_2 n \\leq n \\cdot n = n^2 \\), avec \\( c = 1 \\) et \\( n\_0 = 1 \\).

Utilisez l’application suivante pour comprendre la différence entre \\(\\log n\\), \\(\\n\\), \\(\\n log n\\) et \\(n^2\\). Assurez-vous d’avoir une bonne intuition concernant la forme de ces fonctions.

Max n:  5

1 (constante)

log n

n (linéaire)

n log n

n² (quadratique)

(function(){const i=document.getElementById("graph");if(!i)return;const e=i.getContext("2d"),r=i.width,a=i.height,t={top:40,right:60,bottom:60,left:80},c=r-t.left-t.right,o=a-t.top-t.bottom,n=2;let s=5;const d=document.getElementById("nMaxSlider"),u=document.getElementById("nMaxValue");d.addEventListener("input",function(){s=parseInt(this.value),u.textContent=s,l()});function l(){e.clearRect(0,0,r,a);const i=s\*s;function d(e){return t.left+(e-n)/(s-n)\*c}function u(e){return t.top+o\*(1-e/i)}e.strokeStyle="#000",e.lineWidth=1,e.beginPath(),e.moveTo(t.left,t.top+o),e.lineTo(t.left+c,t.top+o),e.stroke(),e.beginPath(),e.moveTo(t.left,t.top),e.lineTo(t.left,t.top+o),e.stroke(),e.font="16px sans-serif",e.textAlign="center",e.textBaseline="top";const h=\[n,n+(s-n)/4,n+2\*(s-n)/4,n+3\*(s-n)/4,s\];h.forEach(i=>{if(i>=n&&i<=s){const n=d(i);e.fillText(Math.round(i),n,t.top+o+10),e.beginPath(),e.moveTo(n,t.top+o),e.lineTo(n,t.top+o+5),e.stroke()}}),e.textAlign="right",e.textBaseline="middle";const m=\[0,i/4,i/2,3\*i/4,i\];m.forEach(n=>{const s=u(n);e.fillText(Math.round(n),t.left-10,s),e.beginPath(),e.moveTo(t.left-5,s),e.lineTo(t.left,s),e.stroke()}),e.textAlign="center",e.textBaseline="top",e.fillText("n",r/2,a-20),e.save(),e.translate(20,a/2),e.rotate(-Math.PI/2),e.textAlign="center",e.textBaseline="bottom",e.fillText("valeur de la fonction",0,0),e.restore();function l(t,o){e.strokeStyle=t,e.lineWidth=3,e.beginPath();let a=!0;const r=Math.max(1,(s-n)/1e3);for(let t=Math.max(1,n);t<=s;t+=r){const c=o(t);if(!isNaN(c)&&c>=0&&c<=i){const n=d(t),s=u(c);a?(e.moveTo(n,s),a=!1):e.lineTo(n,s)}}e.stroke()}l("#2ca02c",()=>1),l("#1f77b4",e=>Math.log(e)),l("#ff7f0e",e=>e),l("#d62728",e=>e\*Math.log(e)),l("#9467bd",e=>e\*e)}l()})()

### Exemples d’algorithmes en \\( O(n) \\) [#](#exemples-dalgorithmes-en)

Un algorithme est en \\( O(n) \\) si le nombre d’opérations croît linéairement avec la taille de l’entrée. Par exemple, parcourir un tableau pour calculer la somme de ses éléments :

    somme = 0
    POUR i de 0 à n-1
        somme = somme + tableau[i]
    FIN POUR
    

Une variable somme est initialisée à 0 pour accumuler le résultat. La boucle (POUR i de 0 à n-1) parcourt chaque indice i du tableau, et à chaque itération, la valeur de l’élément tableau\[i\] est ajoutée à somme (`somme = somme + tableau[i]`). À la fin de la boucle, somme contient la somme totale des éléments du tableau.

Ici, chaque élément est visité une seule fois, donc le temps d’exécution est proportionnel à \\( n \\).

### Exemples d’algorithmes en \\( O(n^2) \\) [#](#exemples-dalgorithmes-en-1)

Un algorithme est en \\( O(n^2) \\) si le nombre d’opérations croît comme le carré de la taille de l’entrée. C’est typique des algorithmes qui utilisent deux boucles imbriquées, comme la recherche de toutes les paires d’éléments dans un tableau :

    POUR i de 0 à n-1
        POUR j de 0 à n-1
            faire quelque chose avec tableau[i] et tableau[j]
        FIN POUR
    FIN POUR
    

Ce pseudocode décrit une double boucle imbriquée qui parcourt toutes les paires possibles d’éléments dans un tableau de taille n. La boucle externe (POUR i de 0 à n-1) itère sur chaque indice i du tableau, tandis que la boucle interne (POUR j de 0 à n-1) parcourt à nouveau tous les indices j du tableau, indépendamment de i. À chaque itération, une opération (désignée par « faire quelque chose ») est effectuée en utilisant les éléments `tableau[i]` et `tableau[j]`. Cela inclut les cas où i et j désignent le même élément (quand i = j) ainsi que toutes les combinaisons de paires, y compris les permutations (par exemple, (i,j) et (j,i)).

Ici, pour chaque valeur de \\( i \\), on parcourt toutes les valeurs de \\( j \\), ce qui donne \\( n \\times n = n^2 \\) opérations.

Un algorithme \\( O(n^2) \\) est plus _lent_ qu’un algorithme \\( O(n) \\) quand \\( n \\) est très grand.

### Recherche dans un tableau trié [#](#recherche-dans-un-tableau-tri%c3%a9)

Lorsqu’un tableau est trié, on peut utiliser la recherche dichotomique (ou recherche binaire) pour trouver rapidement un élément. Cette méthode consiste à comparer la valeur recherchée à l’élément du milieu du tableau : si la valeur est plus petite, on recommence la recherche dans la moitié gauche ; sinon, dans la moitié droite. On répète jusqu’à trouver l’élément ou à épuiser le tableau.

Voici un exemple de pseudocode pour la recherche binaire :

    DEBUT
        debut ← 0
        fin ← n - 1
        TANT QUE debut ≤ fin
            milieu ← (debut + fin) // 2
            SI tableau[milieu] == valeur
                retourner VRAI
            SINON SI tableau[milieu] < valeur
                debut ← milieu + 1
            SINON
                fin ← milieu - 1
            FIN SI
        FIN TANT QUE
        retourner FAUX
    FIN
    

Le pseudocode décrit ce processus : on initialise deux indices, debut (0) et fin (n-1), délimitant la partie du tableau à explorer. À chaque itération, on calcule l’indice milieu (moyenne de debut et fin) et compare l’élément à cet indice (`tableau[milieu]`) avec la valeur recherchée. Si les deux sont égaux, l’élément est trouvé (retourner VRAI). Si la valeur est plus grande, la recherche se poursuit dans la moitié droite en ajustant debut à milieu + 1 ; sinon, dans la moitié gauche en ajustant fin à milieu - 1. Le processus se répète tant que debut ≤ fin. Si l’intervalle est épuisé sans trouver la valeur, l’algorithme retourne FAUX, indiquant que l’élément n’est pas dans le tableau.

Pour mieux comprendre l’algorithme, essayez de chercher des nombres dans un tableau trié avec l’application suivante.

 Rechercher

Entrez un nombre et cliquez sur "Rechercher" pour voir les étapes de la recherche binaire.

const sortedArray=\[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37\],arrayContainer=document.getElementById("arrayContainer");function renderArray(e=-1,t=-1,n=-1){arrayContainer.innerHTML="",sortedArray.forEach((s,o)=>{const i=document.createElement("span");i.innerText=s,i.style.padding="1px 10px",i.style.border="1px solid #ccc",i.style.borderRadius="1px",i.style.fontSize="12px",i.style.backgroundColor=o===n?"#ffc107":o>=e&&o<=t&&e!==-1&&t!==-1?"#d4edda":"#fff",i.style.transition="background-color 0.5s",arrayContainer.appendChild(i)})}renderArray();async function performBinarySearch(){const t=parseInt(document.getElementById("searchInput").value),c=document.getElementById("stepsContainer"),n=document.getElementById("resultContainer");if(c.innerHTML="",n.innerHTML="",renderArray(),isNaN(t)){n.innerHTML="Veuillez entrer un nombre valide.";return}let s=0,o=sortedArray.length-1,e=\[\],a=!1,r=-1,i=-1;for(;s<=o;){const n=Math.floor((s+o)/2),c=sortedArray\[n\];if(e.push(\`Comparaison avec l'élément au milieu (index ${n}) : ${c}\`),renderArray(s,o,n),addStepToContainer(e\[e.length-1\]),await new Promise(e=>setTimeout(e,1e3)),c===t){a=!0,r=n,e.push(\`Valeur ${t} trouvée à l'index ${n}.\`),addStepToContainer(e\[e.length-1\]);break}c<t?(e.push(\`La valeur ${t} est plus grande, recherche dans la moitié droite.\`),addStepToContainer(e\[e.length-1\]),i=n,s=n+1):(e.push(\`La valeur ${t} est plus petite, recherche dans la moitié gauche.\`),addStepToContainer(e\[e.length-1\]),o=n-1),await new Promise(e=>setTimeout(e,500))}await new Promise(e=>setTimeout(e,500)),a?(n.innerHTML=\`Valeur ${t} trouvée à l'index ${r}.\`,n.style.color="#28a745"):(i!==-1?n.innerHTML=\`Valeur ${t} non trouvée. La plus grande valeur inférieure est ${sortedArray\[i\]} à l'index ${i}.\`:n.innerHTML=\`Valeur ${t} non trouvée. Aucune valeur inférieure dans le tableau.\`,n.style.color="#dc3545")}function addStepToContainer(e){const t=document.createElement("p");t.innerText=e,t.style.margin="5px 0",t.style.color="#555",document.getElementById("stepsContainer").appendChild(t)}

Observez comment vous faites toujours moins de recherche qu’il y a d’éléments dans le tableau. Pouvez-vous faire en sorte qu’une seule étape soit nécessaire ? Quel est le nombre maximal d’étapes nécessaires ?

Cet algorithme a une complexité en \\( O(\\log n) \\), ce qui le rend très efficace pour les grands tableaux triés. Cela signifie que le nombre d’opérations nécessaires pour trouver (ou ne pas trouver) un élément ne croît pas proportionnellement à la taille du tableau, mais beaucoup plus lentement. Par exemple, pour un tableau de 1 000 000 d’éléments, la recherche binaire nécessite au maximum environ 20 comparaisons (car \\( \\log\_2 1\\,000\\,000 \\approx 20 \\)), alors qu’une recherche linéaire pourrait en demander jusqu’à 1 000 000 dans le pire cas. Plus le tableau est grand, plus l’avantage de la recherche binaire est important.

À chaque étape de la recherche binaire, on divise le nombre d’éléments restants par deux. Si on commence avec \\( n \\) éléments, après une comparaison il en reste \\( n/2 \\), puis \\( n/4 \\), puis \\( n/8 \\), etc. On répète ce processus jusqu’à ce qu’il ne reste qu’un seul élément à examiner.

On cherche donc le nombre d’étapes \\( k \\) tel que :

\\\[ \\frac{n}{2^k} = 1 \\\]

En résolvant pour \\( k \\) :

\\\[ n = 2^k \\implies k = \\log\_2 n \\\]

Ainsi, le nombre maximal de comparaisons est proportionnel à \\( \\log\_2 n \\). C’est pourquoi on dit que la recherche binaire a une complexité en \\( O(\\log n) \\).

### Tri [#](#tri)

Le tri consiste à réorganiser les éléments d’un tableau ou d’une liste selon un ordre donné (par exemple, croissant). Un algorithme de tri naïf, comme le tri à bulles (bubble sort) ou le tri par insertion, compare chaque élément à tous les autres et échange leur position si nécessaire. Ces algorithmes effectuent environ \\( n^2 \\) comparaisons pour un tableau de taille \\( n \\), ce qui leur donne une complexité en \\( O(n^2) \\). Cela devient très lent dès que le nombre d’éléments augmente.

Pseudocode du tri à bulle:

    POUR i de 0 à n-2
        POUR j de 0 à n-2-i
            SI tableau[j] > tableau[j+1] ALORS
                échanger tableau[j] et tableau[j+1]
            FIN SI
        FIN POUR
    FIN POUR
    

Le tri à bulle est un algorithme de tri simple qui parcourt un tableau de manière répétée pour comparer et échanger les éléments adjacents s’ils sont dans le mauvais ordre. Dans le pseudocode présenté, la boucle externe (i de 0 à n-2) contrôle le nombre de passes sur le tableau, chaque passe garantissant que l’élément le plus grand non encore trié est placé à la fin. La boucle interne (j de 0 à n-2-i) compare chaque paire d’éléments consécutifs (tableau\[j\] et tableau\[j+1\]) et les échange s’ils sont mal ordonnés (tableau\[j\] > tableau\[j+1\]). À chaque itération, les éléments les plus grands “remontent” comme des bulles vers la fin du tableau, d’où le nom de l’algorithme.

Utilisez cette application pour mieux comprendre le tri à bulle.

Lancer le tri Réinitialiser

(function(){const t=document.getElementById("bubbleSortApp\_startButton"),a=document.getElementById("bubbleSortApp\_resetButton"),o=document.getElementById("bubbleSortApp\_arrayContainer");let e=\[\],n=!1;function i(){e=Array.from({length:64},()=>Math.floor(Math.random()\*100)+10),s()}function s(t=\[\],n=\[\]){o.innerHTML="",e.forEach((e,s)=>{const i=document.createElement("div");i.style.height=\`${e\*2}px\`,i.style.width="20px",i.style.backgroundColor=t.includes(s)?"red":n.includes(s)?"blue":"gray",i.style.display="inline-block",o.appendChild(i)})}async function r(){if(n)return;n=!0,t.disabled=!0,t.style.cursor="not-allowed";for(let t=0;t<e.length;t++)for(let n=0;n<e.length-t-1;n++)s(\[n,n+1\]),await new Promise(e=>setTimeout(e,100)),e\[n\]>e\[n+1\]&&(\[e\[n\],e\[n+1\]\]=\[e\[n+1\],e\[n\]\],s(\[\],\[n,n+1\]),await new Promise(e=>setTimeout(e,100)));s(),n=!1,t.disabled=!1,t.style.cursor="pointer"}t.addEventListener("click",r),a.addEventListener("click",()=>{n||i()}),i()})()

Un autre algorithme simple est le tri par insertion. Il parcourt le tableau élément par élément, insérant chaque nouvel élément à sa place dans la partie déjà triée.

    POUR i de 1 à n-1
        clé ← tableau[i]
        j ← i - 1
        TANT QUE j ≥ 0 ET tableau[j] > clé
            tableau[j+1] ← tableau[j]
            j ← j - 1
        FIN TANT QUE
        tableau[j+1] ← clé
    FIN POUR
    

Le tri par insertion est un algorithme de tri qui construit progressivement une partie triée du tableau en insérant chaque élément à sa position correcte. Dans le pseudocode fourni, la boucle externe (i de 1 à n-1) sélectionne chaque élément (`clé ← tableau[i]`) à partir du deuxième élément. La boucle interne compare cette clé avec les éléments de la partie déjà triée (de `j ← i-1` jusqu’à 0), en déplaçant les éléments plus grands que la clé d’une position vers la droite (`tableau[j+1] ← tableau[j]`) tant que `tableau[j] > clé` et `j ≥ 0`. Une fois la bonne position trouvée, la clé est insérée (`tableau[j+1] ← clé`). Ce processus répété garantit que, à chaque étape, la sous-partie du tableau jusqu’à l’indice i est triée, aboutissant à un tableau entièrement trié à la fin.

Utilisez cette application pour mieux comprendre le tri par insertion.

Lancer le tri Réinitialiser

(function(){const t=document.getElementById("insertionSortApp\_startButton"),a=document.getElementById("insertionSortApp\_resetButton"),o=document.getElementById("insertionSortApp\_arrayContainer");let e=\[\],s=!1;function i(){e=Array.from({length:64},()=>Math.floor(Math.random()\*100)+10),n()}function n(t=-1,n=\[\]){o.innerHTML="",e.forEach((e,s)=>{const i=document.createElement("div");i.style.height=\`${e\*2}px\`,i.style.width="20px",i.style.backgroundColor=s===t?"blue":n.includes(s)?"red":"gray",i.style.display="inline-block",o.appendChild(i)})}async function r(){if(s)return;s=!0,t.disabled=!0,t.style.cursor="not-allowed";for(let s=1;s<e.length;s++){let o=e\[s\],t=s-1;for(n(s),await new Promise(e=>setTimeout(e,100));t>=0&&e\[t\]>o;)n(s,\[t\]),await new Promise(e=>setTimeout(e,100)),e\[t+1\]=e\[t\],t--;e\[t+1\]=o,n(),await new Promise(e=>setTimeout(e,100))}n(),s=!1,t.disabled=!1,t.style.cursor="pointer"}t.addEventListener("click",r),a.addEventListener("click",()=>{s||i()}),i()})()

Heureusement, il existe des algorithmes de tri plus efficaces. Par exemple, le tri fusion (merge sort) utilise une approche « diviser pour régner » : il divise le tableau en deux moitiés, trie chaque moitié récursivement, puis fusionne les deux moitiés triées en un seul tableau trié. Cette méthode réduit considérablement le nombre de comparaisons nécessaires et atteint une complexité en \\( O(n \\log n) \\).

Idée générale du trie fusion :

1.  Si le tableau contient 0 ou 1 élément, il est déjà trié.
2.  Sinon, on divise le tableau en deux parties de taille à peu près égale.
3.  On trie récursivement chaque partie.
4.  On fusionne les deux parties triées pour obtenir un tableau final trié.

Pseudocode du tri fusion:

    FONCTION triFusion(tableau)
        SI taille(tableau) ≤ 1 ALORS
            retourner tableau
        FIN SI
        milieu ← taille(tableau) // 2
        gauche ← triFusion(tableau[0 .. milieu-1])
        droite ← triFusion(tableau[milieu .. fin])
        retourner fusionner(gauche, droite)
    FIN FONCTION
    
    FONCTION fusionner(gauche, droite)
        résultat ← tableau vide
        TANT QUE gauche et droite ne sont pas vides
            SI gauche[0] ≤ droite[0] ALORS
                ajouter gauche[0] à résultat
                retirer gauche[0] de gauche
            SINON
                ajouter droite[0] à résultat
                retirer droite[0] de droite
            FIN SI
        FIN TANT QUE
        ajouter le reste de gauche (s’il en reste) à résultat
        ajouter le reste de droite (s’il en reste) à résultat
        retourner résultat
    FIN FONCTION
    

Le pseudocode décrit deux fonctions principales. La fonction triFusion divise récursivement le tableau en deux moitiés jusqu’à ce que chaque sous-tableau ait au plus un élément (déjà trié). Pour cela, elle calcule l’indice milieu, trie récursivement la moitié gauche (0 à milieu-1) et la moitié droite (milieu à fin), puis fusionne ces deux sous-tableaux triés. La fonction fusionner combine les sous-tableaux gauche et droite en un tableau trié : elle compare les premiers éléments de chaque sous-tableau, ajoute le plus petit à résultat, et retire cet élément de son sous-tableau d’origine. Ce processus continue jusqu’à ce qu’un des sous-tableaux soit vide, puis les éléments restants de l’autre sous-tableau sont ajoutés à résultat.

Le tri fusion est donc beaucoup plus rapide que les tris naïfs pour les grands tableaux, et il illustre l’intérêt des algorithmes efficaces en informatique.

Utilisez cette application pour mieux comprendre le tri fusion.

Lancer le tri Réinitialiser

(function(){const n=document.getElementById("mergeSortApp\_startButton"),r=document.getElementById("mergeSortApp\_resetButton"),i=document.getElementById("mergeSortApp\_arrayContainer");let e=\[\],s=!1;function a(){e=Array.from({length:64},()=>Math.floor(Math.random()\*100)+10),t()}function t(t=\[\],n=\[\]){i.innerHTML="",e.forEach((e,s)=>{const o=document.createElement("div");o.style.height=\`${e\*2}px\`,o.style.width="20px",o.style.backgroundColor=n.includes(s)?"blue":t.includes(s)?"red":"gray",o.style.display="inline-block",i.appendChild(o)})}async function c(n,s,o){let c=\[\],a=0,r=0,i=o;for(;a<n.length&&r<s.length;)t(\[i\],\[i\]),await new Promise(e=>setTimeout(e,100)),n\[a\]<=s\[r\]?(c.push(n\[a\]),e\[i\]=n\[a\],a++):(c.push(s\[r\]),e\[i\]=s\[r\],r++),i++,t(\[o,o+c.length-1\],\[i-1\]),await new Promise(e=>setTimeout(e,100));for(;a<n.length;)c.push(n\[a\]),e\[i\]=n\[a\],t(\[i\],\[i\]),await new Promise(e=>setTimeout(e,100)),a++,i++;for(;r<s.length;)c.push(s\[r\]),e\[i\]=s\[r\],t(\[i\],\[i\]),await new Promise(e=>setTimeout(e,100)),r++,i++;return c}async function o(n,s){if(n<s){const i=Math.floor((n+s)/2);t(e.slice(n,i+1).map((e,t)=>n+t)),await new Promise(e=>setTimeout(e,100)),await o(n,i),t(e.slice(i+1,s+1).map((e,t)=>i+1+t)),await new Promise(e=>setTimeout(e,100)),await o(i+1,s);const a=e.slice(n,i+1),r=e.slice(i+1,s+1);await c(a,r,n)}}async function l(){if(s)return;s=!0,n.disabled=!0,n.style.cursor="not-allowed",await o(0,e.length-1),t(),s=!1,n.disabled=!1,n.style.cursor="pointer"}n.addEventListener("click",l),r.addEventListener("click",()=>{s||a()}),a()})()

Un autre algorithme performant est le tri rapide (quick sort). Il choisit un élément pivot, partitionne le tableau en deux sous-tableaux (les éléments plus petits que le pivot et ceux plus grands), puis trie récursivement chaque sous-tableau. En moyenne, sa complexité est en \\( O(n \\log n) \\), bien qu’il puisse atteindre \\( O(n^2) \\) dans le pire cas (par exemple, si le tableau est déjà trié et que le pivot est mal choisi). Le choix du pivot est crucial : une stratégie courante est de sélectionner la médiane de trois valeurs ou un élément aléatoire.

    FONCTION triRapide(tableau, début, fin)
        SI début < fin ALORS
            pivot ← partitionner(tableau, début, fin)
            triRapide(tableau, début, pivot - 1)
            triRapide(tableau, pivot + 1, fin)
        FIN SI
    FIN FONCTION
    
    FONCTION partitionner(tableau, début, fin)
        pivot ← tableau[fin]
        i ← début - 1
        POUR j de début à fin - 1
            SI tableau[j] ≤ pivot ALORS
                i ← i + 1
                échanger tableau[i] et tableau[j]
            FIN SI
        FIN POUR
        échanger tableau[i + 1] et tableau[fin]
        retourner i + 1
    FIN FONCTION
    

La fonction triRapide vérifie si l’intervalle à trier (de début à fin) contient plus d’un élément ; si oui, elle appelle partitionner pour réorganiser le tableau autour d’un pivot, puis trie récursivement les sous-tableaux à gauche (de début à pivot-1) et à droite (de pivot+1 à fin). La fonction partitionner sélectionne le dernier élément comme pivot (tableau\[fin\]) et réarrange le tableau de sorte que les éléments inférieurs ou égaux au pivot soient à gauche et les plus grands à droite. Elle utilise un indice i pour suivre la frontière des éléments plus petits et échange les éléments appropriés via un parcours (j de début à fin-1). Enfin, le pivot est placé à sa position finale (échange avec tableau\[i+1\]), et son indice (i+1) est retourné.

Utilisez cette application pour mieux comprendre le tri rapide.

Stratégie de pivot : Médiane de troisÉlément aléatoireDernier élémentPremier élément Lancer le tri Réinitialiser

(function(){const n=document.getElementById("quickSortApp\_startButton"),r=document.getElementById("quickSortApp\_resetButton"),c=document.getElementById("quickSortApp\_pivotStrategy"),i=document.getElementById("quickSortApp\_arrayContainer");let e=\[\],s=!1;function a(){e=Array.from({length:64},()=>Math.floor(Math.random()\*100)+10),t()}function t(t=-1,n=\[\],s=\[\]){i.innerHTML="",e.forEach((e,o)=>{const a=document.createElement("div");a.style.height=\`${e\*2}px\`,a.style.width="20px",a.style.backgroundColor=o===t?"green":s.includes(o)?"blue":n.includes(o)?"red":"gray",a.style.display="inline-block",i.appendChild(a)})}function l(t,n){const s=Math.floor((t+n)/2),o=\[{value:e\[t\],index:t},{value:e\[s\],index:s},{value:e\[n\],index:n}\];return o.sort((e,t)=>e.value-t.value),o\[1\].index}async function d(n,s){let o;const a=c.value;a==="first"?o=n:a==="random"?o=n+Math.floor(Math.random()\*(s-n+1)):a==="median"?o=l(n,s):o=s;const r=e\[o\];o!==s&&(\[e\[o\],e\[s\]\]=\[e\[s\],e\[o\]\],o=s),t(o,\[n,s\]),await new Promise(e=>setTimeout(e,100));let i=n-1;for(let a=n;a<s;a++)t(o,\[a,i+1\]),await new Promise(e=>setTimeout(e,100)),e\[a\]<=r&&(i++,i!==a&&(\[e\[i\],e\[a\]\]=\[e\[a\],e\[i\]\],t(o,\[\],\[i,a\]),await new Promise(e=>setTimeout(e,100))));return i+1!==s&&(\[e\[i+1\],e\[s\]\]=\[e\[s\],e\[i+1\]\],t(-1,\[\],\[i+1,s\]),await new Promise(e=>setTimeout(e,100))),i+1}async function o(e,t){if(e<t){const n=await d(e,t);await o(e,n-1),await o(n+1,t)}}async function u(){if(s)return;s=!0,n.disabled=!0,n.style.cursor="not-allowed",await o(0,e.length-1),t(),s=!1,n.disabled=!1,n.style.cursor="pointer"}n.addEventListener("click",u),r.addEventListener("click",()=>{s||a()}),a()})()

Le tri rapide est souvent le plus rapide en pratique pour plusieurs raisons. Premièrement, le tri rapide est efficace en termes de localité de mémoire. Il travaille directement sur le tableau (tri en place), ce qui minimise les accès mémoire et exploite bien la mémoire tampon des processeurs modernes. Comparé au tri fusion, qui nécessite un tableau auxiliaire pour la fusion, le tri rapide réduit les allocations de mémoire et les copies d’éléments. Deuxièmement, le tri rapide effectue moins de comparaisons en moyenne. Lors du partitionnement, il répartit les éléments autour d’un pivot, ce qui réduit rapidement la taille des sous-tableaux à trier. Si le pivot est bien choisi (par exemple, proche de la médiane), les sous-tableaux sont équilibrés, conduisant à une division efficace du problème. Même avec un choix de pivot aléatoire, les cas défavorables sont rares dans des données réelles. Troisièmement, le tri rapide est adaptable aux données. Dans des ensembles partiellement triés ou avec des motifs courants, il peut tirer parti de ces structures pour réduire le nombre d’échanges. Par exemple, un bon choix de pivot peut minimiser les réarrangements inutiles.

Utilisez l’application suivante pour comparer les techniques de tri. Appuyez sur _Lancer tous les tris_ et regardez les 4 algorithmes s’exécuter en même temps. Constatez que certains algorithmes sont plus rapides que d’autres. Que pensez-vous qu’il se passerait si nous avions moins d’éléments (par ex., 4) ou beaucoup plus d’éléments (par ex., 1000) ?

Lancer tous les tris Réinitialiser Stratégie de pivot (tri rapide) : Médiane de troisÉlément aléatoireDernier élémentPremier élément

Tri à bulles

Tri par insertion

Tri par fusion

Tri rapide

(function(){const i=document.getElementById("sortingApp\_startAllButton"),f=document.getElementById("sortingApp\_resetButton"),m=document.getElementById("sortingApp\_pivotStrategy"),c={bubble:document.getElementById("sortingApp\_bubbleSortContainer"),insertion:document.getElementById("sortingApp\_insertionSortContainer"),merge:document.getElementById("sortingApp\_mergeSortContainer"),quick:document.getElementById("sortingApp\_quickSortContainer")};let a=\[\],t={bubble:\[\],insertion:\[\],merge:\[\],quick:\[\]},r=!1,o={bubble:new Set,insertion:new Set,merge:new Set,quick:new Set};const j=64,s=50,w=100,p=10;function d(){a=Array.from({length:j},()=>Math.floor(Math.random()\*(w-p+1))+p),t.bubble=\[...a\],t.insertion=\[...a\],t.merge=\[...a\],t.quick=\[...a\],o={bubble:new Set,insertion:new Set,merge:new Set,quick:new Set},e()}function l(e,t,n,s={comparing:\[\],swapping:\[\],pivot:-1}){e.innerHTML="";const i=e.clientWidth-2\*10,a=2,r=(t.length-1)\*a,c=Math.max(2,Math.floor((i-r)/t.length));t.forEach((t,i)=>{const a=document.createElement("div");a.style.transition="background-color 0.1s ease, height 0.1s ease",a.style.display="inline-block",a.style.borderRadius="4px",a.style.height=\`${t\*2}px\`,a.style.width=\`${c}px\`,o\[n\].has(i)?a.style.backgroundColor="#10b981":i===s.pivot?a.style.backgroundColor="#22c55e":Array.isArray(s.swapping)&&s.swapping.includes(i)?a.style.backgroundColor="#3b82f6":Array.isArray(s.comparing)&&s.comparing.includes(i)?a.style.backgroundColor="#ef4444":a.style.backgroundColor="#6b7280",e.appendChild(a)})}function e(e={}){l(c.bubble,t.bubble,"bubble",{comparing:\[\],swapping:\[\],pivot:-1,...e.bubble}),l(c.insertion,t.insertion,"insertion",{comparing:\[\],swapping:\[\],pivot:-1,...e.insertion}),l(c.merge,t.merge,"merge",{comparing:\[\],swapping:\[\],pivot:-1,...e.merge}),l(c.quick,t.quick,"quick",{comparing:\[\],swapping:\[\],pivot:-1,...e.quick})}const n=e=>new Promise(t=>setTimeout(t,e));async function v(){let i=t.bubble,a=i.length;for(let t=0;t<a-1;t++){for(let o=0;o<a-t-1;o++)e({bubble:{comparing:\[o,o+1\]}}),await n(s),i\[o\]>i\[o+1\]&&(\[i\[o\],i\[o+1\]\]=\[i\[o+1\],i\[o\]\],e({bubble:{swapping:\[o,o+1\]}}),await n(s));o.bubble.add(a-1-t)}o.bubble.add(0),e({bubble:{}})}async function g(){let i=t.insertion,a=i.length;for(let r=1;r<a;r++){let c=i\[r\],t=r-1;for(e({insertion:{comparing:\[r\],swapping:\[t+1\]}}),await n(s);t>=0&&i\[t\]>c;)i\[t+1\]=i\[t\],e({insertion:{comparing:\[t,r\],swapping:\[t+1,t\]}}),await n(s),t--;i\[t+1\]=c,e({insertion:{swapping:\[t+1\]}}),await n(s);for(let e=0;e<=r;e++)o.insertion.add(e)}for(let e=0;e<a;e++)o.insertion.add(e);e({insertion:{}})}async function b(t,o,i,a){let r=\[\],c=o,l=i+1,d=0;for(;c<=i&&l<=a;)e({merge:{comparing:\[c,l\]}}),await n(s),t\[c\]<=t\[l\]?r\[d++\]=t\[c++\]:r\[d++\]=t\[l++\];for(;c<=i;)r\[d++\]=t\[c++\];for(;l<=a;)r\[d++\]=t\[l++\];for(let i=0;i<r.length;i++)t\[o+i\]=r\[i\],e({merge:{swapping:\[o+i\]}}),await n(s)}async function h(t,n,s){if(n>=s){n===s&&o.merge.add(n);return}const i=Math.floor((n+s)/2);await h(t,n,i),await h(t,i+1,s),await b(t,n,i,s);for(let e=n;e<=s;e++)o.merge.add(e);e({merge:{}})}async function y(e,t,n){const s=Math.floor((t+n)/2),o=\[{value:e\[t\],index:t},{value:e\[s\],index:s},{value:e\[n\],index:n}\];return o.sort((e,t)=>e.value-t.value),o\[1\].index}async function \_(t,o,i){let c;const l=m.value;l==="first"?c=o:l==="random"?c=o+Math.floor(Math.random()\*(i-o+1)):l==="median"?c=await y(t,o,i):c=i,\[t\[c\],t\[i\]\]=\[t\[i\],t\[c\]\];let r=i;const d=t\[r\];e({quick:{pivot:r,comparing:\[o,i\]}}),await n(s);let a=o-1;for(let c=o;c<i;c++)e({quick:{pivot:r,comparing:\[c,a+1\]}}),await n(s),t\[c\]<d&&(a++,a!==c&&(\[t\[a\],t\[c\]\]=\[t\[c\],t\[a\]\],e({quick:{pivot:r,swapping:\[a,c\]}}),await n(s)));return a+1!==r&&(\[t\[a+1\],t\[r\]\]=\[t\[r\],t\[a+1\]\],e({quick:{swapping:\[a+1,r\]}}),await n(s)),a+1}async function u(t,n,s){if(n<s){const e=await \_(t,n,s);await u(t,n,e-1),await u(t,e+1,s),o.quick.add(e)}else n===s&&o.quick.add(n);e({quick:{}})}async function O(){if(r)return;r=!0,i.disabled=!0,i.style.cursor="not-allowed",i.style.opacity="0.7",f.disabled=!0,m.disabled=!0,d(),console.log("Starting all sorts concurrently..."),await Promise.all(\[v(),g(),h(t.merge,0,t.merge.length-1),u(t.quick,0,t.quick.length-1)\]),console.log("All sorts finished."),r=!1,i.disabled=!1,i.style.cursor="pointer",i.style.opacity="1",f.disabled=!1,m.disabled=!1}i.addEventListener("click",O),f.addEventListener("click",()=>{r||d()}),d(),window.addEventListener("resize",()=>{r||e()})})()

Le Java utilise généralement Timsort. Timsort est un algorithme de tri hybride, conçu par Tim Peters. Il combine le tri par insertion et le tri fusion pour optimiser les performances sur des données réelles, en exploitant les séquences déjà triées, appelées _runs_. L’algorithme commence par diviser le tableau en petits _runs_, soit naturels (séquences croissantes ou décroissantes), soit créés en triant des blocs de taille minimale (souvent 32 éléments) avec le tri par insertion. Ces _runs_ sont ensuite fusionnés deux à deux à l’aide d’une version optimisée du tri fusion, qui minimise les comparaisons et les copies. Sa complexité est en \\( O(n \\log n) \\) dans le pire cas, mais elle peut descendre à \\( O(n) \\) pour des données presque triées, rendant Timsort particulièrement efficace en pratique. De plus, Timsort est stable, préservant l’ordre relatif des éléments égaux, ce qui est crucial dans certaines applications.

Dans certains cas spécialisés, nous utilisons l’algorithme de tri par niches, également connu sous le nom de _pigeonhole sort_, est un algorithme de tri non comparatif adapté aux ensembles de données où les éléments appartiennent à un ensemble fini de valeurs entières, comme des nombres dans une plage limitée. Il repose sur le principe des “niches” (ou pigeonholes) : chaque valeur possible est associée à une niche, et les éléments sont placés dans la niche correspondant à leur valeur. Ensuite, les niches sont parcourues dans l’ordre pour reconstruire le tableau trié. Sa complexité est en \\( O(n + k) \\), où \\( n \\) est le nombre d’éléments et \\( k \\) la taille de la plage de valeurs. Cet algorithme est très efficace lorsque \\( k \\) est proche de \\( n \\), mais il nécessite un espace auxiliaire proportionnel à \\( k \\) et n’est pas adapté aux données non entières ou à des plages de valeurs très grandes.

    FONCTION triParNiches(tableau, min, max)
        k ← max - min + 1  // Taille de la plage de valeurs
        niches ← tableau de taille k, initialisé à vide
    
        // Étape 1 : placer les éléments dans les niches
        POUR chaque élément dans tableau
            index ← élément - min
            ajouter élément à niches[index]
        FIN POUR
    
        // Étape 2 : reconstruire le tableau trié
        index ← 0
        POUR i de 0 à k-1
            TANT QUE niches[i] n’est pas vide
                tableau[index] ← premier élément de niches[i]
                retirer premier élément de niches[i]
                index ← index + 1
            FIN TANT QUE
        FIN POUR
    
        retourner tableau
    FIN FONCTION
    

Le tri par niches (ou bucket sort) est un algorithme de tri non comparatif adapté aux données uniformément réparties dans une plage de valeurs connue (de min à max). Le pseudocode décrit un processus en deux étapes. D’abord, il calcule la taille de la plage (k ← max - min + 1) et crée un tableau niches de taille k, où chaque niche correspond à une valeur possible. Dans l’étape 1, chaque élément du tableau est placé dans la niche correspondante (index ← élément - min), ce qui regroupe les éléments de même valeur. Dans l’étape 2, le tableau est reconstruit en parcourant les niches dans l’ordre (de 0 à k-1) et en extrayant leurs éléments pour les placer séquentiellement dans le tableau (tableau\[index\]). L’indice index suit la position d’insertion.

#### Vidéo suggérée [#](#vid%c3%a9o-sugg%c3%a9r%c3%a9e)

### Table de hachage [#](#table-de-hachage)

Une table de hachage (ou « hash table ») est une structure de données qui permet d’associer des clés à des valeurs et d’accéder très rapidement à une valeur à partir de sa clé. Le principe repose sur l’utilisation d’une fonction de hachage qui transforme la clé (par exemple, un texte ou un nombre) en un indice de tableau. Les opérations d’insertion, de recherche et de suppression se font en temps moyen \\( O(1) \\), c’est-à-dire en temps constant, quelle que soit la taille de la table (si la fonction de hachage est bonne et la table bien dimensionnée). La table de hachage est efficace pour retrouver rapidement une information à partir d’une clé.

Idée générale :

1.  On applique une fonction de hachage à la clé pour obtenir un indice.
2.  On stocke la valeur à cet indice dans un tableau.
3.  En cas de « collision » (deux clés différentes qui donnent le même indice), on utilise une technique de résolution (chaînage, sondage linéaire, etc.).

Pseudocode d’une recherche dans une table de hachage (sans collision):

    FONCTION rechercher(table, clé)
        indice ← hachage(clé)
        SI table[indice] == clé ALORS
            retourner VRAI
        SINON
            retourner FAUX
        FIN SI
    FIN FONCTION
    

Le pseudocode décrit une fonction de recherche dans une table de hachage, une structure de données optimisée pour retrouver rapidement un élément. La fonction rechercher prend une table (tableau représentant la table de hachage) et une clé à chercher (clé). Elle commence par calculer l’indice correspondant à la clé via une fonction de hachage (indice ← hachage(clé)), qui mappe la clé à une position dans la table. Ensuite, elle vérifie si l’élément à cet indice (`table[indice]`) est égal à la clé recherchée. Si c’est le cas, la fonction retourne VRAI, indiquant que la clé est présente. Sinon, elle retourne FAUX, signifiant que la clé est absente. Ce pseudocode suppose une table de hachage simple sans gestion des collisions (cas où plusieurs clés pointent vers le même indice), ce qui la rend efficace mais limitée aux cas où chaque indice contient au plus un élément.

Pour mieux comprendre, testez l’application suivante. Saisissez des chaînes de caractères qui seront ajoutées à la table de hachage. Pouvez-vous créer une collision ?

 Ajouter

Chaînes saisies
---------------

Chaîne

Valeur de hachage

Position dans la table

Table de hachage
----------------

(function(){const e="hashApp\_",n=10,t={hashTable:Array(n).fill().map(()=>\[\]),strings:\[\]};function o(t){try{let e=0;for(let n of t)e+=n.charCodeAt(0);const s=e%n;return{hashValue:e,index:s}}catch(t){return console.error(\`${e}Erreur dans hashFunction:\`,t),null}}function i(){try{const i=document.getElementById(\`${e}stringInput\`),n=i.value.trim();if(!n)return;const r=o(n);if(!r)return;const{hashValue:l,index:c}=r;t.strings.push({str:n,hashValue:l,index:c}),t.hashTable\[c\].push(n),a(),s(),i.value=""}catch(t){console.error(\`${e}Erreur dans addString:\`,t)}}function a(){try{const n=document.getElementById(\`${e}stringTableBody\`);n.innerHTML="",t.strings.forEach(({str:e,hashValue:t,index:s})=>{const o=document.createElement("tr");o.innerHTML=\` <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">${e}</td> <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">${t}</td> <td style="border: 1px solid #ddd; padding: 8px; text-align: left;">${s}</td> \`,n.appendChild(o)})}catch(t){console.error(\`${e}Erreur dans updateStringTable:\`,t)}}function s(){try{const s=document.getElementById(\`${e}hashTableDisplay\`);s.innerHTML="";for(let e=0;e<n;e++){const o=document.createElement("div");o.style.cssText="padding: 10px; border: 1px solid #ccc; background-color: #f9f9f9;",o.innerHTML=\`<h3 style="margin: 0; font-size: 16px;">Index ${e}</h3><p>${t.hashTable\[e\].length>0?t.hashTable\[e\].join(", "):"Vide"}</p>\`,s.appendChild(o)}}catch(t){console.error(\`${e}Erreur dans updateHashTableDisplay:\`,t)}}function r(){try{const t=document.getElementById(\`${e}addButton\`);t&&t.addEventListener("click",i),s()}catch(t){console.error(\`${e}Erreur dans init:\`,t)}}r()})().hash-app-container{contain:content;padding:20px;max-width:800px;margin:0 auto}

En Java, la classe `HashMap` que nous verrons plus loin dans le cours implémente une table de hachage. Par exemple :

    import java.util.HashMap;
    
    HashMap<String, Integer> dico = new HashMap<>();
    dico.put("chat", 1);
    dico.put("chien", 2);
    System.out.println(dico.get("chat")); // Affiche 1
    

Ce code Java utilise une HashMap pour créer une structure de données associant des clés à des valeurs. Une instance `HashMap<String, Integer>` est déclarée, avec des clés de type String et des valeurs de type Integer. Deux paires clé-valeur sont ajoutées via la méthode put : “chat” associé à 1 et “chien” à 2. La méthode get(“chat”) récupère la valeur liée à la clé “chat”, soit 1, qui est ensuite affichée avec System.out.println.

Les tables de hachage sont omniprésentes en informatique car elles rendent possible la recherche rapide dans de grands ensembles de données.

Imaginons que l’on souhaite stocker un ensemble de chaînes de caractères de différentes longueurs, par exemple « chat », « chien », « girafe », « lion ». Pour retrouver rapidement une chaîne, on peut utiliser une table de hachage où la fonction de hachage choisie est simplement la longueur de la chaîne. Ainsi, « chat » (4 lettres) sera stocké à l’indice 4, « chien » (5 lettres) à l’indice 5, « girafe » (6 lettres) à l’indice 6, et ainsi de suite. Pour rechercher une chaîne, il suffit de calculer sa longueur et d’aller directement à l’indice correspondant dans le tableau. Cette opération ne dépend pas du nombre total de chaînes stockées, ce qui explique pourquoi la recherche est dite « en temps constant » : on ne parcourt pas toute la table, on accède directement à la bonne case.

Cependant, ce choix de fonction de hachage est très simple et peut provoquer des « collisions » : deux chaînes de même longueur, comme « lion » et « chat », auraient le même indice. Dans ce cas, il faut une méthode pour gérer ces collisions, par exemple en stockant les deux chaînes dans une liste à cet indice. En pratique, les tables de hachage utilisent des fonctions de hachage beaucoup plus sophistiquées, capables de transformer n’importe quelle clé (texte, nombre, etc.) en un indice réparti de façon plus uniforme dans le tableau. L’objectif reste toujours de minimiser les collisions, car tant qu’il y en a peu, la recherche, l’insertion et la suppression restent très rapides et efficaces, même avec de très grands ensembles de données.

#### Vidéo suggérée [#](#vid%c3%a9o-sugg%c3%a9r%c3%a9e-1)

### Un problème résoluble en \\( O(n^2) \\) ou en \\( O(n) \\) [#](#un-probl%c3%a8me-r%c3%a9soluble-en--ou-en)

Prenons le problème suivant : « Trouver s’il existe deux éléments dans un tableau qui, additionnés, donnent une valeur cible. »

Solution naïve (\\( O(n^2) \\)) :

    POUR i de 0 à n-1
        POUR j de i+1 à n-1
            SI tableau[i] + tableau[j] == cible
                retourner VRAI
            FIN SI
        FIN POUR
    FIN POUR
    retourner FAUX
    

La boucle externe (POUR i de 0 à n-1) parcourt chaque élément du tableau, tandis que la boucle interne (POUR j de i+1 à n-1) examine tous les éléments suivants (à partir de i+1) pour éviter de considérer le même élément deux fois ou des paires redondantes. À chaque itération, la condition SI `tableau[i] + tableau[j] == cible` teste si la somme des éléments aux indices i et j égale la valeur cible. Si une telle paire est trouvée, la fonction retourne VRAI, indiquant que la solution existe. Si aucune paire ne satisfait la condition après avoir exploré toutes les combinaisons, la fonction retourne FAUX.

Ici, on teste toutes les paires possibles, ce qui prend un temps quadratique.

Solution optimisée (\\( O(n) \\)) :

On peut résoudre ce problème en temps linéaire en utilisant une structure de données comme un ensemble (set) :

    initialiser un ensemble vide
    POUR chaque élément x du tableau
        SI (cible - x) est dans l’ensemble
            retourner VRAI
        AJOUTER x à l’ensemble
    FIN POUR
    retourner FAUX
    

Initialement, un ensemble vide est créé pour stocker les éléments rencontrés. La boucle (POUR chaque élément x du tableau) parcourt chaque élément x du tableau. Pour chaque x, l’algorithme vérifie si cible - x (la valeur nécessaire pour atteindre la somme cible) est déjà dans l’ensemble. Si c’est le cas, une paire d’éléments dont la somme vaut cible a été trouvée, et la fonction retourne VRAI. Sinon, l’élément x est ajouté à l’ensemble pour être utilisé dans les itérations suivantes. Si la boucle se termine sans trouver une telle paire, la fonction retourne FAUX.

Ici, chaque élément est traité une seule fois, et si la recherche dans l’ensemble se fait en temps constant (en moyenne) ou \\( O(1) \\), la solution est en \\( O(n) \\). Dans la solution optimisée, la vérification « (cible - x) est dans l’ensemble » est cruciale. Il n’est pas garanti que la recherche se fasse en temps \\( O(1) \\), mais c’est possible avec une table de hachage.

### Les arbres en informatique [#](#les-arbres-en-informatique)

Les arbres sont des structures de données hiérarchiques non linéaires, composées de nœuds reliés par des arêtes. Un arbre possède une racine unique, à partir de laquelle descendent des sous-arbres. Chaque nœud peut avoir zéro ou plusieurs enfants, mais un seul parent (sauf la racine). À partir du sommet, nous progressons vers les feuilles qui où se terminent la progression. Les arbres permettent de représenter des relations hiérarchiques naturelles, comme des dossiers dans un système de fichiers, des expressions arithmétiques ou des structures organisationnelles.

Parmi les arbres les plus utilisés figure l’arbre binaire, où chaque nœud a au plus deux enfants (gauche et droit). L’arbre binaire de recherche (ABR) est une variante particulièrement utile : pour tout nœud, les valeurs dans le sous-arbre gauche sont inférieures à celle du nœud, et celles dans le sous-arbre droit sont supérieures. Cela permet des opérations de recherche, insertion et suppression efficaces dans un arbre équilibré.

    fonction rechercher(racine, valeur_cible)
        courant ← racine
        tant que courant n'est pas null
            si valeur_cible = courant.valeur
                retourner courant
            fin si
            
            si valeur_cible < courant.valeur
                courant ← courant.gauche
            sinon
                courant ← courant.droit
            fin si
        fin tant que
        
        retourner null  // valeur non trouvée
    fin fonction
    

Pour mieux comprendre le fonctionnement d’un arbre de recherche binaire, utilisez l’application suivante.

 Insérer Rechercher Supprimer Effacer

class Node{constructor(e){this.value=e,this.left=null,this.right=null,this.x=400,this.y=50}}let root=null;const canvas=document.getElementById("canvas"),ctx=canvas.getContext("2d"),nodeRadius=20;let animating=!1;function buildBalanced(e,t,n){if(t>n)return null;let s=Math.floor((t+n)/2),o=new Node(e\[s\]);return o.left=buildBalanced(e,t,s-1),o.right=buildBalanced(e,s+1,n),o}let values=\[10,20,30,40,50,55,70,80\].sort((e,t)=>e-t);root=buildBalanced(values,0,values.length-1);function drawTree(){ctx.clearRect(0,0,canvas.width,canvas.height),root&&drawNode(root,canvas.width/2,50,canvas.width/4)}function drawNode(e,t,n,s){if(!e)return;e.x=t,e.y=n,e.left&&(ctx.beginPath(),ctx.moveTo(t,n),ctx.lineTo(t-s,n+80),ctx.stroke()),e.right&&(ctx.beginPath(),ctx.moveTo(t,n),ctx.lineTo(t+s,n+80),ctx.stroke()),ctx.fillStyle="#f0f0f0",ctx.beginPath(),ctx.arc(t,n,nodeRadius,0,Math.PI\*2),ctx.fill(),ctx.strokeStyle="#000",ctx.stroke(),ctx.fillStyle="#000",ctx.font="14px sans-serif",ctx.textAlign="center",ctx.textBaseline="middle",ctx.fillText(e.value,t,n),drawNode(e.left,t-s,n+80,s/2),drawNode(e.right,t+s,n+80,s/2)}async function insert(e){if(animating)return;if(animating=!0,e=parseInt(e),isNaN(e)){animating=!1;return}if(!root){root=new Node(e),drawTree(),animating=!1;return}let t=root;for(;!0;)if(ctx.fillStyle="rgba(0, 255, 0, 0.3)",ctx.beginPath(),ctx.arc(t.x,t.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),drawTree(),e<t.value){if(!t.left){t.left=new Node(e),drawTree();break}t=t.left}else if(e>t.value){if(!t.right){t.right=new Node(e),drawTree();break}t=t.right}else break;animating=!1}async function search(e){if(animating||!root)return;animating=!0,e=parseInt(e);let t=root,n=!1;for(;t;){if(drawTree(),ctx.fillStyle="rgba(255, 255, 0, 0.4)",ctx.beginPath(),ctx.arc(t.x,t.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),await sleep(800),e===t.value){n=!0,ctx.fillStyle="rgba(0, 255, 0, 0.5)",ctx.beginPath(),ctx.arc(t.x,t.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),await sleep(1e3),drawTree();break}t=e<t.value?t.left:t.right}n||(alert("Valeur non trouvée"),drawTree()),animating=!1}async function remove(e){if(animating||!root)return;animating=!0,root=await removeNode(root,parseInt(e)),drawTree(),animating=!1}async function removeNode(e,t){if(!e)return null;if(ctx.fillStyle="rgba(255, 255, 0, 0.4)",ctx.beginPath(),ctx.arc(e.x,e.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),drawTree(),t<e.value)e.left=await removeNode(e.left,t);else if(t>e.value)e.right=await removeNode(e.right,t);else{if(ctx.fillStyle="rgba(255, 0, 0, 0.5)",ctx.beginPath(),ctx.arc(e.x,e.y,nodeRadius+5,0,Math.PI\*2),ctx.fill(),drawTree(),!e.left)return e.right;if(!e.right)return e.left;let t=e.right;for(;t.left;)t=t.left;e.value=t.value,e.right=await removeNode(e.right,t.value)}return e}function sleep(e){return new Promise(t=>setTimeout(t,e))}function insertValue(){const e=document.getElementById("value").value;insert(e)}function searchValue(){const e=document.getElementById("value").value;search(e)}function deleteValue(){const e=document.getElementById("value").value;remove(e)}function clearTree(){root=null,drawTree()}drawTree()

Nous souhaitons garder la distance entre le sommet et les feuilles aussi petite que possible. Cette distance détermine notre complexité de recherche. L’arbre rouge-noir (red-black tree) est une des arbres les plus populaires, utilisée notamment dans les implémentations de Map et Set en Java (TreeMap, TreeSet). Chaque nœud est coloré en rouge ou noir, et l’arbre respecte cinq propriétés strictes : la racine est noire, chaque feuille (nil) est noire, un nœud rouge a des enfants noirs, tout chemin d’un nœud à une feuille contient le même nombre de nœuds noirs, et aucun chemin ne contient deux rouges consécutifs. Ces règles assurent que l’arbre reste approximativement équilibré, avec une hauteur maximale d’environ \\( 2 \\log n \\). Lors d’insertions ou suppressions, des violations de couleur peuvent survenir ; elles sont corrigées par des opérations locales qui maintiennent l’équilibre. Les arbres rouge-noir offrent des performances garanties. Les opérations de recherche, insertion et suppression s’exécutent en \\( O(\\log n) \\) dans le pire cas, où \\( n \\) est le nombre de nœuds. Dans ce cours, il n’est pas nécessaire de concevoir des structures en arbres.

#### Vidéo suggérée [#](#vid%c3%a9o-sugg%c3%a9r%c3%a9e-2)

Analyse amortie [#](#analyse-amortie)
-------------------------------------

L’analyse amortie est une méthode utilisée pour évaluer la complexité moyenne d’une séquence d’opérations sur une structure de données, même si certaines opérations individuelles peuvent être coûteuses. Plutôt que de se concentrer sur le pire cas d’une seule opération, l’analyse amortie considère le coût total de nombreuses opérations et le répartit uniformément, offrant ainsi une vision plus réaliste de la performance globale. Le tri rapide (quick sort) est un algorithme qui a techniquement une complexité \\( O(n^2) \\), mais qui a une complexité amortie de \\( O(n \\log n) \\). En d’autres termes, le tri rapide est généralement rapide, mais il existe des cas rares où il est lent.

Vidéo optionnelle [#](#vid%c3%a9o-optionnelle)
----------------------------------------------

 [![Previous](/inf1220-hugo/svg/backward.svg "Les problèmes difficiles") Les problèmes difficiles](/inf1220-hugo/docs/modules/module1/difficile/) [Les erreurs communes ![Next](/inf1220-hugo/svg/forward.svg "Les erreurs communes")](/inf1220-hugo/docs/modules/module1/erreurs/) 


*   *   [Notation grand-O](#notation-grand-o)
    *   [Notation grand-O](#notation-grand-o-1)
    *   [Exemples d’algorithmes en](#exemples-dalgorithmes-en)
    *   [Exemples d’algorithmes en](#exemples-dalgorithmes-en-1)
    *   [Recherche dans un tableau trié](#recherche-dans-un-tableau-trié)
    *   [Tri](#tri)
    *   [Table de hachage](#table-de-hachage)
    *   [Un problème résoluble en ou en](#un-problème-résoluble-en--ou-en)
    *   [Les arbres en informatique](#les-arbres-en-informatique)
*   [Analyse amortie](#analyse-amortie)
*   [Vidéo optionnelle](#vidéo-optionnelle)

## Les erreurs communes


Erreurs communes [#](#erreurs-communes)
=======================================

Rédiger du pseudo-code n’a rien de sorcier, mais plusieurs étudiants font des erreurs. Voici quelques erreurs communes.

1.  Certains étudiants rédigent du pseudo-code qui a l’air formel et correct, mais qui est en fait ambigu et inutilisable. Prenons cet exemple: `SI j'ai mal aux dos ALORS je prend des aspirines OU SI j'ai faim ALORS je mange`. Bien sûr, je n’ai utilisé que des expressions logiques. Des SI, des ALORS des OU. Mais qu’est-ce que ça signifie ? Par exemple, est-ce que je peux à la fois manger et prendre des aspirines dans ce scénario ? La réponse est subjective. Votre pseudo-code doit être exécutable sans interprétation. Un pseudo-code n’est pas un texte à interprétation subjective. Vous ne pouvez pas faire semblant d’écrire du pseudo-code en utilisant simplement les termes qu’on trouve fréquemment au sein des pseudo-codes. Ce n’est pas une question de syntaxe. On peut parfaitement écrire du pseudo-code sans jamais utiliser SI, TANT QUE, etc. Plusieurs étudiants obsèdent sur la syntaxe, croyant à tort que si on leur donne les bons termes, la bonne grammaire, ils trouveront comment comprendre ce qu’est un pseudo-code. Or, c’est justement le contraire de la leçon ici: nous voulons que vous compreniez que la syntaxe exacte est secondaire dans la pensée algorithmique. On peut être imprécis et incohérent en utilisant une syntaxe formelle, et on peut être précis et cohérent en utilisant du français usuel. Ce n’est pas parce que vous utilisez des expressions qui vous semblent précises que vous l’êtes. Vous devez avoir une idée précise en tête et vous devez l’exprimer avec précision.
    
2.  Au sein d’une boucle (par ex., TANT QUE), les étudiants peuvent mettre par erreur une condition qui termine toujours le programme. Dans un tel cas, la boucle ne peut pas s’exécuter et elle est de facto brisée. Voici un exemple. Les instructions « retourner minimum » et « retourner tableau\[iterateur\] » terminent le pseudo-code. Assurez-vous de bien comprendre que ce pseudo-code ne va consulter que la première valeur du tableau. Si vous avez une condition ou les deux branches (SI et SINON) retournent une valeur et terminent donc l’algorithme, votre algorithme ne procèdera pas plus loin.
    

    Variable iterateur (entier)
    
    Variable minimum  = tableau[0] 
    
    iterateur = 0
    TANT QUE  iterateur < 100  FAIRE
         SI tableau[iterateur] < minimum ALORS
             retourner tableau[iterateur];
         SINON
             retourner minimum
         FIN SI
         iterateur = iterateur + 1;
    FIN TANT QUE
    

3.  Certains étudiants construisent des boucles qui ne se terminent jamais. Dans une boucle TANT QUE, il faut s’assurer que la condition ne soit plus satisfaite pour ne pas avoir une boucle infinie. Consultez cet exemple. Si vous testez votre pseudo-code, vous saurez éviter de telles erreurs.

    iterateur = 0
    TANT QUE  iterateur < 100  FAIRE
         SI iterateur < 10 ALORS
             ajouter un à itérateur
         FIN SI
    FIN TANT QUE
    

4.  Les étudiants vont aussi fréquemment utiliser des variables et des constructions qui ne sont pas définies et dont le sens doit être deviné. Voici un exemple. Vous constaterez à la lecture de ce pseudo-code qu’il y a plusieurs conventions syntaxiques qui ne sont pas définies. Il y a plusieurs variables, mais il est difficile de connaître leur type et leurs relations. Assurez-vous donc de bien expliquer chaque variable et de bien définir votre syntaxe. Dans ce dernier exemple, que représente iterateur, iterateur\[tableau\], tableau\[iterateur\], etc.? Vous devez être précis. Souvent, nous avons un nombre limité de « types » pour les variables: nombres, entiers, chaînes de caractères. On utilise le plus souvent la convention t\[i\] pour désigner l’élément à l’index i du tableau t. Dans un tel cas, t doit être un tableau, i doit être une valeur entière. Vous être libre de concevoir vos propres conventions, mais vous devez être explicite et précis. Si votre pseudo-code doit retourner une valeur, il faut que le pseudo-code le spécifie explicitement.

    Entier iterateur[tableau] = 0;
    TANT QUE  iterateur[i] < 100  FAIRE
         SI tableau[iterateur] < minimum ALORS
             retourner iterateur[tableau];
         FIN SI
         iterateur = iterateur[tableau] + 1;
    FIN POUR TOUT
    

5.  Si vous avez bien défini le type de vos variables, et toutes vos conventions syntaxiques, il vous reste maintenant à vous assurer que les valeurs de vos variables sont toujours spécifiées. Si vous dites que x est un nombre et que vous posez ensuite l’inéquation x > 1, nous ne pouvons en connaître la valeur que si x a reçu une valeur. Assurez-vous donc de donner une valeur initiale à toutes vos variables. En tout temps, dans votre pseudo-code, le lecteur doit pouvoir déterminer la valeur d’une variable donnée.
    
6.  Parfois les étudiants manquent tout simplement de rigueur. Pour vérifiez si votre pseudo-code est rigoureux, appliquez-le sur un exemple concret comme si vous étiez un robot. Par exemple, si quelqu’un écrit le pseudo-code suivant « je prend chacune des valeurs du tableau, et je l’additionne à la valeur suivante dans le tableau »… vous pourriez alors prendre un tableau à titre d’exemple, comme \[1,2,3\] et tester l’instruction. Qu’est-ce que ça donnerait ? Je prend les valeurs une à une et je l’additionne à la valeur suivante dans le tableau. Je prend donc 1 et sa valeur suivante (1 + 2), ensuite 2 et sa valeur suivante (2 + 3), et ensuite 3 et sa valeur suivante… ? Je me rend compte que l’expression « la valeur suivante » n’est pas bien définie. Voici un autre exemple. Quelqu’un pourrait avoir comme pseudo-code « j’initialise la variable comme ayant comme valeur le premier élément du tableau ». Testons ce pseudo-code sur le tableau vide (de taille zéro). Nous constatons qu’il n’y a pas de premier élément ! Donc si le tableau vide n’est pas exclu, nous avons un problème de rigueur. Voici un truc: testez toujours votre pseudo-code avec plusieurs exemples concrets. Prenez le temps d’appliquer les instructions de votre pseudo-code ligne par ligne, comme si vous étiez un robot. Pensez comme un ordinateur!
    

Nous vous invitons maintenant à passez aux premiers exercices du cours!

 [![Previous](/inf1220-hugo/svg/backward.svg "Complexité algorithmique") Complexité algorithmique](/inf1220-hugo/docs/modules/module1/complex/) [Présentation du pseudocode ![Next](/inf1220-hugo/svg/forward.svg "Présentation du pseudocode")](/inf1220-hugo/docs/modules/module1/syntaxe/)

## Présentation du pseudocode


*   [Indentation](#indentation)
*   [Terminologie](#terminologie)
*   [Commentaires](#commentaires)
*   [Typographie](#typographie)

Guide pour présenter du pseudocode [#](#guide-pour-pr%c3%a9senter-du-pseudocode)
================================================================================

Adoptez un style simple. Testez la lisibilité de votre pseudocode en le lisant à haute voix.

Voici un exemple de pseudocode difficile à comprendre.

    entrée : un nombre
    si mon nombre nombre > 0 alors "positif"
         autrement
        afficher "négatif ou zéro"
    fin du code
    

Voici un bon exemple.

    entrée : nombre
    si nombre > 0 alors
        afficher "positif"
    sinon
        afficher "négatif ou zéro"
    fin si
    

Indentation [#](#indentation)
-----------------------------

L’indentation est utile pour montrer la structure hiérarchique (boucles, conditions, blocs). Utilisez systématiquement 2 à 4 espaces par niveau, vous pouvez aussi utiliser des tabulations. Ne mélangez pas espaces et tabulations. Indentez chaque bloc intérieur d’un niveau supplémentaire. Alignez les instructions de fin de bloc (comme “fin si” ou “fin pour”) avec le début du bloc. Conservez une indentation cohérente dans tout le document.

    pour i de 1 à 10 faire
        si i mod 2 = 0 alors
            afficher i + " est pair"
        fin si
    fin pour
    

Terminologie [#](#terminologie)
-------------------------------

Employez des termes en français ou en anglais courants, mais ne mélangez pas les langues. Utilisez des mots-clés simples et clairs :

*   entrée, sortie
*   si … alors … sinon … fin si
*   pour … faire … fin pour
*   tant que … faire … fin tant que
*   fonction … retour … fin fonction

Évitez les abréviations obscures.

Commentaires [#](#commentaires)
-------------------------------

Insérez des commentaires avec un préfixe comme “//” ou “#” pour expliquer les parties complexes. Numérotez les lignes seulement pour des algorithmes longs ou des références.

Exemple :

    fonction factorielle(n)  // Calcule n!
        si n <= 1 alors
            retour 1
        sinon
            retour n * factorielle(n-1)
        fin si
    fin fonction
    

Typographie [#](#typographie)
-----------------------------

Utilisez une police à espacement fixe (comme Courier) dans les documents. Évitez les lignes trop longues. Séparez les sections logiques par des lignes vides.

    entrée : nombre
    si nombre > 0 alors
        afficher "positif"
    sinon
        afficher "négatif ou zéro"
    fin si
    
    si nombre > 10 alors
        afficher "nombre plus grand que dix"
    fin si
    

 [![Previous](/inf1220-hugo/svg/backward.svg "Les erreurs communes") Les erreurs communes](/inf1220-hugo/docs/modules/module1/erreurs/) [Exercices sur les algorithmes ![Next](/inf1220-hugo/svg/forward.svg "Exercices sur les algorithmes")](/inf1220-hugo/docs/modules/module1/exercices/) 


*   [Indentation](#indentation)
*   [Terminologie](#terminologie)
*   [Commentaires](#commentaires)
*   [Typographie](#typographie)

## Exercices sur les algorithmes


*   *   [Réponses uniques ?](#réponses-uniques-)
    *   [Logiciels](#logiciels)
    *   [Exercice 1 : La somme d’un tableau](#exercice-1--la-somme-dun-tableau)
    *   [Exercice 2 : La recherche d’un entier](#exercice-2--la-recherche-dun-entier)
    *   [Exercice 3 : Somme des multiples de 3 ou 5](#exercice-3--somme-des-multiples-de-3-ou-5)
    *   [Exercice 4 : Plus grand diviseur premier](#exercice-4--plus-grand-diviseur-premier)
    *   [Exercice 5 : Chiffre des dizaines](#exercice-5--chiffre-des-dizaines)
    *   [Exercice 6 : Erreur dans un pseudo-code](#exercice-6--erreur-dans-un-pseudo-code)
    *   [Exercice 7 : Racines d’un polynôme du second degré](#exercice-7--racines-dun-polynôme-du-second-degré)
    *   [Exercice 8 : Exécution de l’algorithme des racines](#exercice-8--exécution-de-lalgorithme-des-racines)
    *   [Exercice 9 : Conversion de base](#exercice-9--conversion-de-base)
    *   [Exercice 10 : Tester la parité en base 2](#exercice-10--tester-la-parité-en-base-2)
    *   [Exercice 11 : Calcul de la factorielle](#exercice-11--calcul-de-la-factorielle)
    *   [Exercice 12 : Inverser un tableau](#exercice-12--inverser-un-tableau)
    *   [Exercice 13 : Compter les voyelles](#exercice-13--compter-les-voyelles)
    *   [Exercice 14 : Tester si un entier est un palindrome](#exercice-14--tester-si-un-entier-est-un-palindrome)
    *   [Exercice 15 : Minimum et maximum d’un tableau](#exercice-15--minimum-et-maximum-dun-tableau)
    *   [Exercice 16 : Recherche dans un tableau](#exercice-16--recherche-dans-un-tableau)
    *   [Exercice 17 : Recherche binaire](#exercice-17--recherche-binaire)
    *   [Exercice 18 : Algorithme quadratique](#exercice-18--algorithme-quadratique)
    *   [Exercice 19 : Algorithme de tri efficace](#exercice-19--algorithme-de-tri-efficace)
    *   [Exercice 20 : Alan Kay](#exercice-20--alan-kay)
    *   [Exercice 21 : Dahl et Nygaard](#exercice-21--dahl-et-nygaard)
    *   [Exercice 22 : James Gosling](#exercice-22--james-gosling)
    *   [Exercice 23 : domaines industriels](#exercice-23--domaines-industriels)
    *   [Exercice 24 : Backus-Naur](#exercice-24--backus-naur)
    *   [Exercice 25 : Cycles](#exercice-25--cycles)
    *   [Exercice 26 : kibioctet](#exercice-26--kibioctet)
    *   [Exercice 27 : doublons](#exercice-27--doublons)
    *   [Exercice 28 : puissance](#exercice-28--puissance)
    *   [Exercice 29 : occurrences d’un caractère spécifique](#exercice-29--occurrences-dun-caractère-spécifique)
    *   [Exercice 30 : recherche d’une clé](#exercice-30--recherche-dune-clé)
    *   [Vidéos suggérées](#vidéos-suggérées)

Exercices sur les algorithmes et problèmes [#](#exercices-sur-les-algorithmes-et-probl%c3%a8mes)
================================================================================================

La notion d’algorithme a été abordée implicitement dès les premiers cours de mathématiques, par exemple avec l’algorithme de la division longue. Ces exercices visent à vous faire décrire formellement un algorithme. La principale difficulté pour la plupart des étudiants réside dans la rigueur et la précision requises. Au-delà d’un certain point, il n’existe pas de lectures supplémentaires : la pratique est essentielle.

> Pour les mathématiques, vous pouvez faire référence à notre rappel sur [les principales notions mathématiques](https://lemire.github.io/inf1220-hugo/docs/extra/math/) du cours.

Il est permis d’utiliser le robot conversationnel du cours pour ces exercices ([voir ici](https://rc-inf1220.teluq.ca/)). Toutefois, entraînez-vous à produire vos propres réponses.

Comment procéder pour les exercices :

1.  Lisez attentivement la question.
2.  Cherchez une solution. Si vous ne trouvez pas immédiatement, consacrez 10 à 15 minutes à y réfléchir. Si le problème exact vous résiste, tentez une solution partielle. Pour cet exercice, vous devez produire du pseudo-code, et non du Java.
3.  Rédigez votre solution avec précision, comme une suite de consignes qu’un enfant pourrait suivre.
4.  Exécutez votre pseudo-code.
5.  Consultez ensuite la ou les solutions proposées.
6.  Assurez-vous de comprendre toutes les solutions. Posez des questions si nécessaire, en fournissant votre propre solution pour appuyer vos interrogations. Comprendre les solutions proposées est impératif.

Ces exercices sont obligatoires et ne doivent pas être survolés ou omis.

Pour lire les formules mathématiques sur le site du cours, utilisez un navigateur compatible avec MathML, comme Chrome, Edge, Firefox ou Safari.

Ces exercices sont conçus pour l’autoévaluation ; ils ne sont pas corrigés. Nous répondons cependant à vos questions sur la matière.

Les solutions à ces exercices ne sont pas uniques. Il existe plusieurs syntaxes possibles pour décrire un algorithme en pseudo-code. Cela ne signifie pas que toutes les solutions sont correctes. Un pseudo-code peut être erroné s’il ne décrit pas une solution logiquement correcte ou s’il manque de précision pour être considéré comme un algorithme. Un pseudo-code doit pouvoir être exécuté littéralement par un humain sans jugement, comme un automate.

Rappel : les mathématiques du collégial sont un préalable obligatoire à ce cours. Une aisance en algèbre, fonctions et arithmétique est nécessaire. Sans ces prérequis, réussir ce cours peut être difficile.

> ### Réponses uniques ? [#](#r%c3%a9ponses-uniques-)
> 
> Les exercices incluent une solution pour comparer votre approche à la nôtre. Il n’existe pas de solution unique ; votre solution peut être meilleure ou moins bonne que celle proposée.

### Logiciels [#](#logiciels)

Certains étudiants utilisent des logiciels comme [AlgoBox](https://www.xm1math.net/algobox/) ou [PseudoFlow](https://online.pseudoflow.app). Cela n’est pas nécessaire, car le pseudo-code doit être écrit dans vos propres mots. Si un logiciel vous aide, utilisez-le, mais vous devriez pouvoir écrire du pseudo-code manuellement, sans outil. C’est l’essence du pseudo-code : il est indépendant des syntaxes et des outils.

### Exercice 1 : La somme d’un tableau [#](#exercice-1--la-somme-dun-tableau)

Dans la plupart des langages informatiques, un tableau correspond à un vecteur en algèbre linéaire, soit une série de nombres, comme \\(\\langle 1,6,4,10 \\rangle\\). Dans cet exercice, vous devez proposer un algorithme pour calculer la somme des nombres entiers d’un tableau à une dimension de longueur quelconque (de 0 à plus d’un million de nombres). Utilisez une structure d’itération (boucle) pour parcourir chaque nombre du tableau.

Pour manipuler le tableau, vous pouvez écrire « Récupérer le nombre à l’index i » (où i est une variable contenant l’index) ou utiliser une syntaxe proche des langages de programmation, par exemple : `Entier e = monTableau[i]`. Pour obtenir la longueur du tableau, utilisez « la taille de monTableau ».

Testez votre pseudo-code en l’appliquant ligne par ligne à un exemple, comme si vous étiez un robot. Prenez votre temps.

Si vous introduisez d’autres conventions de notation, soyez précis. Spécifiez le type de toutes vos variables et donnez explicitement des valeurs initiales, sauf si elles sont reçues en paramètre.

Concevez cet algorithme en pseudo-code, en utilisant des termes concis, explicatifs et cohérents.

Réponse

    Entrée :
    Tableau d’entiers monTableau de taille N
    
    Variables :
    Entier somme = 0 // La somme du tableau
    Entier index = 0 // Index de l’élément du tableau
    
    Sortie :
    Entier somme
    
    Algorithme sommeTableau :
    
    TANT QUE index < taille de monTableau FAIRE
        somme = somme + monTableau[index] // Addition des nombres
        index = index + 1 // Incrémentation de l’index
    FIN TANT QUE
    
    retourne somme

### Exercice 2 : La recherche d’un entier [#](#exercice-2--la-recherche-dun-entier)

La recherche d’information dans une structure de données (tableau, graphe, arbre, etc.) est un domaine clé en informatique. Bien que les bases de données comme MySQL simplifient la recherche, il est souvent nécessaire de concevoir ses propres solutions. À partir de l’exercice 1, proposez un algorithme en pseudo-code pour vérifier si un entier (par exemple, un numéro de téléphone) est présent dans un tableau et retourner son index, ou -1 s’il est absent. Utilisez une structure itérative et une structure de contrôle (SI \_ ALORS \_ FIN SI).

Réponse

    Entrée :
    Tableau d’entiers monTableau de taille N
    Entier nombreATrouver
    
    Variables :
    Entier index = 0 // Index de l’élément du tableau
    
    Sortie :
    Index de l’entier ou -1 si non trouvé
    
    Algorithme trouverEntier :
    
    TANT QUE index < taille de monTableau FAIRE
        SI nombreATrouver est égal à monTableau[index] ALORS
            retourner index // Fin de l’algorithme
        FIN SI
        index = index + 1 // Incrémentation de l’index
    FIN TANT QUE
    
    retourner -1 // Nombre non trouvé

### Exercice 3 : Somme des multiples de 3 ou 5 [#](#exercice-3--somme-des-multiples-de-3-ou-5)

Additionnez tous les nombres naturels inférieurs à \\(1000\\) qui sont multiples de \\(3\\) ou de \\(5\\).

Réponse

Voici un algorithme inefficace. Vous pouvez faire mieux :

    Variable entière i = 0
    Variable entière somme = 0
    TANT QUE i < 1000
        SI le reste de la division par 3 de i est zéro OU le reste de la division par 5 de i est zéro ALORS
            somme = somme + i
        i = i + 1
    FIN TANT QUE
    Retourne somme

### Exercice 4 : Plus grand diviseur premier [#](#exercice-4--plus-grand-diviseur-premier)

Trouvez le plus grand nombre premier qui divise \\(317584931803\\).

Réponse

Voici un algorithme inefficace (effectuant plus d’opérations que nécessaire). Vous pouvez faire mieux :

    Variable entière i = 1
    Variable entière solution = 1
    TANT QUE i < 317584931803
        SI le reste de la division de 317584931803 par i est zéro ALORS
            Variable entière j = 3
            Variable booléenne premier = vrai
            TANT QUE j < i
                SI le reste de la division de i par j est zéro ALORS
                    premier = faux
                j = j + 1
            FIN TANT QUE
            SI premier ALORS
                solution = i
        i = i + 1
    FIN TANT QUE
    Retourne solution
    

Pour les curieux, voici une solution exécutable en Python ([voir ici](https://fr.wikipedia.org/wiki/Python_%28langage%29)) :

    i = 1
    solution = 1
    while i < 317584931803:
        if 317584931803 % i == 0:
            j = 3
            premier = True
            while j < i:
                if i % j == 0:
                    premier = False
                j = j + 1
            if premier:
                print(i, " est premier")
                solution = i
        i = i + 1
    print(solution)
    

Vous pouvez supprimer la ligne `print(i, " est premier")` pour n’obtenir que la réponse finale. Notez que j commence à 3, car tout diviseur premier (sauf 2) est impair d’après le théorème fondamental de l’arithmétique.

### Exercice 5 : Chiffre des dizaines [#](#exercice-5--chiffre-des-dizaines)

Pour un entier positif \\(x\\), trouvez le chiffre occupant la position des dizaines.

Réponse

    Variable entière x
    
    Divise x par 10, stocke le quotient dans la variable y
    
    Divise y par 10, retourne le reste de la division
    

Exemple : si x est 531, le quotient de 531 divisé par 10 est 53, reste 1. Le quotient de 53 divisé par 10 est 5, reste 3.

### Exercice 6 : Erreur dans un pseudo-code [#](#exercice-6--erreur-dans-un-pseudo-code)

Trouvez l’erreur dans le pseudo-code suivant :

    Entrées :
    Tableau R de longueur N
    Valeur X
    
    Sortie :
    Est-ce que la valeur X se trouve dans le tableau R ?
    
    Variables :
    Itérateur i = 0
    
    Tant que i <= N
        Si R[i] = X Alors retourne Vrai
        i = i + 1
    
    retourne Faux
    

Réponse

L’itérateur i prend les valeurs de 0 à N, accédant ainsi à N+1 éléments du tableau R, ce qui provoque une erreur d’accès hors limites.

### Exercice 7 : Racines d’un polynôme du second degré [#](#exercice-7--racines-dun-polyn%c3%b4me-du-second-degr%c3%a9)

Soit \\(P(x) = ax^2 + bx + c\\) un polynôme du second degré à coefficients réels. Les racines se calculent via le discriminant \\(A = b^2 - 4ac\\).

*   Si \\(A < 0\\), il n’y a pas de racine.
*   Si \\(A > 0\\), il existe deux racines : \\(X\_1 = \\frac{-b - \\sqrt{A}}{2a}\\) et \\(X\_2 = \\frac{-b + \\sqrt{A}}{2a}\\).
*   Si \\(A = 0\\), il existe une racine double : \\(X\_1 = X\_2 = \\frac{-b}{2a}\\).

Écrivez un algorithme qui, pour un polynôme donné par ses coefficients, calcule le discriminant, affiche « ce polynôme n’a pas de racine dans R » si A < 0, et calcule les racines sinon.

Réponse

    Algo pol
    
    Entrée :
    Nombres réels a, b, c // Coefficients du polynôme
    
    Variables :
    Nombres réels X1, X2, A // Racines et discriminant
    
    Début
        A = b² - 4ac
        Si A < 0 Alors
            Afficher «&nbsp;ce polynôme n’a pas de racine dans R&nbsp;»
        Sinon
            Si A égale 0
                X1 = X2 = -b/(2a)
            Sinon // A > 0
                X1 = (-b - √A)/(2a)
                X2 = (-b + √A)/(2a)
            Fin Si
        Fin Si
    Fin

### Exercice 8 : Exécution de l’algorithme des racines [#](#exercice-8--ex%c3%a9cution-de-lalgorithme-des-racines)

Exécutez l’algorithme de l’exercice 7 pour \\(P(x) = x^2 - 5x + 6\\), en présentant les résultats dans un tableau.

Réponse

Initialisation

Étape 1

Étape 2

Étape 3

Fin

Entrée

a

1

1

1

1

1

b

\-5

\-5

\-5

\-5

\-5

c

6

6

6

6

6

Variables

X1

2

2

2

X2

3

3

A

1

1

1

1

Sorties

écran

### Exercice 9 : Conversion de base [#](#exercice-9--conversion-de-base)

Pour un entier \\(B > 1\\) et un nombre \\(M\\), la représentation en base \\(B\\) de \\(M\\) s’obtient par division successive : \\(M = B \\times Q\_1 + R\_1\\), puis \\(Q\_1 = B \\times Q\_2 + R\_2\\), jusqu’à un quotient inférieur à \\(B\\). La représentation est \\(Q\_{n-1}R\_n\\ldots R\_1\\). Si \\(B > 10\\), les chiffres de \\(10\\) à \\(B-1\\) sont notés \\(A, B, C, \\ldots\\) (par exemple, pour \\(B = 16\\), \\(10 = A\\), \\(11 = B\\), etc.).

Écrivez un algorithme pour convertir un nombre \\(M\\) dans une base \\(B ≥ 2\\) (\\(B < 17\\)). Affichez un message d’erreur si \\(B < 2\\).

Réponse

    Algo base
    
    Entrée :
    Nombre entier positif B // Base
    Nombre entier positif M // Nombre à convertir
    
    Variables :
    Nombre entier q, r
    Suite de caractères alphanumériques S
    
    Début
        S = chaîne vide
        Si B < 2 Alors
            Afficher «&nbsp;entrez un entier supérieur ou égal à 2&nbsp;»
        Sinon
            q = M
            Tant que q > 0
                r = q - (q ÷ B) × B
                au cas où r
                    égal à 10 : ajouter A au début de S
                    égal à 11 : ajouter B au début de S
                    égal à 12 : ajouter C au début de S
                    égal à 13 : ajouter D au début de S
                    égal à 14 : ajouter E au début de S
                    égal à 15 : ajouter F au début de S
                    dans tous les autres cas : ajouter r au début de S
                q = q ÷ B
            Fin Tant que
        Fin Si
    Fin
    

Voici l’équivalent en Python ([voir ici](https://www.python.org)) :

    def f(M, B):
        s = ""
        if B < 2:
            print("entrez un entier supérieur ou égal à 2")
            return
        q = M
        while q > 0:
            r = q - (q // B) * B
            if r == 10: s = "A" + s
            elif r == 11: s = "B" + s
            elif r == 12: s = "C" + s
            elif r == 13: s = "D" + s
            elif r == 14: s = "E" + s
            elif r == 15: s = "F" + s
            else: s = str(r) + s
            q = q // B
        return s

### Exercice 10 : Tester la parité en base 2 [#](#exercice-10--tester-la-parit%c3%a9-en-base-2)

En utilisant l’algorithme Algo\_base, qui retourne la représentation en base \\(B\\) d’un nombre \\(M\\) (\\(S = \\text{Algo\\\_base}(B, M)\\)), écrivez un algorithme qui teste la parité d’un nombre \\(M\\) et affiche « pair » ou « impair ».

Réponse

    Algo parité
    
    Entrée :
    Nombre entier positif M // Nombre à tester
    
    Variables :
    Suite de caractères alphanumériques S
    
    Début
        S = Algo_base(2, M)
        Si dernier caractère de S est égal au chiffre 0 Alors
            Afficher «&nbsp;pair&nbsp;»
        Sinon
            Afficher «&nbsp;impair&nbsp;»
        Fin Si
    Fin

### Exercice 11 : Calcul de la factorielle [#](#exercice-11--calcul-de-la-factorielle)

Écrivez un algorithme qui calcule la factorielle d’un entier positif \\(n\\) (\\(n!\\)).

Solution

    Entrée :
    Entier positif n
    
    Variable :
    Entier fact = 1
    Entier i = 1
    
    TANT QUE i <= n FAIRE
        fact = fact × i
        i = i + 1
    FIN TANT QUE
    
    Retourner fact

### Exercice 12 : Inverser un tableau [#](#exercice-12--inverser-un-tableau)

Proposez un algorithme pour inverser un tableau d’entiers de taille quelconque.

Solution

    Entrée :
    Tableau d’entiers T de taille N
    
    Variables :
    Entier i = 0
    Entier j = N - 1
    
    TANT QUE i < j FAIRE
        échanger T[i] et T[j]
        i = i + 1
        j = j - 1
    FIN TANT QUE
    
    Retourner T

### Exercice 13 : Compter les voyelles [#](#exercice-13--compter-les-voyelles)

Écrivez un algorithme qui compte le nombre de voyelles dans une chaîne de caractères donnée.

Solution

    Entrée :
    Chaîne de caractères S
    
    Variable :
    Entier compteur = 0
    Entier i = 0
    
    TANT QUE i < longueur de S FAIRE
        SI S[i] est une voyelle ALORS
            compteur = compteur + 1
        FIN SI
        i = i + 1
    FIN TANT QUE
    
    Retourner compteur

### Exercice 14 : Tester si un entier est un palindrome [#](#exercice-14--tester-si-un-entier-est-un-palindrome)

Donnez un algorithme pour déterminer si un nombre entier est un palindrome (se lit de la même façon de gauche à droite et de droite à gauche).

Solution

    Entrée :
    Entier positif n
    
    Variables :
    Entier original = n
    Entier renverse = 0
    
    TANT QUE n > 0 FAIRE
        renverse = renverse × 10 + (reste de la division de n avec 10)
        n = n ÷ 10
    FIN TANT QUE
    
    SI original = renverse ALORS
        Retourner Vrai
    SINON
        Retourner Faux
    FIN SI

### Exercice 15 : Minimum et maximum d’un tableau [#](#exercice-15--minimum-et-maximum-dun-tableau)

Écrivez un algorithme qui trouve le minimum et le maximum dans un tableau d’entiers.

Solution

    Entrée :
    Tableau d’entiers T de taille N
    
    Variables :
    Entier min = T[0]
    Entier max = T[0]
    Entier i = 1
    
    TANT QUE i < N FAIRE
        SI T[i] < min ALORS
            min = T[i]
        FIN SI
        SI T[i] > max ALORS
            max = T[i]
        FIN SI
        i = i + 1
    FIN TANT QUE
    
    Retourner min, max

### Exercice 16 : Recherche dans un tableau [#](#exercice-16--recherche-dans-un-tableau)

Quel est le nombre maximal de comparaisons nécessaires pour rechercher un élément dans un tableau non trié de taille \\( n \\) ? Justifiez votre réponse.

Solution

Dans un tableau non trié de taille \\( n \\), il faut au pire comparer l’élément recherché à chaque élément du tableau, soit \\( n \\) comparaisons. Cela correspond à une recherche linéaire, de complexité \\( O(n) \\).

### Exercice 17 : Recherche binaire [#](#exercice-17--recherche-binaire)

Pourquoi la recherche binaire n’est-elle applicable qu’aux tableaux triés ? Quelle est sa complexité en temps ?

Solution

La recherche binaire n’est applicable qu’aux tableaux triés, car elle repose sur le fait que l’on peut éliminer la moitié des éléments à chaque étape en comparant la valeur recherchée à l’élément du milieu. Si le tableau n’est pas trié, on ne peut pas savoir dans quelle moitié chercher. Sa complexité en temps est \\( O(\\log n) \\).

### Exercice 18 : Algorithme quadratique [#](#exercice-18--algorithme-quadratique)

Donnez un exemple d’algorithme ayant une complexité en \\( O(n^2) \\) et expliquez pourquoi.

Solution

Un exemple classique est le tri à bulles (bubble sort). Pour chaque élément, on compare avec tous les autres, ce qui fait environ \\( n^2 \\) comparaisons pour un tableau de taille \\( n \\). C’est pourquoi sa complexité est \\( O(n^2) \\).

### Exercice 19 : Algorithme de tri efficace [#](#exercice-19--algorithme-de-tri-efficace)

Un algorithme de tri efficace comme le tri fusion (merge sort) a une complexité en \\( O(n \\log n) \\). Expliquez ce que cela signifie et pourquoi c’est plus rapide qu’un tri naïf pour de grands tableaux.

Solution

Une complexité en \\( O(n \\log n) \\) signifie que le nombre d’opérations croît plus vite que linéairement, mais beaucoup moins vite que quadratiquement. Par exemple, le tri fusion (merge sort) divise le tableau en deux à chaque étape (logarithmique) et traite chaque élément à chaque niveau de division (linéaire), d’où le \\( n \\log n \\). Pour de grands tableaux, c’est beaucoup plus rapide qu’un tri naïf en \\( O(n^2) \\).

### Exercice 20 : Alan Kay [#](#exercice-20--alan-kay)

Alan Kay est considéré comme l’un des pères de la programmation orientée objet. Quelles étaient ses motivations principales lorsqu’il a conçu ce paradigme ? En quoi sa vision différait-elle de l’utilisation courante de la programmation orientée objet aujourd’hui ? Résumez brièvement ses objectifs et l’esprit original de la programmation orientée objet selon Kay.

Réponse

Alan Kay a conçu la programmation orientée objet pour faciliter la création de systèmes logiciels modulaires, flexibles et évolutifs, inspirés par la biologie et la communication entre objets autonomes. Son objectif principal était de permettre à chaque « objet » d’être responsable de son propre état et de communiquer avec d’autres objets uniquement via des messages, favorisant ainsi l’encapsulation et l’indépendance des composants.

Pour Kay, la programmation orientée objet devait avant tout encourager l’émergence de systèmes dynamiques, adaptatifs et faciles à modifier, plutôt que de se limiter à la simple hiérarchie de classes et à l’héritage. Il insistait sur l’importance de la communication par messages et sur la capacité à faire évoluer les programmes sans tout réécrire.

De nos jours, la programmation orientée objet est souvent réduite à l’organisation du code et des données, alors que la vision originale de Kay mettait l’accent sur la modularité, la flexibilité et l’autonomie des objets. Sa conception visait à rendre la programmation plus naturelle, intuitive et proche du fonctionnement des systèmes vivants.

### Exercice 21 : Dahl et Nygaard [#](#exercice-21--dahl-et-nygaard)

Ole-Johan Dahl et Kristen Nygaard sont les créateurs du premier langage orienté objet, Simula. Quelles étaient leurs motivations principales lors de la création de ce langage ? Expliquez en quoi leur approche a influencé la programmation moderne.

Réponse

Dahl et Nygaard ont conçu Simula pour faciliter la modélisation et la simulation de systèmes complexes, comme des réseaux, des usines ou des processus sociaux. Leur motivation était de représenter chaque entité du système par un « objet » autonome, regroupant données et comportements, afin de refléter la réalité de manière plus naturelle et modulaire.

Ils voulaient permettre l’encapsulation, la réutilisation du code grâce à l’héritage, et la création de structures hiérarchiques. Cette approche a posé les bases de la programmation orientée objet moderne, en rendant la conception de logiciels plus flexible, évolutive et adaptée à la complexité des systèmes réels.

### Exercice 22 : James Gosling [#](#exercice-22--james-gosling)

Qui est James Gosling et quel a été son rôle dans la création du langage Java ? Quelles étaient les motivations principales derrière la conception de Java ?

Réponse

James Gosling est un informaticien canadien considéré comme le principal créateur du langage Java, développé chez Sun Microsystems dans les années 1990. Son objectif était de concevoir un langage portable, sécurisé, simple et adapté aux systèmes embarqués et aux réseaux. Java devait permettre d’écrire un programme une seule fois et de l’exécuter partout (« Write Once, Run Anywhere »), grâce à la machine virtuelle Java (JVM).

### Exercice 23 : domaines industriels [#](#exercice-23--domaines-industriels)

Citez trois domaines ou secteurs industriels où Java est largement utilisé aujourd’hui. Expliquez brièvement pourquoi Java est apprécié dans ces contextes.

Réponse

Java est largement utilisé dans :

*   **Le développement d’applications d’entreprise** (banques, assurances, télécommunications), grâce à sa robustesse, sa sécurité et la richesse de ses bibliothèques.
*   **Le développement d’applications mobiles** (notamment Android), car Java est le langage principal pour Android et bénéficie d’un vaste écosystème.
*   **Les systèmes embarqués et l’Internet des objets (IoT)**, où la portabilité et la fiabilité de Java sont des atouts majeurs.

### Exercice 24 : Backus-Naur [#](#exercice-24--backus-naur)

Qu’est-ce que la notation de Backus-Naur (BNF) ? À quoi sert-elle en informatique ? Donnez un exemple simple de BNF décrivant la syntaxe d’une expression arithmétique composée de chiffres et de l’opérateur +.

Réponse

La notation de Backus-Naur (BNF) est une méthode formelle pour décrire la syntaxe des langages de programmation et des langages formels. Elle permet de spécifier les règles de formation des expressions valides dans un langage, en utilisant des symboles non terminaux, des symboles terminaux et des règles de production.

La BNF est largement utilisée pour définir la grammaire des langages de programmation, des protocoles ou des formats de données.

**Exemple de BNF pour une expression arithmétique simple :**

<expression> ::= <chiffre> | <expression> "+" <chiffre>
<chiffre> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

Cela décrit une expression composée d’un ou plusieurs chiffres séparés par des +.

### Exercice 25 : Cycles [#](#exercice-25--cycles)

Mon ordinateur roule à une fréquence de 3 GHz. À tous les cycles, il exécute ses opérations. Quelle distance est-ce que la vitesse de la lumière traverse pendant un cycle ?

Réponse

À 3 GHz, un cycle d’horloge dure :

1 / 3 000 000 000 = 0,333... nanoseconde (ns) par cycle.

La lumière parcourt environ 30 cm (0,3 mètre) en 1 ns. Donc, en 0,333 ns, elle parcourt :

30 cm × 0,333... ≈ 10 cm.

**Réponse :** Pendant un cycle d’horloge à 3 GHz, la lumière parcourt environ 10 centimètres dans le vide.

### Exercice 26 : kibioctet [#](#exercice-26--kibioctet)

Quelle est la différence entre un kibioctet et un kilo-octet ?

Réponse

Un kilo-octet (ko) correspond à 1 000 octets (selon le système décimal, préfixe SI), tandis qu’un kibioctet (Kio) correspond à 1 024 octets (selon le système binaire, préfixe IEC). Le préfixe « kilo » (k) est utilisé pour les puissances de 10, alors que « kibi » (Ki) est utilisé pour les puissances de 2. Ainsi, 1 Kio = 1 024 octets, 1 ko = 1 000 octets.

### Exercice 27 : doublons [#](#exercice-27--doublons)

Écrivez un algorithme qui supprime les doublons d’un tableau d’entiers trié en ordre croissant, en renvoyant la nouvelle taille du tableau.

Réponse

    Entrée :
    Tableau d’entiers trié T de taille N
    
    Variables :
    Entier nouvelle_taille = 1
    Entier i = 1
    
    Tant que i < N faire
        Si T[i] ≠ T[nouvelle_taille - 1] alors
            T[nouvelle_taille] = T[i]
            nouvelle_taille = nouvelle_taille + 1
        Fin si
        i = i + 1
    Fin tant que
    
    Retourner nouvelle_taille

### Exercice 28 : puissance [#](#exercice-28--puissance)

Écrivez un algorithme qui calcule \\( a^n \\), où \\( a \\) est un entier et \\( n \\) un entier positif.

Réponse

    
    Entrée :
    Entier a
    Entier positif ou nul n
    
    Variable :
    Entier résultat = 1
    Entier i = 0
    
    Tant que i < n faire
        résultat = résultat × a
        i = i + 1
    Fin tant que
    
    Retourner résultat

### Exercice 29 : occurrences d’un caractère spécifique [#](#exercice-29--occurrences-dun-caract%c3%a8re-sp%c3%a9cifique)

Écrivez un algorithme qui compte le nombre d’occurrences d’un caractère spécifique dans une chaîne de caractères.

Réponse

    Entrée :
    Chaîne de caractères S
    Caractère c
    
    Variable :
    Entier compteur = 0
    Entier i = 0
    
    Tant que i < longueur de S faire
        Si S[i] = c alors
            compteur = compteur + 1
        Fin si
        i = i + 1
    Fin tant que
    
    Retourner compteur

### Exercice 30 : recherche d’une clé [#](#exercice-30--recherche-dune-cl%c3%a9)

Quelle est la complexité algorithme de la recherche d’un clé dans une table de hachage ?

Réponse

Un temps moyen de \\( O(1) \\).

### Vidéos suggérées [#](#vid%c3%a9os-sugg%c3%a9r%c3%a9es)

Des vidéos sur l’algorithmique et le pseudo-code sont disponibles, comme [celles de Loïc & Julien](https://www.youtube.com/playlist?list=PLdi5YpL19uBDkRVGWMeZ0ZhtUQKOW-hUZ).

 [![Previous](/inf1220-hugo/svg/backward.svg "Présentation du pseudocode") Présentation du pseudocode](/inf1220-hugo/docs/modules/module1/syntaxe/) [Travail noté 1 ![Next](/inf1220-hugo/svg/forward.svg "Travail noté 1")](/inf1220-hugo/docs/modules/module1/travail-note-1/) 


*   *   [Réponses uniques ?](#réponses-uniques-)
    *   [Logiciels](#logiciels)
    *   [Exercice 1 : La somme d’un tableau](#exercice-1--la-somme-dun-tableau)
    *   [Exercice 2 : La recherche d’un entier](#exercice-2--la-recherche-dun-entier)
    *   [Exercice 3 : Somme des multiples de 3 ou 5](#exercice-3--somme-des-multiples-de-3-ou-5)
    *   [Exercice 4 : Plus grand diviseur premier](#exercice-4--plus-grand-diviseur-premier)
    *   [Exercice 5 : Chiffre des dizaines](#exercice-5--chiffre-des-dizaines)
    *   [Exercice 6 : Erreur dans un pseudo-code](#exercice-6--erreur-dans-un-pseudo-code)
    *   [Exercice 7 : Racines d’un polynôme du second degré](#exercice-7--racines-dun-polynôme-du-second-degré)
    *   [Exercice 8 : Exécution de l’algorithme des racines](#exercice-8--exécution-de-lalgorithme-des-racines)
    *   [Exercice 9 : Conversion de base](#exercice-9--conversion-de-base)
    *   [Exercice 10 : Tester la parité en base 2](#exercice-10--tester-la-parité-en-base-2)
    *   [Exercice 11 : Calcul de la factorielle](#exercice-11--calcul-de-la-factorielle)
    *   [Exercice 12 : Inverser un tableau](#exercice-12--inverser-un-tableau)
    *   [Exercice 13 : Compter les voyelles](#exercice-13--compter-les-voyelles)
    *   [Exercice 14 : Tester si un entier est un palindrome](#exercice-14--tester-si-un-entier-est-un-palindrome)
    *   [Exercice 15 : Minimum et maximum d’un tableau](#exercice-15--minimum-et-maximum-dun-tableau)
    *   [Exercice 16 : Recherche dans un tableau](#exercice-16--recherche-dans-un-tableau)
    *   [Exercice 17 : Recherche binaire](#exercice-17--recherche-binaire)
    *   [Exercice 18 : Algorithme quadratique](#exercice-18--algorithme-quadratique)
    *   [Exercice 19 : Algorithme de tri efficace](#exercice-19--algorithme-de-tri-efficace)
    *   [Exercice 20 : Alan Kay](#exercice-20--alan-kay)
    *   [Exercice 21 : Dahl et Nygaard](#exercice-21--dahl-et-nygaard)
    *   [Exercice 22 : James Gosling](#exercice-22--james-gosling)
    *   [Exercice 23 : domaines industriels](#exercice-23--domaines-industriels)
    *   [Exercice 24 : Backus-Naur](#exercice-24--backus-naur)
    *   [Exercice 25 : Cycles](#exercice-25--cycles)
    *   [Exercice 26 : kibioctet](#exercice-26--kibioctet)
    *   [Exercice 27 : doublons](#exercice-27--doublons)
    *   [Exercice 28 : puissance](#exercice-28--puissance)
    *   [Exercice 29 : occurrences d’un caractère spécifique](#exercice-29--occurrences-dun-caractère-spécifique)
    *   [Exercice 30 : recherche d’une clé](#exercice-30--recherche-dune-clé)
    *   [Vidéos suggérées](#vidéos-suggérées)

## Travail noté 1


*   [Premier problème](#premier-problème)
    *   [Indices concernant le premier problème](#indices-concernant-le-premier-problème)
*   [Second problème](#second-problème)
*   [En terminant](#en-terminant)

Travail noté 1 - Les algorithmes [#](#travail-not%c3%a9-1---les-algorithmes)
============================================================================

Ce cours d’introduction à la programmation exige une gestion rigoureuse du temps et une préparation approfondie. Les étudiants doivent soumettre leurs travaux notés avant la date de fin de cours, indiquée dans le portail étudiant, sans possibilité de report sauf en cas de circonstances exceptionnelles validées par l’Université. La charge de travail est estimée à neuf heures par semaine sur quinze semaines, et les travaux, d’un niveau comparable à ceux d’autres universités, nécessitent plusieurs heures par activité. Les consignes soulignent l’importance de lire attentivement les énoncés, de tester rigoureusement ses solutions et de consacrer plus de temps à la vérification qu’à la production initiale. L’utilisation du robot conversationnel du cours est autorisée, mais les réponses doivent être personnelles.

Les travaux doivent être soumis en format PDF via l’outil de dépôt officiel de la TÉLUQ, sans envoi par courriel, sous peine de note zéro. Les consignes de présentation insistent sur la clarté, la lisibilité et l’usage d’un français correct, avec des explications détaillées en prose. Les corrections, disponibles sous cinq à dix jours ouvrables, sont accessibles uniquement via le portail étudiant, où les étudiants trouveront leur note et une rétroaction. Aucune solution n’est fournie, et les travaux sont strictement individuels, tout échange sur les réseaux sociaux pouvant entraîner des sanctions graves, y compris l’exclusion.

Pour réussir, les étudiants doivent présenter des solutions claires, précises et testées, accompagnées d’explications factuelles. La rigueur dans l’analyse et la vérification est cruciale, tout comme la réalisation préalable des exercices préparatoires. Les travaux notés évaluent la capacité à comprendre des énoncés logiques et à raisonner abstraitement, sans points attribués pour l’effort seul. Les étudiants sont encouragés à poser des questions sur la matière, à tester leurs solutions avec diverses données et à relire leur travail avant soumission, en évitant de commencer sans une maîtrise solide des concepts

Premier problème [#](#premier-probl%c3%a8me)
--------------------------------------------

Nous souhaitons un algorithme qui détermine si la somme des éléments d'un tableau de nombres positifs excède 100. Par ailleurs, nous souhaitons un algorithme efficace: l'algorithme doit accéder à aussi peu d'éléments du tableau que possible. Produisez un pseudo-code précis et expliquez votre solution. Vous pouvez expliquer le code sous la forme que vous souhaitez, tant que vos explications sont claires. Exécutez votre pseudo-code sur au moins 5 cas, incluant les deux cas suivants: le tableau \[55,55,55,55\] et le tableau \[1,2,3,5,6\].

Vous devez exécuter votre pseudo-code ligne-par-ligne en indiquant à chaque ligne quelle est la valeur de toutes les variables. Votre exécution doit être rigoureuse. Si l'algorithme effectue 50 opérations, votre exécution devrait comprendre 50 lignes.

Vous devez produire du pseudo-code: du code informatique (par ex. Java ou Python) n'est pas accepté. Votre pseudo-code doit être précis et lisible.

Si vous produisez un algorithme logiquement incorrect, vous pourrez obtenir la note de zéro pour cette question. Si vous omettez d'inclure un compte-rendu détaillé de l'exécution, vous pouvez obtenir la note de zéro.

> ### Indices concernant le premier problème [#](#indices-concernant-le-premier-probl%c3%a8me)
> 
> Voici quelques indices concernant l’énoncé que vous pouvez prendre en compte pour vous aider. Un indice n’est jamais une question supplémentaire, un ajout à la question, ou une seconde partie. Un indice ne sert qu’à vous inspirer ou à vous aider. Vous pouvez complètement ignorer les indices. Les indices ne visent qu’à vous aider si vous le souhaitez.
> 
> 1.  **Indice 1.** Rendez-vous sur [la page du robot conversationnel du cours](https://rc-inf1220.teluq.ca/) et saisissez l'énoncé dans la boîte de saisie: « _Nous souhaitons un algorithme qui détermine si la somme des éléments d’un tableau de nombres positifs excède 100. Par ailleurs, nous souhaitons un algorithme efficace: l’algorithme doit accéder à aussi peu d’éléments du tableau que possible. Produisez un pseudo-code précis et expliquez votre solution. Vous pouvez expliquer le code sous la forme que vous souhaitez, tant que vos explications sont claires. Exécutez votre pseudo-code sur au moins 5 cas, incluant les deux cas suivants: le tableau \[55,55,55,55\] et le tableau \[1,2,3,5,6\]._ ».
> 2.  **Indice 2.** Votre algorithme doit retourner soit vrai, soit faux.
> 3.  **Indice 3.** Votre algorithme doit fonctionner même si le tableau a une longueur de zéro.
> 4.  **Indice 4.** Votre algorithme doit fonctionner même si le tableau contient mille milliards d'éléments.
> 5.  **Indice 5.** Imaginez qu'on vous donne ce problème. On vous donne un tableau de grande taille (contenant, disons, un million d'éléments) contenant des valeurs positives et on vous demande de déterminer, le plus rapidement possible, si la somme des valeurs du tableau excède 100. Que feriez-vous? Expliquez de façon précise ce que vous feriez dans cette situation. (Il s'agit d'un indice pour vous aider à répondre à l'énoncé, pas une nouvelle question. Le tableau qu'on vous invite à imaginer n'est pas un second tableau ou un tableau supplémentaire par rapport à l'énoncé.)
> 6.  **Indice 6.** Commencez par le pseudo-code suivant qui calcule la somme des éléments d'un tableau.
>     
>         Entrées :
>         Tableau de nombres positifs :  tableau
>         
>         Variables :
>         Nombre entier : iterateur = 0;
>         
>         Sorties :
>         Nombre : somme = 0;
>         
>         TANT QUE iterateur < la longueur de tableau FAIRE
>                somme = somme + tableau[iterateur];
>                iterateur = iterateur + 1;
>         FIN TANT QUE
>         
>     
>     (Vous n’êtes pas obligé de partir de ce pseudo-code. Il s’agit d’un indice, d’une suggestion. Ce bout de pseudo-code n’introduit pas une question supplémentaire. Le tableau qu’on y trouve n’est pas un second tableau en plus de celui de l’énoncé.)
>     
> 7.  **Indice 7.** Ce n'est pas un problème de programmation Java, C#, C++ ou Python. Vous devez produire du pseudo-code qui est destiné à être lu et compris par un être humain. Il n'est pas nécessaire d'utiliser les constructions et types propres Java, C#, C++ ou Python.
> 8.  **Indice 8.** Beaucoup trop d'étudiants essaient de faire ce travail sans avoir fait tous les exercices sérieusement. Si vous avez analysé et compris les exercices préparatoires pour ce problème, vous ne devriez avoir aucune difficulté. Il est pratiquement impossible de ne pas arriver à faire ce problème en ayant fait tous les exercices solutionnés et en ayant bien compris toutes les solutions. Il est de votre responsabilité de faire tous les exercices.

Second problème [#](#second-probl%c3%a8me)
------------------------------------------

Nous souhaitons afficher les nombres entiers de 0 jusqu’à 100 à l’écran (incluant 0 mais excluant 100), en affichant “Fizz” quand le nombre est divisible par 3 et “Buzz” quand le nombre est divisible par 5.

    ...
    2
    3 Fizz
    4
    5 Buzz
    6 Fizz
    ...
    

Un étudiant nous a offert la solution suivante. Elle est incorrecte. Pour les fins de ce travail, vous pouvez ignorer la mise en page de la sortie (polices de caractères, espaces, etc.). L’erreur de l’étudiant est logique et non pas cosmétique.

Expliquez l’erreur et offrez une version corrigée. Exécutez votre pseudo-code corrigé, ainsi que le pseudo-code original. Expliquez les différences. **Vous devez exécuter votre pseudo-code**. Puisqu’il y a peut-être des dizaines d’itérations à calculer, vous pouvez résumer l’exécution sans aller dans chaque détail de chaque itération.

Votre explication de l’erreur doit être claire et limpide. Si vous ne montrez pas que vous avez bien compris l’erreur et que vous êtes capable de l’expliquez clairement, vous pourrez recevoir une note de zéro pour cette question.

    Entrées :
    Valeur maximale :  100;
    
    Variables :
    Nombre entier : iterateur = 0;
    
    Sorties : à l'écran
    
    
    TANT QUE iterateur < 100 FAIRE
           affiche la valeur de iterateur à l'écran
           SI iterateur est divisible par 3 ALORS
             affiche " Fizz"  à l'écran
           SINON SI iterateur est divisible par 5 ALORS
             affiche " Buzz"  à l'écran
           FIN SI
           change de ligne à l'écran
           iterateur = iterateur + 1
    FIN TANT QUE
    

> **Indice.** Rendez-vous sur [la page du robot conversationnel du cours](https://rc-inf1220.teluq.ca/) et saisissez l'énoncé dans la boîte de saisie: « _Nous souhaitons afficher les nombres entiers de 0 jusqu'à 100 à l'écran (incluant 0 mais excluant 100), en affichant "Fizz" quand le nombre est divisible par 3 et "Buzz" quand le nombre est divisible par 5. Expliquez l'erreur dans ce pseudocode: TANT QUE iterateur < 100 FAIRE affiche la valeur de iterateur à l'écran SI iterateur est divisible par 3 ALORS affiche " Fizz" à l'écran SINON SI iterateur est divisible par 5 ALORS affiche " Buzz" à l'écran FIN SI change de ligne à l'écran iterateur = iterateur + 1 FIN TANT QUE_ ».

Notez: le cours comprend plusieurs liens vers des vidéos et autres ressources externes. Ces ressources sont toujours optionnelles.

En terminant [#](#en-terminant)
-------------------------------

Dans plusieurs cas, vos travaux sont corrigés par un « correcteur ». Il est possible que vous puissiez identifier cette personne en examinant le document de rétroaction que vous recevez au sein du portail étudiant. Vous ne devriez jamais joindre cette personne. Cette personne n'a pas comme mandat de répondre à vos questions suite à la correction. Vos courriels seront ignorés. Il faut plutôt joindre la personne qui vous encadre au sein du cours.

Il est inutile de nous écrire pour obtenir des indices, des exemples de solutions, des pistes de départ, etc. Dans ce cours, nous n'offrons aucun indice par courriel.

Il s'agit d'un travail noté individuel.

 [![Previous](/inf1220-hugo/svg/backward.svg "Exercices sur les algorithmes") Exercices sur les algorithmes](/inf1220-hugo/docs/modules/module1/exercices/) [Module 2: Introduction au langage Java ![Next](/inf1220-hugo/svg/forward.svg "Module 2: Introduction au langage Java")](/inf1220-hugo/docs/modules/module2/) 


*   [Premier problème](#premier-problème)
    *   [Indices concernant le premier problème](#indices-concernant-le-premier-problème)
*   [Second problème](#second-problème)
*   [En terminant](#en-terminant)
