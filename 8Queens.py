import numpy as np
import defFor8queens as functions

#choosing the initial random population
population1 = functions.init_pop(4)
print(population1)

#calculating the fitness value
fitness_vals=functions.calc_fitness(population1)
print(fitness_vals)

#applying the selection base on the fitness value
selected_population = functions.selection(population1, fitness_vals)
print(selected_population)

# applying the crossover+mutation to get the new population
new_pop= functions.crossover_mutation(selected_population, pc=0.7, pm=0.01)
print('new population :', new_pop)

functions.queens8 (pop_size=100,max_gen=10000,pc=0.7,pm=0.01)

