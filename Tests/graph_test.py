import matplotlib.pyplot as plt

x=list({'Alimentation': 9.2, 'Hygiène et beauté': 0, 'Entretien de la maison': 0, 'Animaux': 0, 'Électronique et multimédia': 0, 'Vêtements et accessoires': 159.20000000000002, 'Maison et décoration': 6.85, 'Loisirs et papeterie': 6.63, 'Santé': 0, 'Emballages': 0.1}.keys())
y=list({'Alimentation': 9.2, 'Hygiène et beauté': 0, 'Entretien de la maison': 0, 'Animaux': 0, 'Électronique et multimédia': 0, 'Vêtements et accessoires': 159.20000000000002, 'Maison et décoration': 6.85, 'Loisirs et papeterie': 6.63, 'Santé': 0, 'Emballages': 0.1}.values())

#Bar chart
#plt.bar(x,y)
#plt.title("AAA")
#plt.xlabel("X")
#plt.ylabel("Y")


#plt.plot(x,y)

plt.pie(y, labels=x, autopct='%1.1f%%')


plt.show()

#print(list({'Alimentation': 9.2, 'Hygiène et beauté': 0, 'Entretien de la maison': 0, 'Animaux': 0, 'Électronique et multimédia': 0, 'Vêtements et accessoires': 159.20000000000002, 'Maison et décoration': 6.85, 'Loisirs et papeterie': 6.63, 'Santé': 0, 'Emballages': 0.1}.keys()))
#print(list({'Alimentation': 9.2, 'Hygiène et beauté': 0, 'Entretien de la maison': 0, 'Animaux': 0, 'Électronique et multimédia': 0, 'Vêtements et accessoires': 159.20000000000002, 'Maison et décoration': 6.85, 'Loisirs et papeterie': 6.63, 'Santé': 0, 'Emballages': 0.1}.values()))