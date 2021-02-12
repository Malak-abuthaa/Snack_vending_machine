import unittest
import sys
import os.path

from SnackMachine.Exceptoins import Execptions

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from SnackMachine.SnackMachine import SnackMachine


class TestSolution(unittest.TestCase):

    # test if user insert not allowed note amount of money
    def test_money_slot(self):
        e = SnackMachine()
        self.assertNotEqual(e.set_selected_item(11), '')
        self.assertEqual(e.collection_cash(10, 'Note', 'USD', 'Note'), Execptions.note_exception())

    # test main class
    def test_main_snack_machine(self):
        e = SnackMachine()
        self.assertNotEqual(e.set_selected_item(11), '')
        self.assertNotEqual(e.collection_cash(20,'Note', 'USD', 'Note'), '')
        self.assertNotEqual(e.return_change(), '')


if __name__ == "__main__":
    unittest.main()
