import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import *
import time
import math

def sls(list_):
	s = 0
	for l in list_:
		s += l * l
	return s

def s2l(list_1, list_2):
	s = 0
	for i in range(len(list_1)):
		s += list_1[i] * list_2[i]
	return s

def ml(list_):
	s = 0
	for l in list_:
		s += l
	return s/len(list_)

counts = [6, 5, 7, 3, 7, 7, 9, 6, 7, 4, 8, 10, 5, 6, 9, 8, 5, 6, 6, 8, 7, 8, 7, 9, 6, 4, 9, 10, 7, 5, 7, 11, 6, 12, 8, 10, 5, 8, 14, 4, 6, 10,
		  9, 9, 8, 7, 9, 10, 5, 6, 6, 5, 5, 5, 7, 5, 4, 5, 7, 5, 7, 8, 12, 8, 6, 6, 7, 6, 5, 8, 6, 6, 7, 12, 8, 8, 10, 9, 10, 4, 7, 8, 11, 13, 3,
		  7, 9, 5, 6, 9, 11, 5, 6, 6, 11, 6, 7, 4, 3, 9]

print(len(counts))

unique_counts = set(counts)
est_lambda = ml(counts)

exp_frequencies = dict.fromkeys(unique_counts)
for count in unique_counts:
	p = poisson.pmf(count, est_lambda)
	exp_frequencies[count] = p * len(counts)

obs_frequencies = dict.fromkeys(unique_counts)
for count in unique_counts:
	obs_frequencies[count] = counts.count(count)

chi_squared = 0
for count, _ in exp_frequencies.items():
	chi_squared += (obs_frequencies[count] - exp_frequencies[count]) ** 2 / exp_frequencies[count]
 
print(chi_squared)

obs_probabilities = []

x = poisson.rvs(est_lambda, size=10000)

plt.hist(x, density=True, edgecolor='black')
plt.hist(counts, density=True, edgecolor='black')

plt.savefig("problem_2.png")