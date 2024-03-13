import QuGIT_v2.qgt as qgt
import numpy as np

"""
In this script we explore the Logarithmic Negativity.
"""

# Create an input state with no entanglement, such us a 3-mode vacuum state

state = qgt.Gaussian_state("vacuum", 3)

# Print the state and the symplectic eigenvalues of the partially transposed matrix

print(f"{state}\n") 

partial = state.partial_transpose([0]) # Partial transpose of the state with respect to mode 0
print(f"Symplectic eigenvalues of the partially transposed matrix: {partial.symplectic_eigenvalues()}\n")

# perform a tranformation between some of their modes

state.two_mode_squeezing(1,0,[0,2]) # intensity 1, angle 0, modes 0 and 2
state.two_mode_squeezing(2,0,[1,2]) # intensity 2, angle 0, modes 1 and 2

# Print again the partially transposed matrix symplectic eigenvalues and see that they are below 1, so the state is entangled

partial = state.partial_transpose([0]) # Partial transpose of the state with respect to mode 0
print(f"Symplectic eigenvalues of the partially transposed matrix: {partial.symplectic_eigenvalues()}\n")


# Compute the Logarithmic Negativity of the state

logneg = state.logarithmic_negativity([0]) # Logarithmic Negativity of the state with respect to mode 0

print(f"Logarithmic Negativity: {logneg}\n")