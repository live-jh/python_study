# 계수 정렬
# 특정 조건(데이터의 크기 범위가 제한되며 정수일때)이 부합시 사용 가능 (매우 빠름)
# 일반적으로 min, max의 차가 1,000,000 넘지 않을시 효과적
# 리스트를 선언 후 리스트 안에 정보를 담음


arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 7, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언 (0~9)
count_arr = [0] * (max(arr) + 1)  # 0~9까지 총 10의 길이 리스트 선언

# for i in arr:
#     for j in range(len(count_arr)):
#         if i == j:
#             count_arr[j] += 1

for i in range(len(arr)):
    count_arr[arr[i]] += 1

for i in range(len(count_arr)):
    for j in range(count_arr[i]):
        print(i, end=" ")

# 0 0 1 1 2 2 3 4 5 5 6 7 7 9 9
# 0 0 1 1 2 2 3 4 5 5 6 7 7 9 9