import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

#### 1/

# Chargement des données

# Load .mat files
data_repos = scipy.io.loadmat("ECG_TP_repos.mat")
data_effort = scipy.io.loadmat("ECG_TP_effort.mat")

# Extract variables from loaded data
X_ECG_Rep = data_repos['X_ECG_Rep'].flatten()
X_ECG_Eff = data_effort['X_ECG_Eff'].flatten()

#### 2/

# Initialization
fe = 1000                      # Sampling frequency in Hz
N = len(X_ECG_Rep)             # Length of the vector
t = np.linspace(0, N/fe, N)    # Time scale

# Plot the time series
plt.figure(1)

# ECG at rest
plt.subplot(2, 1, 1)
plt.plot(t, X_ECG_Rep)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.title('ECG Signal at Rest')

# ECG during effort
plt.subplot(2, 1, 2)
plt.plot(t, X_ECG_Eff)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.title('ECG Signal During Effort')

plt.tight_layout()
plt.show()

#### 3/

# Frequency Analysis
NFFT = 2 ** np.ceil(np.log2(N))  # Next power of 2 from length of x
FFT_ECG_Rep = np.fft.fft(X_ECG_Rep, int(NFFT))  # FFT at rest
FFT_ECG_Eff = np.fft.fft(X_ECG_Eff, int(NFFT))  # FFT during effort
f = fe / 2 * np.linspace(0, 1, int(NFFT / 2))  # Frequency scale

# Plot amplitude spectrum (only magnitude, no phase)
plt.figure(2)

