# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:25:51 2020

@author: anike
"""

import numpy

def convolutional_encoder(input_sequence):
    input_sequence += [0,0]
    output_sequence = []
    a = input_sequence[0]
    b = 0
    c = 0
    
    for i in range(1, len(input_sequence)):
        op1 = 0 if [a,b,c].count(1)%2 == 0 else 1
        op2 = 0 if [a,c].count(1)%2 == 0 else 1
        
        output_sequence.append(op1)
        output_sequence.append(op2)
    
        c = b
        b = a
        a = input_sequence[i]
    op1 = 0 if [a,b,c].count(1)%2 == 0 else 1
    op2 = 0 if [a,c].count(1)%2 == 0 else 1
        
    output_sequence.append(op1)
    output_sequence.append(op2)
    
    return output_sequence
    
    
if __name__ == "__main__":
    no_of_bits = 1000
    input_ = numpy.random.randint(2, size=(no_of_bits,)).tolist()
    # input_ = [1,0,0,1,1]
    sequence = convolutional_encoder(input_)
    print(sequence)
