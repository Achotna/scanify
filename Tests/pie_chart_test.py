import matplotlib.pyplot as plt

data={'Alimentation': 9.2, 'Hygiène et beauté': 0, 'Entretien de la maison': 0, 'Animaux': 0, 'Électronique et multimédia': 0, 'Vêtements et accessoires': 159.20000000000002, 'Maison et décoration': 6.85, 'Loisirs et papeterie': 6.63, 'Santé': 0, 'Emballages': 0.1}

x = [key for key, value in data.items() if value > 0]
y=[value for value in data.values() if value > 0]

colors=['turquoise', 'skyblue', 'lightblue', 'darkblue', 'blue']

plt.title("Pie chart categories", fontsize=10)
plt.figure(figsize=(5, 5))
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 5})

plt.show()