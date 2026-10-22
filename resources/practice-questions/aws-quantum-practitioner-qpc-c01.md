---
last-updated: 2026-10-22
difficulty: advanced
---

# AWS Quantum Practitioner (QPC-C01) - Practice Questions

30 questions for the QPC-C01 anticipated study track, weighted toward Amazon Braket (25%), quantum computing fundamentals (20%), then circuits and gates, hybrid workflows, and algorithms.

This is an anticipated exam rather than a confirmed AWS certification. Treat the questions as study material for quantum computing on AWS, and verify whether the exam exists before planning around it.

> **Cert page:** [exams/aws/specialty/quantum-practitioner-qpc-c01/](../../exams/aws/specialty/quantum-practitioner-qpc-c01/)

---

### Question 1
**Scenario:** What distinguishes a qubit from a classical bit?

A. A qubit is faster because it performs each classical operation in less time than a transistor does
B. A qubit can exist in a superposition of the 0 and 1 basis states until measured
C. A qubit stores more bytes, since each qubit holds exponentially many classical bits that you can read out
D. A qubit cannot be measured directly, so its state can only be inferred from the structure of the circuit

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Superposition means the state is a complex linear combination of basis states, and measurement collapses it to one outcome with a probability given by the amplitudes. Speed and storage framings are the common misconception: quantum advantage comes from interference between amplitudes, not from doing classical work faster.
</details>

---

### Question 2
**Scenario:** Two qubits are entangled. What does that mean operationally?

A. They are copies of each other, created by cloning the first qubit's state onto the second one
B. They always hold the same value, so measuring one qubit tells you the other's value in advance in any basis
C. They are physically adjacent on the chip, which is what lets them share a single quantum state
D. Their joint state cannot be written as a product of individual states, so measurements are correlated

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Entanglement is a property of the joint state, not of proximity, and it is the resource behind most quantum algorithms. Note the correlation does not transmit information by itself, which is why entanglement alone does not enable faster-than-light communication.
</details>

---

### Question 3
**Scenario:** Which Amazon Braket component runs a circuit on a simulator without using QPU time?

A. Braket Hybrid Jobs only, since every circuit has to be submitted from inside a job container
B. A QPU device, which runs the circuit on real hardware and bills only for the runtime that is used
C. S3, which executes the circuit when you upload the circuit file into the results bucket
D. On-demand and local simulators (SV1, DM1, and the local simulators in the SDK)

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Simulators are how you develop and debug: the local simulator runs in your notebook, and the managed simulators scale to more qubits with different methods (state vector and density matrix). Moving to a QPU is a deliberate later step because it costs per shot and per task.
</details>

---

### Question 4
**Scenario:** A Braket task must be run 1,000 times to build a distribution of outcomes.

A. Use 1,000 qubits, one for each repetition, so that all the outcomes are measured together
B. Use 1,000 devices in parallel, one per repetition, and merge the results afterwards
C. Specify 1,000 shots, since each shot is one prepare-and-measure repetition
D. Run the circuit once

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A measurement gives one sample, so the output distribution is estimated by repeating the circuit. Shot count trades statistical precision against cost and time, and it is the main knob you tune per experiment.
</details>

---

### Question 5
**Scenario:** Which gate creates superposition from a basis state?

A. Measurement
B. CNOT
C. Hadamard (H) gate
D. Pauli-X

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** The Hadamard gate maps |0> to an equal superposition of |0> and |1>. Pauli-X is the quantum NOT, flipping the basis state. CNOT is the two-qubit entangling gate, and a Hadamard followed by CNOT is the standard way to build a Bell pair.
</details>

---

### Question 6
**Scenario:** Results from a QPU are noisier than the simulator predicted.

A. The simulator is broken, because a correct simulator would always match the hardware's output exactly and should be reinstalled from a clean image
B. The circuit is wrong, so it must contain a logic error that the ideal simulator happened to hide from the developer
C. The shots were too many, which adds noise because each extra shot is a fresh sample of random hardware errors
D. Current hardware is noisy: gate, decoherence, and readout errors grow with depth, so use shorter circuits and error mitigation

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** This is the defining constraint of the NISQ era. Circuit depth is the practical limit because errors compound per gate, which is why algorithms are designed to be shallow and why error mitigation, distinct from full error correction, is used today.
</details>

---

### Question 7
**Scenario:** A variational algorithm alternates quantum circuit evaluation with classical parameter updates.

