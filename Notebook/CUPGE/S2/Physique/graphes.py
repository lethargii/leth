import numpy as np
import matplotlib.pyplot as plt

mu0 = 4*np.pi*10**-7
R = 0.025
N = 200
L = 0.412
n = N/L
I = 3

values = [1.82, 1.79, 1.79, 1.80, 1.80, 1.80, 1.81, 1.80, 1.81, 1.80, 1.81, 1.80, 1.80, 1.78, 1.78, 1.76, 1.74, 1.71, 1.64, 1.52, 1.30, 0.99, 0.64]

z = np.linspace(-0.22, 0.22, 45)
B_th = mu0*n*I/2*(10**3)*((((L/2)-z)/np.sqrt(((L/2)-z)**2+R**2))+(((L/2)+z)/np.sqrt(((L/2)+z)**2+R**2)))
B_exp = values[:0:-1] + values

fig, ax = plt.subplots()
ax.plot(z,B_th, label="Courbe théorique")
ax.plot(z,B_exp, label="Courbe expérimentale")
ax.set_title("Norme du champ magnétique B(z) en fonction de z")
ax.legend()
ax.set_xlabel("z en m")
ax.set_ylabel("B(z) en mT")
ax.xaxis.set_ticks(np.linspace(-0.22, 0.22, 12))
ax.yaxis.set_ticks(np.linspace(0.4, 1.8, 15))
plt.show()
