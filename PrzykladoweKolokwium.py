from typing import List 
import numpy as np

def selekcja_ruletkowa(fitness : List, N : int) -> np.ndarray :
    if N > len(fitness):
        N = len(fitness)
    
    fitness = np.array(fitness)
    probability_fitness = fitness / np.sum(fitness)
    cumulative_probability = np.cumsum(probability_fitness)

    random_numbers = np.random.rand(0, 1, N)

    selected_indices = distinct(np.searchsorted(cumulative_probability, random_numbers))

    return selected_indices