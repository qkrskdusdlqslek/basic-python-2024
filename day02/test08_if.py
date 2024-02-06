# desc : 홀수/짝수 또는 배수
number = int(input('정수입력 >')) # 입력받은 후 정수로 변경

if number % 2 == 0: # 짝수 
    print('짝수!')
else: # 홀수
    print('홀수')

if number % 5 == 0:  # 짝수 또는 배수
    print('5의 배수')  
else: # 홀수 또는 나머지
    print('나머지수')   # pass 넣으면 오류 없이 넘어감 
