from algorithms.ProblemParticleSwarmOptimisation import ProblemParticleSwarmOptimisation
from service.ControllerParticleSwarm import ControllerParticleSwarm
import numpy as np
from matplotlib import pyplot as plt
import time

timer = time.time()

problem = ProblemParticleSwarmOptimisation(5)
cont = ControllerParticleSwarm(problem, 10000, 30)

values = cont.runStatistic()

npArray = np.array(values)

print("Time: ", time.time() - timer)
print("Mean value: " + str(npArray.mean()))
print("Standard deviation: " + str(npArray.std()))


plt.plot(npArray, color='blue')
plt.ylabel("Fitness")
plt.xlabel("Iteration")
plt.show()
