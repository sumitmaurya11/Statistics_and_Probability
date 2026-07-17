# 📊 Probability Foundations with Python

A beginner-friendly Python project that demonstrates fundamental probability concepts using **Python** and **Pandas** through a simple customer purchase dataset.

---

## 📖 Overview

This project explores basic probability concepts by analyzing customer purchase behavior for coffee and pastries. It demonstrates how probability can be calculated from real-world data using Python.

### Concepts Covered

- Marginal Probability
- Joint Probability
- Conditional Probability
- Complement Rule
- Independent Events

---

## 🚀 Features

- Calculate the probability of customers buying coffee.
- Calculate the probability of customers buying pastries.
- Compute the joint probability of buying both coffee and pastry.
- Calculate conditional probabilities:
  - **P(Pastry | Coffee)**
  - **P(Coffee | Pastry)**
- Demonstrate why conditional probabilities are generally different.
- Apply the complement rule to compute the probability that **at least one** of two independent customers buys a pastry.
- Calculate the probability that **neither** customer buys a pastry.

---

## 🛠 Technologies Used

- Python 3
- Pandas

---

## 📂 Dataset

The dataset is created directly in the Python script.

```python
data = {
    "customer_id": [1,2,3,4,5,6,7,8,9,10],
    "bought_coffee": [1,1,0,1,0,1,1,0,1,0],
    "bought_pastry": [1,0,1,1,0,0,1,0,1,0]
}
```

---

## 📐 Probability Concepts

### 1. Marginal Probability

Probability of a single event occurring.

Examples:

- P(Coffee)
- P(Pastry)

---

### 2. Joint Probability

Probability that two events occur together.

```
P(Coffee ∩ Pastry)
```

---

### 3. Conditional Probability

Probability of an event occurring given another event has already occurred.

Formula:

```
P(A | B) = P(A ∩ B) / P(B)
```

Examples:

- P(Pastry | Coffee)
- P(Coffee | Pastry)

---

### 4. Complement Rule

Used to calculate the probability that **at least one** event occurs.

```
P(At least one) = 1 − P(Neither)
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/sumitmaurya11/Statistics_and_Probability.git
```

Navigate to the project directory:

```bash
cd Statistics_and_Probability
```

Install the required package:

```bash
pip install pandas
```

Run the program:

```bash
python "Probability Foundations.py"
```

---

## 📷 Sample Output

```text
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
Statistics_and_Probability/
│
├── Probability Foundations.py
├── README.md
└── LICENSE
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

- Data analysis with Pandas
- Fundamental probability concepts
- Conditional probability
- Complement rule
- Independent events
- Writing clean, well-documented Python code

---

## 👨‍💻 Author

**Sumit Maurya**

GitHub: **[sumitmaurya11](https://github.com/sumitmaurya11)**

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, consider giving the repository a star!
