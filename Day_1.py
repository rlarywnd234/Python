from tkinter import N

# print 함수
print("Come back to the beginning again")
print(5+4)
print(3.14)
print(2*1200)

# 변수
# 파이선 변수는 앞에 일일이 유형 선언 안 해도 됨
RD = "RD-704, it s God Tier Gun"
MMAC = "four class armor"
BP = 7.62


# 문자열(str) 변수
print("What is most powerful bullet at the Escape Tarkov? : "+ str(BP) +"mm")
print("what is most powerful gun in the Escape from Tarkov? : "+ str(RD))
## +는 str 변수 외에 웬만하면 사용하지 말자

# 정수형(int) 변수
age = int(26)
print("How old r u? : {0}".format(age))
print("which age wanna your going back? : {0}".format(age-10))


#연산자
#and
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

# or 
print((3> 0) or (3 < 5)) # True
print((3 > 0) | (3 > 5)) # True 

# 수식 **, %, // 
print(2**3) # 2^3 =8
print(5%2) # 5를 2로 나눴을 때 나머지 1
print(5//3) # 5를 3으로 나눴을 때의 몫 1
print(10//3) # 10으로 3을 나눴을 때의 몫은 3

#수식 활용법
number = 5 # 넘버가 5라고 했을 때
number = number + 2 # 넘버에 2를 더하고 나온 값은 넘버다
number += 2 # 넘버에 2를 더 한다
# 둘 다 똑같은 말이다

#숫자 처리함수
value_A = abs(-5) # -5의 절댓값
value_B = pow(4,2) # 4의 2제곱
value_C = max(5,12) # 5~12 최댓값
value_D = min(5,12) # 5~12 최솟값
print(value_A, value_B, value_C, value_D)

#랜덤함수
from random import * # 임포트로 random 라이브러리 함수 가져오기

print(random()) # 0.0~1.0 미만의 랜덤값 생성
print(int(random() * 10) + 1) # 1~10 이하의 랜덤값 생성
print(int(random() * 45) + 1) # 1~45 이하의 랜덤값 생성
print(int(random() * 25) + 1) # 1~25 이하의 랜덤값 생성

print(randrange(1,46)) # 1~46 미만의 랜덤값 생성
print(randint(1,45)) # 1~45 이하의 랜덤값 생성ㄷ