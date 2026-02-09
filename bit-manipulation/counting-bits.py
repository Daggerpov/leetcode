"""
- Store result of all the bits of each number in dp = [0 for x in range(0, n + 1)]
- Maintain an offset variable where you keep track of the largest offset based on the
  base cases of 0 and 1
- Update the offset variable to i every time it reaches offset * 2 == i
- Calculate dp[i] using the base case dp[i - offset] + 1 (current added offset bit)
"""
