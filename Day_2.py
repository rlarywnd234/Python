#슬라이싱


from re import S


Someone = "his name is Ile"

print("Name : " + Someone[12:16])
print("Name : " + Someone[:-1]) # 처음부터 끝까지
print("Name : " + Someone[-3:]) # 뒤에서부터 3글자 기준 끝까지 

#문자열 처리함수 
python = "python is crazy"
print(python.lower()) # 전부 소문자화
print(python.upper()) # 전부 대문자화 
print(python.isupper()) # 대문자 첨부 확인

print(len(python)) # 해당 문자열 변수의 길이 확인 # 아주 아주 중요한 함수 
print(python.replace("python" , "java")) # 해당하는 문자열 교체 
print(python.index("n")) # 해당하는 문자의 위치 표시
print(python.find("Java")) # 문자열 찾기 있다면 "1" 값 반환

#문자열 포맷 지정
print("I am %d" % 20) # int 포맷 
print("I love %s" % "python") # 문자열 포맷
print("Apple is starting with %c" % "A") #문자 단 하나 포맷
print("my favorite color is %s and %s" % ("blue", "red"))

#문자열 포맷 2 (사실상 거의 이걸 사용한다)
print("나는 {}살입니다".format(20))
print("나는 {0}살이고 {1}에 살며 {2}로 가고 싶습니다".format(20, "경기도", "서울")) # 경기도에서 서울로



#리스트 []
# 순서가 있는 객체의 집합
subway = ["K","G","B"] # 리스트 선언법
print(subway[2], subway[1],subway[0]) #리스트 객체 호출법
print(subway.index("K")) #리스트 인덱스 호출법
subway.append("L") #리스트 요소 추가법
subway.insert(1,"T") #리스트 교체

subway(subway.pop()) #뒤에 부터 리스트 객체를 하나씩 꺼냄, 꺼낸 자리에 있던 인덱스는 사라진다
print(subway.count("K")) #리스트에 있는 K 값의 개수를 카운트

num_list = [1,2,3,4,5]
num_list.sort() # 정리
num_list.reverse() # 뒤집기
num_list.clear() # 리스트 내부 삭제
num_list.extend(subway) # 리스트 확장


#리스트의 장점
# 1. 다양한 자료형과 함께 사용 가능
# 2. 확장 가능(동적 할당 가능)

