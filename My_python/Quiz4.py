from random import *
i_customer = 0
for customer in range(1, 51):
    time = randrange(1, 51)
    if 5 <= time <=15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        i_customer = i_customer + 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
print("총 탑승 승객 : {0} 분".format(i_customer))