import  re
m = re.match('[bh][aiu]t',"bat,")
if m is not None:
    m.group()
    print(m.group())
