from machines.switch_machine import SwitchMachine
from machines.table_machine import TableMachine

if __name__ == '__main__':
    print('Switch machine at work:')
    switch_machine = SwitchMachine()
    for str in open('1.txt', 'r').read().split('\n'):
        if switch_machine.check_string(str):
            print(str)
        switch_machine.reset()
    print('Table machine at work:')
    table_machine = TableMachine()
    for str in open('1.txt', 'r').read().split('\n'):
        if table_machine.check_string(str):
            print(str)
        table_machine.reset()

