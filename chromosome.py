from typing import Tuple
from dataclasses import dataclass

@dataclass(frozen=True)
class Chromosome:

    seed: str

    def __eq__(self, another_chromosome: "Chromosome"):
        return isinstance(another_chromosome, Chromosome) and self.seed == another_chromosome.seed
    
    @property
    def length(self) -> int:
        return len(self.seed)

    def to_string(self) -> str:
        return str(self.seed)

class CrossedChromosomes():

    def __init__(self, first_chromosome: "Chromosome", second_chromosome: "Chromosome",
                 crossover_index: int):

        first_seed = f"{first_chromosome.to_string()[:crossover_index]}{second_chromosome.to_string()[crossover_index:]}"
        second_seed = f"{second_chromosome.to_string()[:crossover_index]}{first_chromosome.to_string()[crossover_index:]}"
        self.crossed_chromosomes = (Chromosome(first_seed), Chromosome(second_seed))
    
    def first(self):
        return self.crossed_chromosomes[0]
    
    def second(self):
        return self.crossed_chromosomes[1]