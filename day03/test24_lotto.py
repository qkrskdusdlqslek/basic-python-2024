# file : test24_lotto.py
# desc : 로또번호 생성
import random as rnd # 랜덤은 rnd로 줄여서 많이 사용

numbers = list(range(1, 46))

# print(numbers)
lottery = list()
print(lottery)

for i in range(6): # 0,1,2,3,4,5 여섯번 반복
    lottery.append(rnd.choice(numbers)) # 1~45까지 숫자 중 하나를 랜덤으로 꺼내기

lottery.sort() # 작은 숫자부터 나열하는 방법
print(lottery)

numbers = weight = list(range(1, 46))
lottery = list()
rnd.shuffle(weight) # 가중치로 섞음

lottery = rnd.choices(numbers, weights=weight, k=6) # 가중치로 한꺼번에 여섯개 뽑기
lottery.sort()
print(lottery)








