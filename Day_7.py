# 메소드 오버라이딩
class Person:
    def greeting(self):
        print('hello.')
        
class Student(Person):
    def greeting(self):
        print('Hello. I am a student of blahblah.')

james = Student()
james.greeting()
# 결과   Hello. I am a student of blahblah.

# 보면 알겠지만 greeting 메소드는 총 두 개다, 이 중 불러와진건 Studnet() 클래스의 greeting
#이와 같이 상속 받은 person클래스의 greeting을 무시하고 새로운 메서드를 만들어서 덮어씌울 수 있다.

# 그럼 왜 사용해?
# 1.어떤 기능이 같은 메서드의 이름으로 계속해서 사용되어야 할 경우
# 즉 그러니까, greeting2로 메서드 이름을 바꿔 특정하면, 아래에서 사용한 메서드 이름을 전부 바꿔야하므로 상당히 피곤하다.

# 메소드 오버라이딩의 적절한 사용법
class Person:
    def greeting(self):
        print('hello.', end="")
        
class Student(Person):
    def greeting(self):
        super().greeting() # super().greeting()으로 기반 클래스 메서드 호출 > 중복을 줄임
        print('. I am a student of blahblah.')

james = Student()
james.greeting()
#결과  hello.. I am a student of blahblah.
