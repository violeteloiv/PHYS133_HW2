import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import *
import time
import math

def poisson_dist(lamb, k):
	return (lamb ** k) * math.exp(-lamb) / math.factorial(k)

def gaussian_dist(mean, sd, x):
	return (1/(sd * math.sqrt(2 * 3.14))) * math.exp(-(1/2) * ((x - mean / sd)) ** 2)

est_poisson = 0
for i in range(75):
	est_poisson += poisson_dist(100, i)

est_gaussian = 0
for i in range(75):
	est_gaussian += gaussian_dist(100, 10, i)

print(est_poisson)
print(est_gaussian)