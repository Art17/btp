from machines.switch_machine import SwitchMachine
from machines.table_machine import TableMachine
from machines.state_machine import StateMachine


def check_machine(machine):
    for str in open('1.txt', 'r').read().split('\n'):
        if machine.check_string(str):
            print(str)
        machine.reset()

if __name__ == '__main__':
    print('Switch machine at work:')
    check_machine(SwitchMachine())
    print('Table machine at work:')
    check_machine(TableMachine())
    print('State machine at work:')
    check_machine(StateMachine())

