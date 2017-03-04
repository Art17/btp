import re

if __name__ == '__main__':
    print('task 1a')
    reg = re.compile('(\[(\+|-)([0-9]+|[A-Z]+)\])')
    for r in re.findall(reg, open('1.txt','r').read()):
        print(r[0])
    print('task 1b')
    for m in reg.finditer(open('2.txt', 'r').read()):
        print(m.start(), m.group())
