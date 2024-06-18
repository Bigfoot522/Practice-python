# sentance = '나는 소년입니다'
# print(sentance)
# sentance2 = "파이썬은 쉬워요"
# print(sentance2)
# sentance3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentance3)

# jumin = "020522 - 1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리" + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리(뒤에서부터)" + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) # 0번째 문자 대문자로 출력
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 대체

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

# print(python.find("Java")) # 없으면 -1 반환
# print(python.index("Java")) # 없으면 오류냄
# print("hi") # 위에서 오류나서 반환 불가
# print(python.count("n")) # 세기

# print("나는 %d살입니다." % 20)
# print("나는 %s를 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요" % "A")
# # %s
# print("나는 %s살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 순서
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("백문이 불여일견\n백견이 불여일타")
# print("저는 '나도코딩'입니다.")
# print("저는 \"나도코딩\"입니다.")
# print("C:\\User\\User\\My_python>")
# print("Red Apple\rPine")
# print("Redd\bApple")
# print("Red\tApple")