import numpy as np
import matplotlib.pyplot as plt
import cmath

# Complex sensor data
data = [3 + 4j, 1 - 2j, -2 + 5j, 4 - 3j, -1 + 1j]

# Extract magnitudes and phase angles (in degrees)
magnitudes = [abs(num) for num in data]
phases = [cmath.phase(num) * (180 / np.pi) for num in data]  # Convert radians to degrees

# --- Polar Plot (Phase Angle vs. Magnitude) ---
fig, ax = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': 'polar'})

# Convert degrees to radians for plotting
angles_rad = [np.deg2rad(angle) for angle in phases]
ax[0].scatter(angles_rad, magnitudes, color='r', label="Sensor Readings")
ax[0].set_title("Polar Plot: Magnitude & Phase Angle")
ax[0].set_theta_zero_location("E")  # Set 0° to the right
ax[0].set_theta_direction(-1)  # Clockwise
ax[0].legend()

# --- Waveform Plot (Real & Imaginary Parts as Waves) ---
t = np.linspace(0, 2*np.pi, 100)
real_wave = [num.real * np.cos(t) for num in data]
imag_wave = [num.imag * np.sin(t) for num in data]

for i in range(len(data)):
    ax[1].plot(t, real_wave[i], linestyle='solid', label=f"Real {data[i]}")
    ax[1].plot(t, imag_wave[i], linestyle='dashed', label=f"Imag {data[i]}")

ax[1].set_title("Waveform of Real & Imaginary Parts")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Amplitude")
ax[1].legend()

plt.tight_layout()
plt.show()
