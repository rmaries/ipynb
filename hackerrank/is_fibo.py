# -*- coding: utf-8 -*-
fib_memo = {0:0,1:1}
def fib(n):    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif not n in fib_memo:
        fib_memo[n] = (fib(n-1) + fib(n-2))
    return fib_memo[n]
fib(52)
print fib_memo
k = input()
for i in range(int(k)):
    n = input()
    if n in fib_memo.values():
        print "IsFibo"
    else:
        print "IsNotFibo"