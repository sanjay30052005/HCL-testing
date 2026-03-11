
import itertools
def multiples_of_three():
    i=1
    while True:
        yield i*3
        i+=1

first_five=list(itertools.islice(multiples_of_three(),5))
print(first_five)
