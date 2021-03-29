import unittest

import naan_factory as nf


class FactoryTest(unittest.TestCase):

    def test_run_factory(self):
        self.assertEqual(nf.run_factory('water', 'flour'), 'naan')

    def test_run_factory_wrong_inputs(self):
        self.assertIsNone(nf.run_factory('water', 'else'))

    def test_run_factory_switch_inputs(self):
        self.assertEqual(nf.run_factory('flour', 'water'), 'naan')

    def test_make_dough(self):
        self.assertEqual(nf.make_dough('water', 'flour'), 'dough')

    def test_bake_dough(self):
        self.assertEqual(nf.bake_dough('dough'), 'naan')
