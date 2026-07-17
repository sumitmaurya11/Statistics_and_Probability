# 📊 Probability Foundations with Python

A beginner-friendly Python project that demonstrates core probability concepts using **Pandas** and a simple customer purchase dataset.

## 📖 Overview

This project analyzes customer purchase behavior by calculating different types of probabilities from a dataset containing coffee and pastry purchases.

It covers:

- Marginal Probability
- Joint Probability
- Conditional Probability
- Complement Rule
- Independent Events

---

## 🚀 Features

- Calculate the marginal probability of buying coffee and pastry.
- Compute the joint probability of customers buying both coffee and pastry.
- Calculate conditional probabilities:
  - P(Pastry | Coffee)
  - P(Coffee | Pastry)
- Demonstrate that conditional probabilities are generally not equal.
- Use the complement rule to calculate the probability that at least one of two independent customers buys a pastry.
- Calculate the probability that neither customer buys a pastry.

---

## 🛠️ Technologies Used

- Python 3
- Pandas

---

## 📂 Dataset

The dataset is created directly in the code using a Python dictionary.

```python
data = {
    "customer_id": [1,2,3,4,5,6,7,8,9,10],
    "bought_coffee": [1,1,0,1,0,1,1,0,1,0],
    "bought_pastry": [1,0,1,1,0,0,1,0,1,0]
}
```

---

## 📐 Probability Concepts

### Marginal Probability

Measures the probability of a single event.

Example:

- P(Coffee)
- P(Pastry)

---

### Joint Probability

Probability that both events occur simultaneously.

```
P(Coffee ∩ Pastry)
```

---

### Conditional Probability

Calculated using:

```
P(A|B) = P(A ∩ B) / P(B)
```

Examples:

- P(Pastry | Coffee)
- P(Coffee | Pastry)

---

### Complement Rule

Used to calculate the probability of at least one success.

```
P(At least one) = 1 − P(Neither)
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/sumitmaurya11/probability-foundations.git
```

Navigate to the project:

```bash
cd probability-foundations
```

Install dependencies:

```bash
pip install pandas
```

Run the program:

```bash
python "Probability Foundations.py"
```

---

## 📷 Sample Output

```
========== Probability Analysis Module ==========

P(Coffee) = 0.60
P(Pastry) = 0.50

P(Coffee ∩ Pastry) = 0.40

P(Pastry | Coffee) = 0.6667
P(Coffee | Pastry) = 0.8000

P(Pastry | Coffee) is not equal to P(Coffee | Pastry).

P(at least one customer buys a pastry) = 0.7500
P(neither customer buys a pastry) = 0.2500
```

---

## 📁 Project Structure

```
probability-foundations/
│── Probability Foundations.py
│── README.md
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Data manipulation with Pandas
- Basic probability theory
- Conditional probability
- Complement rule
- Python programming fundamentals
- Writing clean and readable code

---

## 👨‍💻 Author

**Sumit Maurya**

- GitHub: https://github.com/sumitmaurya11

---

⭐ If you found this project helpful, consider giving it a star!
