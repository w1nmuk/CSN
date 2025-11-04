# # 1. 홀짝 판별기
# sutza = int(input('정수를 입력하시오: '))
# print(f'입력된 정수 {sutza}은(는){'홀수' if sutza%2 != 0 else '짝수'}입니다.')
# # 입력받은 값을 2로 나누고 나머지가 남으면 홀수, 나누어떨어지면 짝수라고 출력한다.
#
# # 2. 졸업 가능 여부
# hakjeom = int(input('이수한 학점을 입력하시오: '))
# score = float(input('평점을 입력하시오: '))
# if hakjeom >= 140 and score >= 2.0: # 140학점 이상, 평균 2.0 이상이면 졸업 가능
#     print('졸업이 가능합니다.')
# else:  # 한 조건이라도 만족하지 못하면 졸업이 힘들다고 출력한다.
#     print('졸업이 힘듭니다.')
#
# # 3. 수하물 비용 계산
# jim = int(input('짐의 무게는 얼마입니까? '))
# answer = ''   # 미리 answer를 선언하지 않아도 된다.
#
# if jim >= 20:
#     answer = '20,000원을 내야합니다.'
# else:
#     answer = '없습니다'
# print('짐에 대한 수수료는',answer)
# import math
#
# # 1. 구구단 출력
# dan = int(input('출력할 단을 입력하시오: '))
# for i in range(1,10):
#     print(dan,'*',i,'=',dan*i)
#
# # 2. 임의의 값까지 합계 계산
# sutza = int(input('어디까지 더할 것인지 입력하시오: '))
# hap = 0   # 미리 hap을 설정해야 for문 밖에서도 사용 가능
# for i in range(1, sutza+1):
#     hap += i
#
# print(f'1부터 {sutza}까지의 정수의 합 = {hap}')
#
# # 3. 팩토리얼 계산
# factorial = int(input('정수를 입력하시오: '))
# hap = 1   # i를 곱하는 것이기 때문에 0으로 초기값을 할당하면 안 된다.
# for i in range(1,factorial+1):
#     hap *= i
# print(f'{factorial}! = {hap}')
#
# # 다른 방법
# print(f'{factorial}! = {math.factorial(factorial)}')

# # 1. 합계 계산
# sutza = int(input('어디까지 더할 것인지 입력하시오: '))
# num, hap = 1, 0
# while sutza >= num:   # 입력받은 sutza 값이 num보다 크거나 같을 동안 반복문을 시행한다.
#     hap += num
#     num += 1
# print(f'1부터 {sutza}까지의 정수의 합 = {hap}')
#
# # 2. 숫자 세기
# a = int(input('a를 입력하시오: '))
# b = int(input('b를 입력하시오: '))
# if a <= b:
#     while a <= b:
#         print('Count', a)
#         a += 1
# else:
#     while b <= a:
#         print('Count', b)
#         b += 1
#
# 3. 자리수 합 계산
# jungsu = int(input('정수를 입력하시오: '))
# jungsu_list = [i for i in str(jungsu)]
# # 리스트 컴프리헨션을 통해 입력받은 int형의 jungsu를 str형으로 바꾸고 리스트에 저장한다.
# hap = 0   # for 문 이전에 hap을 선언하여 변수의 값이 초기화되는 것을 막는다.
# for i in jungsu_list:
#     i = int(i)
#     hap += i
#
# print(hap)

# # 1. 리스트 합계 계산
# a = input('숫자를 입력하시오 (공백으로 구분): ').split()
# hap = 0
# for i in a:
#     i = int(i)
#     hap += i
# print('리스트의 합계는',hap,'입니다')

# # # 2. 최댓값과 최솟값 찾기
# b = list(map(int,input('숫자를 입력하시오 (공백으로 구분): ').split()))
# print(f'최댓값: {max(b)}, 최솟값: {min(b)}')

# # 3. 중복 제거
# c = list(map(int, input('숫자를 입력하시오 (공백으로 구분): ').split()))
# c_set = set(c)
# print('중복 제거 결과:',list(c_set))

# 1. 리스트 정렬

# sutza = list(map(int, input('숫자를 입력하시오 (공백으로 구분): ').split()))
# print('정렬된 리스트:', sorted(sutza))

# # 2. 리스트에서 특정 값 찾기
# num = list(map(int, input('숫자를 입력하시오 (공백으로 구분): ').split()))
# find = int(input('찾을 숫자를 입력하시오: '))
# if find in num:
#     print(f'{find}는 리스트에 있습니다.')
# else:
#     print(f'{find}는 리스트에 없습니다.')

