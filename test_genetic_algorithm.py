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