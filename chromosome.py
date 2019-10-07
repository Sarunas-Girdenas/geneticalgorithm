from typing import Tuple

class Chromosome():

    def __init__(self, seed):

        self.seed = seed

        return None
    def __eq__(self, another_chromosome: "Chromosome"):
        return isinstance(another_chromosome, Chromosome) and self.seed == another_chromosome.value
    
    @property
    def value(self) -> str:
        return self.seed

    def cross(self, another_chromosome: "Chromosome", crossover_index: int) -> Tuple["Chromosome", "Chromosome"]:

        if crossover_index == 1:
            first_seed = f"{self.value[0]}{another_chromosome.value[1]}"
            second_seed = f"{another_chromosome.value[0]}{self.value[1]}"
            return (Chromosome(first_seed), Chromosome(second_seed))
        

        return (another_chromosome, self)