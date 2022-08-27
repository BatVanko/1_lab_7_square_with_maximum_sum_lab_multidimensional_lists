n,m = [int(x) for x in input().split(',') ]

mm = []

for _ in range (n):
    mm.append([int(x) for x in input().split(',')] )
sum_matrix = 0
for i in range(n):
    for j in range (m):
        sum_matrix += mm[i][j]
print (sum_matrix)
print(mm)





