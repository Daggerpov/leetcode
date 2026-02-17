"""
zip() allows for iterating through two lists at once, granted they have equal length. Iterate through both at same time, appending to stack. If what was just appended is greater than the one before it, it doesn't need to wait in the stack, as it can simply go forth and complete its journey (not apart of same fleet). At the end, len(stack) is the num of fleets
"""

pair = [(p, s) for p, s in zip(position, speed)]
pair.sort(reverse=True)
stack = []
for p, s in pair:  # Reverse Sorted Order
    pass
