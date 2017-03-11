import unittest
from machines.switch_machine import SwitchMachine


class TestSwitchMachine(unittest.TestCase):

    def test_word(self):
        self.assertEqual(SwitchMachine().check_string('hell'), False)

    def test_number(self):
        self.assertEqual(SwitchMachine().check_string('443'), False)

    def test_incorrect_1(self):
        self.assertEqual(SwitchMachine().check_string('^321^*^GG^'), False)

    def test_incorrect_2(self):
        self.assertEqual(SwitchMachine().check_string('^FSA3^*^GG^'), False)

    def test_incorrect_3(self):
        self.assertEqual(SwitchMachine().check_string('^AA^6^SS^'), False)

    def test_incorrect_4(self):
        self.assertEqual(SwitchMachine().check_string('&AA^*^AA^'), False)

    def test_incorrect_5(self):
        self.assertEqual(SwitchMachine().check_string('^^*^A^'), False)

    def test_incorrect_6(self):
        self.assertEqual(SwitchMachine().check_string('^G**^A^'), False)

    def test_correct_1(self):
        self.assertEqual(SwitchMachine().check_string('^A^*^GSSSSS^'), True)

    def test_correct_2(self):
        self.assertEqual(SwitchMachine().check_string('^BBS^*^GGGG^'), True)

    def test_correct_3(self):
        self.assertEqual(SwitchMachine().check_string('^B^*^%&^'), True)
