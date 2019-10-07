import unittest
from parameterized import parameterized
from chromosome import Chromosome

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

        first_chromosome_crossed = first_chromosome.cross(second_chromosome, crossover_index)[0]
        second_chromosome_crossed = first_chromosome.cross(second_chromosome, crossover_index)[1]

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed),
            f"crossed: {first_chromosome_crossed.value}, seed: {first_chromosome_crossed_seed}")

        self.assertEqual(second_chromosome_crossed, Chromosome(second_chromosome_crossed_seed),
            f"crossed: {second_chromosome_crossed.value}, seed: {second_chromosome_crossed_seed}")
    

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

        first_chromosome_crossed = first_chromosome.cross(second_chromosome, crossover_index)[0]
        second_chromosome_crossed = first_chromosome.cross(second_chromosome, crossover_index)[1]

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed),
            f"crossed: {first_chromosome_crossed.value}, seed: {first_chromosome_crossed_seed}")

        self.assertEqual(second_chromosome_crossed, Chromosome(second_chromosome_crossed_seed),
            f"crossed: {second_chromosome_crossed.value}, seed: {second_chromosome_crossed_seed}")
