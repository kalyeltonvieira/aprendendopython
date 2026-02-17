import qiskit

A = qiskit.QuantumCircuit(2)
A.h(0)
A.cx(0, 1)
print(A)