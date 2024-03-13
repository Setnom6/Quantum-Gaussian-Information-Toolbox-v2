import QuGIT_v2.qgt as qgt
import numpy as np

"""
In this script we define some elementary states and print their properties.
"""

# Define a two_mode thermal Gaussian State with different temperatures ( number of quanta) for each mode

state1 = qgt.Gaussian_state("thermal", 1, 0.5)
state2 = qgt.Gaussian_state("thermal", 1, 0.25)
state = qgt.tensor_product([state1,state2])

# Another option is to directly use

state = qgt.elementary_states("thermal", [0.5, 0.25])

# Print some of its properties

print(f"{state}\n")


eigs = state.symplectic_eigenvalues() # Calculate its symplectic eigenvalues

print(f"Symplectic eigenvalues: {eigs}\n")

# Perform a symplectic transformation, a two-mode squeezing of intensity 5 and angle 0 and print the transformed state

state.two_mode_squeezing(5,0)

print(f"{state}\n")

eigs2 = state.symplectic_eigenvalues() # Calculate its symplectic eigenvalues once the transformation is performed

print(f"Symplectic eigenvalues: {eigs2}\n")

# The symplectic eigenvalues are still above value 1, at the should be for a physical state. 
# In the LogNeg scripts the symplectic eigenvalues of the partially transposed matrix are computed to check if the state is entangled.

