#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input("Ведите число: "))
    b = int(input("Ведите число: "))
    c = int(input("Ведите число: "))
    if b >= a <= c:
        print("Наименьшее число:",a)
    elif a >= b <= c:
        print("Наименьшее число:",b)
    else:
        print("Наименьшее число:",c)
    if b <= a >= c:
        print("Наибольшее число:",a)
    elif a <= b >= c:
        print("Наибольшее число:",b)
    else:
        print("Наибольшее число:",c)

