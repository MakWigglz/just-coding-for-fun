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
