"""

Kata: Summarize Ranges

#1 Best Practices Solution by hiasen

def summary_ranges(nums):
    if not nums:
        return []
    ranges = []
    first = nums[0]
    for current, previous in zip(nums[1:], nums[:-1]):
        if current - previous not in [0, 1]:
            ranges.append((first, previous))
            first = current
    ranges.append((first, nums[-1]))
    return ["{}->{}".format(a, b) if a!=b else str(a) for a, b in ranges]


Instructions
----------------------------------------------------------------------
Write summary_ranges(nums) that given a sorted array of numbers, returns
the summary of its ranges.


"""


def summary_ranges(some_list):
    """Return a list of strings showing min and max of a range from some list of numbers."""
    if len(some_list) < 1:
        return []
    splits = [0, len(some_list)]
    for i in range(len(some_list) - 1):
        if some_list[i + 1] - some_list[i] > 1:
            splits.append(i + 1)
    splits.sort()
    ranges = [some_list[splits[i]:splits[i + 1]]
              for i in range(len(splits) - 1)]
    output = ['{}'.format(num_range[0]) if min(num_range) == max(
        num_range) else '{}->{}'.format(min(num_range), max(num_range)) for num_range in ranges]
    return output
