# file : test15_output.py
# desc : 콘솔 출력 포맷양식 String Format

print(10)
print('10')

string_1 = '{}'.format(10) # {}위치에 함수 뒤에 들어있는 값을 치환, 원하는 양식으로 표현하라
print(type(string_1))

name = '박나연' # input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000, '만', '빌려주세요')
print(string_3) 
#정수를 문자열포맷
# =: 기호와 숫자를 분리, 숫자 앞에 05는 다섯자리 만들 때 빈자리를 0으로 채우기, d:정수, 자리를 두자리 수로 만들면서 빈자리 0으로 채우는 것 > 02d
string_4 = '_____{:+10d}_____'.format(-100) 
print(string_4)
#실수 문자열포맷 f (기본 소수점 6자리)
string_5 = '_____{}______'.format(78.3333333333)
print(string_5)

string_5 = '_____{}______'.format(78.33) #78.330000
print(string_5)
string_5 = '_____{:.2f}______'.format(78.33333333333)
print(string_5)
string_5 = '_____{:7.2f}______'.format(78.33333333333) # 7.2f 전체 자리수를 7자리로, 소수점 뒤는 2자리 fix
print(string_5)

# 파이썬 3.6 이후 도입 .format() 함수를 아예 사용안함 > 훨씬 편함
val = 78.333333333
string_6 = f'_____{val}______'
print(string_6)

val = 78.333333333
string_6 = f'_____{val:7.2f}______'
print(string_6)

string_7 = 'Hello, World'
print(string_7.upper()) # upper case 대문자 변환
print(string_7.lower()) # lower case 소문자 변환
print(string_7.lower().capitalize()) # capitalize 맨 앞 단어만 대문자 변환

print(string_7.split(' ')) # 특정한 단어로 자르는 함수 > '공백'으로 자름
print(string_7.split(','))

string_8 = "Hello, I am MG Sung. I am a lecturer. Good Luck for your day."
words = string_8.split(' ')
print(words)
print(len(words)) # print(f'문장의 단어 갯수는 {len(words)}개입니다.')

string_9 = 'A10'
print(string_9.isalnum()) #True
print(string_9.isnumeric()) #False A 알파벳
string_10 = '10.5' # 소수점은 함수를 만들어서 처리해야...
print(string_10.isdecimal()) #False

print('안녕' in '안녕하세요') # 문장안에 단어가 있는지 확인할 때 사용


 











