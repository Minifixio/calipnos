# README

## Compte-rendu de mission Télécom Étude

### Traitement de données médicales et représentation graphique sur site web

**Auteur :** Emile Le Gallic  
**Institution :** Telecom Paris, Institut Polytechnique de Paris, F-91120, Palaiseau, France  
**Contact :** emile.legallic@telecom-paris.fr  

**Date :** Novembre 2023

---

## Table des matières

1. [Présentation des technologies utilisées](#présentation-des-technologies-utilisées)
   - [Django](#django)
   - [PythonAnywhere](#pythonanywhere)
2. [Description de l’application](#description-de-lapplication)
   - [Organisation du projet](#organisation-du-projet)
   - [Développement local](#développement-local)
3. [Utilisation de l’application web](#utilisation-de-lapplication-web)
   - [Authentification](#authentification)
   - [Visualisation des données](#visualisation-des-données)
4. [Note à propos des fichiers csv à importer](#note-à-propos-des-fichiers-csv-à-importer)

---

## Présentation des technologies utilisées

### Django

Le framework Django a été choisi pour la réalisation de l'application web en Python. Ce choix s'explique par la volonté de conserver une cohérence avec les scripts de traitement des données de la mission précédente, également réalisés en Python. Django permet d'éviter de séparer la partie application web du traitement de données, contrairement à d'autres frameworks comme React ou Angular qui utilisent JavaScript.

- L'application Django est située dans le répertoire `/dashboard`.
- Le code pour la partie web se trouve dans le répertoire `/dashboard/plotter`.
- Le code de traitement des données issues des fichiers CSV est situé dans `/dashboard/plotter/csv_processing`.
- Le code pour les deux pages web de l'application (authentification et affichage des graphiques) est situé dans `/dashboard/plotter/views`.
- Les fichiers `/dashboard/plotter/constants.py` et `/dashboard/plotter/metrics.py` définissent respectivement les paramètres statiques et les différentes métriques utilisées dans l'application et les scripts de traitement des données.

Pour plus d'informations sur le lancement de l'application en local, voir la section [Développement local](#développement-local).

### PythonAnywhere

PythonAnywhere est un hébergeur spécialisé dans les applications Python, offrant des solutions d'hébergement pour Django. 

- L'accès à la console admin se fait à l'adresse : [https://eu.pythonanywhere.com/](https://eu.pythonanywhere.com/).
- Dans l'onglet « Web » du menu, vous avez accès aux webapps du compte. Ici, il en existe une seule : [www.calipnos.com](http://www.calipnos.com).
- Les noms de domaines calipnos.com, calipnos.fr, et calipnos.eu ont été redirigés vers le site hébergé sur PythonAnywhere.

---

## Description de l’application

### Organisation du projet

L'application possède deux pages principales :
1. **Authentification :** Permet à un utilisateur de s’enregistrer ou de se connecter.
2. **Affichage des résultats :** Permet à l’utilisateur de visualiser ses données issues de fichiers CSV.

- Les codes Python de ces pages sont situés respectivement dans `/dashboard/plotter/views/auth_view.py` et `/dashboard/plotter/views/results_view.py`.
- Les codes HTML sont situés dans le répertoire `/dashboard/plotter/template`.

### Développement local

L'application est compatible avec Python 3.8 et Python 3.9. La version utilisée sur PythonAnywhere est 3.9.

Pour développer en local, installez les librairies listées dans le fichier `/requirements.txt` :
```bash
$ pip install -r requirements.txt
```

Vous pouvez aussi utiliser un environnement virtuel :
```bash
$ pip install virtualenv
$ python -m venv myenv
$ source myvenv/bin/activate
```

Ensuite, rendez-vous dans le répertoire `/dashboard` et lancez le serveur :
```bash
$ python manage.py runserver
```

L’application locale sera disponible à l’adresse [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Utilisation de l’application web

### Authentification

L'identification est nécessaire pour accéder à la page de visualisation des données. Les nouveaux utilisateurs peuvent s'enregistrer en cliquant sur "S'enregistrer ici".

### Visualisation des données

La page de visualisation permet de déposer des fichiers CSV et d'afficher les graphiques résultants :
- **Déposer un fichier :** Cliquez sur "Déposer" puis sélectionnez le fichier CSV.
- **Traiter le fichier :** Cliquez sur "Traiter" pour afficher les graphiques.
- **Paramètres d’affichage :** Cochez les métriques à afficher et ajustez les seuils des paramètres de traitement, puis cliquez sur "Valider".
- **Fenêtre d’échantillonnage :** Définissez le nombre de points utilisés dans la fenêtre glissante de traitement des signaux.
- **Déplacement dans les graphiques :** Utilisez la ligne temporelle en bas pour se déplacer dans le temps. Sélectionnez directement sur les graphiques pour définir une fenêtre de visualisation. Un double clic réinitialise la fenêtre. Des valeurs prédéfinies de 1h, 2h, 30min, et 20sec sont disponibles en haut à gauche.
- **Exporter les graphiques :** Cliquez sur l’icône photo en haut à gauche en passant la souris sur le graphique.

---

## Note à propos des fichiers csv à importer

Les fichiers CSV doivent répondre aux critères suivants :
- Les noms des colonnes ne doivent pas se répéter dans le fichier CSV. 

Par exemple, ce fichier CSV ne convient pas car les noms des colonnes se répètent :
```csv
Index;Date;Time;Temperature(°C);Cardio(BPM);Saturation(%SpO2);Audio(%max);Rotation(rad/s);Acceleration(m/s2)
1;16/03/2023;22:05:58;22.60;0.00;0;0.00;0.19;10.23
...
Index;Date;Time;Temperature(°C);Cardio(BPM);Saturation(%SpO2);Audio(%max);Rotation(rad/s);Acceleration(m/s2)
8;16/03/2023;22:06:12;23.20;40.67;93;3.11;0.23;10.63
```

Les colonnes de valeurs de Temperature, Cardio, Saturation, Audio, Rotation, et Acceleration seront reconnues si les noms des colonnes comportent les trois premières lettres des métriques citées. Par exemple : "Car" pour Cardio ou "Sat(SpO2)" pour Saturation.