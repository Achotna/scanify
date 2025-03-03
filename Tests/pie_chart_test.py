import matplotlib.pyplot as plt
data={'Alimentation': 9.2, 'Hygiène et beauté': 0, 'Entretien de la maison': 0, 'Animaux': 0, 'Électronique et multimédia': 0, 'Vêtements et accessoires': 159.20000000000002, 'Maison et décoration': 6.85, 'Loisirs et papeterie': 6.63, 'Santé': 0, 'Emballages': 0.1}

x = [key for key, value in data.items() if value > 0]
y=[value for value in data.values() if value > 0]

#start add
colors = ['#6a7998', '#3f4d58', '#dddee3', '#879a99', '#b7ccd1']
plt.rcParams['font.family'] = 'Inter'
colors = ['#b7ccd1', '#6a7998', '#dddee3', '#879a99', '#3f4d58']

explode = [0.08 if val == max(y) else 0.03 for val in y]
fig, ax = plt.subplots(figsize=(8, 8), facecolor='none')
wedges, texts, autotexts = ax.pie(
    y, labels=x, autopct='%1.1f%%', startangle=140, colors=colors,
    explode=explode, pctdistance=0.85,
    wedgeprops={'edgecolor': '#fff', 'linewidth': 2, 'alpha': 0.9})
for text in texts:
    text.set(fontsize=13, fontweight="bold", color='white')
for autotext in autotexts:
    autotext.set(fontsize=13, fontweight="bold", color='#1d1e1d')
plt.title("Répartition des Dépenses", fontsize=18, fontweight="bold", color="#dddee3")
plt.gca().set_facecolor('none')
plt.show()
