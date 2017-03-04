from machines.switch_machine import SwitchMachine


if __name__ == '__main__':
    switch_machine = SwitchMachine()
    for str in open('1.txt', 'r').read().split('\n'):
        if switch_machine.check_string(str):
            print(str)
        switch_machine.reset()

