# # print('Assalomu aleykum Rahmatullo')
# # print('')
#
# '''
# sddsf
# fd
# dsgfd
# g
# fd
# '''
#
# # a = 2
# # b = 4
# # print(a - b)
# # print(a + b)
# # print(a * b)
# # print(a / b)
# # print(a // b)
# # print(a % b)
# # print(a ** b)
#
# # pythonda data types
# number = 23     # int - butun son
# number2 = 23.3  # float - o'nli kasr son
# matn = 'Salom'  # str = belgili malumot turi
# mantiq = True  # False # boolean - mantiq
#
# list_ = [1,2,3,4] # tartiblangan, o'zgaruvchan, ro'yxat
# tuple_ = (1,2,3,4) # tartiblangan, o'zgarmas, ro'yxat
# set_ = {1,2,3,4} # tartiblanmagan, o'zgaruvchan, takrorlanmas ro'yxat
# dict_ = {1:"bir",
#          2:"ikki",
#          3:'uch',
#          4:'to\'rt'
#          } # lug'at
#
#
# # print('salom')
# a = 34
# b = 'Salom'
# # c = a + b
# # print(c)
import os
from itertools import product


def check(opers, nums):
    result = nums[0]
    for i, oper in enumerate(opers):
        if oper == "+":
            result += nums[i + 1]
        elif oper == "*":
            result *= nums[i + 1]
    return result


def check2(opers, nums):
    result = nums[0]
    for i, oper in enumerate(opers):
        if oper == "+":
            result += nums[i + 1]
        elif oper == "*":
            result *= nums[i + 1]
        elif oper == "||":
            result = int(str(result) + str(nums[i + 1]))
    return result

def hisobla(target, nums):
    calc = list(product(["+","*"], repeat=len(nums)-1))
    for i in calc:
        if check(i, nums)==target:
            return True
    return False

def hisobla2(target, nums):
    calc = list(product(["+","*","||"], repeat=len(nums)-1))
    for i in calc:
        if check2(i, nums)==target:
            return True
    return False

def partOne():
    numbers = input_nums()
    jami = 0
    for i, j in numbers:
        if hisobla(i, j):
            jami += i
    print(jami)

def partTwo():
    numbers = input_nums()
    jami = 0
    for i, j in numbers:
        if hisobla2(i, j):
            jami += i
    print(jami)

def input_nums():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = f"{dir_path}/input.txt"
    all_rows = []
    
    data = open(input_path, 'r')
    for i in data.readlines():
        target = int(i[:i.index(':')])
        nums = list(map(int,i[i.index(':')+1:].strip().split()))
        all_rows.append((target, nums))
    data.close()
    return all_rows

partOne()
partTwo()

