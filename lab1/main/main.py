import re

if __name__ == '__main__':
    reg = re.compile('(\[(\+|-)([0-9]+|[A-Z]+)\])')
    for r in re.findall(reg, open('1.txt','r').read()):
        print(r[0])
