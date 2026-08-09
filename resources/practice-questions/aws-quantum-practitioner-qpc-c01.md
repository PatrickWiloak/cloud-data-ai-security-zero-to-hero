---
last-updated: 2026-08-09
difficulty: advanced
---

# AWS Quantum Practitioner (QPC-C01) - Practice Questions

15 questions for the QPC-C01 anticipated study track, weighted toward Amazon Braket (25%), quantum computing fundamentals (20%), then circuits and gates, hybrid workflows, and algorithms.

This is an anticipated exam rather than a confirmed AWS certification. Treat the questions as study material for quantum computing on AWS, and verify whether the exam exists before planning around it.

> **Cert page:** [exams/aws/specialty/quantum-practitioner-qpc-c01/](../../exams/aws/specialty/quantum-practitioner-qpc-c01/)

---

### Question 1
**Scenario:** What distinguishes a qubit from a classical bit?

A. A qubit is faster
B. A qubit can exist in a superposition of the 0 and 1 basis states until measured
C. A qubit stores more bytes
D. A qubit cannot be measured

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Superposition means the state is a complex linear combination of basis states, and measurement collapses it to one outcome with a probability given by the amplitudes. Speed and storage framings are the common misconception: quantum advantage comes from interference between amplitudes, not from doing classical work faster.
</details>

---

### Question 2
**Scenario:** Two qubits are entangled. What does that mean operationally?

A. They are physically adjacent
B. Their joint state cannot be written as a product of individual states, so measuring one determines correlations with the other
C. They have the same value
D. They are copies

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Entanglement is a property of the joint state, not of proximity, and it is the resource behind most quantum algorithms. Note the correlation does not transmit information by itself, which is why entanglement alone does not enable faster-than-light communication.
</details>

---

### Question 3
**Scenario:** Which Amazon Braket component runs a circuit on a simulator without using QPU time?

A. On-demand and local simulators (SV1, DM1, TN1, and the local simulator)
B. A QPU device
C. Braket Hybrid Jobs only
D. S3

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Simulators are how you develop and debug: the local simulator runs in your notebook, and the managed simulators scale to more qubits with different methods (state vector, density matrix, tensor network). Moving to a QPU is a deliberate later step because it costs per shot and per task.
</details>

---

### Question 4
**Scenario:** A Braket task must be run 1,000 times to build a distribution of outcomes.

A. Run the circuit once
B. Specify 1,000 shots, since each shot is one prepare-and-measure repetition
C. Use 1,000 qubits
D. Use 1,000 devices

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A measurement gives one sample, so the output distribution is estimated by repeating the circuit. Shot count trades statistical precision against cost and time, and it is the main knob you tune per experiment.
</details>

---

### Question 5
**Scenario:** Which gate creates superposition from a basis state?

A. Hadamard
B. CNOT
C. Pauli-X
D. Measurement

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The Hadamard gate maps |0> to an equal superposition of |0> and |1>. Pauli-X is the quantum NOT, flipping the basis state. CNOT is the two-qubit entangling gate, and a Hadamard followed by CNOT is the standard way to build a Bell pair.
</details>

---

### Question 6
**Scenario:** Results from a QPU are noisier than the simulator predicted.

A. The circuit is wrong
B. Current hardware is noisy: gate errors, decoherence, and readout error accumulate with circuit depth, so mitigate with shorter circuits and error mitigation techniques
C. The shots were too many
D. The simulator is broken

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** This is the defining constraint of the NISQ era. Circuit depth is the practical limit because errors compound per gate, which is why algorithms are designed to be shallow and why error mitigation, distinct from full error correction, is used today.
</details>

---

### Question 7
**Scenario:** A variational algorithm alternates quantum circuit evaluation with classical parameter updates.

A. Braket Hybrid Jobs, which colocate classical compute with the QPU and manage the loop
B. A single quantum task
C. A Lambda per shot
D. A batch job on S3

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Hybrid Jobs run the classical optimizer next to the device with priority access, avoiding queue waits between iterations. Managing the loop from a laptop means every iteration re-queues, which dominates the wall clock for VQE or QAOA.
</details>

---

### Question 8
**Scenario:** Which problem class does Grover's algorithm address?

