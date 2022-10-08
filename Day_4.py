#함수(모듈화)
from msilib.schema import ProgId
from profile import Profile
from tkinter.tix import Balloon

from pip import main


def open_account():
    print("New account has been created")
# def 함수명(arguments*): 
def deposit(balance, money): # arguments 가 들어가는 위치
    print("Transition completed, current balance {0}".format(balance+money))
    return balance + money # 최종적으로 나오는 결과

balance = 0 
balance = deposit(balance, 1000) # deposit 함수에 balance 대입후 return값 balance로 출력
print(balance)

# 함수의 기본값
def profile(name, age=17,main_lang="python"):  # age=17, main_lang="python" 이 값들이 기본값이라고 할 수 있다
    print("name: {0}\t age : {1}\tmain language : {2}".format(name, age, main_lang))

profile("KKJ")

#함수의 키워드값
def profile2(name,age,main_lang):
    print(name, age, main_lang)

profile2(name="KKJ",age=26, main_lang="python") #함수 아규먼트 키워드에 따로 값 추가 가능

#가변 인자
#def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
#   print("name: {0}\tage: {1}\t".format(name, age), end=" ") # end = " " 밑에 존재하는 print문을 줄바꿈 없이 출력한다
#   print(lang1, lang2, lang3, lang4, lang5)

def profile3(name, age, *language): # *로 가변처리 language에는 숫자 상관 없이 넣을 수 있다
    print("name: {0}\tage: {1}\t".format(name, age), end=" ") # end = " " 밑에 존재하는 print문을 줄바꿈 없이 출력한다
    for lang in language: # language에 들어간 값을 처리하는 부분
        print(lang, end=" ") # lang으로 요소를 하나하나 출력
    print()
profile3("YOU Suck", "20", "python", "java", "c", "c++", "c#")
profile3("KKJ", "26", "Jupyter", "java script", "alpha", "beta", "comma", "linux", "and something")


# 지역변수와 전역변수
gun = 10 # 일반 변수

def checkpoint(soldiers): 
    global gun # 전역 공간에 있는 gun 변수를 사용하겠다
    gun = gun - soldiers
    print("left gun :{0}".format(gun))
print(gun) # 10
checkpoint(2)
print(gun) # 8
#함수에서 전역 변수를 사용하면 함수의 영향을 받으니 주의
#보통 전역 변수를 많이 사용하지 않는다, 코드를 읽기 어려워짐, 그냥 함수내에서 처리하고 리턴 값으로 변수에 저장하도록하자


#표준 입출력
print("python", "java", "javascript", sep=",")
print("python", "java", "javascript", sep=" vs ")
print("python", "java", "javascript", sep=",", end="?") # end=의 기본값은 end="\n" 아무것도 넣지않고  end=""이라하면 줄바꿈없이 붙어나온다

import sys
print("python", "java", file=sys.stdout) # stdout 표준 출력
print("python", "java", file=sys.stderr) # stderr 표준 에러 출력

scores = {"math":0, "english":50, "coding":100}
for subject, score in scores.items(): # 딕셔너리 요소를 for문으로 활용하는 방법이다 딕셔너리 요소를 items로 출력
    #print(subject.ljust(8),score) # ljust < 왼쪽으로 정렬, ljust(8): 8칸의 공백을 확보하고 왼쪽으로 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":") 

for num in range(1,21):
    print("waiting_num : " +str(num).zfill(3)) # zfill(3) 3개의 0으로 출력, 값이 있으면 값을 입력하고 0을 출력한다 001, 002, 003~ 이런 식으로