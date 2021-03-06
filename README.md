# 🏆 CHESS GAME TOURNAMENT MANAGER 🏆

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](#)[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](#)[![forthebadge](https://forthebadge.com/images/badges/made-with-markdown.svg)](#)

# POUR COMMENCER

<pre>
                            Bonjour et bienvenu!

                🏁 GESTIONNAIRE DE TOURNOI D'ECHECS 🏁
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~~~~~~~~~~~~~~~ 🏠 MENU PRINCIPAL ~~~~~~~~~~~~~~~~~

            ☰ Faites votre choix en tapant:

            [1] CREER TOURNOI          [2] AJOUTER JOUEURS
            [3] LANCER ROUNDS          [4] ARRETER ROUNDS
            [5] VOIR MATCHES           [6] AJOUTER SCORES
            [7] VOIR RAPPORTS          [8] ACTUALISER JOUEURS
            [9] ACTUALISER TOURNOI     [10] ARRETER LE PROGRAMME
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
</pre>
<br>
* Ce programme est destiné à un public avisé tel qu'un administrateur événementiel, qui est responsable de la gestion sa base de données
dont il/elle devra traiter méticuleusement pour le bon fonctionnement de cette application sur console.

* Ce programme est limité à 4 rounds comme mentionné ci-après.

* Les paramètres à prendre compte avec le système suisse des tournois:
    - Il y a au départ un classement général des joueurs en fonction de leur nombre de points;
    - /!\ Le classement général (cl) des joueurs ne change pas durant un tournoi;
    - Le classement dans un tournoi dépend de la somme de points gagnés par match dans chaque round, et de la position des joueurs au classement général en cas d'égalité;
    - Nombre max de Joueurs (j): 8;
    - Nombre de match par Round (R): 4;
    - Nombre de R par défaut: 4;
    - Les 4 matches de R1:
        - en fonction du nombre de points de chaque joueur au classement général, c-à-d de leur position du 1er au 8ème,
        - le 1er des 4 premières contre le 1er des 4 derniers, et ainsi de suite, tels que:<br>
        <pre>j1 vs j5   |   j2 vs j6   |  j3 vs j7   |   j4 vs j8   |   j1 vs j2 ;</pre><br>
    - Nombre max de match unique joué par un joueur dans un tournoi: 7;
    - Nombre max de R unique: 7 (R5,R6,R7 sont utilisés ici à titre indicatif, mais l'application s'arrête après R4 /!!!\ );
    - Nombre max de match unique joué par tous les joueurs dans un tournoi est de 28, soit:<br>
    <pre>
    j1 vs. j2   |   j2 vs. j3   |   j3 vs. j4   |   j4 vs. j5   |   j5 vs. j6   |   j6 vs. j7   |   j7 vs. j8
    j1 vs. j3   |   j2 vs. j4   |   j3 vs. j5   |   j4 vs. j6   |   j5 vs. j7   |   j6 vs. j8
    j1 vs. j4   |   j2 vs. j5   |   j3 vs. j6   |   j4 vs. j7   |   j5 vs. j8
    j1 vs. j5   |   j2 vs. j6   |   j3 vs. j7   |   j4 vs. j8
    j1 vs. j6   |   j2 vs. j7   |   j3 vs. j8
    j1 vs. j7   |   j2 vs. j8
    j1 vs. j8
    </pre>
    - Point gagnant (w) par match: 1;
    - Point perdant (l) par match: 0;
    - oint égalité (t) par match: 0,5;
    - La création d'une paire de joueurs pour chacun des 4 matches dans un round (après R1) se fait en fonction des scores et du classment général en cas d'égalité:<br>
    <pre>
        - Matches R2 : scores R1 & cl
        - Matches R3 : scores R1 + scores R2 & cl
        - Matches R4 : scores R1 + scores R2 + scores R3 & cl
        - Matches R5 : scores R1 + scores R2 + scores R3 + scores R4 & cl
        - Matches R6 : scores R1 + scores R2 + scores R3 + scores R4 + scores R5 & cl
        - Matches R7 : scores R1 + scores R2 + scores R3 + scores R4 + scores R5 + scores R6 & cl
    </pre>

    Notez qu'avant de poursuivre, ces matches doivent être validés en vérifiant leur existence dans la base de données. S'ils existent, la génération des pairs s'effectue alors en faisant le 1er contre le 3ème joueur.


### PRE-REQUIS
* 🚨 ALL FILES (main.py, view.py, players.py, tournament.py, and data.json) IN THE PROJECT FOLDER MUST BE OPEN SO THAT THE APP COULD FUNCTION !!!!
* 🚨 main.py is the major file that runs the whole program.
* 🚨 DO NOT DELETE DATA.JSON because it's used in the app as a tutorial for better user experience and fast learning curve tool !!!
* Langage: Python > 3.8
* Coding: utf-8
* Environnement virtuel: voir fichier requirements.txt
* requirements.txt: TinyDB, Pandas, Json, datetime, dataclasses, plus modules/paquets annexes
* flake8-html 0.4.1 pour aider à la correction des erreurs (génération de fichier flake-html): dans mes fichiers la plupart des erreurs concerne la mise en page, qui est d'ailleurs intentionnelle pour une meilleure lecture et compréhension... qui n'est malheureusement pas tout le temps conforme aux directives PEP 8.  J'ai pu en changer quelques unes, mais à l'avenir sur un projet commun avec plusieurs individus, je m'y conformerais.

#### I. Création de l'environnement virtuel
* Soit avec le fichier requirements.txt;
* soit avec pip.

#### II. Activation de l'environnement virtuel
* 💡 Pour activer l'environnement virtuel à partir de votre terminal, veuillez exécuter la commande `source env/bin/activate`  (`env/Scripts/activate.bat` si vous êtes sous Windows). A ce stade, votre terminal doit ajoute le nom de votre environnement au début de chaque ligne de votre terminal (ici, **‘env’**).
* 💡 Ensuite, pour que l'**environnement virtuel** soit **fonctionnel**, il va falloir **ajout**er les **paquets** Python requis à cet effet, soit en installant manuellement chaque paquet avec `pip`, soit en utilisant le fichier `requirements.txt` pour installer automatiquement tous les paquets.


### INSTALLATION

##### Installation _"manuelle"_
💡 Avec `$ pip install` vous pouvez installer les paquets/modules requis pour le bon fonctionnement des sccripts. 

##### Installation _"automatique"_
💡 Ajouter dans votre repertoire local **Projet** une copie du fichier _"requirements.txt"_ (provenant du dossier compressé "P4_Nzimbi_Didier.zip"), ensuite exécuter la commande:
> `$ pip install -r requirements.txt`

# DEMARRAGE
🚀 Le programme vous est livré avec une base de données pour vous faciliter son utilisation.  Comme vous pourrez le constater, toutes les données peuvent être actualisées pour vous permettre de relancer un nouveau tournoi.

🎉 Voilà, vous pouvez dès à présent exécuter `main.py` pour passer à l'action 🎊


# Fabriqué avec
🔥 [Forthebadge](http://forthebadge.com) - Badges en-tête

# Auteur
🤓 **Didier K Nzimbi** _alias_ [dbahsa](https://github.com/dbahsa)