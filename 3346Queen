"""
皇后问题
https://acm.ecnu.edu.cn/problem/3346/
"""
import numpy as np

chart = {}

def jiecheng(n):
    if n in chart:
        return chart[n]
    elif n <=1 :
        chart[n] = 1
    else:
        chart[n] = n*jiecheng(n-1)
    return chart[n]


n = int(input())
x_list = []
y_list = []
c = n
while(c):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
    c-=1
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:    
        x_list = np.array(x_list)
        y_list = np.array(y_list)
        xvalue, xcount = np.unique(x_list, return_counts=True)
        yvalue, ycount = np.unique(y_list, return_counts=True)
        
        resist = 0
        for it in xcount:
            if it > 1:
                print(it)
                resist += jiecheng(it)/(2*jiecheng(it-2))
        for it in ycount:
            if it > 1:
                print(it)
                resist += jiecheng(it)/(2*jiecheng(it-2))
        
        count_pri = 0
        count_sub = 0
        for i in range(n):
            if x_list[i] == y_list[i]:
                count_pri+=1
            if x_list[i] + y_list[i] == n+1:
                count_sub+=1
        
        if count_pri > 1:
            resist += jiecheng(count_pri)/(2*jiecheng(count_pri-2))
        if count_sub > 1:
            resist += jiecheng(count_sub)/(2*jiecheng(count_sub-2))
        
        print(int(resist))
