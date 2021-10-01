import gzip
from qiskit.circuit.library import EfficientSU2
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import Parameter

from qiskit.circuit.qpy_serialization import load, dump

gamma = Parameter("$\\gamma$")
qc = QuantumCircuit(4)
for i in range(4):
    qc.h(i)
qc.append(EfficientSU2(4), [0, 1, 2, 3])
for pair in [(0, 1), (1, 2), (2, 3), (3, 0)]:
    qc.rzz(2 * gamma, *pair)
    qc.barrier()
qc.measure_all()

with gzip.open("test.qpy.gz", "wb") as qpy_file:
    dump(qc, qpy_file)

with gzip.open("test.qpy.gz", "rb") as qpy_file:
    loaded_circuit = load(qpy_file)[0]
