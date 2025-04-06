# Script to get the list of IBM backends

# Load libraries 
from qiskit_ibm_runtime import QiskitRuntimeService
import keyring as k3

# Get the API token from keyring
api_token = k3.get_password('ibm_quantum', 'api_key')

# Available backends
# This script lists all available backends and finds the least busy one
service = QiskitRuntimeService(channel="ibm_quantum", token=api_token)
backends = service.backends()
print("Available backends:")
for backend in backends:
    print(f"{backend.name}")

# Find the least busy backend
# This script finds the least busy backend and prints its name
least_busy_backend = service.least_busy()
print("Least busy backend:")
print(least_busy_backend.name)

