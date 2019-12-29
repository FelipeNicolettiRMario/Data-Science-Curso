from functools import reduce
import math
from collections import Counter

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

def shape(A):
    n_rows = len(A)
    n_cols = len(A[0]) if A else 0

    return n_cols,n_rows

def getRow(A,i):
    row = A[i]
    return row

def getCol(A,j):
    return [A_i[j] for A_i in A]

def make_matrix(n_row,n_col,entry_fn):

    return [[entry_fn(i,j) for j in range(n_col) for i in range(n_row)]]

def mean(x):

    return sum(x)/len(x)


def quartile(x,p):
    p_index = int(p*len(x))
    print(p*len(x))
    return sorted(x)[p_index]

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2

    if n%2 == 1:
        return sorted_v[midpoint]

    else:
        lo = midpoint - 1
        hi = midpoint

        return (sorted_v[lo] + sorted_v[hi])/2

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())

    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]
def data_range(x):

    return max(x) - min(x)

def de_mean(x):

    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):

    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/(n-1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quartile(x,0.75) - quartile(x,0.25)

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x),de_mean(y)) / (n-1)

def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)

    if stdev_x>0 and stdev_y>0:
        return covariance(x,y)/stdev_x/stdev_y
    else:
        return 0

print(correlation([1,2,3,4,5,6],[4,2,3,4,7,8]))