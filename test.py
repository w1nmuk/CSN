# # 1. BMI 계산기
#
# height = float(input('키를 입력하세요>>> '))/100   # 키를 cm 단위로 입력받고 m로 변환하여야 하므로 /100
# weight = float(input('몸무게를 입력하세요>>> '))
#
# bmi = weight/height**2
# if bmi < 18.5:
#     answer = '저체중'
# elif bmi < 25:
#     answer = '정상체중'
# elif bmi < 30:
#     answer = '과체중'
# else:
#     answer = '비만'
# print('당신은', answer)
#
# # 2. 사칙연산 계산기
#
# first_num = int(input('첫 번째 숫자를 입력하시오: '))
# second_num = int(input('두 번째 숫자를 입력하시오: '))
# print('덧셈 결과:', first_num+second_num)
# print('뺄셈 결과:', first_num-second_num)
# print('곱셈 결과:', first_num*second_num)
# print('나눗셈 결과:',first_num/second_num if second_num!=0 else '값이 나오지 않습니다.')
#
# # 3. 자동판매기 시뮬레이션
#
# print('음료 가격표: \n물1 - 500원\n콜라2 - 1,000원\n커피3 - 1,500원')
# drink_dict= {1: 500, 2: 1000, 3: 1500} # 리스트로 만들어 for 문을 이용하는 것보다 딕셔너리가 더 유용.
# drink_names = {1: '물', 2: '콜라', 3: '커피'}
#
#
# drink = int(input('선택할 음료를 입력하시오 (1, 2, 3):'))
# money = int(input('투입 금액을 입력하시오: '))
# if drink in drink_dict:   # 딕셔너리는 key값과 일치하는 것이 없으면 error 발생하므로 확인
#     if money - drink_dict[drink] < 0:
#         print('잔액이 부족합니다')
#     else:
#         change = money - drink_dict[drink]
#         print(f'{drink_names[drink]}을(를) 선택하셨습니다. 잔돈은 {change}원입니다.')
#
#
#
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4, 5, 6, 7])
# plt.show()

# import matplotlib.pyplot as plt
# import random
#
# def chaos_game(vertices, n_points):
#     # 초기 점 설정
#     x, y = [0.5], [0.5]  # (0.5, 0.5)에서 시작
#
#     for _ in range(n_points):
#         # 무작위로 꼭짓점 선택
#         chosen_vertex = random.choice(vertices)
#
#         # 현재 점과 선택된 꼭짓점의 중간점 계산
#         x_new = (x[-1] + chosen_vertex[0]) / 2
#         y_new = (y[-1] + chosen_vertex[1]) / 2
#
#         # 새 점 추가
#         x.append(x_new)
#         y.append(y_new)
#
#     return x, y
#
# # 정삼각형 꼭짓점
# vertices = [(0, 0), (1, 0), (0.5, 0.866)]
#
# # 카오스 게임 실행
# n_points = 10000  # 점 개수
# x, y = chaos_game(vertices, n_points)
#
# # 결과 시각화
# plt.scatter(x, y, s=0.1, c='blue')
# plt.axis('equal')
# plt.show()
#

import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

f = open('rain2.csv','r', encoding='cp949')
data = csv.reader(f)
# next(data)
result = []

x = []
y = []

for line in data:
    if line[2] != '' :
        x.append(line[0])
        y.append(float(line[2]))


plt.title("2019년, 2020년 서울 월 별 강수량")

plt.plot(x, y, marker='o', color='blue', label='2019, 2020')
plt.xlabel("년도/월")
plt.ylabel("강수량(mm)")

plt.grid()
plt.legend(['2019, 2020'])

plt.show()
