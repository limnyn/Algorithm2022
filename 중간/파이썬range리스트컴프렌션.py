# for i in (10 ** x for x in range(2, -1, -1)):
#     print(i)
# 100
# 10
# 1


#인덱스 감소 표현  for (int i = n; i > 0; i /= 2) print i
n = 10
for i in (2** x for x in range(n,-1, -1)):
    print(i)
