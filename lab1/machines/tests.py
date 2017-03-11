import unittest
from machines.switch_machine import SwitchMachine
from machines.table_machine import TableMachine
from machines.state_machine import StateMachine


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


class TestTableMachine(unittest.TestCase):

    def test_word(self):
        self.assertEqual(TableMachine().check_string('hell'), False)

    def test_number(self):
        self.assertEqual(TableMachine().check_string('443'), False)

    def test_incorrect_1(self):
        self.assertEqual(TableMachine().check_string('^321^*^GG^'), False)

    def test_incorrect_2(self):
        self.assertEqual(TableMachine().check_string('^FSA3^*^GG^'), False)

    def test_incorrect_3(self):
        self.assertEqual(TableMachine().check_string('^AA^6^SS^'), False)

    def test_incorrect_4(self):
        self.assertEqual(TableMachine().check_string('&AA^*^AA^'), False)

    def test_incorrect_5(self):
        self.assertEqual(TableMachine().check_string('^^*^A^'), False)

    def test_incorrect_6(self):
        self.assertEqual(TableMachine().check_string('^G**^A^'), False)

    def test_correct_1(self):
        self.assertEqual(TableMachine().check_string('^A^*^GSSSSS^'), True)

    def test_correct_2(self):
        self.assertEqual(TableMachine().check_string('^BBS^*^GGGG^'), True)

    def test_correct_3(self):
        self.assertEqual(TableMachine().check_string('^B^*^%&^'), True)


class TestStateMachine(unittest.TestCase):

    def test_word(self):
        self.assertEqual(StateMachine().check_string('hell'), False)

    def test_number(self):
        self.assertEqual(StateMachine().check_string('443'), False)

    def test_incorrect_1(self):
        self.assertEqual(StateMachine().check_string('^321^*^GG^'), False)

    def test_incorrect_2(self):
        self.assertEqual(StateMachine().check_string('^FSA3^*^GG^'), False)

    def test_incorrect_3(self):
        self.assertEqual(StateMachine().check_string('^AA^6^SS^'), False)

    def test_incorrect_4(self):
        self.assertEqual(StateMachine().check_string('&AA^*^AA^'), False)

    def test_incorrect_5(self):
        self.assertEqual(StateMachine().check_string('^^*^A^'), False)

    def test_incorrect_6(self):
        self.assertEqual(StateMachine().check_string('^G**^A^'), False)

    def test_correct_1(self):
        self.assertEqual(StateMachine().check_string('^A^*^GSSSSS^'), True)

    def test_correct_2(self):
        self.assertEqual(StateMachine().check_string('^BBS^*^GGGG^'), True)

    def test_correct_3(self):
        self.assertEqual(StateMachine().check_string('^B^*^%&^'), True)
