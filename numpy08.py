import matplotlib.pyplot as plt
gases = ['Nitrogen','02','Co2','others']
sizes = [78,20,0.3,1.97]
colors = ['pink','yellow','orange','lightskyblue']

plt.pie(sizes, explode=(0,0.1,0,0),labels = gases,colors = colors,autopct='%1.1f%%',shadow=True, startangle=140)

plt.legend()
plt.show()