# # 3. 짝수와 홀수 분리
# numbers = list(map(int, input('숫자를 입력하시오 (공백으로 구분): ').split()))
# odd_list, even_list = [], []
# for i in numbers:
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
#
# print('짝수: ', even_list)
# print('홀수: ', odd_list)
#

# # 1. 합계 함수
# def hap(num_list:list):
#     return sum(num_list)
#
#
# hapgye = list(map(int, input('숫자를 입력하시오 (공백으로 구분): ').split()))
# print('리스트의 합계는', hap(hapgye),'입니다.')


# # 2. 최댓값과 최솟값 함수
# def maxi_mini(num_list:list):
#     return max(num_list), min(num_list)
#
#
# max_min = list(map(int, input('숫자를 입력하시오 (공백으로 구분): ').split()))
# result = maxi_mini(max_min)
# print(f'최댓값: {result[0]}, 최솟값: {result[1]}')

# # 3. 구구단 함수
# def gugudan(dan):
#     for i in range(1, 10):
#         print(f'{dan} * {i} = {dan*i}')
#
#
# dan = int(input('단을 입력하시오: '))
# gugudan(dan)

# +++++ 23 +++++
# 1.
# print(int("15.7"))
# "15.7"이 문자열로 인식해서가 아닌 단지 float형이기 때문에 오류

# 2.
# age = 21
# print("age", "살이다")
# age살이다 가 출력됨.

# 3.
# print('start of the program')
# hello()
# print('end of the program')
#
# def hello():
#     print('hello world')   오류

# 4.
# x = input("첫번째 정수를 입력하세요: ")
# y = input("두번째 정수를 입력하세요: ")
# sum = x + y
# print("합은", sum)
# 205 int(input())이 아닌 input()으로 x, y값을 받았기 때문에 문자열 취급

# 5.
# number = int(input("정수를 입력하시오: "))
# if number % 2 == 0:
#     print("입력된 정수는 짝수입니다.")
# else:
#     print("입력된 정수는 홀수입니다.")
#

# 6.
# number = 3126
# sum = 0
# while number > 0:
#     digit = number % 10
#     print(digit)
#     sum = sum + digit
#     number = number // 10
#     print(number)
#
# print(sum) # 6 312 2 31 1 3 3 0 12

# 7.
# sum = 0
# for i in range(1,201):
#     sum = sum + i
#     if sum >= 1000:
#         break
# print("1부터 200의 합에서 최초로 1000이 넘는 위치: ", i)

# 8.
# A = [2, 4, ['no', 'yes'], 6, 8, 0, 'ok']
# print(len(A))
# A[1:3] = [1]
# print(A)
# print(len(A))
# A[2:3] = [5, 6]
# print(A)
# print(len(A))
# A[1] = ['a', 'b']
# print(A)
# print(len(A))
# A[len(A):len(A)] = [7]
# print(A)
# print(len(A))
# A[4:6] = []
# print(A)
# print(len(A))
# 7 / [2, 1, 6, 8, 0, 'ok'] / 6 / [2, 1, [5, 6], 6, 8, 0, 'ok'] / 7
# [2, ['a', 'b'], [5, 6], 6, 8, 0, 'ok'] / 7 / [2, ['a', 'b'], [5, 6], 6, 8, 0, 'ok', 7]
# 8 / [2, ['a', 'b'], [5, 6], 6, 'ok', 7] / 6

# 7 / [2, 1, 6, 8, 0, 'ok'] / 6 / [2, 1, 5, 6, 8, 0, 'ok'] / 7
# [2, ['a','b'], 5, 6, 8, 0, 'ok'] / 7 / [2, ['a','b'], 5, 6, 8, 0, 'ok', 7] / 8
# [2, ['a','b'], 5, 6, 'ok', 7]

# +++++ 22 +++++
# 1.
# var1 = 100
# var1 += 200
# print(var1) # 300

# 2.
# print(21 + '살이다')
# 오류. int형과 문자형 사이에는 +가 성립하지 않기 때문이다

# 3.
# a = 100
# b = 200
# print(a==b) # False

# 4.
# score = 70
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')
# print("학점입니다.")
# # C
# # 학점입니다.

# 5.
# for i in range(2, -1, -1):
#     print(i, "안녕")
#
# # 2 안녕
# # 1 안녕
# # 0 안녕

# 6.
# 오류 number가 선언되지 않았기 때문

# 7.
# sum = 0
# for i in range(1, 11):
#     if i % 4 == 0:
#         continue
#     sum += i
# print(sum)   # 43

