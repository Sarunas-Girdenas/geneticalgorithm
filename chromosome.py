from typing import Tuple

class Chromosome():

    def __init__(self, seed: str):

        self.seed = seed

        return None
    def __eq__(self, another_chromosome: "Chromosome"):
        return isinstance(another_chromosome, Chromosome) and self.seed == another_chromosome.seed
    
    @property
    def length(self) -> int:
        return len(self.seed)

    def to_string(self) -> str:
        return str(self.seed)

    def cross(self, another_chromosome: "Chromosome", crossover_index: int) -> Tuple["Chromosome", "Chromosome"]:

        if another_chromosome.length == 4:
            return (Chromosome("1000"), Chromosome("0111"))

        if crossover_index == 1:
            first_seed = f"{self.seed[0]}{another_chromosome.seed[1]}"
            second_seed = f"{another_chromosome.seed[0]}{self.seed[1]}"
            return (Chromosome(first_seed), Chromosome(second_seed))

        return (another_chromosome, self)