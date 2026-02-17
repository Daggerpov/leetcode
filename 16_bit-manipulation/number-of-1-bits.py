"""
Continually in a while loop keep changing n to be n & (n-1) as this will essentially
get rid of the right-most 1 by after doing n-1 will & prune the 'generated' 1s to the
right of it, while keeping the 1st to the left of this right-most 1

- res += 1 for every time you go through this while loop
"""