A. Factoring integers
B. Unstructured search, with a quadratic speedup over classical brute force
C. Linear systems
D. Sorting

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Grover gives roughly a square-root reduction in the number of queries, which is meaningful but not exponential. Shor's algorithm is the factoring one, and it is the exponential-speedup result that motivates post-quantum cryptography.
</details>

---

### Question 9
**Scenario:** An organization asks whether quantum computers threaten their encryption today.

A. Yes, immediately
B. Not with current hardware, but harvest-now-decrypt-later means long-lived secrets should migrate to post-quantum algorithms now
C. Never
D. Only symmetric encryption is at risk

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Cryptographically relevant quantum computers do not exist yet, but data captured today can be decrypted later, so the migration timeline is driven by how long your data must stay secret. Asymmetric cryptography is the primary casualty; symmetric keys are weakened by Grover but are addressed by doubling key length.
</details>

---

### Question 10
**Scenario:** Different Braket QPU providers use different qubit technologies.

A. They are identical
B. They differ (superconducting, trapped ion, neutral atom), with different connectivity, gate sets, gate times, and error characteristics
C. Only speed varies
D. Only price varies

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hardware choice affects what circuits run well: trapped ions typically offer all-to-all connectivity with slower gates, while superconducting devices are faster with limited connectivity requiring SWAP insertion. Braket's device properties expose the native gate set and topology so you can compile accordingly.
</details>

---

### Question 11
**Scenario:** A circuit uses a two-qubit gate between physically non-adjacent qubits.

A. It fails
B. The compiler inserts SWAP operations to route the qubits, increasing depth and error
C. It runs unchanged
D. Connectivity is irrelevant

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transpilation maps logical qubits to physical ones and routes around connectivity limits, and each added SWAP is three CNOTs' worth of error. This is why circuit design that respects the device topology outperforms a naive circuit that relies on the compiler.
</details>

---

### Question 12
**Scenario:** Costs on Braket must be controlled.

A. Costs are fixed
B. Use simulators during development, size shot counts deliberately, and monitor per-task and per-shot charges plus Hybrid Jobs instance time
C. Run everything on QPUs
D. Use the largest device

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** QPU billing has both a per-task and a per-shot component, so a loop that submits many small tasks can cost more than its shot count suggests. Develop and validate on simulators, then move to hardware only for the runs that need it.
</details>

---

### Question 13
**Scenario:** What is quantum error correction, as distinct from error mitigation?

A. They are the same
B. Correction encodes a logical qubit across many physical qubits to detect and fix errors during computation; mitigation post-processes noisy results without correcting the computation
C. Mitigation requires more qubits
D. Correction is available on today's devices at scale

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Correction is the path to fault tolerance and requires large physical-to-logical qubit ratios that current hardware cannot supply at useful scale. Mitigation techniques such as zero-noise extrapolation are what practitioners use today, and they improve estimates rather than making the computation reliable.
</details>

---

### Question 14
**Scenario:** Results of a Braket task need to be retrieved later.

A. They are returned only synchronously
B. Task results are written to an S3 bucket you specify, retrievable by task ARN
C. They are emailed
D. They are not stored

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Tasks are asynchronous because devices have queues and availability windows, so results land in S3 and are fetched by ARN. This also means the usual S3 controls apply, including encryption and lifecycle for experimental data.
</details>

---

### Question 15
**Scenario:** A business asks which of their problems are candidates for quantum advantage.

A. All optimization problems
B. A narrow set today: research into simulation of quantum systems, certain optimization and sampling problems, with classical methods still stronger for most production workloads
C. Machine learning generally
D. Database queries

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Being honest here is the practitioner's job. Quantum chemistry and materials simulation are the clearest long-term candidates because the problem is natively quantum. Most business optimization is better served today by classical solvers, and claiming otherwise sets up an expensive disappointment.
</details>

---

## Where to go deeper

- [QPC-C01 cert page](../../exams/aws/specialty/quantum-practitioner-qpc-c01/) - notes, practice plan, strategy
- [AWS Cloud Practitioner practice questions](./aws-cloud-practitioner.md) - the AWS foundations this assumes
- **[📖 Amazon Braket documentation](https://docs.aws.amazon.com/braket/)** - primary source
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - confirm which exams currently exist
