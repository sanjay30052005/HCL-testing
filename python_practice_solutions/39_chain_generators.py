
def gen_numbers():
    for i in range(1,11):
        yield i

def gen_squares(nums):
    for n in nums:
        yield n*n

for x in gen_squares(gen_numbers()):
    print(x)
