'''
functional testing for diversity.py

'''

import unittest
import os
import diversity as d

class TestDiversity(unittest.TestCase):

    def test_toy_dataset_one_calculation(self):
        t = d.betaDiv('test_community_dataset.csv')
        calc = [0.0, 0.9, 1.0, 0.9, 0.6, 0.8, 0.5, 1.0, 0.6, 1.0, 0.4, 1.0, 0.4, 0.9, 0.9, 0.8, 0.8]
        self.assertEqual(t, calc)

    def test_toy_dataset_saves_plot(self):
        t = d.betaDiv('test_community_dataset.csv')
        self.assertTrue(os.path.exists('beta_diversity.png'))

    def test_length_of_counts(self):
        t = d.betaDiv('test_community_dataset.csv')
        length = len(t)
        self.assertEqual(length, 17)

    def test_length_of_counts_full_dataset(self):
        t = d.betaDiv('asv_table_corrected.csv')
        length = len(t)
        self.assertEqual(length, 16)

if __name__ == '__main__':
    unittest.main()
