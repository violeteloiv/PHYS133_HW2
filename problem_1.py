import matplotlib.pyplot as plt
import numpy as np
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

distances = [0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5, 0.5, 0.63, 0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.1, 1.1, 1.4, 1.7, 2.0, 2.0, 2.0, 2.0]
velocities = [170, 290, -130, -70, -185, -220, 200, 290, 270, 200, 300, -30, 650, 150, 500, 920, 450, 500, 500, 960, 500, 850, 800, 1090]

plt.scatter(distances, velocities)

slope = s2l(distances, velocities) / sls(distances)
print(slope)

x_lobf = np.arange(0, 2.1, 0.1)
y_lobf = slope * x_lobf

# calculate error of slope
residues = []
for i in range(len(distances)):
	residues.append(velocities[i] - slope * distances[i])

ssr = sls(residues)
res_sd = math.sqrt(ssr/22)
dist_mean = ml(distances)

dist_res = []
for i in range(len(distances)):
	dist_res.append(distances[i] - dist_mean)

slope_error = res_sd * math.sqrt(1/sls(dist_res))
print(slope_error)

plt.plot(x_lobf, y_lobf)

plt.savefig("problem_1.png")