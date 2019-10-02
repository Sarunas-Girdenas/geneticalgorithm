import unittest
from parameterized import parameterized
from chromosome import Chromosome

class Testalgo(unittest.TestCase):

    # @parameterized.expand([
    #     ["0","0",0,"0"]
    #     ])

    # def test_crossover(self, first_chromosome_seed: str, second_chromosome_seed: str,
    #                    crossover_index: int, first_chromosome_crossed_seed: str):

    #     first_chromosome = Chromosome(first_chromosome_seed)
    #     second_chromosome = Chromosome(second_chromosome_seed)

    #     first_chromosome_crossed = first_chromosome.cross(second_chromosome, crossover_index)

    #     self.assertEqual(first_chromosome_crossed, Chromosome(first_chromosome_crossed_seed))

    def test_equality(self):
        first_chromosome = Chromosome("0")
        second_chromosome = Chromosome("0")

        assert first_chromosome.value == second_chromosome.value