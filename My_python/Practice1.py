print(1+1)
print(3-2)
print(6*3)

print(2**3)
print(5%3) # 나머지
print(10%3)
print(5//2) # 몫
print(42//2)

print(10>3)
print(4 >=10)
print(3 == 3) #앞에 있는 값과 뒤에 있는 값이 같다
print(4 == 3)
print(3+4 == 7)

print(4 != 1)
print(not (4==1))

print((3 > 0) and (9 < 34)) # 둘 다 만족해야 한다.
print((3>2) & (4>12))

print((3>4) or (5 > 1))
print((3>4) | (5 > 1))

print(5>4>3)

print(2 + 3 * 4)
print((2+3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2 #32행과 완벽히 동일한 문장
print(number)
number *= 2
number /= 2
number -= 2
print(number)
number %= 2
print(number)

print(abs(-5)) # 절대값
print(pow(4,2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 가장 큰 값
print(min(5,12))
print(round(3.14)) # 반올림
print(round(4.68))

from math import * # math 라이브러리
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성