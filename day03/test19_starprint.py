# file : test19_starprint.py
# desc : 별찍기 또는 피라미드만들기
# *
# **
# ***
# ****
# *****
for i in range(1, 5+1):
    # i가 1이면, 반복이 range(1,2) 1번 반복
    # i가 2이면, range(1,3) 2번 반복
    for j in range (1, i+1): 
        print('*', end='') # 엔터 대신 empty로 변환
    print() # 안쪽 for문이 끝나면 엔터    

for i in range(1, 5+1): 
    # i가 1이면, 반복이 range(1,2) 1번 반복
    # i가 2이면, range(1,3) 2번 반복
    for j in range(1, 6-i+1): # range() 값 바꿔서 디버깅
        print('*', end='') # 엔터 대신 empty로 변환

for i in range(1, 5+1): 
    # i가 1이면, 반복이 range(1,2) 1번 반복
    # i가 2이면, range(1,3) 2번 반복
    for j in range(1, 5-i+1): # range() 값 바꿔서 디버깅
        print('*', end='') # 엔터 대신 empty로 변환
        
    for j in range(1, i+1):
        print('*', end='')
    print() # 안쪽 for문이 끝나면 엔터















