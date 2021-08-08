import random

print("문자를 입력해주세요.")
input_value = input()
print("입력한 문자는 ->", input_value)

player = ['mount', 'james', 'abraham', 'gilmour', 'pulisic', 'odoi', 'tomori']

for p in player:
    print(p)
print(random.choice(player))
num_1 = 30
print(float(num_1))

# split()
chk_name = 'frankl:ampard'

print(chk_name.split(':'))

# for 루프
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("{} need interpreter".format(lang))
    elif lang in ['c', 'java']:
        print("{} need compiler".format(lang))
    else:
        print("should not reach here")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for no in numbers:
    if no % 2 == 0:
        print(no, "는 짝수")
    else:
        print(no, "는 홀수")
