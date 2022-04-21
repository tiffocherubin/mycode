#!/usr/bin/env python3

def summ():
    sample_list=(8,2,3,0,7)
    summ=i=0
    for t in range(len(sample_list)):
        summ = summ + sample_list[i]
    print (" The sum is ",summ)
    print (range(9))
    print(len(sample_list))
    print(list(range(len(sample_list))))
def multip():
    sample_list=(8,2,3,-1,7)
    mult=1
    for i in range(len(sample_list)):
        mult = mult * sample_list[i]
    print (" The mult is ",mult)

summ()
multip()
