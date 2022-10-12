# 출력 포맷

# 1. 빈 자리는 빈공간으로 두고, 오른쪽 정렬 하되 총 10자리 공간을 확보
print("{0: >10}".format(500)) #결과>       500 # 10자리 중 7자리 공백
# 2. 양수일 경우 + 표시 음수일 경우 -표시
print("{0: >+10}".format(500)) #결과>      +500
print("{0: >+10}".format(-500))#결과>      -500
# 왼쪽 정렬, 빈칸 _으로 채움
print("{0:_<10}".format(500)) #결과>>500_______
# 3자리 마다 콤마를 찍기, +- 부호 추가
print("{0:,}".format(10000000000))
print("{0:+,}".format(10000000))
print("{0:+,}".format(-10000000))




# 파일 입출력

# 파일 생성
score_file = open("score.txt", "w", encoding="utf8") # 파일명, 쓰기 모드(writing), 한글 깨짐방지
print("math : 0", file=score_file)
print("english : 50", file=score_file)
score_file.close() # 파일 저장 > 결과로 score.txt 생성됨

# 파일 텍스트 내용 추가
score_file2 = open("score.txt", "a", encoding= "utf8") # 파일명, 추가 모드(appending), 한글깨짐방지
score_file2.write("science : 80")
score_file2.write("\ncoding : 100")
score_file.close() # 파일 저장

# 파일 읽기
score_file = open("score.txt", "r", encoding="utf8") # 파일명, 읽기 모드(reading), 한글깨짐방지
print(score_file.read()) #전부 읽기
score_file.close() # 파일 저장

# 외부 파일 몇 줄인지 모를 때, 전부 출력
score_file2 = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file2.readline()
    if not line:
        break
    print(line, end="")
score_file2.close()

