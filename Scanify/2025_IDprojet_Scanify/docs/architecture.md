# Architecture du projet

## Organisation des fichiers

```
sources/
 ├── models/
 │   └── ocr.py  # Programme gérant l'OCR
 │
 ├── static/  # Ressources statiques (CSS, JS, images)
 │   ├── Design/  # Éléments graphiques (ex: logo)
 │   ├── bar_days.png  # Graphique des dépenses par jour
 │   ├── bar_months.png  # Graphique des dépenses par mois
 │   ├── chart_categories.png  # Graphique des catégories de dépenses
 │   ├── chart_pay.png  # Graphique des moyens de paiement
 │   ├── script.js  # Interactions frontend
 │   ├── style.css  # Style du site
 │   └── tab_produits_par_categories.png  # Tableau des produits par catégorie
 │
 ├── templates/  # Fichiers HTML pour le rendu des pages
 │   ├── home.html  # Page d'accueil
 │   ├── about.html  # Page "À propos"
 │   ├── dashboard.html  # Tableau de bord utilisateur
 │   ├── login.html  # Page de connexion
 │   └── register.html  # Page d'inscription
 │
 ├── .env  # Variables d’environnement
 ├── .gitignore  # Fichiers à ignorer par Git
 ├── main.py  # Fichier principal de l'application
 ├── example.env  # Exemple de fichier de configuration

docs/  # Documentation du projet
 ├── architecture.md  # Documentation sur l'architecture
 ├── installation.md  # Guide d'installation
 └── utilisation.md  # Guide d'utilisation

tests/  # Tickets de caisse pour les tests

README.md  # Documentation principale
licence.txt  # Licence du projet
presentation.pdf  # Présentation du projet
requirements.txt  # Dépendances du projet
```



### Dossiers créés par le programme

```
instance/  # Base de données
 └── database.db  # Fichier de stockage

uploads/  # Fichiers uploadés par les utilisateurs
```


