# site = "http://daum.com"
# index = site.index(".")
# name = site[7:index]
# e = site.count("e")
# print(name[0:3] + str(index - 7) + str(e) + "!")

url = "http://daum.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")] # my_str = my_str[0:5]
passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url,passward))