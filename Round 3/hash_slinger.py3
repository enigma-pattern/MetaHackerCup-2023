# Copyright (c) 2023 kamyu. All rights reserved.
#
# Meta Hacker Cup 2023 Round 3 - Problem B. Hash Slinger
# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/B
#
# Time:  O(N * (N + M) + M^2) = O(N^2 + M^2)
# Space: O(N * M)
#

def hash_slinger():
    N, M = list(map(int, input().split()))
    A = list(map(lambda x: int(x)%M, input().split()))
    INF = float("inf")
    dp = [INF]*M
    dp2 = [[] for _ in range(N)]
    for i in reversed(range(N)):
        d = 0
        for j in range(i, N):
            d = (d+A[j])%M
            dp[d] = min(dp[d], j)
        dp2[i][:] = dp
    dist = [INF]*(1<<M.bit_length())  # Space: O(M)
    dist[0] = 0
    lookup = [False]*len(dist)
    for _ in range(len(dist)):  # Time: O(M^2), Space: O(M)
        u = -1
        for v in range(len(dist)):
            if lookup[v]:
                continue
            if u == -1 or dist[u] > dist[v]:
                u = v
        if u == -1:
            break
        lookup[u] = True
        for d in range(M):
            if dist[u] < N:
                dist[u^d] = min(dist[u^d], dp2[dist[u]][d]+1)
    return sum(x != INF for x in dist)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, hash_slinger()))
