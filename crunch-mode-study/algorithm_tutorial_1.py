# index

# [start_index : end_index]
#
exam_str_1 = '작은따옴표'
# print(exam_str_1[0:3])  # 작은따
# print(exam_str_1[-4:])  # 은따옴표 [:-4] -> 작 :-4 == :3 같다

# escape sequence
# print('hello \'tom\'')

# string format
# print(
#     "{age}세 개발자 {name}입니다.".format(age=33, name="live")
# )

# sep 는 분류기호(seperator)
demo = "312"
demo_2 = "set"
# print(demo_2, demo, sep='-')

# 10진수 형태로 입력받고 %X 로 출력시 16진수(hex) 대문자로 출력 %x는 소문자
a = 255
# print('%X' % a)  # FF

# 16진수 입력받고 %o로 출력시 8진수 변환
# ab = int('f', 16)
# print('%o' % ab)

# ord() 는 어떤 문자의 순서 위치(ordinal position) 값을 의미 (10진수 유니코드 값으로 변환)
# b = input()  # 영문자 입력 ex) A
# print(ord(b))
print('--------------------------')

# 단항의 연산자 기호인 -(negative)를 변수 앞에 붙일때 부호가 반대로 입력됌
exam_num_1 = -3
print(-exam_num_1)
print('--------------------------')

# 문자 연산
# ord는 문자의 순서를 10진수 유니코드 값으로 변환
# chr는 숫자를 문자로 변환
# exam_num_2 = ord(input()) + 1
# exam_num_3 = chr(exam_num_2)
# print(exam_num_3)
print('--------------------------')

# 소수 원하는 자리까지 자르기
# format(구하려는 수, 조건) '.2f' -> 소수 둘째자리
# demo_a = float(input())
# print(format(demo_a, '.2f'))

# print 가로로 출력
# end 옵션 "" 공백시 옆으로 붙어서 출력
# 콤마(,)로 구분하면, 문자, 숫자 상관없이 공백을 사이에 두고 출력
# print('variable',variable,end='')
