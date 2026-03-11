
def aggregate(*nums, op="sum"):
    if not nums:
        return None
    if op=="sum":
        return sum(nums)
    if op=="avg":
        return sum(nums)/len(nums)
    if op=="max":
        return max(nums)
