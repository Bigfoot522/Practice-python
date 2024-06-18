def std_weight(height, gender):
    if gender == '남성':
        weight = height * height * 22
        return weight
    else:
        weight = height * height * 21
        return weight

height = int(input("키를 입력하세요."))
gender = input("성별을 입력하세요. (남성/여성)")
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))