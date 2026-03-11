
from functools import reduce
def weighted_score(scores, weights):
    return reduce(lambda acc, sw: acc + sw[0]*sw[1], zip(scores,weights), 0)