# 8.
# A = [2, 4, 6, 8, 0]
# A[1:3] = [1] # [2, 1, 8, 0]
# A[2:3] = [5, 6]  # [2, 1, [5, 6], 0]
# A[1:1] = ['a', 'b'] # [2, ['a', 'b'], 1, [5, 6], 0]
# A[len(A):len(A)] = [7] # [2, ['a', 'b'], 1, [5, 6], 0, 7]
# A[4:6] = [] # [2, ['a', 'b'], [5, 6], 0]
# print(A)
# A[1] = []
# print(A)
# print()
# [2, 1, 8, 0]
# [2, 1, 5, 6, 0]
# [2, 'a', 'b', 1, 5, 6, 0]
# [2, 'a', 'b', 1, 5, 6, 0, 7]
# [2, 'a', 'b', 1, 0, 7]
# [2, [], 'b', 1, 0, 7]

# A = [2, 4, ['no', 'yes'], 6, 8, 0, 'ok']
# print(len(A))
# A[1:3] = [1]
# print(A)
# print(len(A))
# A[2:3] = [5, 6]
# print(A)
# print(len(A))
# A[1] = ['a', 'b']
# print(A)
# print(len(A))
# A[len(A):len(A)] = [7]
# print(A)
# print(len(A))
# A[4:6] = []
# print(A)
# print(len(A))

# 7
# [2, 1, 6, 8, 0, 'ok']
# 6
# [2, 1, 5, 6, 8, 0, 'ok']
# 7
# [2, ['a','b'], 5, 6, 8, 0, 'ok']
# 7
# [2, ['a','b'], 5, 6, 8, 0, 'ok', 7]
# 8
# [2, ['a','b'], 5, 6, 'ok', 7]
# 6

# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# def add_mul(choice, *args):
#     if choice == 'add':
#         result = 0
#         for i in args:
#             result += i
#     elif choice == 'mul':
#         result = 1
#         for i in args:
#             result *= i
#
#     return result
#
# result = add_mul()

# def print_kwargs(**kwargs):
#     print(kwargs)
#
# print_kwargs(a=1, b=2, c=3)

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
#
#     def div(self):
#         result = self.first / self.second
#         return result
#
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
#
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
#
# class Family:
#     lastname = "김"
#
# print(Family.lastname)

def mbti_sogye(mbti):
    if mbti == 'ISTJ':
        result = 'ISTJ는 강한 집중력과 현실 감각을 지녔으며, 조직적이고 침착하다. '
    if mbti == 'ISTP':
        result = 'ISTP는 과묵하며 절제된 호기심으로 인생을 관찰하고, 상황을 파악하는 민감성과 도구를 다루는 뛰어난 능력이 있다.'
    if mbti == 'ISFJ':
        result = 'ISFJ는 안정적인 삶을 지향하면서도 변화를 잘 수용한다.'
    if mbti == 'ISFP':
        result = 'ISFP는 말없이 다정하고 온화하며, 사람들에게 친절하다.'
    if mbti == 'INTJ':
        result = "INTJ는 새로운 아이디어에 통찰력과 뛰어난 논리력, 강한 의지를 더해 일을 추진한다."
    if mbti == 'INTP':
        result = "INTP는 조용하고 과묵하며, 논리와 분석으로 문제를 해결하기 좋아한다."
    if mbti == "INFJ":
        result = "INFJ는 인내심이 많고 통찰력과 직관력이 뛰어나며, 화합을 추구하는 유형이다. "
    if mbti == 'INFP':
        result = "INFP는 낭만적인 성향으로 보이면서도 내적 신념이 깊은 열정적인 중재자 유형이다."
    if mbti == "ESTJ":
        result = "ESTJ는 현실적, 구체적, 사실적이다."
    if mbti == 'ESTP':
        result = "ESTP는 실적이고 관대하며 개방적이고, 사람이나 사물에 대한 선입견이 별로 없다."
    if mbti == 'ESFJ':
        result = "ESFJ는 동정심이 많고 다른 사람에게 관심을 쏟으며, 나눔과 베풂을 중시한다. "
    if mbti == 'ESFP':
        result = "ESFP는 사교적이고 활동적이며 수용력이 강하고, 친절하며 낙천적이다. "
    if mbti == 'ENTJ':
        result = 'ENTJ는 권위와 자신감으로 역량을 발휘한다.'
    if mbti == 'ENTP':
        result = 'ENTP는 특유의 능글거리면서 경쾌한 성격을 갖고 있다.'
    if mbti == 'ENFJ':
        result = 'ENFJ는 온화하고 적극적이며 책임감이 강하다. '
    if mbti == 'ENFP':
        result = 'ENFP는 정열적이고 활기가 넘치며 상상력이 풍부하다.'
    return result

# print(mbti_sogye('INTP'))


