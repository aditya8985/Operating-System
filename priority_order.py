n = int(input())
p = list(map(int,input().split()))
b = list(map(int,input().split()))
sal = sorted(p, reverse=True)
dp = p[0::]
c = [0] * n
for i in range(n):
    c[i] = dp.index(sal[i])
    dp[dp.index(sal[i])] = -1
final_sum = 0
ltime = 0
ct = [0] * n
for j in c:
    ltime = ltime + b[j]
    ct[j] = ltime
print("Average CT is: ", ltime/n)
print("CT")
print(*ct)
tat = [0] * n
for i in range(n):
    tat[i] = ct[i]
print("TAT")
print(*tat)
print("Average TAT is : ", sum(tat)/n)
wt = [0] * n
for i in range(n):
    wt[i] = tat[i] - b[i]
print("WT")
print(*wt)
print("Average wt is: ", sum(wt)/n)
