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
            for number, chromosome_value in zip(injected_random_number, self.seed):
                chromosome_seed += Chromosome.mutate_element(number, chromosome_value)
            return Chromosome(chromosome_seed)


        if injected_random_number[0] > threshold:
            chromosome_value = ["0"]
            chromosome_seed = ""
            for number, chromosome_value in zip(injected_random_number, chromosome_value):
                chromosome_seed += Chromosome.mutate_element(number, chromosome_value)
            return Chromosome(chromosome_seed)
            
            
        
        if injected_random_number[0] <= threshold:
            return Chromosome("0")

    @staticmethod
    def mutate_element(random_number, chromosome_value):
        threshold = 0.5
        

        if random_number > threshold and chromosome_value == '0':
            return "1"
        if random_number > threshold and chromosome_value == '1':
            return "0"

        if random_number <= threshold and chromosome_value == '0':
            return "0"
        if random_number <= threshold and chromosome_value == '1':
            return "1"
        


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