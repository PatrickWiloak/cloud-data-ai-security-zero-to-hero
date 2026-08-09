---
last-updated: 2026-08-09
difficulty: beginner
reading-time: 9 min
---

# 01 - AI and machine learning fundamentals

---

## How the terms nest

**Artificial intelligence** is the broad field of systems performing tasks that would require human intelligence. **Machine learning** is a subset where systems learn patterns from data rather than following explicitly programmed rules. **Deep learning** is a subset of machine learning using multi-layer neural networks. **Generative AI** is an application of deep learning that produces new content.

Task categories Oracle uses: **language**, **speech**, **vision**, and **decision**.

---

## Types of learning

| Type | Data | Learns | Examples |
|---|---|---|---|
| **Supervised** | Labelled | To predict a label | Classification, regression |
| **Unsupervised** | Unlabeled | Structure in the data | Clustering, dimensionality reduction, anomaly detection |
| **Reinforcement** | Feedback from an environment | A policy maximizing reward | Game playing, robotics, control |

**Supervised** splits into:
- **Classification**: predict a **category**. Spam or not spam, which of five defect types, will the customer churn
- **Regression**: predict a **continuous value**. House price, tomorrow's demand, time to failure

The tell in a question: if the answer is a number on a scale, it is regression; if it is one of a fixed set of labels, it is classification.

**Unsupervised** includes:
- **Clustering** (k-means): group similar items with no predefined groups
- **Dimensionality reduction** (PCA): reduce features while retaining information
- **Anomaly detection**: identify points that do not fit the learned pattern

---

## The machine learning workflow

1. **Problem definition** - what are we predicting, and what does success mean
2. **Data collection**
3. **Data preparation** - cleaning, handling missing values, encoding, normalizing
4. **Feature engineering** - creating the inputs the model actually learns from, often the highest-leverage step
5. **Split** - training, validation, and test sets
6. **Model selection and training**
7. **Evaluation** on held-out data
8. **Deployment**
9. **Monitoring** - watching for drift, where the live data diverges from the training data and performance degrades

**Why three splits**: the **training set** fits the model, the **validation set** tunes hyperparameters, and the **test set** is held back untouched so the final estimate is honest. Tuning against the test set contaminates it.

---

## Overfitting and underfitting

| | Training performance | Test performance | Cause | Fix |
|---|---|---|---|---|
| **Overfitting** | High | Low | Model memorized the training data, including its noise | More data, regularization, simpler model, early stopping, cross-validation |
| **Underfitting** | Low | Low | Model too simple to capture the pattern | More complex model, better features, train longer |
| **Good fit** | High | High | - | - |

The **bias-variance trade-off** describes this: high bias means the model is too simple (underfitting), high variance means it is too sensitive to the training data (overfitting).

---

## Evaluation metrics

For **classification**, start with the **confusion matrix**:

|  | Predicted positive | Predicted negative |
|---|---|---|
| **Actually positive** | True positive (TP) | False negative (FN) |
| **Actually negative** | False positive (FP) | True negative (TN) |

| Metric | Formula | Answers |
|---|---|---|
| **Accuracy** | (TP + TN) / all | What proportion did I get right overall |
| **Precision** | TP / (TP + FP) | Of what I flagged, how much was correct |
| **Recall** (sensitivity) | TP / (TP + FN) | Of what I should have found, how much did I find |
| **F1** | Harmonic mean of precision and recall | A single balanced score |

**Accuracy misleads on imbalanced data.** A fraud model on a dataset that is 99.9% legitimate can predict "not fraud" every time and score 99.9%, while catching nothing.

Choose by the cost of the error: **recall** when a miss is expensive (disease screening, fraud), **precision** when a false alarm is expensive (blocking legitimate email).

For **regression**: mean absolute error (MAE), mean squared error (MSE), root mean squared error (RMSE), and R-squared. MSE and RMSE penalize large errors more heavily.

---

## Common algorithms

| Algorithm | Type | Used for |
|---|---|---|
| **Linear regression** | Supervised | Predicting a continuous value |
| **Logistic regression** | Supervised | Binary classification, despite the name |
| **Decision tree** | Supervised | Classification and regression, highly interpretable |
| **Random forest** | Supervised | Many trees combined, more accurate and less prone to overfitting |
| **Support vector machine** | Supervised | Classification with a clear margin between classes |
| **k-nearest neighbours** | Supervised | Classification by similarity to nearby examples |
| **k-means** | Unsupervised | Clustering into k groups |
| **PCA** | Unsupervised | Dimensionality reduction |

---

## Responsible AI

Oracle's framing, and a source of exam questions:

- **Fairness** - the system does not produce discriminatory outcomes across groups
- **Transparency** - users know they are interacting with AI and understand its role
- **Explainability** - decisions can be explained to the people they affect
- **Accountability** - a human is responsible for outcomes
- **Privacy** - personal data is protected throughout the lifecycle
- **Robustness and safety** - the system behaves reliably, including under unexpected input

**Bias** enters through the data (historical bias reflected in training examples), the sampling (unrepresentative data), or the labeling (subjective human judgement).

---

## Key terms

- **Artificial intelligence** - systems performing tasks that would otherwise require human intelligence
- **Machine learning** - systems that learn patterns from data rather than following explicit rules
- **Deep learning** - machine learning using multi-layer neural networks
- **Supervised learning** - learning from labeled data to predict a label
- **Unsupervised learning** - finding structure in unlabeled data
- **Reinforcement learning** - learning a policy from reward feedback in an environment
- **Classification** - predicting a discrete category
- **Regression** - predicting a continuous numeric value
- **Clustering** - grouping similar items without predefined labels
- **Feature engineering** - creating the input variables a model learns from
- **Training set** - the data used to fit the model
- **Validation set** - the data used to tune hyperparameters
- **Test set** - held-out data used once for an honest performance estimate
- **Overfitting** - a model that memorizes training data and generalizes poorly
- **Underfitting** - a model too simple to capture the underlying pattern
- **Bias-variance trade-off** - the tension between a model being too simple and too sensitive to its training data
- **Confusion matrix** - the table of true and false positives and negatives used to evaluate a classifier
- **Precision** - the proportion of positive predictions that were correct
- **Recall** - the proportion of actual positives that were correctly identified
- **F1 score** - the harmonic mean of precision and recall
- **Model drift** - degradation of model performance as live data diverges from training data
- **Explainability** - the ability to explain a model's decision to an affected person

---

## Related

- [Notes 02: deep learning](./02-deep-learning.md)
- [AI from scratch](../../../../learn/ai-from-scratch.md)
