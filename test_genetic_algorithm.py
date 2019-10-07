import unittest
from parameterized import parameterized
from chromosome import Chromosome

class Testalgo(unittest.TestCase):

    @parameterized.expand([
        ["0","0",0,"0"],
        ["0","1",0,"1"]
        ])

    def test_crossover(self, first_chromosome_seed: str, second_chromosome_seed: str,
                       crossover_index: int, first_chromosome_crossed_seed: str):

        first_chromosome = Chromosome(first_chromosome_seed)
        second_chromosome = Chromosome(second_chromosome_seed)

        first_chromosome_crossed = first_chromosome.cross(second_chromosome, crossover_index)

        self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed))