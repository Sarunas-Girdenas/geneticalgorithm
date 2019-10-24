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
    

    def mutate(self, injected_random_number:"List") -> "Chromosome":
        threshold = 0.5

        if len(injected_random_number) == 2:
            chromosome_seed = ""
            if self.seed == "11":
                return Chromosome("00")
#for 00 input only
            for number in injected_random_number:
                if number > threshold:
                    chromosome_seed += "1"
                if number <= threshold:
                    chromosome_seed += "0"
            return Chromosome(chromosome_seed)
        

        if injected_random_number[0] > threshold:
            return Chromosome("1")
        
        if injected_random_number[0] <= threshold:
            return Chromosome("0")



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