A. A Lambda function invoked once per shot, passing each measurement result back to the optimizer
B. Braket Hybrid Jobs, which colocate classical compute with the QPU and manage the optimization loop with priority access
C. A batch job that reads circuits from S3, with each iteration queued as a separate unrelated task
D. A single quantum task submitted once, which runs the whole optimization loop inside the QPU

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Hybrid Jobs run the classical optimizer next to the device with priority access, avoiding queue waits between iterations. Managing the loop from a laptop means every iteration re-queues, which dominates the wall clock for VQE or QAOA.
</details>

---

### Question 8
**Scenario:** Which problem class does Grover's algorithm address?

A. Unstructured search, with a quadratic speedup over brute force
B. Sorting, where it reduces the n log n comparisons to a linear number of steps on a list
C. Linear systems, where it solves them exponentially faster than classical elimination methods do
D. Factoring integers, where it breaks RSA moduli in polynomial time using period finding

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Grover gives roughly a square-root reduction in the number of queries, which is meaningful but not exponential. Shor's algorithm is the factoring one, and it is the exponential-speedup result that motivates post-quantum cryptography.
</details>

---

### Question 9
**Scenario:** An organization asks whether quantum computers threaten their encryption today.

A. Not yet, but harvest-now-decrypt-later means long-lived secrets should move to post-quantum cryptography now
B. Only symmetric encryption is at risk, because Shor's algorithm breaks AES-256 outright but cannot touch RSA or elliptic curves
C. Yes, immediately: a quantum computer capable of breaking RSA-2048 is already operating in several research labs today
D. Never, because quantum computers can only run toy circuits and cannot attack encryption of any kind

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Cryptographically relevant quantum computers do not exist yet, but data captured today can be decrypted later, so the migration timeline is driven by how long your data must stay secret. Asymmetric cryptography is the primary casualty; symmetric keys are weakened by Grover but are addressed by doubling key length.
</details>

---

### Question 10
**Scenario:** Different Braket QPU providers use different qubit technologies.

A. Only price varies, since every provider exposes the same native gates, topology, connectivity, and error rates to Braket
B. Only speed varies, because all providers use the same superconducting design with the same connectivity and the same native gate set
C. They differ (superconducting, trapped ion, neutral atom) in connectivity, gate sets, gate times, and errors
D. They are identical, and Braket hides the hardware differences by compiling every circuit the same way

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hardware choice affects what circuits run well: trapped ions typically offer all-to-all connectivity with slower gates, while superconducting devices are faster with limited connectivity requiring SWAP insertion. Braket's device properties expose the native gate set and topology so you can compile accordingly.
</details>

---

### Question 11
**Scenario:** A circuit uses a two-qubit gate between physically non-adjacent qubits.

A. It runs unchanged, because the hardware applies the two-qubit gate across any pair of qubits equally
B. The compiler inserts SWAP operations to route the qubits, increasing depth and error
C. Connectivity is irrelevant, because every Braket QPU offers all-to-all coupling between its qubits
D. It fails with a validation error, because gates between non-adjacent qubits are not allowed at all

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Transpilation maps logical qubits to physical ones and routes around connectivity limits, and each added SWAP is three CNOTs' worth of error. This is why circuit design that respects the device topology outperforms a naive circuit that relies on the compiler.
</details>

---

### Question 12
**Scenario:** Costs on Braket must be controlled.

A. Run everything on QPUs, so that the results are always real-hardware results and never need to be re-run or checked on a simulator
B. Use the largest device available, since larger devices complete each task faster and so cost less
C. Use simulators during development, size shot counts deliberately, and monitor per-task and per-shot charges
D. Costs are fixed, because Braket charges one flat monthly rate regardless of the tasks, shots, or devices you choose to use

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** QPU billing has both a per-task and a per-shot component, so a loop that submits many small tasks can cost more than its shot count suggests. Develop and validate on simulators, then move to hardware only for the runs that need it.
</details>

---

### Question 13
**Scenario:** What is quantum error correction, as distinct from error mitigation?

A. Correction encodes a logical qubit across many physical qubits to fix errors; mitigation post-processes noisy results
B. Mitigation requires more qubits than correction, because it duplicates the whole circuit in parallel
C. They are the same technique, with correction being the name used for software and mitigation for hardware
D. Correction is available on today's devices at scale, which is why circuit depth is no longer the limit on useful results and error mitigation is obsolete

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Correction is the path to fault tolerance and requires large physical-to-logical qubit ratios that current hardware cannot supply at useful scale. Mitigation techniques such as zero-noise extrapolation are what practitioners use today, and they improve estimates rather than making the computation reliable.
</details>

---

