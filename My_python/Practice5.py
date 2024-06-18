# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
    
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name, age, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석", 20)
# profile("김태호", 25)
# profile(name = "유재석", main_lang = "자바", age = 20)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotlin", "Swift")

# 지역변수 = 함수 호출할때 만들어졌다가 끝나면 사라지는 변수, 전역변수 = 프로그램 내 어디서든 사용할 수 있는 변수

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))