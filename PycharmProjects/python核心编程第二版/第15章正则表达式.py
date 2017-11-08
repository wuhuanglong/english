from re import match
def raw_input():
 word = raw_input ('input:')
 m = match('^[bh][aiu]t$', word)
 if m is not None:
    print(m.group())
