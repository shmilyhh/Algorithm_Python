# recursive
def editDistance(s1, s2, m, n):
    if m == len(s1):
        return len(s2) - n

    if n == len(s2):
        return len(s1) - m

    if s1[m] == s2[n]:
        return editDistance(s1, s2, m+1, n+1)

    return 1 + min(editDistance(s1, s2, m, n+1), editDistance(s1, s2, m+1, n),
                   editDistance(s1, s2, m+1, n+1))

s1 = 'sunday'
s2 = 'saturday'

print editDistance(s1, s2, 0, 0)

# dynamic programming
def editDistance_dp(s1, s2, m, n):
    distance = [[0 for c in range(n+1)] for r in range(m+1)]

    for r in range(m, -1, -1):
        for c in range(n, -1, -1):
            if r == m:
                distance[r][c] = n - c

            elif c == n:
                distance[r][c] = m - r

            elif s1[r] == s2[c]:
                distance[r][c] = distance[r+1][c+1]
            else:
                distance[r][c] = 1 + min(distance[r][c+1], distance[r+1][c],
                                     distance[r+1][c+1])
    return distance[0][0]

print editDistance_dp(s1, s2, len(s1), len(s2))