### Question 14
**Scenario:** Results of a Braket task need to be retrieved later.

A. Task results are written to an S3 bucket you specify, retrievable by task ARN, so you can fetch them after the task finishes
B. They are not stored, so the circuit must be rerun whenever you want to read the results again
C. They are returned only synchronously, so the client must stay connected until the task finishes
D. They are emailed to the account's root address as soon as the device finishes the task

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tasks are asynchronous because devices have queues and availability windows, so results land in S3 and are fetched by ARN. This also means the usual S3 controls apply, including encryption and lifecycle for experimental data.
</details>

---

### Question 15
**Scenario:** A business asks which of their problems are candidates for quantum advantage.

A. Machine learning generally, since quantum computers speed up the training of every neural network
B. A narrow set today, such as simulating quantum systems, while classical methods stay stronger for most workloads
C. Every optimization problem, because quantum annealing is proven to beat classical solvers across the board
D. Database queries, since Grover's algorithm gives an exponential speedup for every table lookup in a very large database

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Being honest here is the practitioner's job. Quantum chemistry and materials simulation are the clearest long-term candidates because the problem is natively quantum. Most business optimization is better served today by classical solvers, and claiming otherwise sets up an expensive disappointment.
</details>

---

### Question 16
**Scenario:** A variational algorithm on a QPU runs hundreds of iterations. When each iteration is submitted as a separate task from a laptop, every task waits in the public queue and the run takes days.

A. Submit all iterations at once as one large batch, so that the QPU can run them in any order it chooses
B. Move the optimization loop to an EC2 instance in the same Region, which places its tasks ahead of the queue
C. Run the algorithm as an Amazon Braket Hybrid Job, whose tasks get priority access to the target QPU
D. Switch the target to a managed simulator for every iteration, then report the simulator results as hardware results

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Hybrid Jobs run the classical code in a managed container and give the job's quantum tasks priority access to the chosen QPU while it runs, so iterations do not re-enter the public queue each time. Batching cannot work because each iteration depends on the previous result. Running the loop on EC2 gives no queue priority. Simulator results are not hardware results.
</details>

---

### Question 17
**Scenario:** A researcher wants to see how a 12-qubit circuit behaves under realistic noise, such as depolarizing and amplitude damping channels, before paying for QPU time.

A. The DM1 density matrix simulator, which supports noise channels in the circuit
B. The SV1 state vector simulator, which models noise from the device calibration data
C. The local state vector simulator, which applies the target QPU's noise automatically
D. A QPU with fewer shots, since only real hardware can show the effect of noise on a circuit

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** A density matrix represents mixed states, so DM1 (and the local density matrix simulator) can apply noise channels and show their effect. SV1 and the local state vector simulator simulate ideal pure states and do not add device noise on their own. Noise can be studied on a simulator first, which is the cheaper path.
</details>

---

### Question 18
**Scenario:** A qubit is prepared in an equal superposition of 0 and 1 and then measured 1,000 times, re-preparing it before each shot.

A. Every shot returns the same value, because the first measurement fixes the state for all shots after it
B. Every shot returns a value of 0.5, because measurement reports the average of the two basis states
C. The shots return 0 and 1 in a fixed alternating pattern, because the two basis states are equally weighted
D. About half the shots return 0 and half return 1, with each individual outcome random

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Measurement collapses a superposition to one basis state, with probabilities given by the squared amplitudes, so an equal superposition yields 0 or 1 with 50% probability each. Re-preparing before each shot means earlier results do not carry over. Measurement never returns a fractional value, and outcomes are random, not alternating.
</details>

---

### Question 19
**Scenario:** A circuit applies a Hadamard gate to qubit 0, then a CNOT with qubit 0 as control and qubit 1 as target. Both qubits start in 0.

A. Both qubits end up in 1, because the CNOT flips the target and the Hadamard flips the control
B. The qubits end in a Bell state, so measurements always agree: both 0 or both 1, each half the time
C. Qubit 0 is in superposition and qubit 1 stays 0, because a CNOT acts only on control qubits in basis states
D. The qubits end in four equally likely outcomes, 00, 01, 10, and 11, with no correlation between them

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Hadamard puts qubit 0 in superposition, and the CNOT copies that superposition into a correlation, giving the Bell state (|00> + |11>)/sqrt(2). Outcomes are 00 or 11 with equal probability and never 01 or 10. A CNOT acts linearly on superpositions, so the target does not stay 0, and the outcomes are perfectly correlated rather than independent.
</details>

---

