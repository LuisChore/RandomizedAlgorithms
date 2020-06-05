'''
Vazquez Choreno Luis Ernesto
Randomized Algorithms
Application: Median

python3 Median.py
'''

import numpy as np
import math
import matplotlib.pyplot as plt


limit = 10000
number_operations = 0
number_operations2 = 0


def get_rng(value):
    return np.random.randint(low=1, high=value+1)


### MEDIAN ALGORITHM ###
def generate_random_array(n):
    S = []
    for i in range(n):
        S.append(get_rng(limit))
    return S



def process_agorithm_randomized(S):
    found = False
    global number_operations2
    number_operations2 = 0
    n = len(S)
    while found == False:
        size_r = int(np.ceil(pow(n,0.75)))
        R = []

        # first step
        number_operations2 += int(size_r)
        for i in range(size_r):
            R.append(S[get_rng(n) - 1])

        #second step
        number_operations2 += int(size_r * math.log2(size_r))
        R.sort()


        #third step
        d = R[int(np.floor(size_r/2.00 - pow(n,0.5)))]

        #fourth step
        u = R[int( np.ceil(size_r/2.00 + pow(n,0.5)))]

        #fifth step
        number_operations2 += len(S)
        C = []
        ld = 0
        lu = 0
        for si in S:
            if d <= si and si <= u:
                C.append(si)
            elif si < d:
                ld+=1
            else:
                lu+=1
        # sixth step
        if ld > int(n/2) or lu > int(n/2):
            continue

        #seventh step
        if len(C) > 4*size_r:
            continue
        C.sort()
        number_operations2 += int(len(C)*math.log2(len(C)))

        ##eight step
        median_index = int(n/2.00) - ld
        print("Median computed: " + str(C[median_index]))
        found = True
    return number_operations2






### R-SELECT ###
def partition(S,l,r):
    value = S[r]
    i = l
    for j in range(l,r):
        if S[j] <= value:
            temp = S[i]
            S[i] = S[j]
            S[j] = temp
            i+=1
    temp = S[i]
    S[i] = S[r]
    S[r] = temp
    return i



def rselect(S,l,r,k):
    L = r - l + 1
    pivot = get_rng(L) - 1 + l
    temp = S[pivot]
    S[pivot] = S[r]
    S[r] = temp
    global number_operations
    number_operations += L
    pos = partition(S,l,r)
    if pos - l == k:
        return S[pos]
    if pos - l > k:
        return rselect(S,l,pos-1,k)
    return rselect(S,pos+1,r,k-pos+l-1)

def r_select(S):
    L = len(S)
    global number_operations
    number_operations = 0
    median = rselect(S,0,L-1,int(np.floor(L/2.00)))
    print("Median computed: " + str(median))
    return number_operations







def main():
    n = 100
    S = generate_random_array(n)
    copyS = S.copy()
    copyS.sort()
    print("Real median: " + str(copyS[int(np.floor(n/2.00))]))
    r_select(S)
    process_agorithm_randomized(S)




    '''
    x = []
    y = []
    y1 = []
    for i in range(1000,10000,1000):
        n = i
        x.append(i)
        yi = 0
        y1i = 0
        for j in range(0,10):
            S = generate_random_array(n)
            yi += r_select(S)
            y1i += process_agorithm_randomized(S)
        y.append(yi/10.00)
        y1.append(y1i/10.00)

    plt.plot(x,y,label = 'R-SELECT')
    plt.plot(x,y1,label = 'MEDIAN ALGORITHM')
    plt.plot(x,x, label = 'LINEAR TIME')
    plt.legend()
    plt.show()
    '''
main()
