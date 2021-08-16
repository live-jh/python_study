# def solution(nums):
#     result_set = list(set(nums))
#     result_count = len(result_set)
#     choice_count = len(nums) // 2
#     if choice_count < result_count:
#         return choice_count
#     else:
#         return result_count
#
#
# print(solution([3, 3, 3, 2, 2, 2]))


# 2번
# [5][5] == 0, 0
def solution(dirs):
    init_map = [[0] * 11 for _ in range(11)]
    x = 5
    y = 5
    init_map[5][5] = 1
    str_set = list(dirs)
    for i in range(len(str_set)):
        if x <= 0 or y <= 0 or x >= 10 or y >= 10:
            pass
        else:
            if str_set[i] == 'U':
                init_map[x - 1][y] = 1
                x = x - 1
            elif str_set[i] == 'D':
                init_map[x + 1][y] = 1
                x = x + 1
            elif str_set[i] == 'L':
                init_map[x][y - 1] = 1
                y = y - 1
            elif str_set[i] == 'R':
                init_map[x][y + 1] = 1
                y = y + 1

    sum = 0
    for i in range(len(init_map)):
        for j in range(len(init_map)):
            if init_map[i][j] == 1:
                sum+=1

    return sum


print(solution("UDUD"))


# 3번
# def solution(a, b):
#     b.sort()
#     count = 0
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if b[j] > a[i]:
#                 count += 1
#                 del b[j]
#                 print(b)
#                 break
#     return count
#
#
# print(solution([5, 1, 3, 7], [2, 2, 6, 8]))

# def third(a_list=[], b_list=[]):
#     b_list.sort()
#     win_count = 0
#     for a in a_list:
#         for index, b in enumerate(b_list):
#             if b - a > 0:
#                 win_count += 1
#                 del b_list[index]
#                 break
#     return win_count
#
#
# print(third([5, 1, 3, 7], [2, 2, 6, 8]))
