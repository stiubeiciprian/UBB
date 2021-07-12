# from algorithms import *
# from service import *
# from domain import *
#
#
# class UI:
#     def __init__(self):
#         pass
#
#     def showMainMenu(self):
#         s = "Select solving method:\n"
#         s += "1.Evolutionary Algorithm\n"
#         s += "2.Hill Climbing\n"
#         s += "3.Partical Swarm Optimisation\n"
#
#         print(s)
#
#     def run(self):
#
#         while True:
#             self.showMainMenu()
#             method = int(input(">>"))
#
#             if method == 1:
#                 self.evolutionaryAlgorithm()
#             elif method == 2:
#                 self.hillClimbing()
#             else:
#                 return
#
#     def evolutionaryAlgorithm(self):
#         print("-------------------------------------------------------------------")
#         print("Using Evolutionary Algorithm...")
#
#         problemSize = int(input("Enter problem size:"))
#         iterations = int(input("Enter max number of iterations:"))
#         populationSize =  int(input("Enter population size:"))
#         probability = float(input("Enter probability of mutation:"))
#
#         problem = ProblemEvolutionaryAlgorithm(problemSize)
#         cont = ControllerEvolutionary(problem, populationSize, probability, iterations)
#
#         solution, iteration = cont.run()
#
#         sol = State()
#         sol.setValues(solution[0])
#
#         print("Best solution:", sol, "found at iteration no:", iteration)
#         print("-------------------------------------------------------------------")
#
#     def hillClimbing(self):
#         print("-------------------------------------------------------------------")
#         print("Using Hill Climbing Algorithm...")
#
#         problemSize = int(input("Enter problem size:"))
#         iterations = int(input("Enter max number of iterations:"))
#
#         problem = ProblemHillClimbing(problemSize)
#         cont = ControllerHillClimbing(problem, iterations)
#
#         solution, iteration = cont.run()
#
#         sol = State()
#         sol.setValues(solution)
#
#         print("Best solution:", sol, "found at iteration no:", iteration)
#         print("-------------------------------------------------------------------")
#
#     def pso(self):
#         print("Using Particle Swarm Optimisation Algorithm")
