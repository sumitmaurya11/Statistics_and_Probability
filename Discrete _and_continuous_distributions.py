# Discrete & Continuous Distributions

import numpy as np
from scipy import stats

scores = [55, 62, 70, 75, 80, 85, 90, 95]

#computes Z-scores for a given list of exam scores using the formula Z = (X − μ) / σ
#A Z-score (also called a standard score) tells you how many standard deviations a data point is away from the mean of a dataset.

#Positive Z-score → Value is above the mean.
#Negative Z-score → Value is below the mean.
#Z-score = 0 → Value is exactly equal to the mean.

scores_array = np.array(scores)

std_dev = np.std(scores)

mean = np.mean(scores)

z_scores = (scores_array - mean)/ std_dev

# Prints the mean and standard deviation of both the original and standardised scores to verify the standardisation.

print("Mean of original scores:", mean)

print(f"Standard Deviation of original scores: {std_dev:.3f}")

z_scores_mean = np.mean(z_scores)

print(f"Mean of standardised Z-Scores: {z_scores_mean:.3f}")

std_z_scores = np.std(z_scores)

print(f"Standard Deviation of standardised Z-Scores: {std_z_scores:.3f}")

# Uses scipy to compute and print the Binomial PMF for k = 0, 1, 2, 3, 4, 5,
# successes given n = 10 trials and p = 0.3 success probability — 
# modelling how many trainees out of 10 pass a certification test 
# where each trainee independently has a 30% pass rate.

#Binomial PMF
#The Binomial PMF (Probability Mass Function) is a formula used to calculate the probability of getting exactly k successes in n independent trials, where each trial has only two possible outcomes:
#n = Total number of trials
#k = Number of successes
#p = Probability of success

n = 10
p = 0.3
k = [0, 1, 2, 3, 4, 5]

print("\nBinomial PMF (n=10, p=0.3):")
for k in range(0, 6):
    pmf_val = stats.binom.pmf(k, n, p)
    print(f"k={k}: PMF = {pmf_val}")
