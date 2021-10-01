from qiskit.circuit.library import QuantumVolume
from qiskit.compiler import transpile

from qiskit.test.mock import FakeMontreal

backend = FakeMontreal()
backend.set_options(method="stabilizer")

qc = QuantumVolume(10)
qc.measure_all()
tqc = transpile(
    qc, backend, optimization_level=3, routing_method="sabre",
    layout_method="sabre"
)
results = backend.run(tqc, shots=1e6).result()
print(results.get_counts())
