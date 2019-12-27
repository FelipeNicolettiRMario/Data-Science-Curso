from functools import reduce
import math

def vector_add(v,w):
    #Soma elementos correspondentes
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v,w):
    #Subtrai os elementos correspondentes
    return [v_i - w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add,vectors)

def scalar_multiply(c,v):
    #C é um numero V é um vetor
    return [c*v_i for v_i in v]

def vector_mean(vectors):
    #Computar o vetor cujo i-ésimo elemento seja a média dos
    #ii-éssimos eleemenntos dos veetoress inclusos
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
    #Produto escalar
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return magnitude(vector_subtract(v,w))

print(vector_mean([[1,2,3,4,5],[10,4,5,6,7],[3,4,5,6,7]]))