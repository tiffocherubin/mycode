#!/usr/bin/env python3

sample_list=(8,2,3,0,7)
def summ(x):
    summ=i=0
    for t in range(len(x)):
        summ = summ + x[i]
    print (" xxx  ")
    print (" The sum is ",summ)
    print (range(9))
    print(len(x))
    print(list(range(len(x))))
def multip():
    sample_list=(8,2,3,-1,7)
    mult=1
    for i in range(len(sample_list)):
        mult = mult * sample_list[i]
    print (" The mult is ",mult)

summ(sample_list)
multip()
