Python script using the cmath module to analyze a dataset where complex numbers represent data points with magnitude and phase (angle).

Example: Complex Number Data Management
Scenario:
Let’s say we’re processing sensor data, where each reading has:

Magnitude (absolute value) representing signal strength.

Phase (angle in radians) representing direction or frequency shift.

We’ll:

Store complex data in a list.

Calculate the total energy (sum of squared magnitudes).

Find the dominant phase angle (average phase).

python
import cmath

# Example dataset: Complex numbers representing sensor readings
data = [3 + 4j, 1 - 2j, -2 + 5j, 4 - 3j, -1 + 1j]

# Compute total energy (sum of squared magnitudes)
total_energy = sum(abs(num) ** 2 for num in data)

# Compute average phase angle
average_phase = sum(cmath.phase(num) for num in data) / len(data)

# Display results
print(f"Total Energy: {total_energy:.2f}")
print(f"Average Phase: {average_phase:.2f} radians")

# Convert average phase to degrees for easier interpretation
print(f"Average Phase: {cmath.degrees(average_phase):.2f}°")
Why This Is Useful?
Signal Processing: Helps analyze power levels and frequency shifts in communication systems.

Financial Data: Complex numbers can model certain types of asset movements (e.g., stock trends with phase shifts).

Scientific Simulations: Used in wave mechanics, quantum calculations, and control systems.
