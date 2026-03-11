
from collections import OrderedDict
def element_counts(lst):
    d=OrderedDict()
    for x in lst:
        d[x]=d.get(x,0)+1
    return list(d.items())
