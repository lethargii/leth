import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Partie 1 : Convolution et Transformée de Fourier

# 1/
# Initialisation
fe = 1024  # Fréquence d'échantillonnage en Hz
D = 1    # Durée du signal en s
t = np.arange(-D/2, D/2, 1/fe)  # Création de l'axe temporel
T = 25     # Largeur de la porte en nb d'échantillons

# Création du signal s
s = np.ones_like(t)
s[t > T/1024] = 0
s[t < -T/1024] = 0

# Affichage du signal
plt.figure(1)
plt.plot(t, s)
plt.title('Signal s')
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.show()

# 2/
f = np.fft.fftfreq(len(s),1/fe)  # Création de l'axe des fréquences
f = np.fft.fftshift(f)  # Déplacer les fréquences de manière centrée
S = np.fft.fft(s)  # TF du signal s

# Affichage
plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(f, np.abs(S))
plt.xlabel('fréquences (Hz)')
plt.ylabel('spectre de s')
plt.title('Module et phase de la TF de s')
plt.subplot(2, 1, 2)
plt.plot(f, np.angle(S))
plt.xlabel('fréquences (Hz)')
plt.ylabel('phase')
plt.show()

# 3/
Y = np.fft.fftshift(S)  # Permutation avec fftshift
plt.figure(3)
plt.subplot(2, 1, 1)
plt.plot(f, np.abs(Y))
plt.xlabel('fréquences (Hz)')
plt.ylabel('spectre de y')
plt.title('Module et phase de Y')

plt.subplot(2, 1, 2)
plt.plot(f, np.angle(Y))
plt.xlabel('fréquences (Hz)')
plt.ylabel('phase')
plt.show()

# 4/
y_prime = np.fft.ifft(Y)  # TF inverse de Y
s_prime = np.fft.ifft(S)  # TF inverse de S
plt.figure(4)
plt.subplot(1, 2, 1)
plt.plot(t, y_prime)
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.title('FFT inverse de Y')
plt.xlim(-0.05, 0.05)

plt.subplot(1, 2, 2)
plt.plot(t, s_prime)
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.title('FFT inverse de S')
plt.show()

# 5/
x = np.convolve(s, s, 'same')  # Produit de convolution
plt.figure(5)
plt.plot(t, x)
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.title('Produit de convolution x = s*s')
plt.show()

# 6/
X = np.fft.fft(x)  # TF de x
S_carre = S**2  # Élévation au carré de S

plt.figure(6)
plt.plot(f, np.abs(X), label='X')
plt.plot(f, S_carre, '--', label='S^2')
plt.xlabel('fréquence (Hz)')
plt.ylabel('phase')
plt.title('Comparaison de la FFT de x et de la FFT de s')
plt.legend()
plt.show()

# Partie 2 : TF d'un signal carré

# 1/
# Initialisation
fe = 1000  # Fréquence d'échantillonnage en Hz
F = 100    # Fréquence du signal en Hz
N = 10     # Nombre de périodes
D = N/F  # Durée du signal en s
t = np.arange(0, D, 1/fe)  # Création de l'axe temporel

s = np.sign(np.sin(2*np.pi*F*t))  # Signal carré
plt.figure(7)
plt.plot(t, s)
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.title('Signal carré')
plt.show()

# 2/
nb_points_fft = 1024  # Nombre de points de la FFT
f = np.fft.fftfreq(nb_points_fft,1/fe)  # Création du vecteur fréquentiel associé
f = np.fft.fftshift(f)  # Déplacer les fréquences de manière centrée

S = np.fft.fft(s, nb_points_fft)  # FFT de s
plt.figure(8)
plt.plot(f, np.abs(S))
plt.xlabel('fréquence (Hz)')
plt.ylabel('spectre de s')
plt.title('FFT de s')
plt.show()

# Partie 3 : Débruitage d'un signal par FFT

# TF et TF inverse
# Initialisation
fe = 1000  # Fréquence d'échantillonnage en Hz
F = 10     # Fréquence du signal en Hz
D = 1      # Durée du signal en s
A = 3      # Amplitude du signal
t = np.arange(0, D, 1/fe)  # Création de l'axe temporel

