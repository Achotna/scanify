# Architecture du projet

## Organisation des fichiers

- `instance/` : Contient la base de données
  - `database.db` : Stockage de la base de données

- `models/` : Définitions des modèles de données
  - `ocr.py` : Programme gérant l'OCR

###########################"- `static/` : Ressources statiques (CSS, JS, images)
  - `Design/` : Dossier contenant des éléments graphiques
  - `bar_days.png` : Graphique des dépenses par jour
  - `bar_months.png` : Graphique des dépenses par mois
  - `chart_categories.png` : Graphique des catégories de dépenses
  - `chart_pay.png` : Graphique des moyens de paiement
  - `close.svg` : Icône de fermeture
  - `menu.svg` : Icône de menu
  - `script.js` : Fichier JavaScript pour les interactions frontend
  - `style.css` : Fichier CSS pour le style du site
  - `tab_produits_par_categories.png` : Tableau des produits par catégorie
  - `user_image.jpg` : Image d’utilisateur

- `templates/` : Fichiers HTML pour le rendu des pages
  - `about.html` : Page "À propos"
  - `dashboard.html` : Tableau de bord utilisateur
  - `home.html` : Page d'accueil
  - `login.html` : Page de connexion
  - `register.html` : Page d'inscription

- `tesseract_download/` : Contient les fichiers liés à Tesseract OCR

- `tickets_tests/` : Dossier pour les tickets de caisse destinées aux tests

- `uploads/` : Stocke les fichiers uploadés par les utilisateurs

- `.env` : Fichier des variables d’environnement

- `.gitignore` : Fichier pour ignorer certains fichiers/dossiers dans Git

- `app.py` : Fichier principal de l'application

- `example.env` : Exemple de fichier de configuration

- `modifs/` : Contient des fichiers de modifications diverses

- `requirements.txt` : Liste des dépendances du projet


