# mike-papa [![build](https://travis-ci.org/angellandros/mike-papa.svg?branch=master)](https://travis-ci.org/angellandros/mike-papa)
Mike Papa: Tiny Parser for Bitwise Operators

## Usage
Put your code inside a `.txt` file, e.g. `mycode.txt`. The code must contain lines of the form:
```
15 -> a
16 -> b
2 -> d
a OR b -> c
NOT c -> e
e RSHIFT b -> f
f XOR 7 -> g
```

Then open the file `parse.py` in an interactive mode, e.g. `ipython -i parse.py`, then
``` python
load('mycode.txt')
parse('f')
parse('g')
```
