# 리스트
# subway1 = 10
# subway2 = 20
# subway3 = 30
# subway = [10, 20, 30]
# print(subway[0])
# subway = ["유재석", "조세호", "박명수"]
# print(subway.index("조세호")) # 위치
# subway.append("하하") # 추가
# print(subway)
# subway.insert(1, "정형돈")
# print(subway)
# print(subway.pop()) # 뒤에서 하나씩 꺼냄
# print(subway)
# subway.append("유재석")
# print(subway.count("유재석")) # 카운트하기
# num_list = [5, 4, 3, 2, 1]
# num_list.sort() # 정렬
# print(num_list)
# num_list.reverse() # 순서 뒤집기
# print(num_list)
# num_list.clear() # 모두 지우기
# print(num_list)
# num_list = [5, 4, 3, 2, 1]
# mix_list = ["조세호", 20, True] # 다양한 자료형
# num_list.extend(mix_list) # 리스트 확장
# print(num_list)

# 사전
# cabinet = {1 : "유재석", 100 : "김태호"}
# print(cabinet[1])
# print(cabinet.get(1))
# # print(cabinet[5]) # 에러가 남
# print("hi")
# print(cabinet.get(5)) # none 출력
# print(cabinet.get(5, "사용가능"))
# print(1 in cabinet) # True
# print(5 in cabinet) # False
# cabinet = {"A-1" : "유재석", "B-100" : "김태호"}
# print("A-1")
# print("B-100")
# print(cabinet) # 새 손님
# cabinet["A-1"] = "김종국"
# cabinet["B-100"] = "송지효"
# print(cabinet)
# del cabinet["A-1"] # 간 손님
# print(cabinet)
# print(cabinet.keys()) # key 들만 출력
# print(cabinet.values()) # value 들만 출력
# print(cabinet.item()) # key, value 쌍으로 출력
# cabinet.clear() # 모두 지우기
# print(cabinet)

# 튜플 (변경 불가)
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# # menu.add("생선까스") # 오류 남
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set)
# java = {"유재석", "김태호", "양세형"} # 아래도 똑같이 세트 만드는 법
# python = set(["유재석", "박명수"])
# print(java & python) # 교집합
# print(java | python) # 합집합
# print(java - python) # 차집합
# print(java.difference(python))
# python.add("김태호") # 자료 추가
# java.remove("김태호") # 자료 제거

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))