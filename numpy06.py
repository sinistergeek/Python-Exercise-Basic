import matplotlib.pyplot as plt
x1 = [102,103,105,106,107,111]
y1 = [78,57,89,99,86,72]

x2 = [102,103,105,106,107,111]
y2 = [89,100,98,67,100,20]

plt.bar(x1,y1,label='Science deparment')
plt.bar(x2,y2,label='Commerce department')

plt.xlabel("Student id")
plt.ylabel("%Score")
plt.title("Score for Science and Commerce Students")
plt.legend()
plt.show()
