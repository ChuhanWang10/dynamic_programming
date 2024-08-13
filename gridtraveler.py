# Solve it with recursive algorithm
# time complexity: o(2^(m+n))
# space complexity: o(m+n)
def gridTraveler(m,n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m-1, n) + gridTraveler(m, n-1)

# Solve it with DP
def gridTravelerDP(m:int, n:int):
    memo={}
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveler(m-1, n) + gridTraveler(m, n-1)
    return memo[key]


m, n = 3, 4
print(f"answer: {gridTravelerDP(m,n)}")
    