### Question 20
**Scenario:** A logistics team wants to experiment with a combinatorial optimization problem, such as Max-Cut on a graph, using near-term gate-based hardware.

A. Shor's algorithm, which finds the optimal cut by factoring the graph's adjacency matrix
B. Quantum phase estimation, which needs deep circuits and fault tolerance to return a usable answer
C. Grover's algorithm on the full graph, which returns the optimal cut in a single query of the oracle
D. QAOA, a variational algorithm whose parameterized circuit encodes the cost function of the problem

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** The Quantum Approximate Optimization Algorithm encodes a combinatorial cost function in a parameterized circuit and tunes the parameters with a classical optimizer, which fits shallow near-term circuits. Shor's algorithm addresses factoring and discrete logarithms, not graphs. Phase estimation is a fault-tolerant era algorithm. Grover gives a quadratic speedup over many queries, not a one-query answer.
</details>

---

### Question 21
**Scenario:** A chemistry team wants to estimate the ground-state energy of a small molecule on today's noisy hardware.

A. The Variational Quantum Eigensolver, which minimizes the measured energy of a parameterized circuit
B. The Deutsch-Jozsa algorithm, which decides whether the molecule's energy function is constant
C. Shor's algorithm, which finds the ground state by factoring the molecular Hamiltonian
D. Quantum key distribution, which shares the energy estimate securely between two labs

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** VQE prepares a trial state with a shallow parameterized circuit, measures the expected energy, and lets a classical optimizer adjust parameters to find the minimum, which is suited to noisy hardware. Deutsch-Jozsa is a textbook oracle problem. Shor's algorithm is for factoring. QKD is a communication protocol and computes nothing.
</details>

---

### Question 22
**Scenario:** Tasks sent to a QPU stay in the QUEUED state for hours, while the same circuits finish quickly on SV1.

A. The S3 results bucket is full, so the tasks cannot start until older results are deleted
B. The circuit is too deep for the QPU, so Braket holds it in the queue until it can be compiled
C. The QPU runs only during its availability windows and has a queue; check its availability and queue depth
D. The account has run out of simulator minutes, which Braket draws on before running any QPU task

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** QPUs are shared physical devices that run during provider availability windows and process tasks from a queue, so tasks can wait. The SDK and console show device availability and queue depth. S3 buckets do not fill up. A circuit the device cannot run fails validation rather than waiting. Simulator usage does not gate QPU tasks.
</details>

---

### Question 23
**Scenario:** A team has existing circuits written in OpenQASM 3 and wants to run them on Braket without rewriting them in another SDK.

A. Translate each circuit by hand into the Braket Python SDK, since Braket only accepts its own circuit objects
B. Submit the OpenQASM 3 programs directly as Braket tasks, which Braket accepts as an input format
C. Convert the circuits to a Hybrid Job container image, since only jobs can accept text-based programs
D. Upload the files to the S3 results bucket, which triggers Braket to run each program as a task

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Braket supports OpenQASM 3.0 as a program format for gate-based devices and simulators, so the programs can be submitted as they are. Rewriting is unnecessary. Hybrid Jobs are for iterative classical-quantum workloads, not a format conversion step. Uploading to S3 does not start tasks.
</details>

---

### Question 24
**Scenario:** A research group needs guaranteed, exclusive time on a specific QPU for a scheduled week of experiments, without competing with the public queue.

A. Run the tasks as a Hybrid Job, which reserves the device exclusively for the whole week
B. Set a higher shot count on each task, which raises its priority in the device's public queue
C. Submit the tasks at night, when Braket guarantees an empty queue on every QPU device
D. Book a reservation through Amazon Braket Direct for dedicated access to the device

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Braket Direct lets you reserve dedicated capacity on a QPU for a set time window, billed for the reservation rather than per task and shot. Hybrid Jobs give priority while the job runs but are not an exclusive scheduled booking. Shot count does not change queue priority, and no time of day guarantees an empty queue.
</details>

---

### Question 25
**Scenario:** A deep circuit gives near-random results on hardware, while a shallower version of the same algorithm works. What physical limit is the most likely cause?

A. The qubits ran out of memory, since each gate stores its result on the qubit until the circuit finishes
B. Decoherence, since qubits lose their quantum state over time, so long circuits exceed the coherence time
C. The S3 bucket throttled the results, since deeper circuits write more data back for each shot
D. The classical optimizer diverged, since deep circuits cannot be run without a classical feedback loop

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Qubits interact with their environment and lose phase and energy over characteristic times (often called T1 and T2). Each gate also adds error, so deep circuits accumulate noise until the output is near random. Qubits do not have memory in the classical sense. Result storage does not affect the outcome, and a fixed circuit has no optimizer.
</details>

