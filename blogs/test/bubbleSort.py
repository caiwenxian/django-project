# -*- coding:utf-8 -*-


def bubbleSort(list):
    if len(list) == 0:
        return []
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                # list[j], list[j + 1] = list[j + 1], list[j]
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

def insertSort(list):
    if len(list) == 0:
        return []
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1

            list[j + 1] = temp
    return list

if __name__ == '__main__':
    s = bubbleSort([1,2,3,5,8,7,4,8,3,7,3,8,9,9,4,32,2])
    print("s: %s" % s);
    s = insertSort([1,2,3,5,8,7,4,8,3,7,3,8,9,9,4,32,2])
    print("s: %s" % s);