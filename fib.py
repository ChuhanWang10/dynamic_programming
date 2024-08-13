'''
Find the n-th number in the Fibonacci sequence
'''

# solve it with recursive algorithm 
def fib(n):
    # Fibonacci sequence: 1,1,2,3,5,8,13,21,34,...
    # input is the n-th number in the sequence, output is the corresponding number in the sequence.
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# solve Fibonacci problem with dp 
# class Solution(object):
#     def fib(self, n: int) -> int:
#         '''
#         the index of memo[n] starts from 0, though the index of fib sequence may start from 1.
#         '''
#         memo = [1 for _ in range(n+1)]
#         return self.my_fib(n, memo)

#     def my_fib(self, n, memo) -> int:
#         # if n == 0:
#         #     return 0
#         if n <= 2:
#             return 1

#         if memo[n] != 1:
#             return memo[n]

#         memo[n] = self.my_fib(n - 1, memo) + self.my_fib(n - 2, memo)
#         return memo[n]

def fibDP(n:int):
    memo = [1 for _ in range(n+1)]
    if n <= 2:
        return 1
    if memo[n] != 1:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]     

n = 8
print(f"answer: {fib(n)}")
print(f"answer: {fibDP(n)}")
