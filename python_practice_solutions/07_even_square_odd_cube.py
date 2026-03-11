
def transform(nums):
    return [x**2 if x%2==0 else x**3 for x in nums]