def mbti_good(mbti):
    if mbti == 'ISTJ':
        result = 'ISTJ에게 추천하는 활동: 주어진 임무를 완수하고 규칙을 준수하는 활동'
    if mbti == 'ISTP':
        result = 'ISTP에게 추천하는 활동: 자신의 능력을 적당히 활용하는 활동'
    if mbti == 'ISFJ':
        result = 'ISFJ에게 추천하는 활동: 다른 사람들의 감정을 파악하는 활동'
    if mbti == 'ISFP':
        result = 'ISFP에게 추천하는 활동: 사람들을 중재하고 화합시키는 활동'
    if mbti == 'INTJ':
        result = "INTJ에게 추천하는 활동: 문제에 의문을 던지고 해결 방법을 찾는 활동"
    if mbti == 'INTP':
        result = "INTP에게 추천하는 활동: 논리력을 필요로 하는 활동"
    if mbti == "INFJ":
        result = "INFJ에게 추천하는 활동: 직관적이고 통찰력이 필요한 활동"
    if mbti == 'INFP':
        result = "INFP에게 추천하는 활동: 인문학과 관련된 분야 활동"
    if mbti == "ESTJ":
        result = "ESTJ에게 추천하는 활동: 조직관리를 하고 목표를 설정 및 이행하는 활동"
    if mbti == 'ESTP':
        result = "ESTP에게 추천하는 활동: 문제를 해결하고 즐기는 활동"
    if mbti == 'ESFJ':
        result = "ESFJ에게 추천하는 활동: 다른 사람들을 돕는 활동"
    if mbti == 'ESFP':
        result = "ESFP에게 추천하는 활동: 주변의 사람들과 친해지고 분위기를 조성하는 활동"
    if mbti == 'ENTJ':
        result = 'ENTJ에게 추천하는 활동: 문제 해결 과정을 체계화하는 활동'
    if mbti == 'ENTP':
        result = 'ENTP에게 추천하는 활동: 토론을 하고 논쟁하는 활동'
    if mbti == 'ENFJ':
        result = 'ENFJ에게 추천하는 활동: 리더십을 갖고 통솔하는 활동'
    if mbti == 'ENFP':
        result = 'ENFP에게 추천하는 활동: 새롭고 도전적인 활동'
    return result

# print(mbti_good('INTP'))


# import numpy as np
# import matplotlib.pyplot as plt

# import numpy as np
# import matplotlib
# matplotlib.use('TKAgg')  # 비인터랙티브 백엔드 사용
#
# import matplotlib.pyplot as plt
#
#
# def koch_curve_recursive(p1, p2, depth):
#     if depth == 0:
#         return [p1, p2]
#
#     p1 = np.array(p1)
#     p2 = np.array(p2)
#
#     # 점 A, B 계산
#     A = p1 + (p2 - p1) / 3
#     B = p1 + 2 * (p2 - p1) / 3
#
#     # 점 C 계산 (회전행렬 사용)
#     rotation_matrix = np.array([[0.5, -np.sqrt(3) / 2],
#                                 [np.sqrt(3) / 2, 0.5]])
#     C = A + np.dot(rotation_matrix, (B - A))
#
#     # 재귀 호출
#     return (
#             koch_curve_recursive(p1, A, depth - 1) +
#             koch_curve_recursive(A, C, depth - 1) +
#             koch_curve_recursive(C, B, depth - 1) +
#             koch_curve_recursive(B, p2, depth - 1)
#     )
#
# # 시각화
# depth = 4
# points = koch_curve_recursive((0, 0), (1, 0), depth)
#
# x, y = zip(*points)
# plt.figure(figsize=(8, 4))
# plt.plot(x, y, color='blue')
# plt.title("Koch Curve (Depth = 4)")
# plt.axis("equal")
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib n
# matplotlib.use('TKAgg')  # 비인터랙티브 백엔드 사용
#
# # Mandelbrot 집합을 생성하는 함수
# def mandelbrot(c, max_iter):
#     z = 0
#     n = 0
#     while abs(z) <= 2 and n < max_iter:
#         z = z*z + c
#         n += 1
#     return n
#
# # 시각화할 영역과 해상도 설정
# width, height = 800, 800
# x_min, x_max = -2.0, 1.0
# y_min, y_max = -1.5, 1.5
# max_iter = 256
#
# # 좌표 그리드 생성
# x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
# X, Y = np.meshgrid(x, y)
#
# # 각 점에 대해 Mandelbrot 집합 반복 계산
# Z = np.array([[mandelbrot(complex(x, y), max_iter) for x, y in zip(X_row, Y_row)]
#               for X_row, Y_row in zip(X, Y)])
#
# # Mandelbrot 집합 시각화
# plt.figure(figsize=(8, 8))
# plt.imshow(Z, cmap='twilight', extent=(x_min, x_max, y_min, y_max))
# plt.colorbar()
# plt.title("Mandelbrot Set")
# plt.show()

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()

