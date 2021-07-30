# index

# [start_index : end_index]
#
exam_str_1 = '작은따옴표'
print(exam_str_1[0:3])  # 작은따
print(exam_str_1[-4:])  # 은따옴표 [:-4] -> 작 :-4 == :3 같다

# escape sequence
print('hello \'tom\'')

# string format
print(
    "{age}세 개발자 {name}입니다.".format(age=33, name="live")
)
# sep 는 분류기호(seperator)
demo = "312"
demo_2 = "set"
print(demo_2, demo, sep='-')

# 10진수 형태로 입력받고 %X 로 출력시 16진수(hex) 대문자로 출력 %x는 소문자
a = 255
print('%X' % a)  # FF

# 16진수 입력받고 %o로 출력시 8진수 변환
ab = int('f', 16)
print('%o' % ab)

# ord() 는 어떤 문자의 순서 위치(ordinal position) 값을 의미 (10진수 유니코드 값으로 변환)
b = input() # 영문자 입력 ex) A
print(ord(b))
