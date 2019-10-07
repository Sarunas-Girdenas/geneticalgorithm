class Chromosome():

    def __init__(self, seed):

        self.seed = seed

        return None
    def __eq__(self, another_chromosome: "Chromosome"):
        return isinstance(another_chromosome, Chromosome) and self.seed == another_chromosome.value
    
    @property
    def value(self) -> str:
        return self.seed

    def cross(self, another_chromosome: "Chromosome", crossover_index: int) -> "Chromosome":

        if another_chromosome.value == "0":
            Chromosome("0")
        
        return Chromosome("1")
