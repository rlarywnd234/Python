#pickel 라이브러리. 
#파일을 생성후 데이터 입력, 저장
from msilib import datasizemask
import pickle
from socketserver import DatagramRequestHandler
from unicodedata import name

profile_file = open("profile.pickle", "wb") #파일명 , 쓰기, 바이너리타입
profile = {"name": "kkj", "age":26, "hobby" : ["a","b","c"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 존재하는 데이터를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # 파일명, 읽기, 바이너리타입
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile) # 프로필 출력
profile_file.close() #프로필_파일 저장 후 종료

#with
with open("profile.pickle", "rb") as profile_file: #profile.pickle이라는 파일을 읽어서 profile_file이라는 변수에 저장
    print(pickle.load(profile_file))# profile_file 변수를 pickle로 출력
# with문 사용시 close()안 쓰고 바로 탈출 가능

with open("study.txt","w", encoding="utf8") as study_file: # 쓰기 모드
    study_file.write("I am studing python now") # write로 쓰기 모드

with open("study.txt","r", encoding="utf8") as study_file: # 읽기 모드
    study_file.read() # read로 읽기 모드 진입

# Class 
class unit: # 클래스명
    def __init__(self, name, hp, damage): # 클래스에 들어가는 멤버 변수
        self.name = name # 멤버 변수 선언
        self.hp = hp
        self.damage = damage
        print("{} Unit has been generated".format(self.name)) # 멤버 변수 처리식
        print("HP {0}, Damage {1}".format(self.hp, self.damage))

Marine1 = unit("Marine", 40, 5)
Marine2 = unit("Marine", 40, 5)
tank = unit("tank", 150, 35)

# Method
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name  = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location): # 메소드 부분
        print("{0} : attacing {1} clock way damaging{2}".format(self.name, location, self.damage))

    def damaged(self, damage): # 메소드 
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : Current HP is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : has been destroied".format(self.name))

firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack("5") # Attackunit의 attack 메소드를 사용, 값 5를 지정

firebat1.damaged(25) # Attackunit의 damagaed 메소드를 사용, 값 25를 지정
firebat1.damaged(25) 

#pass
class BuildingUnit(unit):
    def __init__(self, name, hp, damage):
        pass
supply_depot = BuildingUnit("Supply depot", 500, "7" )
# 일부 코드가 구문상 필요하긴 하지만 아무 작업도 하지 않길 원하는 경우에 사용
# 클래스가 내부 동작은 필요 없고, 의미적으로 껍데기만 필요한 경우에 pass를 통해서 껍데기만 만들 때 사용가능
