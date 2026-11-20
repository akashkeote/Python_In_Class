import numpy as np 
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

arr_gen=gen(pcg(seed=100))
#with same seed we get the same value via normal function
print(arr_gen)
#we have the generator types
#  but we don't have the values

print(arr_gen.normal(size=(5,5)))


#generate using the integer
arr_gen = gen(pcg(seed=230))
print(arr_gen.integers(low=10,high=100,size=(5,5)))
#if i change the value of the seec then the value also change

arr_gen = gen(pcg(seed=200))
print(arr_gen.random)
#<bound method Generator.random of Generator(PCG64) at 0x1BC3FCCA7A0>

print(arr_gen.random(size=(2,2)))
#ab random value hoge generate
