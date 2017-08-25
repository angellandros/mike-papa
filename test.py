#! /bin/python

from parse import *


if __name__ == '__main__':
    load('test.txt')
    assert parse('x') == 123
    assert parse('g') == 114
    assert parse('f') == 492

