---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 7 min
---

# 02 - Deep learning fundamentals

---

## Neural networks

A neural network is layers of connected **neurons**. Each neuron takes inputs, multiplies them by **weights**, adds a **bias**, and passes the result through an **activation function**.

- **Input layer** - receives the features
- **Hidden layers** - learn intermediate representations. "Deep" means more than one
- **Output layer** - produces the prediction

**Activation functions** introduce non-linearity, without which the whole network collapses into a single linear transformation:

| Function | Range | Typically used |
|---|---|---|
| **ReLU** | 0 to infinity | Hidden layers; the default |
| **Sigmoid** | 0 to 1 | Binary classification output |
| **Softmax** | 0 to 1, summing to 1 | Multi-class classification output |
| **Tanh** | -1 to 1 | Hidden layers, older architectures |

---

## Training

1. **Forward propagation** - inputs flow through the network to a prediction
2. **Loss function** - measures how wrong the prediction is (cross-entropy for classification, mean squared error for regression)
3. **Backpropagation** - computes how much each weight contributed to the error
4. **Gradient descent** - adjusts weights to reduce the loss
5. Repeat over many passes

**Parameters versus hyperparameters** is a reliably tested distinction:
- **Parameters** are the weights and biases, **learned** during training
- **Hyperparameters** are set **before** training: learning rate, number of epochs, batch size, number of layers, number of neurons per layer

| Hyperparameter | Meaning | If wrong |
|---|---|---|
| **Learning rate** | Step size for weight updates | Too high, training diverges; too low, training crawls |
| **Epoch** | One full pass over the training data | Too few, underfitting; too many, overfitting |
| **Batch size** | Examples processed before a weight update | Affects memory use and training stability |

Techniques to reduce overfitting: **dropout** (randomly disable neurons during training), **regularization** (penalize large weights), **early stopping**, and **data augmentation**.

---

## Architectures

| Architecture | Suited to | Why |
|---|---|---|
| **Feedforward (dense)** | Tabular data | The simplest fully connected form |
| **CNN** (convolutional) | Images and video | Convolution detects local spatial patterns and reuses filters across the image |
| **RNN** (recurrent) | Sequences: text, time series, audio | Maintains state across a sequence |
| **LSTM / GRU** | Longer sequences | Gating mechanisms mitigate the vanishing gradient problem of plain RNNs |
| **Transformer** | Language, and increasingly vision | Attention relates all positions in parallel, so it trains far faster than an RNN and handles long-range dependencies better |
| **GAN** | Image generation | A generator and a discriminator trained against each other |
| **Autoencoder** | Compression, denoising, anomaly detection | Learns to reconstruct its input through a narrow bottleneck |

Transformers replaced RNNs for language because attention removes the sequential bottleneck: an RNN must process tokens one at a time, while a transformer processes the whole sequence in parallel.

---

## Why GPUs

Training is dominated by matrix multiplication, which is **massively parallel**. A CPU has a few dozen powerful cores optimized for sequential work; a GPU has thousands of simpler cores optimized for doing the same operation across a lot of data at once.

For large models, one GPU is not enough, so training is **distributed** across many, which makes the interconnect between them the bottleneck. That is why OCI offers **RDMA cluster networking**: low-latency, high-throughput node-to-node communication for distributed training.

**Inference** is much cheaper than training, and often runs on smaller GPUs or CPUs, which is why the two are priced and provisioned separately.

---

## Key terms

- **Neuron** - the basic unit computing a weighted sum of inputs passed through an activation function
- **Weight** - a learned parameter scaling an input to a neuron
- **Bias** - a learned parameter offsetting a neuron's weighted sum
- **Activation function** - a non-linear function applied to a neuron's output, enabling the network to learn non-linear patterns
- **ReLU** - the rectified linear unit, the common default activation for hidden layers
- **Softmax** - the output activation producing a probability distribution across classes
- **Forward propagation** - passing inputs through the network to produce a prediction
- **Loss function** - the measure of how far a prediction is from the correct answer
- **Backpropagation** - the algorithm computing each weight's contribution to the loss
- **Gradient descent** - the optimization method adjusting weights to reduce loss
- **Parameter** - a value learned during training, such as a weight or bias
- **Hyperparameter** - a value set before training, such as learning rate or batch size
- **Learning rate** - the step size used when updating weights
- **Epoch** - one complete pass through the training dataset
- **Batch size** - the number of examples processed before each weight update
- **Dropout** - randomly disabling neurons during training to reduce overfitting
- **CNN** - a convolutional neural network, suited to images and spatial data
- **RNN** - a recurrent neural network, suited to sequential data
- **LSTM** - a recurrent architecture using gates to handle longer sequences
- **Transformer** - the attention-based architecture underlying modern language models
- **GAN** - a generative adversarial network, training a generator against a discriminator
- **Autoencoder** - a network learning to reconstruct its input through a compressed representation
- **RDMA cluster networking** - low-latency high-throughput interconnect used for distributed GPU training

---

## Related

- [Notes 03: generative AI and LLMs](./03-generative-ai-and-llms.md)
- [Transformer architecture](../../../../learn/concepts/transformer-architecture.md)
