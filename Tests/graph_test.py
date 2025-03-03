import matplotlib.pyplot as plt
import random

# ✅ Adding random values to categories for testing
categories_amount = {
    "Alimentation": random.randint(10, 100),
    "Hygiène et beauté": random.randint(10, 100),
    "Entretien de la maison": random.randint(10, 100),
    "Animaux": random.randint(10, 100),
    "Électronique et multimédia": random.randint(10, 100),
    "Vêtements et accessoires": random.randint(10, 100),
    "Maison et décoration": random.randint(10, 100),
    "Loisirs et papeterie": random.randint(10, 100),
    "Santé": random.randint(10, 100),
    "Emballages": random.randint(10, 100),
}

dates = {f"Day {i}": random.randint(20, 150) for i in range(1, 11)}
months = {month: random.randint(100, 1000) for month in [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]}

data_categories = categories_amount
x = [key for key, value in data_categories.items() if value > 0]
y = [value for value in data_categories.values() if value > 0]

tableau = [["Catégorie", "Montant (€)"]] + [[key, round(value, 2)] for key, value in categories_amount.items()]

#changeeeeeeeeeeeeeeeeeee
fig, ax = plt.subplots(figsize=(8, 4), facecolor='none')
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=tableau, cellLoc='center', loc="center", colWidths=[0.5, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(12)
for i, cell in table.get_celld().items():
    cell.set_edgecolor('#6a7998')
    cell.set_height(0.1)
    if i[0] == 0:
        cell.set_fontsize(14)
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#3f4d58')
    else:
        cell.set_facecolor('#262931')
        cell.set_text_props(color='white')

plt.show()


#bar change
fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')
#attention do not report as it
plt.bar([key for key, value in dates.items() if value > 0], [value for value in dates.values() if value > 0], color='#6a7998')
#bar change
plt.title('Money spent according to days', fontsize=14, fontweight='bold', color='#dddee3')
plt.xlabel('Dates', fontsize=12, color='white')
plt.ylabel('Money spent (€)', fontsize=12, color='white')
plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

plt.show()

#bar months
fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')
#attention do not report as it
plt.bar([key for key, value in months.items() if value > 0], [value for value in months.values() if value > 0], color='#b7ccd1')
#bar months
plt.title('Money spent according to months', fontsize=14, fontweight='bold', color='#dddee3')
plt.xlabel('Months', fontsize=12, color='white')
plt.ylabel('Money spent (€)', fontsize=12, color='white')
plt.grid(axis='y', linestyle='--', alpha=0.5, color='gray')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

plt.show()