s = A*np.sin(2*np.pi*F*t)
plt.figure(9)
plt.plot(t, s)
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.title('Signal sinusoïdal')
plt.show()

# 1/
f = np.fft.fftfreq(len(s), 1/fe)  # Création de l'axe des fréquences
f = np.fft.fftshift(f)  # Déplacer les fréquences de manière centrée
S = np.fft.fft(s)  # FFT de s
plt.figure(10)
plt.plot(f, np.abs(S))
plt.xlabel('fréquence (Hz)')
plt.ylabel('spectre de s')
plt.title('Module de la TF de s')
plt.show()

# 2/
s_inv = np.fft.ifft(S)  # FFT inverse de S
plt.figure(11)
plt.plot(t, s_inv)
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.title('FFT inverse de S')
plt.show()

# Bruit Blanc
# 3/
bruit = np.random.rand(len(s))  # Création d'un bruit blanc centré d'amplitude 1
plt.figure(12)
plt.subplot(2, 1, 1)
plt.plot(t, bruit)
plt.xlabel('temps(s)')
plt.ylabel('amplitude')
plt.title('Signal et module de bruit')

plt.subplot(2, 1, 2)
plt.plot(f, np.abs(np.fft.fft(bruit)))
plt.xlabel('fréquence (Hz)')
plt.ylabel('spectre de bruit')
plt.show()

# Bruitage du signal
# 4/
signal_bruite = s + bruit*(s.max()/(bruit.max()*2))
SIGNAL_BRUITE = np.fft.fft(signal_bruite)
plt.figure(13)
plt.subplot(2, 1, 1)
plt.plot(t, signal_bruite)
plt.xlabel('temps (s)')
plt.ylabel('amplitude')
plt.title('Signal et module du signal bruité')

plt.subplot(2, 1, 2)
plt.plot(f, np.abs(SIGNAL_BRUITE))
plt.xlabel('fréquence (Hz)')
plt.ylabel('spectre de SIGNAL_BRUITE')
plt.show()

# Filtrage par FFT
# 5/ et 6/
M = abs(SIGNAL_BRUITE).max()  # Amplitude maximale de la TF du signal bruite
print(M)
seuil = 0.1  # Seuil à 10%
H = np.zeros_like(SIGNAL_BRUITE)
H[abs(SIGNAL_BRUITE) > M*seuil] = 1

SIGNAL_BRUITE_FILTRE = SIGNAL_BRUITE * H
signal_bruite_filtre = np.fft.ifft(SIGNAL_BRUITE_FILTRE)
plt.figure(14)
plt.subplot(2, 1, 1)
plt.plot(t, signal_bruite_filtre)
plt.xlabel('temps(s)')
plt.ylabel('amplitude')
plt.title('Signal et module du signal bruité filtré')

plt.subplot(2, 1, 2)
plt.plot(f, SIGNAL_BRUITE_FILTRE)
plt.xlabel('fréquence (Hz)')
plt.ylabel('spectre de SIGNAL_BRUITE_FILTRE')
plt.show()

# 7/
A1 = 1
A2 = 3
A3 = -6
f1 = 10
f2 = 55
f3 = 122

s = np.cos(2*f1*t) + 3*np.cos(2*f2*t) - 6*np.cos(2*f3*t)
s_bruitee = s + np.random.rand(len(t))*s.max()/2
S_BRUITEE = np.fft.fft(s_bruitee)
M = abs(S_BRUITEE).max()
seuil = 0.1
H = np.zeros_like(S_BRUITEE)
H[abs(S_BRUITEE) > M*seuil] = 1
S_DEBRUITEE = S_BRUITEE * H
s_debruitee = np.fft.ifft(S_DEBRUITEE)

plt.figure(15)
plt.subplot(3, 1, 1)
plt.title('Signal originale, bruitée et débruitée')
plt.plot(t, s)
plt.xlabel('temps(s)')
plt.ylabel('amplitude')
plt.subplot(3, 1, 2)
plt.plot(t, s_bruitee)
plt.xlabel('temps(s)')
plt.ylabel('amplitude')
plt.subplot(3, 1, 3)
plt.plot(t, s_debruitee)
plt.xlabel('temps(s)')
plt.ylabel('amplitude')
plt.show()
