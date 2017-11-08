import re
def raw_input():
 name = raw_input('input:')
 m = re.match('.+\s.+',name)
 if m is not None:
    print(m.group())



