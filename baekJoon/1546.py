n = int(input())
score = list(map(int, (input().split())))
m = max(score)
sum = sum(score)

print((sum/m*100)/n)
