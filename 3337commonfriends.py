"""
3337. 我认识你
https://acm.ecnu.edu.cn/problem/3337/
"""
n, m = map(int,input().split())
friends = {}
for i in range(1, n+1):
    friends[i] = []
for i in range(m):
    u, v = map(int,input().split())
    friends[u].append(v)
    friends[v].append(u)
q = int(input())
search = []
for i in range(q):
    s, t = map(int,input().split())
    search.append([s, t])
for i in range(q):
    print(len(set(friends[search[i][0]]).intersection(set(friends[search[i][1]]))))
