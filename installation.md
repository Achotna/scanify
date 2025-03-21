# Installation et exécution du projet

## Prérequis
Avant d'exécuter le projet, assurez-vous d'avoir installé les éléments suivants :
- **Python 3.11 ou plus** (vérifiez avec `python --version`)
- **Les bibliothèques Python nécessaires** (listées dans `requirements.txt`)
- **Tesseract OCR** (téléchargeable depuis [ce lien](https://github.com/UB-Mannheim/tesseract/wiki))

## Installation

### 1. Installer Python 3.11+
Si Python n'est pas installé, téléchargez-le depuis [python.org](https://www.python.org/downloads/) et suivez les instructions d'installation.

### 2. Installer les bibliothèques Python
Dans un terminal, exécutez la commande suivante depuis le dossier racine du projet :
```bash
pip install -r requirements.txt
```
Cela installera toutes les dépendances nécessaires pour exécuter le projet.

### 3. Installer Tesseract OCR
1. Téléchargez et installez **Tesseract** depuis [ce lien](https://github.com/UB-Mannheim/tesseract/wiki).
2. Notez le chemin d'installation (exemple : `C:\Program Files\Tesseract-OCR\tesseract.exe`).
3. Ouvrez le fichier **`ocr.py`** dans le dossier `model` et modifiez la ligne suivante pour y indiquer le bon chemin :

```python
window_path=r"votre_path\tesseract.exe"
```
### 4. Ajouter voter clé API
1. Créer un fichier **.env**
2. Placer dans ce fichier votre clé sous format (voir example.env)

```python
ANTHROPIC_API_KEY=METTEZ_VOTRE_CLE_API_SANS_GUILLEMETS
```

## Exécution du projet

Une fois l'installation terminée, lancez le projet en exécutant :
```bash
python sources/main.py
```

