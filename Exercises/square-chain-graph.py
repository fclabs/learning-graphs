# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
# For example,

# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# Write a function using graphs to calculate how many starting numbers below n, n being ten million will arrive at 89?
# Hint: Use graphs to speed up the search of already calculated numbers in past numbers chains

def calc_89( n: int ) -> int :
    pass