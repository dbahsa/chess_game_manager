# CHESS GAME TOURNAMENT MANAGER

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](#)[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](#)[![forthebadge](https://forthebadge.com/images/badges/made-with-markdown.svg)](#)

# POUR COMMENCER

* Ce programme est destiné à un public avisé tel qu'un administrateur événementiel, qui est responsable de la gestion sa base de données
dont il/elle devra traiter méticuleusement pour le bon fonctionnement de cette application sur console.

* Ce programme comporte ses limites et n'est n'est pas sous sa forme aboutie à l'heure actuelle.

* Les paramètres à prendre compte avec le système suisse des tournois:
    - Il y a au départ un classement général des joueurs en fonction de leur nombre de points;
    - /!\ Le classement général (cl) des joueurs ne change pas durant un tournoi;
    - Le classement dans un tournoi dépend de la somme de points gagnés par match dans chaque round, et de la position des joueurs au classement général en cas d'égalité;
    - Nombre max de Joueurs (j): 8;
    - Nombre de match par Round (R): 4;
    - Nombre de R par défaut: 4;
    - Les 4 matches de R1:
        - en fonction du nombre de points de chaque joueur au classement général, c-à-d de leur position du 1er au 8ème,
        - le 1er des 4 premiers rencontre le 1er des 4 derniers, et ainsi de suite, tels que:<br>
        > j1 vs j5   |   j2 vs j6   |  j3 vs j7   |   j4 vs j8   |   j1 vs j2 ;
    - Nombre max de match unique joué par un joueur dans un tournoi: 7;
    - Nombre max de R unique: 7 (R5,R6,R7 sont utilisés ici à titre indicatif, mais l'application s'arrête après R4 /!!!\ );
    - Nombre max de match unique joué par tous les joueurs dans un tournoi est de 28, soit:
    > j1 vs. j2   |   j2 vs. j3   |   j3 vs. j4   |   j4 vs. j5   |   j5 vs. j6   |   j6 vs. j7   |   j7 vs. j8<br>
    > j1 vs. j3   |   j2 vs. j4   |   j3 vs. j5   |   j4 vs. j6   |   j5 vs. j7   |   j6 vs. j8<br>
    > j1 vs. j4   |   j2 vs. j5   |   j3 vs. j6   |   j4 vs. j7   |   j5 vs. j8<br>
    > j1 vs. j5   |   j2 vs. j6   |   j3 vs. j7   |   j4 vs. j8<br>
    > j1 vs. j6   |   j2 vs. j7   |   j3 vs. j8<br>
    > 1 vs. j7   |   j2 vs. j8<br>
    > j1 vs. j8<br>
    - Point gagnant (w) par match: 1;
    - Point perdant (l) par match: 0;
    - oint égalité (t) par match: 0,5;
    - Nombre max et min de points accumulés par un joueur dans chaque round durant le tournoi:
             R1      R2      R3      R4      R5      R6      R7<br>
    > MAX     1       2       3       4       5       6       7<br>
    > MIN     0       0       0       0       0       0       0
    - La création d'une paire de joueurs pour chacun des 4 matches dans un round (après R1) se fait en fonction:
        - de scores et du classment général en cas d'égalité:
            - Matches R2 : scores R1 & cl
            - Matches R3 : scores R1 + scores R2 & cl
            - Matches R4 : scores R1 + scores R2 + scores R3 & cl
            - Matches R5 : scores R1 + scores R2 + scores R3 + scores R4 & cl
            - Matches R6 : scores R1 + scores R2 + scores R3 + scores R4 + scores R5 & cl
            - Matches R7 : scores R1 + scores R2 + scores R3 + scores R4 + scores R5 + scores R6 & cl
            
        - et de scénarios de résultats obtenus à la fin de chaque round (w: gagnant | l: perdant | t: nul):
            - Cas 1:  4w   |   4l   |   0t
            - Cas 2:  3w   |   3l   |   2t
            - Cas 3:  2w   |   2l   |   4t
            - Cas 4:  1w   |   1l   |   6t
            - Cas 5:  0w   |   0l   |   8t
            <pre>
            /!!!\ Ces scénarios sont très importants pour l'écriture des algorithmes pour générer les paires de joueurs
            (match) de R2 à R7. Par exemple:
            
            (M: Match | T: Top | L: Low | w: gagnant | l: perdant | t: nul)

                Les Matches de R1                  Probables Resultats R1 (Cas3)
            ----------------------                -----------------------------
                M1   M2   M3   M4                   M1     M2     M3     M4
            T:  j1 | j2 | j3 | j4                   j1.t | j6.w | j3.t | j8.w
                vs | vs | vs | vs                   j5.t | j2.l | j7.t | j4.l
            L:  j5 | j6 | j7 | j8                   
                                                    Classement: j6,j8,j1,j3,j5,j7,j2,j4
                                                    Matches R2 en faisant jouer le 1er contre le 2ème:
                                                    j6 vs. j8 | j1 vs. j3 | j5 vs. j7 | j2 vs. j4 
            
            (ex: j1.t == j1 a fait match nul avec j5; j6.w veut dire j6 a gagné, et j2 a jerdu (j2.l))

            Resultats R1 (Cas4)            Resultats R1 (Cas5)            Resultats R1 (Cas1)            Resultats R1 (Cas2)
            ----------------------         ------------------------       ------------------------       ------------------------
            M1     M2     M3     M4        M1     M2     M3     M4        M1     M2     M3     M4        M1     M2     M3     M4
            j1.l \ j2.t \ j3.t \ j4.t      j1.t \ j2.t \ j3.t \ j4.t      j1.w \ j2.l \ j3.w \ j4.l      j1.t \ j2.l \ j3.w \ j4.w
            j5.w \ j6.t \ j7.t \ j8.t      j5.t \ j6.t \ j7.t \ j8.t      j5.l \ j6.w \ j7.l \ j8.w      j5.t \ j6.w \ j7.l \ j8.l
            
            Classement par cas:
            
            j5,j2,j3,j4,j6,j7,j8,j1        j1,j2,j3,j4,j5,j6,j7,j8        j1,j3,j6,j8,j2,j4,j5,j7        j3,j4,j6,j1,j5,j2,j7,j8

            Matches R2 par cas,
            en faisant jouer le 1er
            contre le 2ème:
            
            j5 vs. j2 | j3 vs. j4          j1 vs. j2 | j3 vs. j4          j1 vs. j3 | j6 vs. j8          j3 vs. j4 | j6 vs. j1
            j6 vs. j7 | j8 vs. j1          j5 vs. j6 | j7 vs. j8          j2 vs. j4 | j5 vs. j7          j5 vs. j2 | j7 vs. j8

            </pre>
            Comme vous pouvez le contaster, ces différents scénarios ne fonctionnent pas pour R2 vu qu'aucun des joueurs n'a la possibilité
            de renconter son oppsant du R1 parce que la création des paires a changé; soit en faisant jouer le 1er contre le 2ème,
            soit le 1er contre le 3ème, en fonction du classement établi à l'issu du R1.  Par exemple, j1 et j5 ne peuvent pas jouer ensemble
            au R2 parce que la répartition des points (0, 0,5, 1) ferait qu'au classement final du R1, ils seront toujours éloignés d'une
            probable opposition peu importe le cas (scénario).

            Donc pour R2, seul le classement des joueurs à l'issu de R1 est suffisant pour générer ses 4 nouvelles paires de joueurs.
            Ensuite, c'est après les matches du R2 que l'algorithme devrait prendre en compte ces scénarios/cas pour générer les matches
            de R3 à R7 pour éviter l'arrêt de l'application.

            Pour illustrer, si les résultats du R2 orientent vers le Cas1 (4w, 4l, 0t), une liste des 4w doit être constituée et triée,
            ainsi que celle des 4l.  Ensuite, les concatener pour obtenir une liste finale qui sera utilisée pour générer les matches.
            Mais avant de poursuivre, ces matches doivent être validés en vérifiant dans la base de données s'ils n'existent pas déjà.
            S'ils existent, la génération des pairs se fait alors entre le 1er et le 3ème joueur.


### PRE-REQUIS
- Langage: Python > 3.8
- Coding: utf-8
- Environnement virtuel: voir fichier requirements.txt
- requirements.txt: TinyDB, Pandas, Json, datetime, dataclasses, plus modules/paquets annexes

#### I. Création de l'environnement virtuel
- Soit avec le fichier requirements.txt;
- soit avec pip.

#### II. Activation de l'environnement virtuel
- Pour activer l'environnement virtuel à partir de votre terminal, veuillez exécuter la commande `source env/bin/activate`  (`env/Scripts/activate.bat` si vous êtes sous Windows). A ce stade, votre terminal doit ajoute le nom de votre environnement au début de chaque ligne de votre terminal (ici, **‘env’**).
- Ensuite, pour que l'**environnement virtuel** soit **fonctionnel**, il va falloir **ajout**er les **paquets** Python requis à cet effet, soit en installant manuellement chaque paquet avec `pip`, soit en utilisant le fichier `requirements.txt` pour installer automatiquement tous les paquets.


### INSTALLATION

##### Installation _"manuelle"_
Avec `$ pip install` vous pouvez installer les paquets/modules requis pour le bon fonctionnement des sccripts. 

##### Installation _"automatique"_
Ajouter dans votre repertoire local **Projet** une copie du fichier _"requirements.txt"_ (provenant du dossier compressé "P4_Nzimbi_Didier.zip"), ensuite exécuter la commande:
> `$ pip install -r requirements.txt`

# DEMARRAGE
Voilà, vous pouvez dès à présent exécuter le script contenu dans le fichier `main.py`.


# Fabriqué avec
* [DILLINGER](https://dillinger.io) - Editeur de texte
* [Forthebadge](http://forthebadge.com) - Badges en-tête

# Auteur
* **Didier K Nzimbi** _alias_ [dbahsa](https://github.com/dbahsa)