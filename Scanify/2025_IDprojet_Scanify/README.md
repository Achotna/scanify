# Scanify
#Auteurs : Antonina Savchenko & Elisa Salignon

Ce projet a été développé dans le cadre du concours des Trophées NSI. Il permet d'analyser des tickets de caisse en générant des graphiques et facilite ainsi la gestion des dépenses.


## Installation

### Prérequis
Avant de lancer le projet, assurez-vous d’avoir installé :
- **Python 3.11 ou plus**
- **Les bibliothèques listées dans `requirements.txt`**
- **Tesseract OCR** (Téléchargeable depuis [ce lien](https://github.com/UB-Mannheim/tesseract/wiki))
- **Une clé API ainsi que la création du fichier pour l'utiliser**
- **Suivez les indications dans `installation.md`**


## Usage

```python
python sources/main.py
```


##Contraintes et Limitations

Système d'exploitation : Le projet a été testé uniquement sous Windows. Certaines fonctionnalités peuvent ne pas fonctionner sous macOS ou Linux.

Version de Python : Doit être 3.11 ou plus pour éviter des incompatibilités avec certaines bibliothèques.

Dépendances : L'installation des bibliothèques via requirements.txt est obligatoire avant d'exécuter le projet.

Tesseract OCR : Le chemin d'installation de Tesseract doit être correctement configuré dans ocr.py.

Taille des images : Les performances de l'OCR peuvent être affectées si les images sont de trop mauvaise qualité ou trop volumineuses.

Fichiers téléchargés : Les tickets doivent être au format d'image car notre programme ne peut que traiter des images (JPEG ou JPG).

Tickets de caisse : Les tickets doivent être de bonne qualité, comme ceux présents dans le dossier `test`. Ils doivent également être plutôt courts, ne pas contenir de réduction et avoir des noms d'articles clairs, car notre code n'est pas encore adapté pour des tickets plus complexes.


## License

Ce projet est sous licence **GPL v3+**. Voir `LICENCE.txt` pour plus de détails.

