UserMoney= float(input("Change Maker Machine\n====================\nEnter dollars and cents amount to convert to coins: "))
TooniesLeft = float(UserMoney%2.00)
LooniesLeft = float(TooniesLeft%1.00)
QuartersLeft = float(LooniesLeft%0.25)

print("$2.00 Toonies X {0} (remaining: ${1:.2f})".format(int(UserMoney//2),TooniesLeft)) # {1:.2f} < 소수점 자리수 출력 제한
print("$1.00 Loonies X {0} (remaining: ${1:.2f})".format(int(TooniesLeft//1), LooniesLeft))
print("$0.25 Quarters X {0} (remaining: ${1:.2f})".format(int(LooniesLeft//0.25), QuartersLeft))
