from tabulate import tabulate

data = {
    'Nom du magasin': 'Berqhotel Grosse Scheidegg',
    'Date': '30/07/2007',
    'Total': 54.5,
    'Type de paiement': 'E',
    'Articles': [
        {'Nom_article': 'Latte Macchiato', 'Catégorie': 'Alimentation', 'Prix': 4.5},
        {'Nom_article': 'Latte Macchiato', 'Catégorie': 'Alimentation', 'Prix': 4.5},
        {'Nom_article': 'Gloki', 'Catégorie': 'Alimentation', 'Prix': 5.0},
        {'Nom_article': 'Schweinschnitze', 'Catégorie': 'Alimentation', 'Prix': 22.0},
        {'Nom_article': 'Chasspaétz', 'Catégorie': 'Alimentation', 'Prix': 18.5}
    ]
}

# Affichage des informations générales
print(f"Nom du magasin : {data['Nom du magasin']}")
print(f"Date : {data['Date']}")
print(f"Total : {data['Total']} CHF")
print(f"Type de paiement : {data['Type de paiement']}")
print("\nArticles :")

# Affichage des articles sous forme de tableau
articles_table = [[article['Nom_article'], article['Catégorie'], article['Prix']] for article in data['Articles']]
print(tabulate(articles_table, headers=["Nom de l'article", "Catégorie", "Prix (CHF)"], tablefmt="grid"))
