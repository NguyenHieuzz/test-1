# Hàm def

'''
def sum(a,b):
    #sum_of_a_and_b
    sum = a+b
    return sum
a=int(input())
b=int(input())
x = sum(a,b)
print(x)
'''




# def name_user(name):
#     print("Welcome back!" + name)
#     return name
# name = name_user(input())


def TBM(T,L,H,V,A):
    TBM = int((T+L+H+A+V)/5)
    if TBM in range [9,10]:
        print("Very good!")
    if TBM in range[7,8]:
        print("good")
    if TBM in range[5,6]:
        print("Not bad")
    else:
        print("Try it again!")
dang_gia = TBM(float(input()))







