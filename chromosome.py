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
            
        return (another_chromosome, Chromosome("0"))
