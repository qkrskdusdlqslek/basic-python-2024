# file : test20_function.py
# desc : 함수 만들기 (계산기 기능)

def add(x, y) -> int:
    result = x + y
    return result

def minus(x, y) -> int:
    result = x - y
    return result
 
def multi(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> int:
    result = x / y
    return result

def say_hello() -> None: # None을 return 한다 (return문이 없다고 할 수 있다. 그래서 생략 -> return None 생략)
    print('Hello')
    return

say_hello()    
print('더하기 -> ')
a, b = map(int, input('두 정수 입력 >').split(' '))
결과 = add(a, b)  # 리턴은 함수 결과값으로 바뀐다!
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a, b)}')
print(f'{a} x {b} = {multi(a, b)}')
print(f'{a} ÷ {b} = {divide(a, b)}')