# FFT at rest
plt.subplot(2, 1, 1)
plt.plot(f, 2 * np.abs(FFT_ECG_Rep[:int(NFFT / 2)]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('|FFT_ECG_Rep(f)|')
plt.title('Single-Sided Amplitude Spectrum of X_ECG_Rep')
plt.xscale('log')  # Logarithmic scale for the x-axis

# FFT during effort
plt.subplot(2, 1, 2)
plt.plot(f, 2 * np.abs(FFT_ECG_Eff[:int(NFFT / 2)]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('|FFT_ECG_Eff(f)|')
plt.title('Single-Sided Amplitude Spectrum of X_ECG_Eff')
plt.xscale('log')  # Logarithmic scale for the x-axis

plt.tight_layout()
plt.show()

#### 4/

### Step 1:

# Thresholding

threshold_Rep = 0.60*max(X_ECG_Rep)
threshold_Eff = 0.60*max(X_ECG_Eff)

# Plot with thresholding
plt.figure(3)

# ECG au repos avec seuil
plt.subplot(2, 1, 1)
plt.plot(t, X_ECG_Rep, label='ECG at Rest')
plt.axhline(y=threshold_Rep, color='r', linestyle='--', label=f'Threshold = {threshold_Rep:.2f}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.title('ECG Signal at Rest with Threshold')

# ECG pendant l'effort avec seuil
plt.subplot(2, 1, 2)
plt.plot(t, X_ECG_Eff, label='ECG during Effort')
plt.axhline(y=threshold_Eff, color='r', linestyle='--', label=f'Threshold = {threshold_Eff:.2f}')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.title('ECG Signal during Effort with Threshold')

plt.tight_layout()
plt.show()

### Step 2:

Diag_ECG_Rep = np.zeros(N, dtype=int)
Diag_ECG_Eff = np.zeros(N, dtype=int)

# Logical vector for rest
for i in range(len(X_ECG_Rep)):
    if X_ECG_Rep[i]>threshold_Rep:
        Diag_ECG_Rep[i] = 1
    else:
        Diag_ECG_Rep[i] = 0

# Logical vector for effort
for i in range(len(X_ECG_Eff)):
    if X_ECG_Eff[i]>threshold_Eff:
        Diag_ECG_Eff[i] = 1
    else:
        Diag_ECG_Eff[i] = 0

plt.figure(4)  # Create a new figure

plt.subplot(2,1,1)
#Repos
plt.plot(t,Diag_ECG_Rep,label="ECG at rest")
plt.xlabel('Time (s)')
plt.title("ECG at rest with threshold appliqued")

plt.subplot(2,1,2)
#Effort
plt.plot(t,Diag_ECG_Eff,label="ECG at rest")
plt.xlabel('Time (s)')
plt.title("ECG after effort with threshold appliqued")

plt.tight_layout()
plt.show()

### Step 3:

## Rest (Repos)

# Calculate the positive and negative transitions for rest ECG signal
diff_diag_ecg_rep = np.diff(Diag_ECG_Rep)
Diff_Diag_ECG_Rep_P = np.where(diff_diag_ecg_rep == 1)[0]
Diff_Diag_ECG_Rep_N = np.where(diff_diag_ecg_rep == -1)[0]

# Remove the last element of Diff_Diag_ECG_Rep_P, equivalent to `end = []` in MATLAB
Diff_Diag_ECG_Rep_P = Diff_Diag_ECG_Rep_P[:-1]

# Initialize lists for storing results
A_Rep = []
B_Rep = []

# Loop through the detected peaks in the resting ECG signal
for k in range(len(Diff_Diag_ECG_Rep_P)):
    # Find the maximum value and index in the segment between transitions
    segment = X_ECG_Rep[Diff_Diag_ECG_Rep_P[k]:Diff_Diag_ECG_Rep_N[k]]
    max_value = np.max(segment)
    max_index = np.argmax(segment) + Diff_Diag_ECG_Rep_P[k]

    # Store the results
    A_Rep.append(max_value)
    B_Rep.append(max_index)

# Create an array to store the peak values for rest ECG
Peak_ECG_Rep = np.zeros_like(X_ECG_Rep)
Peak_ECG_Rep[B_Rep] = X_ECG_Rep[B_Rep]

## Effort (Effort)

# Calculate the positive and negative transitions for effort ECG signal
diff_diag_ecg_eff = np.diff(Diag_ECG_Eff)
Diff_Diag_ECG_Eff_P = np.where(diff_diag_ecg_eff == 1)[0]
Diff_Diag_ECG_Eff_N = np.where(diff_diag_ecg_eff == -1)[0]

# Remove the last element of Diff_Diag_ECG_Eff_P
Diff_Diag_ECG_Eff_P = Diff_Diag_ECG_Eff_P[:-1]

# Initialize lists for storing results
A_Eff = []
B_Eff = []

# Loop through the detected peaks in the effort ECG signal
for k in range(len(Diff_Diag_ECG_Eff_P)):
    # Find the maximum value and index in the segment between transitions
    segment = X_ECG_Eff[Diff_Diag_ECG_Eff_P[k]:Diff_Diag_ECG_Eff_N[k]]
    max_value = np.max(segment)
    max_index = np.argmax(segment) + Diff_Diag_ECG_Eff_P[k]

    # Store the results
    A_Eff.append(max_value)
    B_Eff.append(max_index)

# Create an array to store the peak values for effort ECG
Peak_ECG_Eff = np.zeros_like(X_ECG_Eff)
Peak_ECG_Eff[B_Eff] = X_ECG_Eff[B_Eff]

plt.figure(5)

# Plot for ECG Signal at Rest with Peaks
plt.subplot(2, 1, 1)
plt.plot(t, X_ECG_Rep, label='ECG Signal at Rest')
plt.plot(t[B_Rep], Peak_ECG_Rep[B_Rep], 'r*', label='Peaks at Rest')
plt.title('ECG Signal at Rest with Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.legend('|FFT_ECG_Rep(f)|')

# Plot for ECG Signal During Effort with Peaks
plt.subplot(2, 1, 2)
plt.plot(t, X_ECG_Eff, label='ECG Signal During Effort')
plt.plot(t[B_Eff], Peak_ECG_Eff[B_Eff], 'r*', label='Peaks During Effort')
plt.title('ECG Signal During Effort with Peaks')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (mV)')
plt.legend('|FFT_ECG_Eff(f)|')

plt.tight_layout()
plt.show()

### Step 4:

# RR Series

RR_ECG_Rep = np.diff(t[B_Rep])
RR_ECG_Eff = np.diff(t[B_Eff])

plt.figure(6)

# RR intervals for Rest
plt.subplot(2, 1, 1)
plt.plot(RR_ECG_Rep, label='RR Intervals at Rest')
plt.xlabel('Temps (s)')
plt.ylabel('RR Interval (s)')
plt.title('RR Series for ECG at Rest')
plt.legend()

# RR intervals for Effort
plt.subplot(2, 1, 2)
plt.plot(RR_ECG_Eff, label='RR Intervals during Effort')
plt.xlabel('Temps (s)')
plt.ylabel('RR Interval (s)')
plt.title('RR Series for ECG during Effort')
plt.legend()

plt.tight_layout()
plt.show()


#### 5/

# Filtering

# Define bandf filter function
def bandf(data, lowcut, highcut, fs):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(1, [low, high], btype='band')
    return filtfilt(b, a, data)

fc1 = 0.4    # High cutoff frequency
fc2 = 0.04   # Low cutoff frequency
fe_RR = 1     # Theoretical sampling frequency for RR series

# Filter RR series
RR_ECG_Rep_filtre = bandf(RR_ECG_Rep, fc2, fc1, fe_RR)
RR_ECG_Eff_filtre = bandf(RR_ECG_Eff, fc2, fc1, fe_RR)

# Frequency analysis of filtered signals
nb_points_fft = 128
f = fe_RR / 2 * np.linspace(0, 1, nb_points_fft // 2)
TF_RR_ECG_Rep_filtre = np.fft.fft(RR_ECG_Rep_filtre, nb_points_fft)
TF_RR_ECG_Eff_filtre = np.fft.fft(RR_ECG_Eff_filtre, nb_points_fft)

# Plot filtered FFT
plt.figure(7)

# Plot for ECG Signal at Rest
plt.subplot(2, 1, 1)
plt.plot(f, 2 * np.abs(TF_RR_ECG_Rep_filtre[:nb_points_fft // 2]))
plt.title('ECG Signal at Rest filtred')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectre')

# Plot for ECG Signal During Effort
plt.subplot(2, 1, 2)
plt.plot(f, 2 * np.abs(TF_RR_ECG_Eff_filtre[:nb_points_fft // 2]))
plt.title('ECG Signal During Effort filtred')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectre')

plt.tight_layout()
plt.show()

#### 6/

# Apply the Hann window to the filtered RR series and compute the FFT
hann_window_Rep = np.hanning(len(RR_ECG_Rep_filtre))
hann_window_Eff = np.hanning(len(RR_ECG_Eff_filtre))

# Compute the Power Spectral Density (PSD) using FFT
PSD_RR_ECG_Rep_filtre = np.abs(np.fft.fft(RR_ECG_Rep_filtre * hann_window_Rep, nb_points_fft))**2
PSD_RR_ECG_Eff_filtre = np.abs(np.fft.fft(RR_ECG_Eff_filtre * hann_window_Eff, nb_points_fft))**2

# Plot the results
plt.figure(8)

# PSD for RR signal at rest
plt.subplot(2, 1, 1)
plt.plot(f, PSD_RR_ECG_Rep_filtre[:nb_points_fft // 2])
plt.title('PSD of Filtered RR Signal at Rest')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')

# PSD for RR signal during effort
plt.subplot(2, 1, 2)
plt.plot(f, PSD_RR_ECG_Eff_filtre[:nb_points_fft // 2])
plt.title('PSD of Filtered RR Signal During Effort')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')

plt.tight_layout()
plt.show()
