"""
  @Author: hardcodecoder
  @Date:   06:16:26 Monday 06 July 2020
  @Last modified by:   hardcodecoder
  @Last modified time: 08:21:55 Friday 10 July 2020
"""

"""
Teacher provides a question bank consisting of N questions and 
guarantees all the questions in the test will be from this question bank. 
Due to lack of time and his laziness, Codu could only practice M questions. 
There are T questions in a question paper selected randomly.
Codu can't solve the question he didn't practice. 
What is the probability that Codu will solve at least 1 question in the test?

Output : If probability is p/q where p & q are co-prime, print (p*mulInv(q)) modulo 1000000007, 
         where mulInv(x) is multiplicative inverse of x under modulo 1000000007.
"""

import math


# function to calculate nCr
def binomialCoefficient(n, k): 
    if(k > n - k): 
        k = n - k 
    res = 1
    for i in range(k): 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res


# get number of test cases
num_tests = int(input())

prime = 10**9 + 7

""" 
To find nCr we can also use pascals triangle
where n corresponds to row and r corresponds to column
For example: 15C5 => pascals[15][5] 
"""

# max_n = 1000

# pascals = [[0 for i in range(j+1)] for j in range(max_n+1)]

# pascals[0][0] = 1

# for row in range(1, len(pascals)):
#     pascals[row][0] = 1
#     for col in range(1, row):
#         pascals[row][col] = pascals[row-1][col-1] + pascals[row-1][col]
#     pascals[row][row] = 1



for test in range(num_tests):
    N, T, M = map(int, input().split())
    
    if M == 0:
        print(0)
        continue
    if N-M < T:
        print(1)
        continue

    numerator = binomialCoefficient(N-M, T) # or use pascals[N-M][T]
    denominator = binomialCoefficient(N, T) # or use pascals[N][T]

    gcd = math.gcd(numerator, denominator)

    p = denominator - numerator
    q = denominator

    p = p//gcd
    q = q//gcd

    mul_inv_q = pow(q, prime-2, prime)

    ans = (p * mul_inv_q) % prime
    print(ans)








