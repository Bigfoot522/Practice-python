# by me
# from random import *
# chat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(chat)
# chicken = sample(chat, 1)
# # del chat[chicken]
# coffee = sample(chat, 3)
# coffee.sort()

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : " + str(chicken))
# print("커피 당첨자 :", coffee)
# print("-- 축하합니다 --")

# by nadocoding
from random import *
users = range(1, 21) # 1부터 20까지 숫자 생성
users = list(users)
shuffle(users)
winners = sample(users, 4)


print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")



# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --