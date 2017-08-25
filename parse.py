#! /bin/python


context = {}


def parse(var):
    if var.isdigit():  # literal
        return int(var)
    value = context[var]
    if isinstance(value, (int, long)):
        return value
    value = value.split(' ')
    if len(value) == 1:  # assignment
        parsed = parse(value[0])
        context[var] = parsed
        return parse(value[0])
    if len(value) == 2:
        o, a = value[0], value[1]  # not
        aa = parse(a)
        context[var] = ~ aa
        return ~ aa
    a, o, b = value[0], value[1], value[2]
    aa = parse(a)
    bb = parse(b)
    answer = 0
    if o == 'AND':
        answer = aa & bb
    if o == 'OR':
        answer = aa | bb
    if o == 'XOR':
        answer = aa ^ bb
    if o == 'LSHIFT':
        answer = aa << bb
    if o == 'RSHIFT':
        answer = aa >> bb
    context[var] = answer
    return answer


def load(path):
    with open(path, 'r') as f:
        for l in f:
            val, var = l.strip().split(' -> ')
            context[var] = val

