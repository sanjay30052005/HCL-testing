
from collections import defaultdict
def group_items(pairs):
    d=defaultdict(list)
    for item,cat in pairs:
        d[cat].append(item)
    return dict(d)
