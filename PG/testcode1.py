import sys
sys.stdout = open("output.txt", "w")
sys.stdin = open("input.txt", "r")
#! TEST CODE 1
# TODO ==============================================================
# TODO START CODE HERE:

import math
print(math.gcd(20, 100))