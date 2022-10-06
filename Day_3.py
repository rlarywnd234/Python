#딕셔너리
# {key : value, Key2 : value}
# key값의 중복이 허용되지 않음, Key1이 이미 있다면 Key1은 존재할 수 없다.

from codecs import charmap_build
from itertools import count
from random import randint


cabinet = {1:"누군가1", 2:"누군가2", 45:"누군가3"} # 딕셔너리 선언법
print(cabinet[2])
print(cabinet[45]) # *인덱스로 호출하는 방식이 아니다*

print(cabinet.get(5)) # get으로 호출시 에러를 발생시키지 않고 None이라는 메세지를 호출한다
print(cabinet.get(5, "비어있습니다")) # None이라는 메세지를 "비어있습니다"로 교체할 수 있다

print(3 in cabinet) # 3이라는 키값이 있으면 True, 존재하지 않으면 False
print(5 in cabinet) 

# 업데이트 및 추가
cabinet[45] = "KKJ" # 45이라는 키값이 있다면 value를 KKJ로 업데이트한다
cabinet[46] = "KKK" # 46이라는 키값이 있다면 value를 업데이트 하지만 없다면 새로이 추가한다
print(cabinet)

# Key만 출력
print(cabinet.keys())
# value만 출력
print(cabinet.values())
#key, value 둘 다 출력
print(cabinet.items())

# 삭제
del cabinet[46]
print(cabinet)
#전부 삭제
cabinet.clear()
print(cabinet)



#튜플
#변경할 수 없음, 고정, 그러니까 추가 및 삭제 전혀 불가능
# 장점: 라스트보다 빠름
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

(name, age, hobby) = ("KKJ", "26", "VideoGame") # 이런 식으로 고정 변수를 선언할 수 있다
#절대 바꾸지 말아야할 값들을 고정하는데 사용함


#자료구조 변경법
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


#if 조건문
weather = input("Today's weather? :")
if weather == "Nothing":                        # if 조건문
    print("Nothing happened")
elif weather == "micro dust":                   # else if 다른 조건
    print("prepare a mask")
else: 
    print("You don't need to prepare anything") # elif, if 조건에 맞지 않으면 무조건 출력


temp = int(input("how's Temperture? :"))
if temp >= 30:                                  # 논리 연산자 조건문
    print("Hot as shit, don't go outside")
elif temp <= 20 and temp >= 10:
    print("Good")
elif temp <=0: 
    print("Too cold, don't go outside")

#반복문 for < 매우 많이 사용함
for waiting_num in range(0,5): # 0~4
    print("waiting num currently: {0}".format(waiting_num))


#반복문 while < 잘 안씀 무한루프의 위험성이 존재
customer = "A_san"
index = 5
while index <= 10 :
    print("{0}, coffee is ready. {1} left".format(customer, index))
    index = index + 1

# break , continue
absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent: # absent리스트 안에 student 객체가 존재할 경우
        continue # continue를 실행하면 바로 다음 반복으로 넘어감
    elif student in no_book:
        print("you little brat, do not come school without a book")
        break # 반복 종료, 루프문 강제 종료 
    print("{0}, read 134 page pls".format(student)) # for안에서 조건없이 반복함

# 한 줄자리 for
students = [1,2,3,4,5]
students = [i+100 for i in students] # for 앞 실행할 명령문, for 뒤 반복을 돌릴 객체
print(students)