---

### Question 26
**Scenario:** A developer notices that each added qubit makes state vector simulation dramatically slower, and that simulating around 50 qubits this way is impractical.

A. The simulator adds one gate per qubit, so runtime grows linearly but the constant factor is large
B. The simulator stores results in S3, and object writes slow down as qubit counts rise
C. A state of n qubits has 2^n complex amplitudes, so memory and time double with each added qubit
D. Simulators can only use one CPU core per qubit, and managed instances are capped at a few dozen cores

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** A full state vector for n qubits holds 2^n amplitudes, so memory and compute grow exponentially. This is why state vector simulation tops out in the low tens of qubits on any machine. The growth is exponential, not linear, and is not caused by storage or core limits.
</details>

---

### Question 27
**Scenario:** A qubit is expected to be in the |+> state. Braket measures in the computational (Z) basis, but the team wants to confirm the qubit is in |+> rather than |->.

A. Apply a Hadamard gate before measurement, which maps |+> to |0> and |-> to |1>
B. Apply a CNOT to an extra qubit, then measure only that extra qubit in the Z basis
C. Measure in the Z basis with more shots, since |+> and |-> give different Z statistics
D. Apply an X gate before measurement, which maps |+> to |1> and |-> to |0>

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** |+> and |-> differ only in relative phase, so Z-basis measurement gives 50/50 for both no matter how many shots. A Hadamard rotates the X basis into the Z basis, turning |+> into |0> and |-> into |1>, so the measurement now distinguishes them. An X gate leaves |+> unchanged and gives |-> only a global phase, so it does not help. Copying into a second qubit with a CNOT still measures in the Z basis.
</details>

---

### Question 28
**Scenario:** A team wants to train a quantum circuit as part of a machine learning model, using automatic differentiation and a familiar Python interface, on Braket devices.

A. Write a custom gradient routine in the Braket SDK, since Braket has no integration with any ML framework
B. Export the circuit to Amazon SageMaker, which converts it into a classical neural network
C. Use PennyLane with the Amazon Braket plugin, which computes gradients of quantum circuits
D. Submit it as an analog Hamiltonian program, which Braket differentiates on its own

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** PennyLane is a quantum ML library with automatic differentiation of quantum circuits, and its Braket plugin runs those circuits on Braket simulators and QPUs, including inside Hybrid Jobs. A custom routine is unnecessary. SageMaker does not convert circuits into classical networks. Analog Hamiltonian programs are a different paradigm and are not differentiated automatically.
</details>

---

### Question 29
**Scenario:** Before running a notebook that submits many tasks, a developer wants an estimate of what the simulator and QPU tasks in it will cost.

A. Check the monthly AWS invoice, the only place where Braket task charges are recorded
B. Wrap the code in the Braket SDK cost Tracker, which reports estimated charges for tasks
C. Count the qubits in each circuit, since Braket charges a flat price per qubit used
D. Set a shot limit on the account, which caps the total Braket spend for each month

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** The Braket SDK's Tracker records the tasks created inside its context and reports simulator time and estimated QPU charges, so you can see costs while you work. The invoice arrives too late to guide development. Braket does not price by qubit count. There is no account-level shot cap that acts as a budget, though AWS Budgets can alert on spend.
</details>

---

### Question 30
**Scenario:** Before targeting a QPU, a developer needs its native gate set, qubit connectivity, and latest calibration data to design a circuit that compiles well.

A. Run a test task with many shots and infer the gates and connectivity from the measurement results
B. Read the device properties from the GetDevice API, the SDK device object, or the console Devices tab
C. Open a support case, since device topology is shared with customers only on request
D. Read the CloudWatch metrics for the device, which publish its gate set and calibration values

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Each Braket device exposes its properties, including native gates, topology, and calibration data, through the GetDevice API, the SDK's device.properties, and the console. Inferring them from test runs costs money and is unreliable. The data is public, so no support case is needed. CloudWatch does not publish gate sets or calibration values.
</details>

---

## Where to go deeper

- [QPC-C01 cert page](../../exams/aws/specialty/quantum-practitioner-qpc-c01/) - notes, practice plan, strategy
- [AWS Cloud Practitioner practice questions](./aws-cloud-practitioner.md) - the AWS foundations this assumes
- **[📖 Amazon Braket documentation](https://docs.aws.amazon.com/braket/)** - primary source
- **[📖 AWS Certification](https://aws.amazon.com/certification/)** - confirm which exams currently exist
