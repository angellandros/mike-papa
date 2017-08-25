#! /bin/python


context = {}


def parse(var):
    if var.isdigit():  # literal
        return int(var)
    value = context[var].split(' ')
    if len(value) == 1:  # assignment
        return parse(value[0])
    if len(value) == 2:
        o, a = value[0], value[1]  # not
        return ~ parse(a)
    a, o, b = value[0], value[1], value[2]
    aa = parse(a)
    bb = parse(b)
    if o == 'AND':
        return aa & bb
    if o == 'OR':
        return aa | bb
    if o == 'XOR':
        return aa ^ bb
    if o == 'LSHIFT':
        return aa << bb
    if o == 'RSHIFT':
        return aa >> bb
    return 0


def load(path):
    with open(path, 'r') as f:
        for l in f:
            val, var = l.strip().split(' -> ')
            context[var] = val

