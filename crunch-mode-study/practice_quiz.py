# Quiz 1.
# 1~10000까지의 8이 들어가는 숫자 갯수 찾기
count = 0

for i in range(1, 10000):
    for j in str(i):  # 8080 -> 4번 for문
        if j == '8':
            count = count + 1

print(count)

# Quiz 2.
# 구구단 2단
# for i in range(1, 10):
#     print(
#         "{0} * {1} = {2}".format(2, i, 2 * i)
#     )

# Quiz 3.
# 구구단 모두 출력 1~9
# for i in range(2, 10):
#     print(i, "단")
#     for j in range(1, 10):
#         print(
#             "{} * {} = {}".format(i, j, i * j)
#         )

a, b, c =map(int,input().split())
plus_no = a+b+c
avg_no = plus_no / 3
print(plus_no, format(avg_no, '.2f'))
