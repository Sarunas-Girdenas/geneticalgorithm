from typing import Tuple
from dataclasses import dataclass

@dataclass(frozen=True)
class Chromosome:

    seed: str
    default_threshold: float = 0.5

    def __eq__(self, another_chromosome: "Chromosome"):
        return isinstance(another_chromosome, Chromosome) and self.seed == another_chromosome.seed
    
    @property
    def length(self) -> int:
        return len(self.seed)

    def to_string(self) -> str:
        return str(self.seed)

    def threshold(self, kwargs):
        if 'threshold' in kwargs.keys():
            threshold = kwargs['threshold']
        if 'threshold' not in kwargs.keys():
            threshold = self.default_threshold
        return threshold

    def mutate(self, injected_random_number: "List", **kwargs) -> "Chromosome":
        
        return Chromosome(self.mutate_seed(injected_random_number,self.threshold(kwargs)))

    def mutate_seed(self, injected_random_number: "List", threshold):
        
        chromosome_seed = ""

        change_map = self.change_map(injected_random_number, threshold)

        for change, chromosome_value in zip(change_map, self.seed):
            chromosome_seed += self.mutate_element(chromosome_value, change)
        return chromosome_seed

    def mutate_element(self,chromosome_value, change):       

        if chromosome_value == '0' and change:   
            return "1"
        if chromosome_value == '1' and change:
            return "0"
        if not change:
            return chromosome_value
    
    def should_change(self, number: float, threshold: float) -> bool:
        return number > threshold
    
    def change_map(self, injected_random_number: "List", threshold: float) -> "List":

        return [self.should_change(number, threshold) for number in injected_random_number]


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