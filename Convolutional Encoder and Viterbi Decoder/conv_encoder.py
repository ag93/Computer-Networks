# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:25:51 2020

@author: anike
"""

import numpy

def convolutional_encoder(input_sequence):
    output_sequence = []
    
    next_states = {"00": ["00", "10"],
                   "10": ["01", "11"],
                   "01": ["00", "10"],
                   "11": ["01", "11"]
        }
    
    outputs = {"00": ["00", "11"],
               "10": ["01", "10"],
               "01": ["11", "00"],
               "11": ["10", "01"]
        }
    
    current_state = "00"
    for bit in input_sequence:
        temp_output = outputs[current_state][bit]
        
        output_sequence.append(int(temp_output[0]))
        output_sequence.append(int(temp_output[1]))
        
        current_state = next_states[current_state][bit]
        print(current_state)

    return output_sequence



if __name__ == "__main__":
    no_of_bits = 1000
    input_ = numpy.random.randint(2, size=(no_of_bits,)).tolist()
    input_ = [1,0,0,1,1,1,0,1,1]
    sequence = convolutional_encoder(input_)
    print(sequence)