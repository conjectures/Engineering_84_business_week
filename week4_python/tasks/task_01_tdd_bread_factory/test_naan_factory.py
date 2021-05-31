import unittest

import naan_factory as nf


class FactoryTest(unittest.TestCase):

    # Test if adding 'water' and 'flour' in the 'run_factory' function will create 'naan'
    def test_run_factory(self):
        self.assertEqual(nf.run_factory('water', 'flour'), 'naan')

    # Test if adding 'water' and something other than 'flour' in the 'run_factory' function will create give None
    def test_run_factory_wrong_inputs(self):
        self.assertIsNone(nf.run_factory('water', 'else'))

    # Test if adding 'water' and 'flour' with swithced positions in the 'run_factory' function will create 'naan'
    def test_run_factory_switch_inputs(self):
        self.assertEqual(nf.run_factory('flour', 'water'), 'naan')

    # Test if adding 'water' and 'flour' in the 'make_dough' function will produce 'flour'
    def test_make_dough(self):
        self.assertEqual(nf.make_dough('water', 'flour'), 'dough')

    # Test if adding 'flour' 'bake_dough' function will produce 'naan'
    def test_bake_dough(self):
        self.assertEqual(nf.bake_dough('dough'), 'naan')
