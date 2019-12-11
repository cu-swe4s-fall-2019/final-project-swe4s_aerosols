'''
functional testing for diversity.py

'''

import unittest
import diversity

class TestDiversity(unittest.TestCase):
    def test_toy_dataset_one_calculation(self):
        t = betaDiv('test_community_dataset.csv')
        calc = [0.0, 0.9, 1.0, 0.9, 0.6, 0.8, 0.5, 1.0, 0.6, 1.0, 0.4, 1.0, 0.4, 0.9, 0.9, 0.8, 0.8]
        self.assertEquals(t, calc)
    def test_toy_dataset_saves_plot(self):
        t = betaDiv('test_community_dataset.csv')
        self.assertExists('beta_diversity.png')
    def test_input_file_does_not_exist(self):
        t = 0
    def test_length_of_counts(self):
        t = 0


if __name__ == '__main__':
    unittest.main()
