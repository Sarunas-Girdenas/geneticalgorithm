import unittest
from parameterized import parameterized
from chromosome import Chromosome, CrossedChromosomes

class Testalgo(unittest.TestCase):

    @parameterized.expand([
        ["0","0",0,"0","0"],
        ["0","1",0,"1","0"],
        ["1","1",0,"1","1"]
    ])

    def test_crossover_at_index_0(self, first_chromosome_seed: str, second_chromosome_seed: str,
                                  crossover_index: int, first_chromosome_crossed_seed: str,
                                  second_chromosome_crossed_seed: str):

        first_chromosome = Chromosome(first_chromosome_seed)
        second_chromosome = Chromosome(second_chromosome_seed)

        first_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).first()
        second_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).second()

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed),
            f"crossed: {first_chromosome_crossed.to_string()}, seed: {first_chromosome_crossed_seed}")

        self.assertEqual(second_chromosome_crossed, Chromosome(second_chromosome_crossed_seed),
            f"crossed: {second_chromosome_crossed.to_string()}, seed: {second_chromosome_crossed_seed}")
    

    @parameterized.expand([
        ["11", "00", 1, "10", "01"],
        ["10", "01", 1, "11", "00"],
        ["01", "01", 1, "01", "01"]
    ])

    def test_crossover_at_index_1(self, first_chromosome_seed: str, second_chromosome_seed: str,
                                  crossover_index: int, first_chromosome_crossed_seed: str,
                                  second_chromosome_crossed_seed: str):

        first_chromosome = Chromosome(first_chromosome_seed)
        second_chromosome = Chromosome(second_chromosome_seed)

        first_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).first()
        second_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).second()

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed),
            f"crossed: {first_chromosome_crossed.to_string()}, seed: {first_chromosome_crossed_seed}")

        self.assertEqual(second_chromosome_crossed, Chromosome(second_chromosome_crossed_seed),
            f"crossed: {second_chromosome_crossed.to_string()}, seed: {second_chromosome_crossed_seed}")

    @parameterized.expand([
        ["1111", "0000", 1, "1000", "0111"],
        ["1100", "0011", 1, "1011", "0100"],
        ["1111111111", "0000000000", 1, "1000000000", "0111111111"]
    ])

    def test_crossover_at_index_1_longer_chromosomes(self, first_chromosome_seed: str, second_chromosome_seed: str,
                                  crossover_index: int, first_chromosome_crossed_seed: str,
                                  second_chromosome_crossed_seed: str):

        first_chromosome = Chromosome(first_chromosome_seed)
        second_chromosome = Chromosome(second_chromosome_seed)

        first_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).first()
        second_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).second()

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed),
            f"crossed: {first_chromosome_crossed.to_string()}, seed: {first_chromosome_crossed_seed}")

        self.assertEqual(second_chromosome_crossed, Chromosome(second_chromosome_crossed_seed),
            f"crossed: {second_chromosome_crossed.to_string()}, seed: {second_chromosome_crossed_seed}")

    @parameterized.expand([
        ["0000000000", "1111111111", 7, "0000000111", "1111111000"]
    ])

    def test_crossover_at_given_index_longer_chromosomes(self, first_chromosome_seed: str, second_chromosome_seed: str,
                                  crossover_index: int, first_chromosome_crossed_seed: str,
                                  second_chromosome_crossed_seed: str):

        first_chromosome = Chromosome(first_chromosome_seed)
        second_chromosome = Chromosome(second_chromosome_seed)

        first_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).first()
        second_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).second()

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed),
            f"crossed: {first_chromosome_crossed.to_string()}, seed: {first_chromosome_crossed_seed}")

        self.assertEqual(second_chromosome_crossed, Chromosome(second_chromosome_crossed_seed),
            f"crossed: {second_chromosome_crossed.to_string()}, seed: {second_chromosome_crossed_seed}")

    @parameterized.expand([
        ["0000000000", "1111111111", 10, "0000000000", "1111111111"]
    ])

    def test_crossover_at_last_index_longer_chromosomes(self, first_chromosome_seed: str, second_chromosome_seed: str,
                                  crossover_index: int, first_chromosome_crossed_seed: str,
                                  second_chromosome_crossed_seed: str):
                                  
        first_chromosome = Chromosome(first_chromosome_seed)
        second_chromosome = Chromosome(second_chromosome_seed)

        first_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).first()
        second_chromosome_crossed = CrossedChromosomes(first_chromosome, second_chromosome, crossover_index).second()

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed),
            f"crossed: {first_chromosome_crossed.to_string()}, seed: {first_chromosome_crossed_seed}")

        self.assertEqual(second_chromosome_crossed, Chromosome(second_chromosome_crossed_seed),
            f"crossed: {second_chromosome_crossed.to_string()}, seed: {second_chromosome_crossed_seed}")
    


    @parameterized.expand([
        ["0", "1", [0.7]],
        ["0", "0", [0.3]],
        ["00", "01", [0.4, 0.9]],
        ["00", "11", [0.8, 0.6]],
        ["11", "00", [0.8, 0.6]],
        ["101010101010", "110011001100", [0, 1, 0.9, 0.1, 0.2, 0.8, 0.7, 0.3, 0.4, 0.6, 0.7, 0.3]]
        
    ])

    def test_mutate(self,chromosome_seed: str, mutated_seed: str,  injected_random_number: "List"):
        chromosome = Chromosome(chromosome_seed)

        chromosome_mutated = chromosome.mutate(injected_random_number)

        self.assertEqual(chromosome_mutated, Chromosome(mutated_seed))
    

    @parameterized.expand([
        ["1", "1", [0.7], 1]
    ])
    def test_optional_threshold(self,chromosome_seed: str, mutated_seed: str,  injected_random_number: "List", threshold:float):
        chromosome = Chromosome(chromosome_seed)

        chromosome_mutated = chromosome.mutate(injected_random_number, threshold=threshold)

        self.assertEqual(chromosome_mutated, Chromosome(mutated_seed))