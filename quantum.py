import numpy as np


class QuantumState:
    def __init__(self, alpha: 'complex', beta: 'complex'):
        self.state = np.empty([alpha, beta])

class ZeroState:
    def __init__(self):
        self.state = np.array([1+0j, 0+0j])


class OneState:
    def __init__(self):
        self.state = np.array([0+0j, 0+1j])
        

class QuantumRegister:
    def __init__(self, n: int):
        self.n_qubits = n
        self.n_states = 1 << n
        self.vector = None
        self.qubits_states = []
        
        for state in range(len(self.qubits_states):
            self.qubits.append(Qubit)


def hadamard(quantum_state):
    return

def hadamard_reg(quantum_state):
    return
