# 📊 Discrete & Continuous Distributions with SciPy

A beginner-friendly Python project demonstrating fundamental statistical concepts using **NumPy** and **SciPy**. This project covers **Z-score standardization** and the **Binomial Probability Mass Function (PMF)**, which are widely used in data science and statistics.

## 📌 Project Overview

This project demonstrates:

- Calculating the **mean** of a dataset
- Calculating the **standard deviation**
- Computing **Z-scores** manually
- Verifying that standardized data has:
  - Mean ≈ 0
  - Standard Deviation ≈ 1
- Computing **Binomial PMF** using SciPy
- Understanding discrete probability distributions

---

## 📂 Technologies Used

- Python 3
- NumPy
- SciPy

---

## 📁 Project Structure

```
.
├── discrete_continuous_distributions.py
├── README.md
└── LICENSE
```

---

## 📈 Z-Score Standardization

A Z-score tells how many standard deviations a value is from the dataset's mean.

Formula:

```
Z = (X - μ) / σ
```

Where:

- X = Data value
- μ = Mean
- σ = Standard deviation

The project manually calculates Z-scores using NumPy and verifies that the standardized values have:

- Mean ≈ 0
- Standard Deviation ≈ 1

---

## 🎲 Binomial Probability Mass Function (PMF)

The project also demonstrates the Binomial PMF using SciPy.

The Binomial PMF calculates the probability of getting **exactly k successes** in **n independent trials**.

Formula:

```
P(X = k) = C(n, k) × p^k × (1-p)^(n-k)
```

Example used:

- Number of trials (n) = 10
- Probability of success (p) = 0.3
- Successes (k) = 0 to 5

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project directory:

```bash
cd your-repository
```

Install dependencies:

```bash
pip install numpy scipy
```

Run the program:

```bash
python discrete_continuous_distributions.py
```

---

## 📚 Concepts Covered

- Mean
- Standard Deviation
- Z-Score
- Standardization
- Probability
- Binomial Distribution
- Probability Mass Function (PMF)
- NumPy Arrays
- SciPy Statistics

---

## 🎯 Learning Objectives

This project is intended for beginners learning:

- Python for Data Science
- Statistics
- Probability
- Scientific Computing with SciPy

---

## 👨‍💻 Author

**Sumit Maurya**

GitHub: https://github.com/your-username

---

## 📄 License

This project is licensed under the MIT License.
